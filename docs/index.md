# MDPro3 Sacred Book

<div class="sacred-home-hero">
  <div class="home-copy">
    <p class="home-kicker">MDPro3 / YGOPro Lua scripting</p>
    <h2>From first card file to real Chain resolution.</h2>
    <p>Practical, source-checked documentation for writing and reading MDPro3 card scripts.</p>
    <div class="home-actions">
      <a class="home-primary" href="learn/">Start Learning</a>
      <a class="home-secondary" href="tools/script-explorer">Explore Scripts</a>
    </div>
  </div>
  <div class="home-code-panel" aria-label="Example Lua effect block">
    <div class="home-code-top">
      <span>c12345678.lua</span>
      <span>effect block</span>
    </div>
    <pre><code>local e1=Effect.CreateEffect(c)
e1:SetDescription(aux.Stringid(id,0))
e1:SetCategory(CATEGORY_TOHAND)
e1:SetType(EFFECT_TYPE_IGNITION)
e1:SetRange(LOCATION_MZONE)
e1:SetTarget(s.thtg)
e1:SetOperation(s.thop)
c:RegisterEffect(e1)</code></pre>
  </div>
</div>

<div class="home-route">
  <a href="learn/script-structure">
    <strong>1</strong>
    <span>Script structure</span>
  </a>
  <a href="learn/effect-object">
    <strong>2</strong>
    <span>Build effects</span>
  </a>
  <a href="learn/activated-effects">
    <strong>3</strong>
    <span>Activate and resolve</span>
  </a>
  <a href="learn/filters-and-groups">
    <strong>4</strong>
    <span>Find cards</span>
  </a>
  <a href="learn/continuous-effects">
    <strong>5</strong>
    <span>Apply rules</span>
  </a>
</div>

## Start Here

<div class="sacred-grid">
  <a class="sacred-card" href="learn/">
    <strong>Learning path</strong>
    <span>A complete beginner route from card script anatomy to activated effects, Groups, movement, Equip Cards, LP changes, and continuous rules.</span>
  </a>
  <a class="sacred-card" href="tools/script-explorer">
    <strong>Script Explorer</strong>
    <span>Search local card scripts by ID, name, path, or API call and jump into real examples.</span>
  </a>
  <a class="sacred-card" href="api/">
    <strong>API reference</strong>
    <span>Generated function and constant pages from this repository's MDPro3/YGOPro data.</span>
  </a>
  <a class="sacred-card" href="tools/page-analysis">
    <strong>Tutorial coverage</strong>
    <span>The downloaded tutorial-topic audit and where each original Sacred Book equivalent lives.</span>
  </a>
</div>

## Core Lessons

- [Structure of a card script](learn/script-structure)
- [Creation, building, and registration of an effect object](learn/effect-object)
- [Activated effects](learn/activated-effects)
- [Activation legality](learn/activation-legality)
- [Filters, Card objects, and Group objects](learn/filters-and-groups)
- [Functions that move cards across locations](learn/moving-cards)
- [Continuous stat modifiers](learn/continuous-stat-modifiers)
- [Equip Spells and Equip Cards](learn/equip-spells)
- [LP Recovery and Effect Damage](learn/lp-recovery-and-damage)

## Reference

- [Function reference](api/functions/)
- [Constant reference](api/constants)
- [Featured card examples](examples/)
- [Roadmap](roadmap)
