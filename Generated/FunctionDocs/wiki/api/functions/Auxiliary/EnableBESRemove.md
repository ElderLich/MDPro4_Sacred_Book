# Auxiliary.EnableBESRemove

## Signature

```lua
Auxiliary.EnableBESRemove(Card c) -> void
```

## Description

Registers the shared B.E.S. maintenance trigger on c. After c battles, it removes one 0x1f counter if possible; otherwise it destroys c.

## Parameters

- `c` `Card`

## Source

- `Utilities/utility.lua:1796`
