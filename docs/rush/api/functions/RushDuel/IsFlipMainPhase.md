# RushDuel.IsFlipMainPhase

Alias: `RD.IsFlipMainPhase`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsFlipMainPhase(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 这张卡反转的自己主要阶段
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:52`

```lua
function RushDuel.IsFlipMainPhase(card)
    return card:GetFlagEffect(FLAG_FLIP_MAIN_PHASE) ~= 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsFlipMainPhase) with `RushDuel.IsFlipMainPhase`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Crystal Seer](/examples/rush-cards/120109067) | `120109067` | [Rush/Scripts/c120109067.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109067.lua) | 1 |
| Aussa the Earth Charmer | `120301001` | [Rush/Scripts/c120301001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301001.lua) | 1 |
| Eria the Water Charmer | `120301002` | [Rush/Scripts/c120301002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301002.lua) | 1 |
| Hiita the Fire Charmer | `120301003` | [Rush/Scripts/c120301003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301003.lua) | 1 |
| Wynn the Wind Charmer | `120301004` | [Rush/Scripts/c120301004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301004.lua) | 1 |

## Script Examples

### Crystal Seer (`120109067`)

Source: [Rush/Scripts/c120109067.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109067.lua)

```lua
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return RD.IsFlipMainPhase(c)
		or Duel.IsExistingMatchingCard(cm.confilter,tp,LOCATION_MZONE,0,1,c)
end
```

### Aussa the Earth Charmer (`120301001`)

Source: [Rush/Scripts/c120301001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301001.lua)

```lua
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return RD.IsFlipMainPhase(c)
		or Duel.IsExistingMatchingCard(cm.confilter,tp,LOCATION_MZONE,0,1,c)
end
```

### Eria the Water Charmer (`120301002`)

Source: [Rush/Scripts/c120301002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301002.lua)

```lua
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return RD.IsFlipMainPhase(c)
		or Duel.IsExistingMatchingCard(cm.confilter,tp,LOCATION_MZONE,0,1,c)
end
```
