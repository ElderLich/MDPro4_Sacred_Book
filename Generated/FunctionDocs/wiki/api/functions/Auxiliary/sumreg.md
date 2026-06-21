# Auxiliary.sumreg

## Signature

```lua
Auxiliary.sumreg(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Used by Yosenju Yamamisaki (39853199) and some other cards (49249907, 93368494), though the purpose of this function is unclear.
Card 54109233, while not using this function, uses a similar implementation with an unclear purpose, equivalent to
function aux.sumreg(e, tp, eg, ep, ev, re, r, rp)
  local tc=eg:GetFirst()
  local code=e:GetLabel()
  while tc do
    if tc:GetOriginalCode()==code then
      tc:RegisterFlagEffect(code, RESET_EVENT+0x1ec0000+RESET_PHASE+PHASE_END, 0, 1)
    end
    tc=eg:GetNext()
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

- `Utilities/utility.lua:848`
