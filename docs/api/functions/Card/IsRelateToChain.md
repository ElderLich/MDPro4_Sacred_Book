# Card.IsRelateToChain

## Signature

```lua
Card.IsRelateToChain(Card c, [int chainc]) -> bool
```

## Description

Checks whether c is still related to chainc.
The activating card and cards selected as targets with Duel.SetTargetCard or Duel.SelectTarget automatically become related to that Chain. The relation is lost when the card leaves the expected place.

## Parameters

- `c` `Card`
- `chainc` `int` optional - default: 0

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3563`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **529** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsRelateToChain`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer, the Star Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua) | 80 |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua) | 73 |
| [Exciting Melffy Time](/examples/cards/58036097) | `58036097` | [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua) | 69 |
| [Favorite HERO Flame Wingman](/examples/cards/13243124) | `13243124` | [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13243124.lua) | 66 |
| [Invoked Sorath](/examples/cards/43989315) | `43989315` | [Scripts/c43989315.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43989315.lua) | 66 |
| [Hecahands Tartaros](/examples/cards/57809669) | `57809669` | [Scripts/c57809669.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57809669.lua) | 65 |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28454232.lua) | 64 |
| [Aiwass the Spirit of the Law](/examples/cards/84288367) | `84288367` | [Scripts/c84288367.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84288367.lua) | 64 |
| [Teleport Fusion](/examples/cards/36494597) | `36494597` | [Scripts/c36494597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36494597.lua) | 64 |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua) | 63 |
| [D/D/D/D Dimensional King Arc Crisis](/examples/cards/71398055) | `71398055` | [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71398055.lua) | 63 |
| [Future Fusion Nova](/examples/cards/92058902) | `92058902` | [Scripts/c92058902.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92058902.lua) | 63 |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua) | 62 |
| [Enneacraft - Aiza.LEON](/examples/cards/82359538) | `82359538` | [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82359538.lua) | 62 |
| [Junoldo the Shadespirit Power Patron](/examples/cards/10266279) | `10266279` | [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10266279.lua) | 62 |
| [Tellusion the Magna Warrior](/examples/cards/24431911) | `24431911` | [Scripts/c24431911.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24431911.lua) | 62 |
| [The Gaze of Timaeus](/examples/cards/22283204) | `22283204` | [Scripts/c22283204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22283204.lua) | 62 |
| [Penetration Fusion](/examples/cards/8778267) | `8778267` | [Scripts/c8778267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8778267.lua) | 62 |
| [Vidolium the Unstable Power Patron of Unity](/examples/cards/70488851) | `70488851` | [Scripts/c70488851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70488851.lua) | 61 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 61 |
| [Witchcrafter Celebration](/examples/cards/6958567) | `6958567` | [Scripts/c6958567.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6958567.lua) | 61 |
| [Chef de Nouvelles](/examples/cards/29251488) | `29251488` | [Scripts/c29251488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29251488.lua) | 60 |
| [Jupredo the Shademachine Power Patron](/examples/cards/43871165) | `43871165` | [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43871165.lua) | 60 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5148778.lua) | 60 |
| ...and 505 more |  |  |  |

## Script Examples

### Astrograph Sorcerer, the Star Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
function s.pop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToChain() then return end
	if Duel.Destroy(c,REASON_EFFECT)==0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOFIELD)
```

### Surprise Fusion (`35167375`)

Source: [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua)

```lua
	local race,att=e:GetLabel()
	local ec=Duel.GetFirstTarget()
	if ec:IsRelateToChain() and ec:IsFaceup() and ec:IsType(TYPE_MONSTER) then
		local cres=ec:GetRace()~=race or ec:GetAttribute()~=att
		local e1=Effect.CreateEffect(c)
```

### Exciting Melffy Time (`58036097`)

Source: [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua)

```lua
function s.activate(e,tp,eg,ep,ev,re,r,rp)
	local tc=Duel.GetFirstTarget()
	if tc and tc:IsRelateToChain() and aux.NecroValleyFilter()(tc)
		and Duel.SendtoHand(tc,nil,REASON_EFFECT)~=0 and tc:IsLocation(LOCATION_HAND) then
		local chkf=tp
```
