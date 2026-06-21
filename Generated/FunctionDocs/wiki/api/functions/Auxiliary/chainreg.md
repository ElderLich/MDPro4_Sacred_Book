# Auxiliary.chainreg

## Signature

```lua
Auxiliary.chainreg(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Used by Dark Armed Dragon (81059524), equivalent to
function aux.chainreg(e, tp, eg, ep, ev, re, r, rp)
  if e:GetHandler():GetFlagEffect(1)==0 then
    e:GetHandler():RegisterFlagEffect(1, RESET_EVENT+RESETS_STANDARD-RESET_TURN_SET+RESET_CHAIN, 0, 1)
  end
end

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `any`
- `re` `Effect`
- `r` `any`
- `rp` `int`

## Source

- `Utilities/utility.lua:814`
