# MDPro3 Sacred Book

<div class="sacred-home-hero">
  <div class="home-copy">
    <p class="home-kicker">MDPro3 / YGOPro Lua scripting</p>
    <h2>Learn card scripting one working effect at a time.</h2>
    <p>Start with a card file, build real effects, then use local script examples and generated API pages when you need exact behavior.</p>
    <div class="home-actions">
      <a class="home-primary" href="learn/">Start Learning</a>
      <a class="home-secondary" href="learn/common-script-errors-and-debugging">Debug a Script</a>
    </div>
  </div>
  <div class="home-code-panel" aria-label="Example Lua effect block">
    <div class="home-code-top">
      <span>c12345678.lua</span>
      <span>activated effect</span>
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

<div class="home-start-path" aria-label="Beginner learning path">
  <a href="learn/script-structure">
    <strong>Start</strong>
    <span>Read a card file</span>
    <small><code>GetID</code>, <code>initial_effect</code>, and callback names</small>
  </a>
  <a href="learn/effect-object">
    <strong>Build</strong>
    <span>Create an effect</span>
    <small>Set type, code, range, target, and operation</small>
  </a>
  <a href="learn/activated-effects">
    <strong>Resolve</strong>
    <span>Follow a Chain Link</span>
    <small>Legality, cost, target, and operation flow</small>
  </a>
  <a href="learn/selection-and-group-handling">
    <strong>Select</strong>
    <span>Handle cards safely</span>
    <small>Targets, Groups, relation checks, and stored state</small>
  </a>
</div>

## Start Here

<div class="home-portal-grid">
  <a class="home-portal-card" href="learn/">
    <small>Beginner path</small>
    <strong>Learn</strong>
    <span>Follow a progression from script anatomy through effects, Chains, Groups, movement, card types, and common mistakes.</span>
  </a>
  <a class="home-portal-card" href="api/">
    <small>Exact signatures</small>
    <strong>API</strong>
    <span>Use generated function and constant pages sourced from this repository's local MDPro3/YGOPro data.</span>
  </a>
  <a class="home-portal-card" href="examples/">
    <small>Local scripts</small>
    <strong>Examples</strong>
    <span>Read featured card pages and focused case studies that point back to local <code>Scripts/</code> files.</span>
  </a>
  <a class="home-portal-card" href="tools/script-explorer">
    <small>Search by use</small>
    <strong>Script Explorer</strong>
    <span>Find real cards by ID, name, script path, or API call when you need another pattern to compare against.</span>
  </a>
  <a class="home-portal-card" href="roadmap">
    <small>Project status</small>
    <strong>Roadmap</strong>
    <span>See what has been covered, what is still planned, and how the source-checking work is being tracked.</span>
  </a>
</div>

## Beginner Progression

1. [Structure of a card script](learn/script-structure)
2. [Creation, building, and registration of an effect object](learn/effect-object)
3. [EFFECT_TYPE constants and templates](learn/effect-types)
4. [Conditions, costs, activation procedures, and resolution](learn/effect-callbacks)
5. [Activated effects](learn/activated-effects)
6. [Activation legality](learn/activation-legality)
7. [Selection and Group handling](learn/selection-and-group-handling)
8. [Common script errors and debugging](learn/common-script-errors-and-debugging)

## Reference While Scripting

- [Function reference](api/functions/)
- [Constant reference](api/constants)
- [Featured card examples](examples/)
- [Script Explorer](tools/script-explorer)
- [Downloaded tutorial coverage map](tools/page-analysis)
