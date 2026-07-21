(function () {
  const year = document.getElementById("year");
  if (year) {
    year.textContent = String(new Date().getFullYear());
  }

  const canvas = document.getElementById("signal-canvas");
  if (!(canvas instanceof HTMLCanvasElement)) {
    return;
  }

  const context = canvas.getContext("2d");
  if (!context) {
    return;
  }

  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const palette = ["#f7d58a", "#9ee7da", "#ffffff", "#e29b66", "#bdb3f0"];
  let width = 0;
  let height = 0;
  let points = [];
  let frame = 0;

  function resize() {
    const rect = canvas.getBoundingClientRect();
    const scale = Math.min(window.devicePixelRatio || 1, 2);
    width = Math.max(1, Math.floor(rect.width));
    height = Math.max(1, Math.floor(rect.height));
    canvas.width = Math.floor(width * scale);
    canvas.height = Math.floor(height * scale);
    context.setTransform(scale, 0, 0, scale, 0, 0);

    points = Array.from({ length: 34 }, (_, index) => ({
      x: (index * 67) % width,
      y: ((index * 97) % height) + 12,
      radius: 2 + (index % 4),
      speed: 0.18 + (index % 5) * 0.035,
      phase: index * 0.74,
      color: palette[index % palette.length]
    }));
  }

  function drawGrid() {
    context.strokeStyle = "rgba(255, 255, 255, 0.06)";
    context.lineWidth = 1;

    for (let x = 0; x < width; x += 52) {
      context.beginPath();
      context.moveTo(x, 0);
      context.lineTo(x, height);
      context.stroke();
    }

    for (let y = 0; y < height; y += 52) {
      context.beginPath();
      context.moveTo(0, y);
      context.lineTo(width, y);
      context.stroke();
    }
  }

  function drawConnections() {
    for (let i = 0; i < points.length; i += 1) {
      for (let j = i + 1; j < points.length; j += 1) {
        const a = points[i];
        const b = points[j];
        const dx = a.x - b.x;
        const dy = a.y - b.y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < 148) {
          context.strokeStyle = `rgba(255, 255, 255, ${0.16 - distance / 1200})`;
          context.lineWidth = 1;
          context.beginPath();
          context.moveTo(a.x, a.y);
          context.lineTo(b.x, b.y);
          context.stroke();
        }
      }
    }
  }

  function drawPoints() {
    points.forEach((point) => {
      context.beginPath();
      context.fillStyle = point.color;
      context.shadowColor = point.color;
      context.shadowBlur = 16;
      context.arc(point.x, point.y, point.radius, 0, Math.PI * 2);
      context.fill();
      context.shadowBlur = 0;
    });
  }

  function step() {
    frame += 1;
    context.clearRect(0, 0, width, height);
    drawGrid();

    points.forEach((point, index) => {
      point.x += Math.sin(frame * 0.01 + point.phase) * point.speed;
      point.y += Math.cos(frame * 0.012 + point.phase) * point.speed;

      if (point.x < -10) point.x = width + 10;
      if (point.x > width + 10) point.x = -10;
      if (point.y < -10) point.y = height + 10;
      if (point.y > height + 10) point.y = -10;

      if (index % 7 === 0) {
        point.radius = 3 + Math.sin(frame * 0.04 + index) * 1.2;
      }
    });

    drawConnections();
    drawPoints();

    if (!prefersReducedMotion) {
      requestAnimationFrame(step);
    }
  }

  resize();
  step();
  window.addEventListener("resize", resize);
})();
