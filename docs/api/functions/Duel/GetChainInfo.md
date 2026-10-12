# Duel.GetChainInfo

## Signature

```lua
Duel.GetChainInfo(int chainc, ... any) -> ...
```

## Description

Returns information fields from chainc in the same order as the requested CHAININFO_* constants.
Use chainc=0 for the currently resolving Chain. Unknown requested fields return nil, and no values are returned if the Chain does not exist.
For stored LP/player data, read CHAININFO_TARGET_PLAYER and CHAININFO_TARGET_PARAM. For official targets you are about to affect, prefer relation-aware target helpers.

## How To Use It

Use `chainc=0` inside an operation to read data from the currently resolving Chain Link.

```lua
local p,d=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER,CHAININFO_TARGET_PARAM)
local tg=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS)
```

For official card targets, prefer relation-aware helpers such as `Duel.GetFirstTarget()` or `Duel.GetTargetsRelateToChain()` when you are about to act on them.

## Related Functions

- [Duel.SetTargetPlayer](/api/functions/Duel/SetTargetPlayer)
- [Duel.SetTargetParam](/api/functions/Duel/SetTargetParam)
- [Duel.GetOperationInfo](/api/functions/Duel/GetOperationInfo)

## Parameters

- `chainc` `int` - Chain index/count to inspect; scripts commonly use 0 for the current Chain Link.
- `...` `any` - One or more CHAININFO_* constants. Each requested field produces one return value.

## Returns

- `...` - Values corresponding to the requested CHAININFO_* constants. CHAININFO_TARGET_CARDS returns the Chain's target Group.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4947`

## Guided Examples

Learn how to use this function in context:

- [Categories, Properties, And Hint Timing](/learn/categories-properties-and-hints)
- [Chain Timing And Activation Windows](/learn/chain-timing-and-activation-windows)
- [Client UI And Prompt Behavior](/learn/client-ui-and-prompt-behavior)
- [Common Script Errors And Debugging](/learn/common-script-errors-and-debugging)
- [Cost, Target, And Operation Lifecycle](/learn/cost-target-operation-lifecycle)
- [Write Your First Custom Card](/learn/first-custom-card)

::: details More guided lessons (5)

- [First Scripts To Study](/learn/first-scripts)
- [LP Recovery and Effect Damage](/learn/lp-recovery-and-damage)
- [Player-Targeted Effects](/learn/player-targeted-effects)
- [Spell Card Patterns](/learn/spell-card-patterns)
- [Targeting Flow](/learn/targeting-flow)

:::

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2180** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetChainInfo) with `Duel.GetChainInfo`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62091148.lua) | 2 |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59255742.lua) | 3 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24166324.lua) | 1 |
| [Performage Cup Tricker](/examples/cards/6812770) | `6812770` | [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6812770.lua) | 1 |
| [Pere-Zenet Em Heru](/examples/cards/46273941) | `46273941` | [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46273941.lua) | 1 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44509529.lua) | 1 |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28454232.lua) | 1 |
| [Converging Wishes](/examples/cards/20007374) | `20007374` | [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20007374.lua) | 2 |
| [PSY-Framelord Omega](/examples/cards/74586817) | `74586817` | [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74586817.lua) | 1 |
| [Graydle Split](/examples/cards/75361204) | `75361204` | [Scripts/c75361204.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75361204.lua) | 2 |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81237046.lua) | 1 |
| [D/D/D/D Dimensional King Arc Crisis](/examples/cards/71398055) | `71398055` | [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71398055.lua) | 1 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5997110.lua) | 1 |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71801447.lua) | 3 |
| [Enneacraft - Aiza.LEON](/examples/cards/82359538) | `82359538` | [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82359538.lua) | 1 |
| [Junoldo the Shadespirit Power Patron](/examples/cards/10266279) | `10266279` | [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10266279.lua) | 1 |
| [Bujinki Ahashima](/examples/cards/71095768) | `71095768` | [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71095768.lua) | 5 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57261568.lua) | 1 |
| [DoSolfachord Coolia](/examples/cards/80776622) | `80776622` | [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80776622.lua) | 1 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4993187.lua) | 1 |
| [A Bao A Qu, the Lightless Shadow](/examples/cards/4731783) | `4731783` | [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4731783.lua) | 1 |
| [Radiant Typhoon Varuroon, the Marine Eidolon](/examples/cards/39341885) | `39341885` | [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39341885.lua) | 1 |
| Flower Cardian Willow with Calligrapher | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89818984.lua) | 1 |
| Prank-Kids Rocket Ride | `18514525` | [Scripts/c18514525.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18514525.lua) | 1 |
| ...and 2156 more |  |  |  |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
	if chk==0 then return true end
	local c=e:GetHandler()
	local cid=Duel.GetChainInfo(0,CHAININFO_CHAIN_ID)
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_SINGLE)
```

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
end
function c59255742.operation(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS):Filter(Card.IsRelateToEffect,nil,e)
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<g:GetCount() then return end
	Duel.GetControl(g,tp)
```

### Meteoroa Drytron (`24166324`)

Source: [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24166324.lua)

```lua
end
function s.thop(e,tp,eg,ep,ev,re,r,rp)
	local tg=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS)
	local rg=tg:Filter(Card.IsRelateToEffect,nil,e)
	if rg:GetCount() then
```
