# Setup

You need three things when learning scripts:

- A script editor.
- A card database (`cards.cdb`) with the card's text and stats.
- A scripts folder containing `c{id}.lua` files.

For this book, the reference data is local to this repository. The generated
examples use `cards.cdb` and `Scripts/` directly.

## File Names

If a card has ID `12345678`, its script is usually:

```text
Scripts/c12345678.lua
```

The engine loads that script and calls:

```lua
function c12345678.initial_effect(c)
  -- register effects here
end
```

Modern scripts often use `local s,id=GetID()` instead, but the idea is the same:
the script binds code to one card ID.
