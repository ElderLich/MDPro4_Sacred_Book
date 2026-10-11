# RushDuel.ValueDoubleTributeAll

Alias: `RD.ValueDoubleTributeAll`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ValueDoubleTributeAll(any ignore) -> any
```

## Description

Rush Duel helper declared in `RDValue.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
效果值: 双重解放 全范围
```

## Parameters

- `ignore` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDValue.lua:52`

```lua
function RushDuel.ValueDoubleTributeAll(ignore)
    return function(e, c)
        if e == nil then
            return ignore, 1
        end
        return true
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ValueDoubleTributeAll) with `RushDuel.ValueDoubleTributeAll`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Bikuribot | `120109043` | [Rush/Scripts/c120109043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109043.lua) | 1 |
| Furtunate Cat | `120246016` | [Rush/Scripts/c120246016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246016.lua) | 1 |
| Excutie Power Up! | `120208052` | [Rush/Scripts/c120208052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208052.lua) | 1 |
| Beast Swords - Tiger Sabre | `120228058` | [Rush/Scripts/c120228058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228058.lua) | 1 |

## Script Examples

### Bikuribot (`120109043`)

Source: [Rush/Scripts/c120109043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109043.lua)

```lua
end
--Special Summon
cm.trival=RD.ValueDoubleTributeAll()
function cm.spfilter(c,e,tp)
	return c:IsLevel(7) and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP)
```

### Furtunate Cat (`120246016`)

Source: [Rush/Scripts/c120246016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246016.lua)

```lua
end
--Discard Deck
cm.trival=RD.ValueDoubleTributeAll()
function cm.spfilter(c,e,tp)
	return c:IsCode(list[1]) and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP)
```

### Excutie Power Up! (`120208052`)

Source: [Rush/Scripts/c120208052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208052.lua)

```lua
end
--Activate
cm.trival=RD.ValueDoubleTributeAll()
function cm.filter(c)
	return c:IsFaceup() and RD.IsCanAttachDoubleTribute(c,cm.trival)
```
