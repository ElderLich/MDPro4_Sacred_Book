# MDPro3 Sacred Book

<div class="home-console">
  <section class="home-console-main">
    <p class="home-kicker">MDPro3 / YGOPro Lua scripting</p>
    <h2>Start with one card. Learn the engine around it.</h2>
    <p>Use the beginner path when you are learning, the API when you need exact calls, and the Script Explorer when you want a real local pattern fast.</p>
    <div class="home-actions">
      <a class="home-primary" href="learn/">Start Learning</a>
      <a class="home-secondary" href="learn/first-custom-card">Write A Card</a>
      <a class="home-secondary" href="tools/script-explorer">Search Scripts</a>
    </div>
  </section>
  <section class="home-console-code" aria-label="Example Lua effect block">
    <div class="home-code-top">
      <span>first activated effect</span>
      <span>c55144522.lua</span>
    </div>
    <pre><code>local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_DRAW)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetTarget(s.target)
e1:SetOperation(s.activate)
c:RegisterEffect(e1)</code></pre>
  </section>
</div>

<div class="home-choice-grid" aria-label="Primary documentation entry points">
  <a class="home-choice home-choice-primary" href="learn/">
    <small>Guided path</small>
    <strong>Learn</strong>
    <span>Read scripts, build small effects, wire card data, then debug with structure.</span>
  </a>
  <a class="home-choice" href="api/">
    <small>Exact calls</small>
    <strong>API</strong>
    <span>Generated functions and constants from the local MDPro3/YGOPro data.</span>
  </a>
  <a class="home-choice" href="examples/">
    <small>Real cards</small>
    <strong>Examples</strong>
    <span>Featured local scripts with detected API calls and source links.</span>
  </a>
  <a class="home-choice" href="tools/script-explorer">
    <small>Find patterns</small>
    <strong>Script Explorer</strong>
    <span>Search by card text, type, category, ID, script path, or function use.</span>
  </a>
</div>

## Beginner Curve

<div class="home-stepper">
  <a href="learn/script-structure"><b>01</b><span>Read a card file</span></a>
  <a href="learn/first-scripts"><b>02</b><span>Study local patterns</span></a>
  <a href="learn/beginner-script-ladder"><b>03</b><span>Build small effects</span></a>
  <a href="learn/first-custom-card"><b>04</b><span>Write your first card</span></a>
  <a href="learn/effect-callbacks"><b>05</b><span>Trace activation flow</span></a>
  <a href="learn/common-script-errors-and-debugging"><b>06</b><span>Debug safely</span></a>
</div>

## Choose Your Branch

<div class="home-branch-grid">
  <a href="learn/targeting-flow">Target or select cards</a>
  <a href="learn/moving-cards">Move cards</a>
  <a href="learn/spell-card-patterns">Script Spells</a>
  <a href="learn/trap-card-patterns">Script Traps</a>
  <a href="learn/continuous-effects">Continuous effects</a>
  <a href="learn/ritual-procedure">Summon procedures</a>
  <a href="learn/archetypes-and-setcodes">Archetypes</a>
  <a href="learn/client-ui-and-prompt-behavior">Client prompts</a>
</div>

## Reference

- [Function reference](api/functions/)
- [Constant reference](api/constants)
- [Featured card examples](examples/)
- [Script Explorer](tools/script-explorer)

## Credits & Support

<div class="home-credit-panel">
  <div>
    <strong>Created and documented by Senator John.</strong>
    <p>If Sacred Book helped you learn scripting, build a card, or find the right local pattern faster, consider supporting the work on <a href="https://ko-fi.com/senatorjohn1">Ko-fi</a>.</p>
  </div>
  <div>
    <strong>Documentation inspiration</strong>
    <p>Credit to the <a href="https://ygoproscripting.miraheze.org/wiki/Main_Page">YGOPro Scripting Wiki</a> and <a href="https://ygoproscripting.miraheze.org/wiki/User:XGlitchy30">Glitchy</a> for wiki notes and scripting explanations that helped inspire this learning reference.</p>
  </div>
  <div>
    <strong>Upstream YGOPro projects</strong>
    <p>MDPro3 builds on the YGOPro ecosystem, including <a href="https://github.com/Fluorohydride/ygopro">Fluorohydride/ygopro</a>, <a href="https://github.com/Fluorohydride/ygopro-core">Fluorohydride/ygopro-core</a>, and <a href="https://github.com/Fluorohydride/ygopro-scripts">Fluorohydride/ygopro-scripts</a>.</p>
  </div>
</div>
