# Duel.Damage

## Signature

```lua
Duel.Damage(int player, int value, int reason, [bool is_step]) -> int
```

## Description

To the reason reason to give players the player caused value damage, the actual value of the damage received
The return value is 0 if the damage becomes an effect such as a reply.
Is_step to true is the damage / recovery LP process decomposition, need to call Duel.RDComplete() trigger point

## Parameters

- `player` `int`
- `value` `int`
- `reason` `int`
- `is_step` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4901`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **817** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.Damage`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua) | 63 |
| [Enneacraft - Aiza.LEON](/examples/cards/82359538) | `82359538` | [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82359538.lua) | 62 |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua) | 61 |
| Vaylantz Genesis Grand Duke | `76075139` | [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76075139.lua) | 60 |
| Trickstar Light Stage | `35371948` | [Scripts/c35371948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35371948.lua) | 60 |
| Forbidden Dark Contract with the Swamp King | `10833828` | [Scripts/c10833828.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10833828.lua) | 59 |
| Chaos Emperor, the Dragon of Armageddon | `4538826` | [Scripts/c4538826.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4538826.lua) | 58 |
| Grandpa Demetto | `44190146` | [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44190146.lua) | 58 |
| Meklord Astro Mekanikle | `63468625` | [Scripts/c63468625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63468625.lua) | 57 |
| Number 4: Stealth Kragen | `67557908` | [Scripts/c67557908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67557908.lua) | 55 |
| Genex Ally Triforce | `52709508` | [Scripts/c52709508.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52709508.lua) | 55 |
| Gladiator Beast Gaiodiaz | `90957527` | [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90957527.lua) | 54 |
| Cupid Pitch | `21915012` | [Scripts/c21915012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21915012.lua) | 54 |
| Indiora Doom Volt the Cubic Emperor | `3775068` | [Scripts/c3775068.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3775068.lua) | 53 |
| Meklord Astro the Eradicator | `2992036` | [Scripts/c2992036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2992036.lua) | 53 |
| Vulcan Dragni the Cubic King | `77387463` | [Scripts/c77387463.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77387463.lua) | 53 |
| Chaos Emperor Dragon - Envoy of the End | `82301904` | [Scripts/c82301904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82301904.lua) | 53 |
| Dark Contract with the Swamp King | `73360025` | [Scripts/c73360025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73360025.lua) | 53 |
| D/D/D Super Doom King Bright Armageddon | `72402069` | [Scripts/c72402069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72402069.lua) | 52 |
| Master Spirit Tech Force - Pendulum Ruler | `68508433` | [Scripts/c68508433.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68508433.lua) | 52 |
| Black-Winged Assault Dragon | `73218989` | [Scripts/c73218989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73218989.lua) | 52 |
| Earthbound Servant Geo Gremlina | `33202303` | [Scripts/c33202303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33202303.lua) | 52 |
| Raidraptor - Rising Rebellion Falcon | `71222868` | [Scripts/c71222868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71222868.lua) | 52 |
| Vanquish Soul Heavy Borger | `92895501` | [Scripts/c92895501.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92895501.lua) | 52 |
| ...and 793 more |  |  |  |

## Script Examples

### Enneacraft - Archa.TAIL (`81237046`)

Source: [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua)

```lua
function s.damop1(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_CARD,0,id)
	Duel.Damage(1-tp,900,REASON_EFFECT)
end
function s.regcon(e,tp,eg,ep,ev,re,r,rp)
```

### Enneacraft - Aiza.LEON (`82359538`)

Source: [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82359538.lua)

```lua
	Duel.Hint(HINT_CARD,0,id)
	local ct=eg:FilterCount(Card.IsControler,nil,1-tp)
	Duel.Damage(1-tp,ct*900,REASON_EFFECT)
end
function s.regcon(e,tp,eg,ep,ev,re,r,rp)
```

### Starving Venemy Dragon (`93729065`)

Source: [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua)

```lua
			tc:RegisterEffect(e6)
		end
		Duel.Damage(1-tp,500,REASON_EFFECT)
	end
end
```
