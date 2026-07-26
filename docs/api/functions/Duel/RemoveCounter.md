# Duel.RemoveCounter

## Signature

```lua
Duel.RemoveCounter(int player, int s, int o, int countertype, int count, int reason) -> bool
```

## Description

Lets player remove count counters of countertype from the selected field locations for reason and returns whether removal succeeded.
s marks locations on player's own field and o marks locations on the opponent's field, from player's perspective. The core can offer applicable counter-removal replacement effects before removing counters.

## Parameters

- `player` `int`
- `s` `int`
- `o` `int`
- `countertype` `int`
- `count` `int`
- `reason` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4877`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **58** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.RemoveCounter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Endymion, the Mighty Master of Magic | `3611830` | [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3611830.lua) | 1 |
| Magister of Endymion | `66104644` | [Scripts/c66104644.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66104644.lua) | 1 |
| Lightsworn Sanctuary | `52665542` | [Scripts/c52665542.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52665542.lua) | 1 |
| Mythical Beast Master Cerberus | `53842431` | [Scripts/c53842431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53842431.lua) | 1 |
| Mythical Beast Medusa | `54965929` | [Scripts/c54965929.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54965929.lua) | 1 |
| Mythical Beast Garuda | `28570310` | [Scripts/c28570310.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28570310.lua) | 1 |
| Chaos Zone | `94243005` | [Scripts/c94243005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94243005.lua) | 1 |
| Mythical Beast Jackal | `91182675` | [Scripts/c91182675.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91182675.lua) | 1 |
| Fire Fortress atop Liang Peak | `66750703` | [Scripts/c66750703.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66750703.lua) | 3 |
| Selene, Queen of the Master Magicians | `45819647` | [Scripts/c45819647.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45819647.lua) | 1 |
| Synchro World | `36742774` | [Scripts/c36742774.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36742774.lua) | 1 |
| Signal Warrior | `9634146` | [Scripts/c9634146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9634146.lua) | 1 |
| Mythical Institution | `94599451` | [Scripts/c94599451.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94599451.lua) | 1 |
| Cosmic Fortress Gol'gar | `68319538` | [Scripts/c68319538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68319538.lua) | 1 |
| Mythical Beast Bashilisk | `80959027` | [Scripts/c80959027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80959027.lua) | 1 |
| Symphonic Warrior Miccs | `5399521` | [Scripts/c5399521.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5399521.lua) | 1 |
| Jizukiru, the Star Destroying Kaiju | `63941210` | [Scripts/c63941210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63941210.lua) | 1 |
| Gateway of the Six | `27970830` | [Scripts/c27970830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27970830.lua) | 3 |
| Black Feather Whirlwind | `7602800` | [Scripts/c7602800.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7602800.lua) | 1 |
| Kumongous, the Sticky String Kaiju | `29726552` | [Scripts/c29726552.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29726552.lua) | 1 |
| Mature Chronicle | `92650749` | [Scripts/c92650749.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92650749.lua) | 5 |
| Gadarla, the Mystery Dust Kaiju | `36956512` | [Scripts/c36956512.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36956512.lua) | 1 |
| Super Anti-Kaiju War Machine Mecha-Dogoran | `84769941` | [Scripts/c84769941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84769941.lua) | 1 |
| Supreme Arcanite Magician | `21113684` | [Scripts/c21113684.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21113684.lua) | 1 |
| ...and 34 more |  |  |  |

## Script Examples

### Endymion, the Mighty Master of Magic (`3611830`)

Source: [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3611830.lua)

```lua
function c3611830.descost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsCanRemoveCounter(tp,1,0,0x1,6,REASON_COST) end
	Duel.RemoveCounter(tp,1,0,0x1,6,REASON_COST)
end
function c3611830.cfilter(c)
```

### Magister of Endymion (`66104644`)

Source: [Scripts/c66104644.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66104644.lua)

```lua
function c66104644.spcost2(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsCanRemoveCounter(tp,1,0,0x1,3,REASON_COST) end
	Duel.RemoveCounter(tp,1,0,0x1,3,REASON_COST)
end
function c66104644.spfilter2(c,e,tp)
```

### Lightsworn Sanctuary (`52665542`)

Source: [Scripts/c52665542.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52665542.lua)

```lua
function c52665542.desop(e,tp,eg,ep,ev,re,r,rp)
	local count=e:GetLabel()
	Duel.RemoveCounter(tp,1,0,0x5,count*2,REASON_EFFECT)
end
```
