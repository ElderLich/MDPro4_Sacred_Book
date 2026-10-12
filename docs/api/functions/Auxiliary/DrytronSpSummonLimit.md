# Auxiliary.DrytronSpSummonLimit

## Signature

```lua
Auxiliary.DrytronSpSummonLimit(Effect e, Card c, int sump, int sumtype, int sumpos, int targetp, Effect se) -> void
```

## Description

Oath target for the shared Drytron cost; it prevents Special Summoning monsters that can be Normal Summoned/Set, excluding cards whose original type is Spell/Trap or Trap Monster.

## Parameters

- `e` `Effect`
- `c` `Card`
- `sump` `int`
- `sumtype` `int`
- `sumpos` `int`
- `targetp` `int`
- `se` `Effect`

## Source

- `Utilities/utility.lua:1057`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.DrytronSpSummonLimit) with `Auxiliary.DrytronSpSummonLimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Drytron Nova | `94187078` | [Scripts/c94187078.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94187078.lua) | 1 |

## Script Examples

### Drytron Nova (`94187078`)

Source: [Scripts/c94187078.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94187078.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
	e1:SetTargetRange(1,0)
	e1:SetTarget(Auxiliary.DrytronSpSummonLimit)
	e1:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e1,tp)
```
