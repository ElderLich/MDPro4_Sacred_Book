# RushDuel.IsDefenseBelow

Alias: `RD.IsDefenseBelow`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsDefenseBelow(any card, any def) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 守备力在 def 以下
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `def` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:99`

```lua
function RushDuel.IsDefenseBelow(card, def)
    return card:IsDefenseBelow(def) and not RushDuel.IsMaximumMode(card)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **12** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsDefenseBelow) with `RushDuel.IsDefenseBelow`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Soul Flip | `120301055` | [Rush/Scripts/c120301055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301055.lua) | 1 |
| Mezame the Ringing Alarm | `120199015` | [Rush/Scripts/c120199015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199015.lua) | 1 |
| Healthie Sati | `120306024` | [Rush/Scripts/c120306024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306024.lua) | 1 |
| Seyanen the Blazing Conqueror | `120246050` | [Rush/Scripts/c120246050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246050.lua) | 1 |
| Ancient Arise Dragon | `120145024` | [Rush/Scripts/c120145024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120145024.lua) | 1 |
| Jointech Stegosilos | `120231044` | [Rush/Scripts/c120231044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231044.lua) | 1 |
| Makiu, the Magical Mist | `120205058` | [Rush/Scripts/c120205058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120205058.lua) | 1 |
| Yokai Tiger Orient Strike | `120222057` | [Rush/Scripts/c120222057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120222057.lua) | 1 |
| Animagica Leader | `120260074` | [Rush/Scripts/c120260074.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260074.lua) | 1 |
| Speed Major | `120301057` | [Rush/Scripts/c120301057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301057.lua) | 1 |
| Mormolith | `120285027` | [Rush/Scripts/c120285027.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285027.lua) | 1 |
| Magical Sevens Fusion | `120285050` | [Rush/Scripts/c120285050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285050.lua) | 1 |

## Script Examples

### Soul Flip (`120301055`)

Source: [Rush/Scripts/c120301055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301055.lua)

```lua
--Activate
function cm.confilter(c,tp)
	return c:GetSummonPlayer()==tp and c:IsLevelBelow(4) and RD.IsDefenseBelow(c,1400)
end
function cm.exfilter(c)
```

### Mezame the Ringing Alarm (`120199015`)

Source: [Rush/Scripts/c120199015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199015.lua)

```lua
end
function cm.atktg(e,c)
	return RD.IsDefenseBelow(c,1900)
end
```

### Healthie Sati (`120306024`)

Source: [Rush/Scripts/c120306024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306024.lua)

```lua
--Special Summon
function cm.spfilter(c,e,tp)
	return RD.IsDefenseBelow(c,1300) and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP_DEFENSE)
end
function cm.posfilter(c,e,tp)
```
