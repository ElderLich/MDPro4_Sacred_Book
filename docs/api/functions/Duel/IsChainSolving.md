# Duel.IsChainSolving

## Signature

```lua
Duel.IsChainSolving() -> bool
```

## Description

Checks whether the game is currently resolving a Chain or resolving an effect that does not start a Chain.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5060`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **13** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.IsChainSolving`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua) | 63 |
| [Enneacraft - Aiza.LEON](/examples/cards/82359538) | `82359538` | [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82359538.lua) | 62 |
| Awakening of the Sacred Beasts | `53701259` | [Scripts/c53701259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53701259.lua) | 57 |
| Odd-Eyes Pendulumgraph Dragon | `66425726` | [Scripts/c66425726.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66425726.lua) | 49 |
| Guilt-Gripping Morganite | `61822419` | [Scripts/c61822419.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61822419.lua) | 44 |
| Crystal Tree | `47408488` | [Scripts/c47408488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47408488.lua) | 40 |
| Mulcharmy Purulia | `84192580` | [Scripts/c84192580.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84192580.lua) | 39 |
| Ghost Sister &amp; Spooky Dogwood | `60643553` | [Scripts/c60643553.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60643553.lua) | 39 |
| Mulcharmy Fuwalos | `42141493` | [Scripts/c42141493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42141493.lua) | 38 |
| Mulcharmy Meowls | `87126721` | [Scripts/c87126721.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87126721.lua) | 38 |
| Trickstar Lycoris | `35199656` | [Scripts/c35199656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35199656.lua) | 37 |
| Maxx "C" | `23434538` | [Scripts/c23434538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23434538.lua) | 25 |
| Shared Ride | `1372887` | [Scripts/c1372887.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1372887.lua) | 22 |

## Script Examples

### Enneacraft - Archa.TAIL (`81237046`)

Source: [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua)

```lua
function s.damcon1(e,tp,eg,ep,ev,re,r,rp)
	return e:GetHandler():GetFlagEffect(id)>0
		and eg:IsExists(s.damfilter,1,nil,1-tp) and not Duel.IsChainSolving()
end
function s.damop1(e,tp,eg,ep,ev,re,r,rp)
```

### Enneacraft - Aiza.LEON (`82359538`)

Source: [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82359538.lua)

```lua
function s.damcon1(e,tp,eg,ep,ev,re,r,rp)
	return e:GetHandler():GetFlagEffect(id)>0
		and eg:IsExists(Card.IsControler,1,nil,1-tp) and not Duel.IsChainSolving()
		and re and re:GetOwnerPlayer()==1-tp
end
```

### Awakening of the Sacred Beasts (`53701259`)

Source: [Scripts/c53701259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53701259.lua)

```lua
function c53701259.lpcon1(e,tp,eg,ep,ev,re,r,rp)
	return c53701259.lpcon(e,tp,eg,ep,ev,re,r,rp)
		and not Duel.IsChainSolving()
end
function c53701259.lpop1(e,tp,eg,ep,ev,re,r,rp)
```
