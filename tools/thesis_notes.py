"""Editorial study notes. Illustrative context, never admitted trading rules."""

# id | direction | diagram | location | evidence | trigger | invalidation | first target | skip condition
ROWS = '''
1|Long|spike|First shallow pullback after a bull breakout|Large bull bodies and weak, overlapping bear responses|A completed bull signal followed by a break above its high|A strong break below the protected higher low or spike base|Prior spike high; reassess before a measured move|The spike runs straight into major resistance or the pullback becomes a bear breakout
2|Short|spike|First weak rally after a bear breakout|Bear follow-through persists; bulls cannot reclaim the breakdown|A completed bear signal followed by a break below its low|Acceptance above the protected lower high|Prior spike low; then the next downside magnet|Consecutive strong bull bars replace the weak rally
3|Long|second|Structural support during a bull pullback|The first resumption attempt fails, but sellers cannot establish control|The second upward attempt clears its signal bar|A break below the pullback structure|Prior trend high|An H2 forms directly beneath range resistance with little reward available
4|Short|second|Resistance during a bear-trend rally|The first downward attempt fails without creating a bull reversal|The second downward attempt breaks its signal bar|A break above the rally structure|Prior trend low|An L2 sits on major support or the rally shows sustained bull pressure
5|Long|ema|EMA near a protected higher low|The decline is weak; buying resumes at the location|Bull response or failed bear breakout at the EMA|Failure of the higher low, not an arbitrary distance below the average|Prior high|The EMA is falling in a balanced range or sellers have strong follow-through
6|Short|ema|EMA near a protected lower high|The rally is weak; selling resumes at the location|Bear response or failed bull breakout at the EMA|Failure of the lower high, not an arbitrary distance above the average|Prior low|The average is rising and bulls are breaking above structure
7|Long|breakout|Retest of former resistance|The breakout has follow-through and the retest holds outside the old range|Bull signal after the breakout point holds|Sustained acceptance back inside the prior range|Breakout high; then range-height projection|The retest penetrates deeply into the range with strong bear closes
8|Short|breakout|Retest of former support|The breakdown holds and old buyers cannot reclaim support|Bear signal after the retest fails|Sustained acceptance back above the breakdown level|Breakout low; then range-height projection|Strong bull closes regain the old range
9|Long|channel|Lower edge of an orderly bull channel|Pullbacks remain corrective after the initial spike|Failed bear attempt at a channel support area|Bear breakout through the last higher low with follow-through|Channel high|The channel is mature, crowded into resistance, or already breaking down
10|Short|channel|Upper edge of an orderly bear channel|Rallies remain corrective after the initial spike|Failed bull attempt at channel resistance|Bull breakout above the last lower high with follow-through|Channel low|The channel is exhausting into major support
11|Long|small|Brief pause in a small-pullback bull trend|Bears cannot sustain even a modest correction|Renewed bull pressure after a pause or H1|A meaningful lower high followed by a strong bear break|Next realistic continuation magnet|A wide entry bar makes the structural stop unaffordable
12|Short|small|Brief pause in a small-pullback bear trend|Bulls repeatedly fail to sustain a rally|Renewed bear pressure after a pause or L1|A meaningful higher low followed by a strong bull break|Next realistic downside magnet|A selloff is already at support with insufficient remaining reward
13|Both|twoleg|Second corrective leg into trend support|Both countertrend legs fail to produce a change of control|Reversal after the second leg and renewed trend pressure|Failure of the correction extreme|Prior trend extreme|The second leg is accelerating rather than losing pressure
14|Long|deep|New reversal structure after a deep pullback|The old trend is uncertain; buyers must rebuild evidence|Failed breakdown, higher low, and bull follow-through|Failure of the newly formed reversal low|Prior lower high or range midpoint|The only argument is that price is cheaper than the old high
15|Both|flag|Late flag close to a trend extreme|Continuation is still strong, but the trend is mature|Flag breakout with follow-through and room to a target|Immediate failed breakout back into the flag|Nearest measured-move magnet|The breakout is climactic or its target is too close
16|Long|rangefail|Just below a mature range low|Sellers break support but cannot sustain prices below it|Reclaim into the range followed by a bull trigger|Failure below the rejected breakout low|Range midpoint|Price is accepting below the range in a strong bear breakout
17|Short|rangefail|Just above a mature range high|Buyers break resistance but cannot sustain prices above it|Return into the range followed by a bear trigger|Failure above the rejected breakout high|Range midpoint|Price is accepting above the range in a strong bull breakout
18|Long|range2|Lower edge of a mature trading range|Sellers fail twice to achieve downside continuation|Second bull trigger at the range edge|Break below the range extreme|Range midpoint|The second attempt develops in the middle of the range
19|Short|range2|Upper edge of a mature trading range|Buyers fail twice to achieve upside continuation|Second bear trigger at the range edge|Break above the range extreme|Range midpoint|The second attempt is a pause in a strong bull breakout
20|Long|double|Retest of a range swing low|The second test cannot establish new selling pressure|Bull signal above the second-bottom structure|Failure below the double bottom|Midpoint or prior swing high|Equal lows appear without rejection or a credible trigger
21|Short|double|Retest of a range swing high|The second test cannot establish new buying pressure|Bear signal below the second-top structure|Failure above the double top|Midpoint or prior swing low|Equal highs appear without rejection or a credible trigger
22|Long|vacuum|Accelerating test of a range low|The fast move reaches a magnet, then sellers fail|Failed breakdown and confirmed return into the range|Failure below the vacuum extreme|Range midpoint|Buying simply because the move was fast or touched support
23|Short|vacuum|Accelerating test of a range high|The rally reaches a magnet, then buyers fail|Failed breakout and confirmed return into the range|Failure above the vacuum extreme|Range midpoint|Selling the first touch without rejection
24|Short|disappoint|Middle-to-upper part of a balanced range|A weak bull breakout disappoints its buyers|Bear response after the failed bull attempt|Strong bull breakout with follow-through|Nearby equilibrium or midpoint|The proposed scalp has poor reward after costs
25|Wait|compression|Tight overlap with no accepted direction|Breakouts in both directions repeatedly fail|Wait for a directional breakout and follow-through, then reassess|A later breakout thesis fails if price returns into compression|Range-height projection only after a valid breakout|Predicting direction from the middle of the compression
26|Both|opposite|Opposite boundary after a failed breakout|One side is trapped and the other achieves real follow-through|Pullback after the opposite-side breakout|Regaining and accepting inside the old range|Measured move beyond the new breakout|The opposite breakout also lacks follow-through
27|Both|broadening|Rejected extreme of an expanding range|Higher highs and lower lows reveal poor directional control|Rejection and reversal at an outer extreme|A break beyond the rejected extreme|Range middle|Mistaking every new extreme for trend confirmation
28|Wait|middle|Middle of a trading range|Nearby targets are small relative to a structural stop|No entry; wait for an edge or accepted breakout|Reassess only when location or market state changes|No target while flat|Inventing an entry because standing aside feels unproductive
29|Short|mtr|Failed high retest after a bull trend-line break|Bulls cannot resume the trend after a meaningful bear response|Bear trigger after the lower high or failed new high|Break above the retest high|Prior higher low or nearest support|Selling a trend-line break before testing bull strength
30|Long|mtr|Failed low retest after a bear trend-line break|Bears cannot resume the trend after a meaningful bull response|Bull trigger after the higher low or failed new low|Break below the retest low|Prior lower high or nearest resistance|Buying a trend-line break without a failed resumption test
31|Long|wedge|Third push down reaching support|New lows have weakening follow-through or greater overlap|Bull reversal or break of the bear micro-channel|Break below the wedge extreme|Prior lower high or origin of the final leg|All three pushes remain powerful and closes remain bearish
32|Short|wedge|Third push up reaching resistance|New highs have weakening follow-through or greater overlap|Bear reversal or break of the bull micro-channel|Break above the wedge extreme|Prior higher low or origin of the final leg|All three pushes remain powerful and closes remain bullish
33|Long|parabolic|Accelerating selloff into a climax|Momentum is extreme; exhaustion still needs confirmation|Bull reversal, failed bear resumption, and follow-through|Break below the climax low|First resistance in a potential two-legged correction|Buying an accelerating decline before sellers fail
34|Short|parabolic|Accelerating rally into a climax|Momentum is extreme; exhaustion still needs confirmation|Bear reversal, failed bull resumption, and follow-through|Break above the climax high|First support in a potential two-legged correction|Selling an accelerating rally before buyers fail
35|Short|climax|Late bull climax followed by a weak new high|Urgent buying is followed by failed continuation|Bear control after a failed bull retest|Break above the climax extreme|EMA area or base of the climax|Assuming every large bull bar ends the trend
36|Long|climax|Late bear climax followed by a weak new low|Urgent selling is followed by failed continuation|Bull control after a failed bear retest|Break below the climax extreme|EMA area or origin of the final selloff|Assuming every large bear bar ends the trend
37|Long|microdouble|Close retest of a sell-climax low|The second low attracts less selling and is rejected|Bull trigger after the small double bottom|Failure of the second-low structure|Nearby resistance or EMA area|Treating a visual double bottom as confirmation by itself
38|Short|microdouble|Close retest of a buy-climax high|The second high attracts less buying and is rejected|Bear trigger after the small double top|Failure of the second-high structure|Nearby support or EMA area|Treating a visual double top as confirmation by itself
39|Both|finalfail|Failed breakout from a mature trend flag|Late breakout traders lose their expected continuation|Opposite-side confirmation back through the flag|Renewed acceptance beyond the failed breakout extreme|Opposite flag edge, then EMA area|Calling a flag final before an actual failure
40|Both|overshoot|Outside a mature channel boundary|The overshoot fails and the market returns to the channel|Opposite follow-through or a failed extreme retest|Break beyond the overshoot high or low|EMA area or opposite channel area|Trading the overshoot alone
41|Both|magap|A bar fully separated from the moving average|Separation is context; it does not prove a trend reversal|For a reversal thesis, require a trend break and failed resumption test|Failure of the tested reversal extreme|Nearest opposing structure before a deeper correction|Confusing a gap bar with an automatic reversal signal
42|Long|trap|Reclaimed support after a breakdown fails|Breakdown sellers lose acceptance below their entry area|Strong reclaim followed by a bull entry trigger|Failure below the rejected breakdown|Next resistance or range midpoint|Assuming a wick alone proves sellers are trapped
43|Short|trap|Lost resistance after an upside breakout fails|Breakout buyers lose acceptance above their entry area|Strong return below the level followed by a bear trigger|Failure above the rejected breakout|Next support or range midpoint|Assuming a wick alone proves buyers are trapped
44|Both|badentry|Obvious signal in poor location|An apparent continuation entry immediately meets opposing structure|Clear rejection of the original stop-entry setup|Acceptance in the direction of the original breakout|Opposite side of the local structure|Fading a signal before it actually fails
45|Both|countertrap|Failed countertrend attempt inside a strong trend|Countertrend entries cannot attract follow-through|Trend-direction break beyond the failed countertrend signal|Failure of the trend pullback structure|Prior trend extreme|The countertrend move has already broken structure with strength
46|Long|pressure|Repeated tests of the upper range boundary|Stronger bull closes and shallower pullbacks accumulate|Accepted breakout or successful breakout pullback|Deep return and acceptance inside the range|Range-height measured move|Buying directly into resistance before it breaks
47|Short|pressure|Repeated tests of the lower range boundary|Stronger bear closes and weaker rallies accumulate|Accepted breakdown or successful breakdown pullback|Return and acceptance above the broken range low|Range-height measured move|Buying the range low despite increasing selling pressure
48|Long|hidden|Lower lows with increasingly weak selling|Rejected lows and more bull bars suggest emerging buying|Trend-line break, higher low, and bull trigger|Failure below the higher-low structure|Nearest lower high before larger reversal targets|Treating hidden pressure as a completed reversal
49|Short|hidden|Higher highs with increasingly weak buying|Rejected highs and more bear bars suggest emerging selling|Trend-line break, lower high, and bear trigger|Failure above the lower-high structure|Nearest higher low before larger reversal targets|Treating hidden pressure as a completed reversal
50|Long|gapaccept|Opening gap above prior resistance|Early gap-fill attempts fail; strong closes hold higher prices|First credible pullback that holds the breakout area|Acceptance back inside the prior range|Opening projection or next higher-timeframe magnet|Assuming a gap is accepted before observing the response
51|Both|gapreject|Opening gap that returns to the old range|The gap fails to attract continued participation|Confirmation after returning inside the prior range|Break beyond the failed opening extreme|Prior close or nearest internal magnet|Expecting every opening gap to fill
52|Both|overnight|Test of an overnight extreme during the open|The regular-session test fails to achieve acceptance|Opposite-side trigger after reclaiming the level|Break beyond the rejected overnight test|Open, VWAP area, or nearest opening-range magnet|Trading the overnight level without rejection evidence
53|Both|opening|Breakout from a balanced opening range|Strong breakout bars and subsequent closes show acceptance|Pullback that holds outside the opening range|Return and acceptance inside the opening range|Opening-range height projection|Chasing a large breakout bar with poor structural reward
54|Wait|chaos|Open with large reversals in both directions|Follow-through is poor and control is unresolved|Stay flat until acceptance or a clear edge failure develops|Reassess when a directional premise becomes supported|None until the context qualifies|Taking every opening reversal as a new trend
55|Both|magnet|Trend approaching a measured projection|Continuation pressure is intact and room remains|A valid continuation setup before reaching the magnet|Failure of that continuation structure|The measured-move projection|Treating a projection as an automatic reversal signal
56|Both|prior|Trend approaching an obvious prior extreme|Opposition may pause while the market tests the level|Continuation only with room; reversal only after failure|Failure of the chosen continuation or reversal structure|Prior high or low|Fading a strong move simply because it approaches a prior extreme
57|Both|gapclose|Price moving toward the prior close|Pressure favors a gap test while countertrend interest waits|A valid setup in the direction of the gap-close magnet|Failure of the supporting swing structure|Prior close|Expecting movement through the magnet without reassessment
58|Long|probe|Possible failure at major range support|Selling weakens, but confirmation is incomplete|Optional research-only probe under a predefined plan|The predefined stop beyond the extreme; no additions|A realistic opposing magnet|Using a probe to justify averaging into a losing trade
59|Long|earlyprobe|Climactic decline at major support|Always-In remains short; the reversal is still speculative|Advanced research-only probe with an accepted fixed loss|Continuation through the predefined extreme|A plausible two-legged correction|Calling overextension confirmation or enlarging a failed probe
60|Long|confirmed|Higher low after a trend-line break and low test|Bears fail to resume and buyers supply stronger evidence|Confirmed bull trigger after the higher low|Failure of the new higher-low structure|Nearest opposing swing, then reevaluate|Chasing confirmation when too little reward remains
'''

