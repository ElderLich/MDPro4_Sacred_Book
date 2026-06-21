# Duel.CheckLPCost

## Signature

```lua
Duel.CheckLPCost(int player, int cost, [bool must_pay]) -> bool
```

## Description

Checks whether player can pay the specified LP cost.

## Parameters

- `player` `int`
- `cost` `int`
- `must_pay` `bool` optional - default: false

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4908`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **352** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.CheckLPCost`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ultra Polymerization](/examples/cards/76647978) | `76647978` | [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76647978.lua) | 71 |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua) | 68 |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua) | 64 |
| [Enlightenment Dragon](/examples/cards/46186135) | `46186135` | [Scripts/c46186135.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46186135.lua) | 62 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua) | 61 |
| [El Shaddoll Meshachrer](/examples/cards/32467459) | `32467459` | [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua) | 61 |
| Super Duper Polymerization | `44886582` | [Scripts/c44886582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44886582.lua) | 59 |
| Chaos Emperor, the Dragon of Armageddon | `4538826` | [Scripts/c4538826.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4538826.lua) | 58 |
| Gem-Knight Phantom Quartz | `24484270` | [Scripts/c24484270.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24484270.lua) | 58 |
| Beyond the Pendulum | `22125101` | [Scripts/c22125101.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22125101.lua) | 56 |
| Ursarctic Quint Charge | `15758127` | [Scripts/c15758127.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15758127.lua) | 56 |
| R.B. Lambda Blade | `17188206` | [Scripts/c17188206.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17188206.lua) | 56 |
| R.B. Lambda Cannon | `81794107` | [Scripts/c81794107.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81794107.lua) | 56 |
| Kaiki the Unity Star | `60822251` | [Scripts/c60822251.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60822251.lua) | 55 |
| Todoroki the Earthbolt Star | `30118701` | [Scripts/c30118701.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30118701.lua) | 55 |
| Abyss Actor - Mellow Madonna | `78310590` | [Scripts/c78310590.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78310590.lua) | 54 |
| Psychic Arsenal | `16238373` | [Scripts/c16238373.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16238373.lua) | 54 |
| Materiactor Meltthrough | `66059345` | [Scripts/c66059345.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66059345.lua) | 53 |
| Masterking Archfiend | `35606858` | [Scripts/c35606858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35606858.lua) | 53 |
| Chaos Emperor Dragon - Envoy of the End | `82301904` | [Scripts/c82301904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82301904.lua) | 53 |
| Salamangreat Sanctuary | `1295111` | [Scripts/c1295111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1295111.lua) | 53 |
| Ekto Enneacraft - "tromarIA" | `29570824` | [Scripts/c29570824.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29570824.lua) | 52 |
| Enato Enneacraft - "oknirIA" | `55965529` | [Scripts/c55965529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55965529.lua) | 52 |
| Psychic Omnibuster | `70659412` | [Scripts/c70659412.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70659412.lua) | 52 |
| ...and 328 more |  |  |  |

## Script Examples

### Ultra Polymerization (`76647978`)

Source: [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76647978.lua)

```lua
end
function c76647978.cost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.CheckLPCost(tp,2000) end
	Duel.PayLPCost(tp,2000)
end
```

### Deftero Enneacraft - "alazoneIA" (`92171126`)

Source: [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua)

```lua
end
function s.thcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.CheckLPCost(tp,900) end
	Duel.PayLPCost(tp,900)
end
```

### Odd-Eyes Revolution Dragon (`16306932`)

Source: [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua)

```lua
end
function c16306932.thcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsDiscardable() and Duel.CheckLPCost(tp,500) end
	Duel.SendtoGrave(e:GetHandler(),REASON_COST+REASON_DISCARD)
	Duel.PayLPCost(tp,500)
```
