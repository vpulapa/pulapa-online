/* Progressive enhancement: every thesis remains readable without JavaScript. */
function matchesThesis(item, query, family, direction) {
  const text = [item.id, item.title, item.body, item.location, item.evidence, item.trigger, item.invalidation, item.target, item.avoid, item.familyLabel].join(' ').toLowerCase();
  return (!family || item.family === family) && (!direction || item.direction === direction) && query.toLowerCase().trim().split(/\s+/).every(word => text.includes(word));
}
if (typeof module !== 'undefined') module.exports = {matchesThesis};
if (typeof document !== 'undefined') {
  const form = document.querySelector('.filters');
  if (form) {
    const search = document.querySelector('#search'), family = document.querySelector('#family'), direction = document.querySelector('#direction');
    const cards = [...document.querySelectorAll('.thesis-card')];
    let records = cards.map(card => ({id:card.dataset.id, family:card.dataset.family, direction:card.dataset.direction, title:card.textContent}));
    const restore = () => {
      const params = new URLSearchParams(location.search);
      search.value = params.get('q') || '';
      family.value = params.get('family') || '';
      direction.value = params.get('direction') || '';
    };
    const apply = (updateURL = true) => {
      let count = 0;
      cards.forEach((card,i) => { card.hidden = !matchesThesis(records[i],search.value,family.value,direction.value); if(!card.hidden) count++; });
      document.querySelector('#result-count').textContent = `${count} ${count === 1 ? 'THESIS' : 'THESES'}`;
      document.querySelector('#empty').hidden = count !== 0;
      if(updateURL) {
        const params = new URLSearchParams();
        if(search.value.trim()) params.set('q',search.value.trim());
        if(family.value) params.set('family',family.value);
        if(direction.value) params.set('direction',direction.value);
        history.replaceState(null,'',location.pathname+(params.size?'?'+params.toString():''));
      }
    };
    restore(); apply(false);
    fetch('/playbook/assets/theses.json').then(r => {if(!r.ok) throw Error('Search unavailable'); return r.json();}).then(data => {records=data;apply(false);}).catch(() => {document.querySelector('.search-help').textContent='Full-text search is unavailable. You can still search visible titles and browse all pages.';});
    form.addEventListener('submit',e => {e.preventDefault();apply();});
    form.addEventListener('input',() => apply());
    form.addEventListener('change',() => apply());
    form.addEventListener('reset',() => setTimeout(() => apply(),0));
    addEventListener('popstate',() => {restore();apply(false);});
    document.addEventListener('keydown',e => {
      if(e.key==='/' && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)){e.preventDefault();search.focus();}
      if(e.key==='Escape' && document.activeElement===search){search.value='';apply();}
    });
  }
}