NOTES={}
for line in ROWS.strip().splitlines():
    parts=line.split('|')
    assert len(parts)==9,(parts[0],len(parts))
    ident,direction,diagram,location,evidence,trigger,invalidation,target,avoid=parts
    NOTES[int(ident)]=dict(direction=direction,diagram=diagram,location=location,evidence=evidence,trigger=trigger,invalidation=invalidation,target=target,avoid=avoid)

# Coordinates represent relative illustrative price, not historical data.
# All base sequences are in the long orientation except the noted reversal patterns.
# Mapping: prices, annotated points, protected stop, first target, structural level.
PATTERNS={
'spike':([20,22,21,27,36,48,61,73,78,76,73,71,72,70,74,79],[3,8,13,15],67,88,70),
'second':([20,27,35,46,56,68,72,68,63,66,61,57,59,64,68],[5,9,12,14],53,76,57),
'ema':([22,30,39,36,45,53,50,59,67,63,59,56,54,57,62],[4,8,12,14],49,70,54),
'breakout':([35,46,54,49,40,50,55,48,53,64,74,72,65,61,63,68],[6,10,13,15],56,83,57),
'channel':([18,25,38,52,65,61,57,65,71,67,63,72,78,72,68,74],[4,8,14,15],62,83,63),
'small':([20,28,36,34,42,51,49,58,66,63,71,77,74,80],[2,8,12,13],68,89,70),
'twoleg':([20,30,43,56,69,74,69,62,58,62,66,62,55,51,55,61],[5,8,13,15],46,75,51),
'deep':([20,33,47,64,78,72,64,54,45,38,42,49,54,48,46,52,58],[4,9,14,16],41,67,46),
'flag':([20,31,43,39,51,63,70,76,73,75,72,75,79,84],[5,7,11,13],68,93,76),
'rangefail':([62,73,62,49,42,52,64,72,65,51,42,36,33,41,48,53],[3,10,12,15],28,61,42),
'range2':([67,73,65,52,43,49,56,51,44,40,44,49,53],[2,6,9,12],35,62,42),
'double':([65,71,60,49,40,44,54,61,54,46,41,44,50,55],[2,4,10,13],36,65,40),
'vacuum':([60,68,63,56,63,69,71,65,57,43,30,35,42,47],[3,7,10,13],25,61,40),
'disappoint':([43,56,66,56,45,53,63,69,66,65,60,54,49],[2,7,9,12],74,41,68),
'compression':([44,65,48,61,50,60,52,58,53,57,54,57,55,56],[1,5,10,13],40,75,56),
'opposite':([43,56,68,63,52,61,69,75,68,56,43,34,29,35,39,33],[6,7,11,15],46,19,43),
'broadening':([50,62,47,67,42,71,36,68,75,61,43,30,37,45],[3,8,11,13],25,55,35),
'middle':([42,55,72,62,43,52,68,61,52,56,51,55,53,54],[2,4,10,13],39,72,55),
'mtr':([79,70,75,65,56,64,51,43,35,39,49,56,50,43,41,47,54],[6,8,10,16],36,65,41),
'wedge':([79,70,60,66,71,61,52,45,51,57,49,41,36,40,47,53],[2,7,12,15],31,62,36),
'parabolic':([86,84,80,82,76,69,73,61,48,53,35,18,29,36,30,28,37,43],[4,8,11,17],13,56,28),
'climax':([85,77,72,74,64,55,60,46,28,23,32,39,29,25,32,41],[5,9,13,15],18,55,25),
'microdouble':([78,69,61,55,46,29,24,32,36,30,25,29,35,40],[3,6,10,13],20,53,25),
'finalfail':([21,31,43,54,66,74,71,73,70,74,81,78,70,65,62],[4,8,10,14],85,51,70),
'overshoot':([25,32,40,36,48,57,51,64,71,66,78,89,82,75,70],[4,8,11,14],94,57,77),
'magap':([25,35,48,61,72,77,72,66,59,52,58,66,70,64,59,53],[5,9,12,15],75,41,62),
'trap':([63,70,58,46,39,51,60,55,44,35,29,38,46,52],[4,9,10,13],24,63,39),
'badentry':([35,43,56,65,59,54,58,55,61,67,72,66,60,54],[3,8,10,13],77,43,68),
'countertrap':([22,34,43,39,52,62,57,63,71,66,59,64,71,76],[4,8,10,13],54,85,59),
'pressure':([42,65,47,66,52,67,57,68,61,68,65,69,76,83],[3,7,11,13],61,95,70),
'hidden':([79,69,58,65,59,49,55,50,42,48,45,40,49,55,49,47,55,61],[2,8,11,17],42,71,47),
'gapaccept':([36,40,37,43,39,42,67,73,79,75,71,73,79,85],[4,6,10,13],65,94,62),
'gapreject':([36,41,38,44,40,43,75,79,73,65,58,54,59,53,47],[4,6,10,14],84,40,62),
'overnight':([47,57,69,63,52,58,67,74,80,73,67,63,68,61],[2,8,10,13],85,50,72),
'opening':([44,61,48,66,53,64,57,63,58,64,74,81,75,71,76,83],[3,8,11,15],65,95,68),
'chaos':([40,66,35,74,41,70,36,69,44,72,39,65,48,58],[1,3,8,13],29,80,55),
'magnet':([20,27,39,34,47,55,51,62,70,66,63,69,76],[4,8,10,12],58,91,91),
'prior':([38,56,76,70,59,48,54,63,59,68,73,68,69,72],[2,6,10,13],63,76,76),
'gapclose':([74,79,76,81,78,80,42,36,44,48,43,51,57,54,61,68],[4,7,10,15],48,80,80),
'probe':([70,63,68,56,48,51,40,33,36,31,34,38],[2,6,9,11],26,63,33),
'earlyprobe':([89,85,79,81,70,61,65,52,38,42,27,19,24,29],[4,8,11,13],14,54,19),
'confirmed':([78,68,72,61,50,55,41,31,38,49,58,51,43,40,47,55,62],[4,7,9,16],35,74,40),
}

# These base shapes end in a bearish decision; mirror only when needed.
BEAR_BASE={'disappoint','opposite','finalfail','overshoot','magap','badentry','gapreject','overnight'}
