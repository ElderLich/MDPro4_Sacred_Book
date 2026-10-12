# Duel.Damage

## Signature

```lua
Duel.Damage(int player, int value, int reason, [bool is_step]) -> int
```

## Description

Deals value effect damage to player for reason and returns the damage actually applied.
If damage is changed into LP recovery or prevented, the return value reflects the final applied damage. Negative input amounts are clamped to 0 by the local binding.
With is_step=true, finish the damage/recovery batch with Duel.RDComplete.

## How To Use It

Use this during resolution when a player takes effect damage or another scripted damage action.

```lua
local dealt=Duel.Damage(1-tp,800,REASON_EFFECT)
if dealt>0 then
    -- follow-up that requires actual damage
end
```

The return value is the actual damage applied. If damage is reversed, prevented, or the input amount is below 0, the returned damage can be 0. For simultaneous LP changes, pass `is_step=true` for each call and finish with `Duel.RDComplete()`.

## Related Functions

- [Duel.Recover](/api/functions/Duel/Recover)
- [Duel.RDComplete](/api/functions/Duel/RDComplete)
- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)

## Parameters

- `player` `int`
- `value` `int`
- `reason` `int`
- `is_step` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4901`

## Guided Examples

Learn how to use this function in context:

- [LP Recovery and Effect Damage](/learn/lp-recovery-and-damage)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **824** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.Damage) with `Duel.Damage`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Destiny HERO - Destro-Dogma](/examples/cards/25158975) | `25158975` | [Scripts/c25158975.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25158975.lua) | 1 |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81237046.lua) | 2 |
| [Enneacraft - Aiza.LEON](/examples/cards/82359538) | `82359538` | [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82359538.lua) | 2 |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93729065.lua) | 1 |
| Vaylantz Genesis Grand Duke | `76075139` | [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76075139.lua) | 1 |
| Trickstar Light Stage | `35371948` | [Scripts/c35371948.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35371948.lua) | 1 |
| Forbidden Dark Contract with the Swamp King | `10833828` | [Scripts/c10833828.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10833828.lua) | 1 |
| Chaos Emperor, the Dragon of Armageddon | `4538826` | [Scripts/c4538826.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4538826.lua) | 1 |
| Grandpa Demetto | `44190146` | [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44190146.lua) | 1 |
| Meklord Astro Mekanikle | `63468625` | [Scripts/c63468625.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63468625.lua) | 1 |
| Number 4: Stealth Kragen | `67557908` | [Scripts/c67557908.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67557908.lua) | 1 |
| Genex Ally Triforce | `52709508` | [Scripts/c52709508.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52709508.lua) | 1 |
| Gladiator Beast Gaiodiaz | `90957527` | [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90957527.lua) | 1 |
| Cupid Pitch | `21915012` | [Scripts/c21915012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21915012.lua) | 1 |
| Indiora Doom Volt the Cubic Emperor | `3775068` | [Scripts/c3775068.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3775068.lua) | 1 |
| Meklord Astro the Eradicator | `2992036` | [Scripts/c2992036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2992036.lua) | 1 |
| Vulcan Dragni the Cubic King | `77387463` | [Scripts/c77387463.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77387463.lua) | 1 |
| Chaos Emperor Dragon - Envoy of the End | `82301904` | [Scripts/c82301904.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82301904.lua) | 1 |
| Dark Contract with the Swamp King | `73360025` | [Scripts/c73360025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73360025.lua) | 1 |
| D/D/D Super Doom King Bright Armageddon | `72402069` | [Scripts/c72402069.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72402069.lua) | 1 |
| Master Spirit Tech Force - Pendulum Ruler | `68508433` | [Scripts/c68508433.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c68508433.lua) | 1 |
| Black-Winged Assault Dragon | `73218989` | [Scripts/c73218989.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73218989.lua) | 1 |
| Earthbound Servant Geo Gremlina | `33202303` | [Scripts/c33202303.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33202303.lua) | 1 |
| Raidraptor - Rising Rebellion Falcon | `71222868` | [Scripts/c71222868.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71222868.lua) | 1 |
| ...and 800 more |  |  |  |

## Script Examples

### Destiny HERO - Destro-Dogma (`25158975`)

Source: [Scripts/c25158975.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25158975.lua)

```lua
function s.damop2(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_CARD,0,id)
	Duel.Damage(1-tp,2000,REASON_EFFECT)
end
function s.fspcon(e,tp,eg,ep,ev,re,r,rp)
```

### Enneacraft - Archa.TAIL (`81237046`)

Source: [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81237046.lua)

```lua
function s.damop1(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_CARD,0,id)
	Duel.Damage(1-tp,900,REASON_EFFECT)
end
function s.regcon(e,tp,eg,ep,ev,re,r,rp)
```

### Enneacraft - Aiza.LEON (`82359538`)

Source: [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82359538.lua)

```lua
	Duel.Hint(HINT_CARD,0,id)
	local ct=eg:FilterCount(Card.IsControler,nil,1-tp)
	Duel.Damage(1-tp,ct*900,REASON_EFFECT)
end
function s.regcon(e,tp,eg,ep,ev,re,r,rp)
```
