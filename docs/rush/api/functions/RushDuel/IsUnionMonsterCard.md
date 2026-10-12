# RushDuel.IsUnionMonsterCard

Alias: `RD.IsUnionMonsterCard`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsUnionMonsterCard(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 卡片是同盟怪兽卡
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:9`

```lua
function RushDuel.IsUnionMonsterCard(card)
    return card:GetOriginalType()&TYPE_UNION==TYPE_UNION
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsUnionMonsterCard) with `RushDuel.IsUnionMonsterCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Lostream Reading | `120309043` | [Rush/Scripts/c120309043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309043.lua) | 1 |
| Lostream Stream | `120309046` | [Rush/Scripts/c120309046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309046.lua) | 1 |
| Cross Lostream Melutine | `120309036` | [Rush/Scripts/c120309036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309036.lua) | 1 |
| Cross Lostream Verdias | `120309035` | [Rush/Scripts/c120309035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309035.lua) | 1 |

## Script Examples

### Lostream Reading (`120309043`)

Source: [Rush/Scripts/c120309043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309043.lua)

```lua
end
function cm.filter(c)
	return c:IsFaceup() and RD.IsUnionMonsterCard(c) and c:GetSequence()<5 and c:IsAbleToHand()
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```

### Lostream Stream (`120309046`)

Source: [Rush/Scripts/c120309046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309046.lua)

```lua
end
function cm.filter(c)
	return c:IsFaceup() and RD.IsUnionMonsterCard(c) and c:IsAbleToGrave()
end
function cm.exfilter(c)
```

### Cross Lostream Melutine (`120309036`)

Source: [Rush/Scripts/c120309036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309036.lua)

```lua
--Multiple Attack
function cm.confilter(c)
	return c:IsFaceup() and RD.IsUnionMonsterCard(c)
end
function cm.filter(c,ct)
```
