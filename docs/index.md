# MDPro3 Sacred Book

<div class="sacred-home-hero">
  <div class="home-copy">
    <p class="home-kicker">MDPro3 / YGOPro Lua scripting</p>
    <h2>Learn card scripting by building real effects.</h2>
    <p>Start with a working card file, follow a few small local scripts, then use the lessons and generated API pages when you need exact behavior.</p>
    <div class="home-actions">
      <a class="home-primary" href="learn/">Start Learning</a>
      <a class="home-secondary" href="learn/beginner-script-ladder">Build The Ladder</a>
      <a class="home-secondary" href="tools/script-explorer">Find Local Examples</a>
    </div>
  </div>
  <div class="home-code-panel" aria-label="Example Lua effect block">
    <div class="home-code-top">
      <span>c55144522.lua</span>
      <span>first activated effect</span>
    </div>
    <pre><code>local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_DRAW)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetTarget(s.target)
e1:SetOperation(s.activate)
c:RegisterEffect(e1)</code></pre>
  </div>
</div>

<div class="home-start-path" aria-label="Beginner learning path">
  <a href="learn/script-structure">
    <strong>1</strong>
    <span>Read a script</span>
    <small>Understand <code>GetID</code>, <code>initial_effect</code>, effects, filters, and callbacks.</small>
  </a>
  <a href="learn/first-scripts">
    <strong>2</strong>
    <span>Study five real patterns</span>
    <small>Draw, target, prompt, continuous, and stat-based local examples.</small>
  </a>
  <a href="learn/beginner-script-ladder">
    <strong>3</strong>
    <span>Build small effects</span>
    <small>Walk through complete draw, target, Group, trigger, Quick-Play, and Trap scripts.</small>
  </a>
  <a href="learn/effect-callbacks">
    <strong>4</strong>
    <span>Follow activation flow</span>
    <small>Condition, cost, target, operation, and <code>chk==0</code> legality.</small>
  </a>
  <a href="learn/targeting-flow">
    <strong>5</strong>
    <span>Choose cards safely</span>
    <small>Targets, Groups, relation checks, and resolution choices.</small>
  </a>
  <a href="learn/common-script-errors-and-debugging">
    <strong>6</strong>
    <span>Debug with structure</span>
    <small>Trace invisible prompts, nil values, stale targets, and reset mistakes.</small>
  </a>
</div>

## Start Here

<div class="home-portal-grid">
  <a class="home-portal-card" href="learn/">
    <small>Guided curriculum</small>
    <strong>Learn</strong>
    <span>Follow the beginner curve first, then branch into card types, summon procedures, outcomes, and debugging.</span>
  </a>
  <a class="home-portal-card" href="learn/beginner-script-ladder">
    <small>Concrete practice</small>
    <strong>Script Ladder</strong>
    <span>Build up from tiny complete scripts before jumping into the full lesson library.</span>
  </a>
  <a class="home-portal-card" href="api/">
    <small>Exact signatures</small>
    <strong>API</strong>
    <span>Generated function and constant pages from local MDPro3/YGOPro data.</span>
  </a>
  <a class="home-portal-card" href="examples/">
    <small>Local scripts</small>
    <strong>Examples</strong>
    <span>Featured card pages and case studies that point back to local script files.</span>
  </a>
  <a class="home-portal-card" href="tools/script-explorer">
    <small>Search by use</small>
    <strong>Script Explorer</strong>
    <span>Find cards by ID, name, script path, or API call when you need another pattern.</span>
  </a>
  <a class="home-portal-card" href="roadmap">
    <small>Project status</small>
    <strong>Roadmap</strong>
    <span>Track what has been covered, what is planned, and which source checks were used.</span>
  </a>
</div>

## Beginner Curve

1. [Structure of a card script](learn/script-structure)
2. [First Scripts To Study](learn/first-scripts)
3. [Beginner Script Ladder](learn/beginner-script-ladder)
4. [Creation, building, and registration of an effect object](learn/effect-object)
5. [EFFECT_TYPE constants and templates](learn/effect-types)
6. [Conditions, costs, activation procedures, and resolution](learn/effect-callbacks)
7. [Activated effects](learn/activated-effects)
8. [Activation legality](learn/activation-legality)
9. [Targeting flow](learn/targeting-flow)
10. [Selection and Group handling](learn/selection-and-group-handling)
11. [Client UI and prompt behavior](learn/client-ui-and-prompt-behavior)
12. [Common script errors and debugging](learn/common-script-errors-and-debugging)

After that, choose the branch that matches the card you are scripting: Spells,
Traps, summon procedures, card movement, continuous effects, player effects,
or special card families.

## Reference While Scripting

- [Function reference](api/functions/)
- [Constant reference](api/constants)
- [Featured card examples](examples/)
- [Script Explorer](tools/script-explorer)
- [Downloaded tutorial coverage map](tools/page-analysis)
