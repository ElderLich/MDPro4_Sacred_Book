# Duel.GetChainInfo

## Signature

```lua
Duel.GetChainInfo(int chainc, ... any) -> ...
```

## Description

Returns the chainc information, if chainc = 0, returns the chain of information currently being processed
This function returns the corresponding number of return values ​​in sequence according to the number of arguments passed in. The arguments can be:
CHAININFO_CHAIN_COUNT The serial number of the chain
CHAININFO_TRIGGERING_EFFECT The effect of the chain
CHAININFO_TRIGGERING_PLAYER
CHAININFO_TRIGGERING_CONTROLER The player to which the chained position belongs
CHAININFO_TRIGGERING_LOCATION The location where the chain occurred
CHAININFO_TRIGGERING_SEQUENCE The number of the position where the chain occurred
CHAININFO_TARGET_CARDS Chain of object cards
CHAININFO_TARGET_PLAYER The target player for the chain
CHAININFO_TARGET_PARAM The object parameters of the chain
CHAININFO_DISABLE_REASON The chain is invalid for the effect of the effect
CHAININFO_DISABLE_PLAYER The chain is invalid for the reason the player
CHAININFO_CHAIN_ID The unique identifier for the chain
CHAININFO_TYPE Type of Chain Card (Monster, Magic, Trap)
CHAININFO_EXTTYPE The specific type of chain card (for example, monster, continuous magic, counterattack trap)
For example:
Duel.GetChainInfo(0, CHAININFO_TRIGGERING_LOCATION, CHAININFO_TARGET_CARDS)
This will return the location and object card where the current chain occurred

## Parameters

- `chainc` `int`
- `...` `any`

## Returns

- `...`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4947`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2166** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetChainInfo`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua) | 81 |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 70 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua) | 67 |
| [Performage Cup Tricker](/examples/cards/6812770) | `6812770` | [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua) | 65 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44509529.lua) | 65 |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28454232.lua) | 64 |
| [Converging Wishes](/examples/cards/20007374) | `20007374` | [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20007374.lua) | 64 |
| [PSY-Framelord Omega](/examples/cards/74586817) | `74586817` | [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74586817.lua) | 64 |
| [Graydle Split](/examples/cards/75361204) | `75361204` | [Scripts/c75361204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75361204.lua) | 64 |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua) | 63 |
| [D/D/D/D Dimensional King Arc Crisis](/examples/cards/71398055) | `71398055` | [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71398055.lua) | 63 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua) | 63 |
| [Dracotail Shaulas](/examples/cards/42125140) | `42125140` | [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42125140.lua) | 63 |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua) | 62 |
| [Enneacraft - Aiza.LEON](/examples/cards/82359538) | `82359538` | [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82359538.lua) | 62 |
| [Junoldo the Shadespirit Power Patron](/examples/cards/10266279) | `10266279` | [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10266279.lua) | 62 |
| [Bujinki Ahashima](/examples/cards/71095768) | `71095768` | [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71095768.lua) | 62 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua) | 62 |
| [Ecclesia and the Dark Dragon](/examples/cards/78397661) | `78397661` | [Scripts/c78397661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78397661.lua) | 62 |
| [DoSolfachord Coolia](/examples/cards/80776622) | `80776622` | [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80776622.lua) | 61 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 61 |
| [A Bao A Qu, the Lightless Shadow](/examples/cards/4731783) | `4731783` | [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4731783.lua) | 61 |
| [Radiant Typhoon Varuroon, the Marine Eidolon](/examples/cards/39341885) | `39341885` | [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39341885.lua) | 61 |
| [Flower Cardian Willow with Calligrapher](/examples/cards/89818984) | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89818984.lua) | 61 |
| ...and 2142 more |  |  |  |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
	if chk==0 then return true end
	local c=e:GetHandler()
	local cid=Duel.GetChainInfo(0,CHAININFO_CHAIN_ID)
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_SINGLE)
```

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
end
function c59255742.operation(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS):Filter(Card.IsRelateToEffect,nil,e)
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<g:GetCount() then return end
	Duel.GetControl(g,tp)
```

### Meteoroa Drytron (`24166324`)

Source: [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua)

```lua
end
function s.thop(e,tp,eg,ep,ev,re,r,rp)
	local tg=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS)
	local rg=tg:Filter(Card.IsRelateToEffect,nil,e)
	if rg:GetCount() then
```
