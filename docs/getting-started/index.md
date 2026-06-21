# Getting Started

Card scripting is easier when the moving pieces have names:

- `cards.cdb` stores card names, text, stats, types, and category flags.
- `Scripts/c{id}.lua` stores the Lua script for that card.
- `initial_effect(c)` registers the effects that the engine will use.
- The generated API reference explains what `Duel`, `Card`, `Effect`, `Group`,
  and `aux` functions expect.

## Path

1. [Setup](setup)
2. [Your First Card](first-card)
3. [Reading Card Scripts](reading-scripts)
