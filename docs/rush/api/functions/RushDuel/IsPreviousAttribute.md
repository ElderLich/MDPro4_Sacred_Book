# RushDuel.IsPreviousAttribute

Alias: `RD.IsPreviousAttribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPreviousAttribute(any card, any attr) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 位置变化前的属性
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `attr` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:202`

```lua
function RushDuel.IsPreviousAttribute(card, attr)
    return (card:GetPreviousAttributeOnField() & attr) ~= 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPreviousAttribute) with `RushDuel.IsPreviousAttribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Collapsing Chairs | `120150041` | [Rush/Scripts/c120150041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120150041.lua) | 1 |
| Dark Nebula | `120235059` | [Rush/Scripts/c120235059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235059.lua) | 1 |
| Resurrection of the Blaze Fiends | `120231017` | [Rush/Scripts/c120231017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231017.lua) | 1 |
| Climax Clash | `120208060` | [Rush/Scripts/c120208060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120208060.lua) | 1 |
| Imaginary Arc Turnback | `120196014` | [Rush/Scripts/c120196014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120196014.lua) | 1 |

## Script Examples

### Collapsing Chairs (`120150041`)

Source: [Rush/Scripts/c120150041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120150041.lua)

```lua
	return RD.IsPreviousControler(c,tp) and c==Duel.GetAttackTarget()
		and c:IsPreviousPosition(POS_FACEUP_ATTACK)
		and RD.IsPreviousAttribute(c,ATTRIBUTE_DARK)
		and RD.IsPreviousAttack(c,0)
end
```

### Dark Nebula (`120235059`)

Source: [Rush/Scripts/c120235059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235059.lua)

```lua
function cm.confilter(c,tp)
	return RD.IsPreviousControler(c,tp) and c==Duel.GetAttackTarget()
		and RD.IsPreviousAttribute(c,ATTRIBUTE_DARK)
		and RD.IsPreviousRace(c,RACE_GALAXY)
		and RD.IsPreviousAttackAbove(c,1500)
```

### Resurrection of the Blaze Fiends (`120231017`)

Source: [Rush/Scripts/c120231017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231017.lua)

```lua
	return RD.IsPreviousControler(c,tp) and c==Duel.GetAttackTarget()
		and RD.IsPreviousType(c,TYPE_MAXIMUM)
		and RD.IsPreviousAttribute(c,ATTRIBUTE_FIRE)
end
function cm.spfilter(c,e,tp)
```
