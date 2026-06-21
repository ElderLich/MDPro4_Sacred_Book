# Learning Path

This section teaches MDPro3/YGOPro Lua card scripting from the shape of a card
script up to real effect resolution. It is written for this project and links
back into the generated API reference and live card examples.

<div class="sacred-grid">
  <a class="sacred-card" href="script-structure">
    <strong>Script structure</strong>
    <span>How one card file is loaded and where effects are registered.</span>
  </a>
  <a class="sacred-card" href="effect-object">
    <strong>Effect objects</strong>
    <span>The practical order for CreateEffect, setters, and RegisterEffect.</span>
  </a>
  <a class="sacred-card" href="effect-types">
    <strong>Effect types</strong>
    <span>Common EFFECT_TYPE values and the templates they usually imply.</span>
  </a>
  <a class="sacred-card" href="moving-cards">
    <strong>Moving cards</strong>
    <span>Which Duel functions send, destroy, banish, summon, equip, or set cards.</span>
  </a>
</div>

## Suggested Order

1. Start with [Structure of a card script](script-structure).
2. Build an effect in [Creation, building, and registration of an effect object](effect-object).
3. Choose timing and shape in [EFFECT_TYPE constants and templates](effect-types).
4. Write callbacks with [Conditions, costs, activation procedures, and resolution](effect-callbacks).
5. Check legality with [Activation legality](activation-legality).
6. Work with cards and groups through [Filters, Card objects, and Group objects](filters-and-groups).
7. Move cards correctly with [Functions that move cards across locations](moving-cards).
8. Use card families through [Archetypes and set codes](archetypes-and-setcodes).

## Useful Reference While Learning

- [Function index](/api/functions/)
- [Constants](/api/constants)
- [Featured script examples](/examples/)
