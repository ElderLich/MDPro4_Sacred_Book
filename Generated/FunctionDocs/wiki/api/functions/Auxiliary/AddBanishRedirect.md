# Auxiliary.AddBanishRedirect

## Signature

```lua
Auxiliary.AddBanishRedirect(Card c, [function condition]) -> void
```

## Description

Registers an EFFECT_LEAVE_FIELD_REDIRECT effect that banishes c when condition is true, defaulting to face-up c.

## Parameters

- `c` `Card`
- `condition` `function` optional - default: face-up condition

## Source

- `Utilities/utility.lua:1932`
