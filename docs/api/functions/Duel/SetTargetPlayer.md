# Duel.SetTargetPlayer

## Signature

```lua
Duel.SetTargetPlayer(int player) -> void
```

## Description

Stores player as the target player for the currently handled Chain.
Operations commonly read it with Duel.GetChainInfo(0, CHAININFO_TARGET_PLAYER), often together with CHAININFO_TARGET_PARAM.
This stores Chain data for a player-facing effect; it does not select a card target.

## How To Use It

Use this when the Chain Link stores a player choice or player destination rather than an official card target.

```lua
Duel.SetTargetPlayer(1-tp)
Duel.SetTargetParam(1000)
Duel.SetOperationInfo(0,CATEGORY_DAMAGE,nil,0,1-tp,1000)
```

Read it during resolution with `Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER)`. This is Chain data; it does not make the player a card target.

## Related Functions

- [Duel.SetTargetParam](/api/functions/Duel/SetTargetParam)
- [Duel.GetChainInfo](/api/functions/Duel/GetChainInfo)
- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)

## Parameters

- `player` `int` - Player value stored on the current Chain.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5006`

## Guided Examples

Learn how to use this function in context:

- [Categories, Properties, And Hint Timing](/learn/categories-properties-and-hints)
- [Client UI And Prompt Behavior](/learn/client-ui-and-prompt-behavior)
- [Cost, Target, And Operation Lifecycle](/learn/cost-target-operation-lifecycle)
- [Write Your First Custom Card](/learn/first-custom-card)
- [First Scripts To Study](/learn/first-scripts)
- [LP Recovery and Effect Damage](/learn/lp-recovery-and-damage)

::: details More guided lessons (1)

- [Player-Targeted Effects](/learn/player-targeted-effects)

:::

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **967** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SetTargetPlayer) with `Duel.SetTargetPlayer`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pere-Zenet Em Heru](/examples/cards/46273941) | `46273941` | [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46273941.lua) | 1 |
| [Junoldo the Shadespirit Power Patron](/examples/cards/10266279) | `10266279` | [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10266279.lua) | 1 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57261568.lua) | 1 |
| [A Bao A Qu, the Lightless Shadow](/examples/cards/4731783) | `4731783` | [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4731783.lua) | 1 |
| Flower Cardian Willow with Calligrapher | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89818984.lua) | 1 |
| Magikey Dragon - Andrabime | `71159974` | [Scripts/c71159974.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71159974.lua) | 1 |
| Forbidden Dark Contract with the Swamp King | `10833828` | [Scripts/c10833828.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10833828.lua) | 1 |
| Meklord Astro Mekanikle | `63468625` | [Scripts/c63468625.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63468625.lua) | 1 |
| Abyss-steam | `63941169` | [Scripts/c63941169.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63941169.lua) | 1 |
| Purrely | `25550531` | [Scripts/c25550531.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25550531.lua) | 1 |
| Flower Cardian Moonflowerviewing | `33541430` | [Scripts/c33541430.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33541430.lua) | 1 |
| Witchcrafter Pittore | `95245544` | [Scripts/c95245544.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95245544.lua) | 1 |
| Fallen Paradise of the Sacred Beasts | `65861210` | [Scripts/c65861210.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65861210.lua) | 1 |
| Genex Ally Triforce | `52709508` | [Scripts/c52709508.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52709508.lua) | 1 |
| Vernusylph of the Thawing Mountains | `9238125` | [Scripts/c9238125.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9238125.lua) | 1 |
| Gladiator Beast Gaiodiaz | `90957527` | [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90957527.lua) | 1 |
| Megalith Anastasis | `29876299` | [Scripts/c29876299.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29876299.lua) | 1 |
| Fabled Realm's Revival | `57775790` | [Scripts/c57775790.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57775790.lua) | 1 |
| Miracle Synchro Fusion | `36484016` | [Scripts/c36484016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36484016.lua) | 1 |
| Neo Super Quantal Mech King Blaster Magna | `95493471` | [Scripts/c95493471.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95493471.lua) | 1 |
| Indiora Doom Volt the Cubic Emperor | `3775068` | [Scripts/c3775068.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3775068.lua) | 1 |
| Vulcan Dragni the Cubic King | `77387463` | [Scripts/c77387463.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77387463.lua) | 1 |
| Rank-Up-Magic Zexal Force | `36224040` | [Scripts/c36224040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36224040.lua) | 1 |
| Yummy★Redemption | `65853758` | [Scripts/c65853758.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65853758.lua) | 1 |
| ...and 943 more |  |  |  |

## Script Examples

### Pere-Zenet Em Heru (`46273941`)

Source: [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46273941.lua)

```lua
function s.drtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDraw(tp,1) end
	Duel.SetTargetPlayer(tp)
	Duel.SetTargetParam(1)
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,1)
```

### Junoldo the Shadespirit Power Patron (`10266279`)

Source: [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10266279.lua)

```lua
function s.drtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDraw(tp,2) end
	Duel.SetTargetPlayer(tp)
	Duel.SetTargetParam(2)
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,2)
```

### Flower Cardian Peony with Butterfly (`57261568`)

Source: [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57261568.lua)

```lua
function c57261568.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	Duel.SetTargetPlayer(tp)
	Duel.SetTargetParam(1)
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,1)
```
