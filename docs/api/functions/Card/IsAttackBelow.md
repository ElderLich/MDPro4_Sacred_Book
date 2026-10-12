# Card.IsAttackBelow

## Signature

```lua
Card.IsAttackBelow(Card c, int atk) -> bool
```

## Description

Checks whether c is a monster, or treated as one, whose current ATK is known and less than or equal to atk.
Cards with unknown ATK return false because the core requires the current ATK to be at least 0.

## Parameters

- `c` `Card` - Card whose current ATK is checked.
- `atk` `int` - Maximum ATK value accepted by the check.

## Returns

- `bool` - True if c is a monster or treated as one, has known ATK, and that ATK is at most atk.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3673`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **174** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsAttackBelow) with `Card.IsAttackBelow`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28454232.lua) | 1 |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81237046.lua) | 1 |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71801447.lua) | 1 |
| [Enneacraft - Aiza.LEON](/examples/cards/82359538) | `82359538` | [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82359538.lua) | 1 |
| [DoSolfachord Coolia](/examples/cards/80776622) | `80776622` | [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80776622.lua) | 1 |
| Enneacraft - Atori.MAR | `54842941` | [Scripts/c54842941.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54842941.lua) | 1 |
| Drytron Meteonis DA Draconids | `56863746` | [Scripts/c56863746.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56863746.lua) | 1 |
| Madolche Dessert | `51650038` | [Scripts/c51650038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51650038.lua) | 1 |
| Helping Robo for Underwater Combat | `77856460` | [Scripts/c77856460.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77856460.lua) | 1 |
| Proxy F Magician | `12450071` | [Scripts/c12450071.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12450071.lua) | 1 |
| Number 93: Utopia Kaiser | `23187256` | [Scripts/c23187256.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23187256.lua) | 1 |
| Odd-Eyes Pendulum Dragon, Four Heavenly Dragons | `75787708` | [Scripts/c75787708.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75787708.lua) | 1 |
| Shade the Obscure | `77157846` | [Scripts/c77157846.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77157846.lua) | 1 |
| Performapal Corn | `33103459` | [Scripts/c33103459.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33103459.lua) | 1 |
| Supreme King Dragon Odd-Eyes | `96733134` | [Scripts/c96733134.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c96733134.lua) | 1 |
| Armed Rebeellion | `21056275` | [Scripts/c21056275.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21056275.lua) | 1 |
| Seventh Eternity | `60158866` | [Scripts/c60158866.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60158866.lua) | 1 |
| Clockwork Knight | `41739381` | [Scripts/c41739381.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41739381.lua) | 1 |
| Assault Spirits | `87043568` | [Scripts/c87043568.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87043568.lua) | 1 |
| Xyz Double Back | `57836546` | [Scripts/c57836546.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57836546.lua) | 1 |
| Odd-Eyes Rebellion Xyz Dragon | `30095833` | [Scripts/c30095833.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30095833.lua) | 1 |
| Officiator of Doom Samuel | `76213610` | [Scripts/c76213610.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76213610.lua) | 1 |
| Sky Striker Ace - Azalea Temperance | `56741506` | [Scripts/c56741506.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56741506.lua) | 1 |
| Steel Star Regulator | `32986898` | [Scripts/c32986898.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c32986898.lua) | 1 |
| ...and 150 more |  |  |  |

## Script Examples

### Enneacraft - Asta.PIXEA (`28454232`)

Source: [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28454232.lua)

```lua
end
function s.desfilter(c,atk)
	return c:IsFaceup() and c:IsAttackBelow(atk-1)
end
function s.destg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Enneacraft - Archa.TAIL (`81237046`)

Source: [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81237046.lua)

```lua
end
function s.desfilter(c,atk)
	return c:IsFaceup() and c:IsAttackBelow(atk-1)
end
function s.destg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Enneacraft - Atil.SPIA (`71801447`)

Source: [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71801447.lua)

```lua
end
function s.desfilter(c,atk)
	return c:IsFaceup() and c:IsAttackBelow(atk-1)
end
function s.destg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
