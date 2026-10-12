# RushDuel.ValueDoubleTributeMix

Alias: `RD.ValueDoubleTributeMix`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ValueDoubleTributeMix(any ignore, any code, any attribute, any type, any level, any race, any attack, any defense) -> any
```

## Description

Rush Duel helper declared in `RDValue.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
效果值: 双重解放
```

## Parameters

- `ignore` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `attribute` `any`: Type and behavior are not yet reviewed; see the source.
- `type` `any`: Type and behavior are not yet reviewed; see the source.
- `level` `any`: Type and behavior are not yet reviewed; see the source.
- `race` `any`: Type and behavior are not yet reviewed; see the source.
- `attack` `any`: Type and behavior are not yet reviewed; see the source.
- `defense` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDValue.lua:37`

```lua
function RushDuel.ValueDoubleTributeMix(ignore, code, attribute, type, level, race, attack, defense)
    return function(e, c)
        if e == nil then
            return ignore, RushDuel._private_double_tribute_info(code, attribute, type, level, race, attack, defense)
        end
        return (code == nil or c:IsCode(code))
            and (attribute == nil or c:IsAttribute(attribute))
            and (type == nil or c:IsType(type))
            and (level == nil or c:IsLevel(level))
            and (race == nil or c:IsRace(race))
            and (attack == nil or c:IsAttack(attack))
            and (defense == nil or c:IsDefense(defense))
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ValueDoubleTributeMix) with `RushDuel.ValueDoubleTributeMix`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Multiply Skull | `120261041` | [Rush/Scripts/c120261041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261041.lua) | 1 |

## Script Examples

### Multiply Skull (`120261041`)

Source: [Rush/Scripts/c120261041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261041.lua)

```lua
end
--Double Tribute
cm.trival=RD.ValueDoubleTributeMix(true,nil,ATTRIBUTE_DARK,TYPE_EFFECT,nil,RACE_FIEND,0,0)
```
