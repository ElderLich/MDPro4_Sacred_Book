# Card.GetLinkRace

## Signature

```lua
Card.GetLinkRace(Card c, [int player]) -> int
```

## Description

Returns the Race c uses as Link Material for player, defaulting to the current reason player.

## Parameters

- `c` `Card`
- `player` `int` optional - default: current reason player

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3489`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **15** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetLinkRace) with `Card.GetLinkRace`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Cyberse Contract Witch | `37458564` | [Scripts/c37458564.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37458564.lua) | 1 |
| Keel, Shipwright Fur Hire | `66736884` | [Scripts/c66736884.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66736884.lua) | 1 |
| Crossrose Dragon | `72218246` | [Scripts/c72218246.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72218246.lua) | 1 |
| Folgo, Justice Fur Hire | `66023650` | [Scripts/c66023650.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66023650.lua) | 1 |
| Donner, Dagger Fur Hire | `8728498` | [Scripts/c8728498.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8728498.lua) | 1 |
| Union Carrier | `83152482` | [Scripts/c83152482.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83152482.lua) | 2 |
| ASHLAN U1000 | `44376395` | [Scripts/c44376395.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44376395.lua) | 1 |
| Akashic Magician | `28776350` | [Scripts/c28776350.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28776350.lua) | 1 |
| Curious, the Lightsworn Dominion | `98095162` | [Scripts/c98095162.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98095162.lua) | 1 |
| Summon Sorceress | `61665245` | [Scripts/c61665245.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61665245.lua) | 1 |
| Herald of Mirage Lights | `46935289` | [Scripts/c46935289.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46935289.lua) | 1 |
| Ra'ten, the Heavenly General | `30163008` | [Scripts/c30163008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30163008.lua) | 1 |
| Darkness Metal, the Dragon of Dark Steel | `79266769` | [Scripts/c79266769.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c79266769.lua) | 1 |
| Ib the World Chalice Priestess | `77610772` | [Scripts/c77610772.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77610772.lua) | 1 |
| Aleister the Invoker of Madness | `97973962` | [Scripts/c97973962.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97973962.lua) | 1 |

## Script Examples

### Cyberse Contract Witch (`37458564`)

Source: [Scripts/c37458564.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37458564.lua)

```lua
end
function s.lcheck(g)
	return aux.SameValueCheck(g,Card.GetLinkRace)
end
function s.thcon(e,tp,eg,ep,ev,re,r,rp)
```

### Keel, Shipwright Fur Hire (`66736884`)

Source: [Scripts/c66736884.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66736884.lua)

```lua
end
function s.lcheck(g,lc)
	return not aux.SameValueCheck(g,Card.GetLinkRace)
end
function s.setcon(e,tp,eg,ep,ev,re,r,rp)
```

### Crossrose Dragon (`72218246`)

Source: [Scripts/c72218246.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72218246.lua)

```lua
end
function c72218246.lcheck(g)
	return g:GetClassCount(Card.GetLinkRace)==g:GetCount()
end
function c72218246.spcon1(e,tp,eg,ep,ev,re,r,rp)
```
