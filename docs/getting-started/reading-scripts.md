# Reading Card Scripts

Read a card script in this order:

1. Find `initial_effect`.
2. List every `Effect.CreateEffect(c)`.
3. For each effect, read its type, code, property, range, category, and count
   limit.
4. Follow the condition, cost, target, and operation callbacks.
5. Look up unfamiliar engine calls in the API reference.

## Small Vocabulary

- `c`: the card whose script is running.
- `e`: the effect currently being checked or resolved.
- `tp`: the player who controls or activates the effect.
- `eg`, `ep`, `ev`, `re`, `r`, `rp`: event information.
- `Group`: a set of cards selected or collected by the engine.

## Example Reading Habit

When you see:

```lua
Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)
```

Open `Duel.SpecialSummon` in the function reference and compare each argument
with the script. This is the fastest way to move from copying patterns to
understanding them.
