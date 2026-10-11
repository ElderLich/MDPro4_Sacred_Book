# RushDuel.GetBaseAttackOnDestroy

Alias: `RD.GetBaseAttackOnDestroy`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetBaseAttackOnDestroy(any c) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
获取被破坏时的基础攻击力
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:189`

```lua
function RushDuel.GetBaseAttackOnDestroy(c)
    local atk
    if RushDuel.IsPreviousMaximumMode(c) and c:IsReason(REASON_DESTROY) then
        atk = c.maximum_attack
    else
        atk = c:GetTextAttack()
    end
    return math.max(0, atk)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.GetBaseAttackOnDestroy) with `RushDuel.GetBaseAttackOnDestroy`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Elemental HERO Shining Flare Wingman | `120264000` | [Rush/Scripts/c120264000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264000.lua) | 1 |
| Elemental HERO Flame Wingman | `120263001` | [Rush/Scripts/c120263001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263001.lua) | 1 |

## Script Examples

### Elemental HERO Shining Flare Wingman (`120264000`)

Source: [Rush/Scripts/c120264000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264000.lua)

```lua
function cm.damop(e,tp,eg,ep,ev,re,r,rp,tc)
	if tc then
		local dam=RD.GetBaseAttackOnDestroy(tc)
		Duel.Hint(HINT_CARD,0,m)
		Duel.Damage(1-tp,dam,REASON_EFFECT)
```

### Elemental HERO Flame Wingman (`120263001`)

Source: [Rush/Scripts/c120263001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263001.lua)

```lua
function cm.damop(e,tp,eg,ep,ev,re,r,rp,tc)
	if tc then
		local dam=RD.GetBaseAttackOnDestroy(tc)
		Duel.Hint(HINT_CARD,0,m)
		Duel.Damage(1-tp,dam,REASON_EFFECT)
```
