# Duel.GetCounter

## Signature

```lua
Duel.GetCounter(int player, int s, int o, int countertype) -> int
```

## Description

Returns the number of counterstype types that exist on the farm
S represents the position of the player's own removable pointer, o represents the position of the opponent's removable pointer for the player

## Parameters

- `player` `int`
- `s` `int`
- `o` `int`
- `countertype` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4879`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **12** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetCounter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua) | 61 |
| Dimonno Vaalmonica | `30432463` | [Scripts/c30432463.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30432463.lua) | 53 |
| Mythical Beast Master Cerberus | `53842431` | [Scripts/c53842431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53842431.lua) | 49 |
| Enneapolis | `17621695` | [Scripts/c17621695.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17621695.lua) | 48 |
| Battle Shogun of the Six Samurai | `74752631` | [Scripts/c74752631.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74752631.lua) | 48 |
| Predaplant Moray Nepenthes | `22011689` | [Scripts/c22011689.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22011689.lua) | 44 |
| Starving Venemy Lethal Dose Dragon | `22070401` | [Scripts/c22070401.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22070401.lua) | 43 |
| Tempest Magician | `63101919` | [Scripts/c63101919.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63101919.lua) | 40 |
| Six Strike - Sextuple Barrage | `90939874` | [Scripts/c90939874.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90939874.lua) | 39 |
| Snowdust Giant | `73659078` | [Scripts/c73659078.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73659078.lua) | 31 |
| Cloudian - Nimbusman | `20003527` | [Scripts/c20003527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20003527.lua) | 29 |
| Cold Enchanter | `24661486` | [Scripts/c24661486.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24661486.lua) | 26 |

## Script Examples

### Starving Venemy Dragon (`93729065`)

Source: [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua)

```lua
end
function c93729065.atkval(e,c)
	return Duel.GetCounter(0,1,1,0x104f)*-200
end
function c93729065.rdcon(e,tp,eg,ep,ev,re,r,rp)
```

### Dimonno Vaalmonica (`30432463`)

Source: [Scripts/c30432463.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30432463.lua)

```lua
end
function s.adval(e,c)
	return Duel.GetCounter(e:GetHandlerPlayer(),1,0,0x6a)*-100
end
function s.pzcost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Mythical Beast Master Cerberus (`53842431`)

Source: [Scripts/c53842431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53842431.lua)

```lua
end
function c53842431.incon(e)
	return Duel.GetCounter(e:GetHandlerPlayer(),1,0,0x1)>=4
end
function c53842431.rmcost(e,tp,eg,ep,ev,re,r,rp,chk)
```
