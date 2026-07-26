# Card.IsAttack

## Signature

```lua
Card.IsAttack(Card c, int atk1, [int atk2], [... int]) -> bool
```

## Description

Checks whether c is a monster or currently treated as one, and whether its current ATK equals any supplied atk value.
Nil atk arguments are skipped. Non-monsters that are not treated as monsters return false.

## Parameters

- `c` `Card`
- `atk1` `int`
- `atk2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3493`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **163** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsAttack`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 77 |
| [Spirit Illusion](/examples/cards/71939275) | `71939275` | [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71939275.lua) | 65 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua) | 63 |
| Starving Venom Fusion Dragon of the Four Heavenly Dragons | `27118421` | [Scripts/c27118421.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27118421.lua) | 59 |
| Grandpa Demetto | `44190146` | [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44190146.lua) | 58 |
| Tails of the Fairy Tails | `82119326` | [Scripts/c82119326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82119326.lua) | 57 |
| Union Activation | `38527680` | [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua) | 57 |
| Black Garden | `71645242` | [Scripts/c71645242.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71645242.lua) | 56 |
| Kaiki the Unity Star | `60822251` | [Scripts/c60822251.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60822251.lua) | 55 |
| Drytron Meteonis DA Draconids | `56863746` | [Scripts/c56863746.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56863746.lua) | 53 |
| Masterking Archfiend | `35606858` | [Scripts/c35606858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35606858.lua) | 53 |
| Salamangreat Sanctuary | `1295111` | [Scripts/c1295111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1295111.lua) | 53 |
| Jiaotu, Darkness of the Yang Zing | `25935625` | [Scripts/c25935625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25935625.lua) | 52 |
| Egyptian God Slime | `42166000` | [Scripts/c42166000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42166000.lua) | 52 |
| Multiplying Kuriboh! | `14965712` | [Scripts/c14965712.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14965712.lua) | 51 |
| Loka Samsara | `2116237` | [Scripts/c2116237.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2116237.lua) | 51 |
| Token Support | `53545926` | [Scripts/c53545926.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53545926.lua) | 51 |
| Doll House | `67331360` | [Scripts/c67331360.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67331360.lua) | 51 |
| Mechanical Mechanic | `22106558` | [Scripts/c22106558.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22106558.lua) | 50 |
| Allied Code Talker @Ignister | `39138610` | [Scripts/c39138610.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39138610.lua) | 50 |
| Invoked Babalon | `70383419` | [Scripts/c70383419.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70383419.lua) | 50 |
| Box of Friends | `81587028` | [Scripts/c81587028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81587028.lua) | 50 |
| Horoscope Sorcerer, the Stargazer Magician | `1186447` | [Scripts/c1186447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1186447.lua) | 49 |
| The Chaotic Sacred Beasts | `7894706` | [Scripts/c7894706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7894706.lua) | 49 |
| ...and 139 more |  |  |  |

## Script Examples

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
end
function c55795155.thfilter(c,code)
	return c:IsType(TYPE_PENDULUM) and c:IsAttack(2500) and not c:IsCode(code) and c:IsAbleToHand()
end
function c55795155.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Spirit Illusion (`71939275`)

Source: [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71939275.lua)

```lua
	local tc=ec:GetBattleTarget()
	e:SetLabelObject(tc)
	return not ec:IsAttack(0) and tc and tc:IsFaceup()
end
function s.atktg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### D/D Count Surveyor (`5997110`)

Source: [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua)

```lua
function s.thfilter(c)
	return c:IsSetCard(0xaf) and c:IsType(TYPE_MONSTER)
		and (c:IsAttack(0) or c:IsDefense(0)) and c:IsAbleToHand()
end
function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```
