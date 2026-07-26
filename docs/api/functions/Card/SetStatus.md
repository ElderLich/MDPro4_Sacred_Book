# Card.SetStatus

## Signature

```lua
Card.SetStatus(Card c, int status, bool enable) -> void
```

## Description

Sets or clears status on c.
This is an internal-status helper. The binding does nothing while c is copying another card's effect.

## Parameters

- `c` `Card`
- `status` `int`
- `enable` `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3512`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **54** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.SetStatus`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua) | 63 |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua) | 62 |
| [Enneacraft - Aiza.LEON](/examples/cards/82359538) | `82359538` | [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82359538.lua) | 62 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua) | 62 |
| [Camelot, Realm of Noble Knights and Noble Arms](/examples/cards/15635751) | `15635751` | [Scripts/c15635751.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15635751.lua) | 61 |
| Magical Hats | `81210420` | [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81210420.lua) | 59 |
| Ojama Pajama | `75884822` | [Scripts/c75884822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75884822.lua) | 55 |
| Sea Lancer | `22842214` | [Scripts/c22842214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22842214.lua) | 53 |
| Dual Avatar Feet - Armored Un-Gyo | `7631534` | [Scripts/c7631534.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7631534.lua) | 52 |
| Lost World | `17228908` | [Scripts/c17228908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17228908.lua) | 51 |
| Fire King Sanctuary | `65305978` | [Scripts/c65305978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65305978.lua) | 51 |
| Odd-Eyes Lancer Dragon | `83347294` | [Scripts/c83347294.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83347294.lua) | 51 |
| D/D/D Abyss King Gilgamesh | `9024198` | [Scripts/c9024198.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9024198.lua) | 50 |
| Harpie Conductor | `85696777` | [Scripts/c85696777.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85696777.lua) | 50 |
| Empire of Endymion | `34041788` | [Scripts/c34041788.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34041788.lua) | 47 |
| Dragunity Senatus | `92868896` | [Scripts/c92868896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92868896.lua) | 45 |
| Pennant of Revolution | `73193552` | [Scripts/c73193552.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73193552.lua) | 44 |
| Superheavy Samurai Brave Masurawo | `64193046` | [Scripts/c64193046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64193046.lua) | 44 |
| Simorgh, Bird of Sovereignty | `72330894` | [Scripts/c72330894.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72330894.lua) | 43 |
| Miracle of the Supreme King | `40456412` | [Scripts/c40456412.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40456412.lua) | 43 |
| Poly-Chemicritter Hydragon | `80476891` | [Scripts/c80476891.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80476891.lua) | 43 |
| Escapegoat | `33676146` | [Scripts/c33676146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33676146.lua) | 43 |
| Legendary Lord Six Samurai - Shi En | `34235530` | [Scripts/c34235530.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34235530.lua) | 42 |
| Kozmo Tincan | `64280356` | [Scripts/c64280356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64280356.lua) | 42 |
| ...and 30 more |  |  |  |

## Script Examples

### Enneacraft - Archa.TAIL (`81237046`)

Source: [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua)

```lua
	local c=e:GetHandler()
	c:RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD,EFFECT_FLAG_CLIENT_HINT,1,0,aux.Stringid(id,3))
	c:SetStatus(STATUS_EFFECT_ENABLED,true)
end
function s.damfilter(c,tp)
```

### Enneacraft - Atil.SPIA (`71801447`)

Source: [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua)

```lua
	local c=e:GetHandler()
	c:RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD,EFFECT_FLAG_CLIENT_HINT,1,0,aux.Stringid(id,3))
	c:SetStatus(STATUS_EFFECT_ENABLED,true)
end
function s.chainop(e,tp,eg,ep,ev,re,r,rp)
```

### Enneacraft - Aiza.LEON (`82359538`)

Source: [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82359538.lua)

```lua
	local c=e:GetHandler()
	c:RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD,EFFECT_FLAG_CLIENT_HINT,1,0,aux.Stringid(id,3))
	c:SetStatus(STATUS_EFFECT_ENABLED,true)
end
function s.damcon1(e,tp,eg,ep,ev,re,r,rp)
```
