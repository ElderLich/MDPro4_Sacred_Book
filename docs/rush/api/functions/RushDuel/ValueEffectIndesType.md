# RushDuel.ValueEffectIndesType

Alias: `RD.ValueEffectIndesType`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ValueEffectIndesType(any self_type, any opponent_type, any ignore) -> any
```

## Description

Rush Duel helper declared in `RDValue.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
效果值: 效果破坏抗性 抵抗类型
```

## Parameters

- `self_type` `any`: Type and behavior are not yet reviewed; see the source.
- `opponent_type` `any`: Type and behavior are not yet reviewed; see the source.
- `ignore` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDValue.lua:108`

```lua
function RushDuel.ValueEffectIndesType(self_type, opponent_type, ignore)
    local s_type = self_type or 0
    local o_type = opponent_type or 0
    return function(e, re, rp)
        if e == nil then
            return ignore or false, s_type, o_type
        end
        local op = e:GetOwnerPlayer()
        if rp == op then
            return s_type ~= 0 and re:IsActiveType(s_type)
        else
            return o_type ~= 0 and re:IsActiveType(o_type)
        end
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **168** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ValueEffectIndesType) with `RushDuel.ValueEffectIndesType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lufer the Symbol of the Devils](/examples/rush-cards/120309059) | `120309059` | [Rush/Scripts/c120309059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309059.lua) | 1 |
| [Rising Protect](/examples/rush-cards/120304055) | `120304055` | [Rush/Scripts/c120304055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304055.lua) | 1 |
| [Sunset Rebirth](/examples/rush-cards/120257066) | `120257066` | [Rush/Scripts/c120257066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257066.lua) | 1 |
| [Supreme Machine Magnum Overlord](/examples/rush-cards/120150002) | `120150002` | [Rush/Scripts/c120150002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120150002.lua) | 1 |
| Fusionic Defense | `120257064` | [Rush/Scripts/c120257064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257064.lua) | 1 |
| Sevens Road Protection | `120217021` | [Rush/Scripts/c120217021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217021.lua) | 1 |
| Super Princess of the Flock - Max Mutton \[L\] | `120293007` | [Rush/Scripts/c120293007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293007.lua) | 1 |
| Voidvelg Kyrie | `120244006` | [Rush/Scripts/c120244006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244006.lua) | 1 |
| Celeb Rose Influencers | `120257044` | [Rush/Scripts/c120257044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257044.lua) | 1 |
| Sevens Road Charmy Witch | `120260062` | [Rush/Scripts/c120260062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260062.lua) | 1 |
| Tamabot King Golem | `120285039` | [Rush/Scripts/c120285039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285039.lua) | 1 |
| Voidvelg Elysium | `120227001` | [Rush/Scripts/c120227001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120227001.lua) | 1 |
| Voidvelg Elysium | `120273004` | [Rush/Scripts/c120273004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120273004.lua) | 1 |
| Divinebreath the Orchestral Music Fiend | `120247018` | [Rush/Scripts/c120247018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247018.lua) | 1 |
| Fate of the World | `120271054` | [Rush/Scripts/c120271054.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271054.lua) | 1 |
| Roaring Firestorm Volcalize Phoenix | `120249016` | [Rush/Scripts/c120249016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249016.lua) | 1 |
| OuTerverSe Burst Oblivion | `120290008` | [Rush/Scripts/c120290008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290008.lua) | 1 |
| Eternal Galactica Oblivion | `120244035` | [Rush/Scripts/c120244035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244035.lua) | 1 |
| Abysskite Ultimail | `120239048` | [Rush/Scripts/c120239048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239048.lua) | 1 |
| Dragonic Escape | `120249062` | [Rush/Scripts/c120249062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249062.lua) | 1 |
| Ultra Evolution Miracle | `120274051` | [Rush/Scripts/c120274051.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120274051.lua) | 1 |
| Conduction Alchemicalizer Suirai | `120254042` | [Rush/Scripts/c120254042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254042.lua) | 1 |
| Transam Variable Linac | `120245002` | [Rush/Scripts/c120245002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120245002.lua) | 1 |
| Wish of OuTerverSe the World-Shattering Emperor \[L\] | `120293058` | [Rush/Scripts/c120293058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293058.lua) | 1 |
| ...and 144 more |  |  |  |

## Script Examples

### Lufer the Symbol of the Devils (`120309059`)

Source: [Rush/Scripts/c120309059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309059.lua)

```lua
end
--Activate
cm.indval=RD.ValueEffectIndesType(TYPE_MONSTER+TYPE_SPELL+TYPE_TRAP,TYPE_MONSTER+TYPE_SPELL+TYPE_TRAP)
function cm.confilter(c,tp)
	return c:GetSummonPlayer()==tp
```

### Rising Protect (`120304055`)

Source: [Rush/Scripts/c120304055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304055.lua)

```lua
end
--Activate
cm.indval=RD.ValueEffectIndesType(TYPE_MONSTER+TYPE_SPELL+TYPE_TRAP,TYPE_MONSTER+TYPE_SPELL+TYPE_TRAP)
function cm.filter(c)
	return (cm.filter1(c) or cm.filter2(c)) and c:IsAbleToHand()
```

### Sunset Rebirth (`120257066`)

Source: [Rush/Scripts/c120257066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257066.lua)

```lua
end
--Activate
cm.indval=RD.ValueEffectIndesType(0,TYPE_MONSTER+TYPE_SPELL+TYPE_TRAP)
function cm.confilter(c,tp)
	return RD.IsPreviousControler(c,tp) and c:IsPreviousLocation(LOCATION_MZONE)
```
