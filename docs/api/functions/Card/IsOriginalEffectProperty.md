# Card.IsOriginalEffectProperty

## Signature

```lua
Card.IsOriginalEffectProperty(Card c, function filter) -> bool
```

## Description

Checks whether c is originally a card with an effect matching filter.

## Parameters

- `c` `Card`
- `filter` `function` - filter(Effect)

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3510`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsOriginalEffectProperty`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Armament Reincarnation | `53770666` | [Scripts/c53770666.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53770666.lua) | 1 |
| Liberator Eto | `24643913` | [Scripts/c24643913.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24643913.lua) | 1 |
| Learning Elf | `32126000` | [Scripts/c32126000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32126000.lua) | 1 |

## Script Examples

### Armament Reincarnation (`53770666`)

Source: [Scripts/c53770666.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53770666.lua)

```lua
end
function s.eqfilter(c)
	return c:IsType(TYPE_EQUIP) or c:IsType(TYPE_TRAP) and c:IsOriginalEffectProperty(s.equip_filter)
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Liberator Eto (`24643913`)

Source: [Scripts/c24643913.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24643913.lua)

```lua
end
function s.cfilter(c)
	return c:IsOriginalEffectProperty(s.quick_filter) and c:GetOriginalType()&TYPE_MONSTER==TYPE_MONSTER and c:IsFaceupEx()
end
function s.spcon(e,c)
```

### Learning Elf (`32126000`)

Source: [Scripts/c32126000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32126000.lua)

```lua
end
function s.ssfilter(c)
	return c:IsType(TYPE_TRAP) and c:IsSSetable() and c:IsOriginalEffectProperty(s.equip_filter)
end
function s.sstg(e,tp,eg,ep,ev,re,r,rp,chk)
```
