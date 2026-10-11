# Duel.SelectTarget

## Signature

```lua
Duel.SelectTarget(int sel_player, [function|nil f], int player, int s, int o, int min, int max, [Card|Group|nil ex], ... any) -> Group
```

## Description

Lets sel_player choose min to max cards that satisfy filter f, are not excluded by ex, and can be targeted by the currently handled effect.
The selected cards are registered as the current Chain's target cards. For non-continuous effects, the core also creates Chain relations used by IsRelateToEffect and related helpers.
This requires a current Chain; use Duel.SelectMatchingCard or Group.Select for ordinary resolution choices.

## How To Use It

Use this in the Target callback of an activated effect that targets cards.

The selected cards are saved as the Chain's targets. This function needs a current Chain; use `Duel.SelectMatchingCard` or `Group.Select` for ordinary resolution choices.
For one target, read it with `Duel.GetFirstTarget` and check `tc:IsRelateToEffect(e)` before applying the effect.
For several targets, use `Duel.GetTargetsRelateToChain` to get the target group that is still related to the resolving Chain.

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return chkc:IsOnField() and s.filter(chkc) end
    if chk==0 then return Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,0,1,nil) end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TARGET)
    Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,0,1,1,nil)
end

function s.operation(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc and tc:IsRelateToEffect(e) then
        Duel.Destroy(tc,REASON_EFFECT)
    end
end
```

## Related Functions

- [Duel.IsExistingTarget](/api/functions/Duel/IsExistingTarget)
- [Duel.GetFirstTarget](/api/functions/Duel/GetFirstTarget)
- [Duel.GetTargetsRelateToChain](/api/functions/Duel/GetTargetsRelateToChain)

## Parameters

- `sel_player` `int` - Player who makes the selection.
- `f` `function|nil` optional - Filter called with each candidate card first, then any extra arguments after ex.
- `player` `int` - Viewpoint player for s and o.
- `s` `int` - Locations on player's side to search.
- `o` `int` - Locations on the opponent's side to search.
- `min` `int` - Minimum number of cards to select.
- `max` `int` - Maximum number of cards to select.
- `ex` `Card|Group|nil` optional - Card or Group excluded from the selection.
- `...` `any` - Extra values passed to f after the candidate card.

## Returns

- `Group` - Group of cards selected by sel_player and registered as current Chain targets. If there is no current Chain or sel_player is invalid, the core returns no value.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4986`

## Guided Examples

Learn how to use this function in context:

- [Beginner Script Ladder](/learn/beginner-script-ladder)
- [Categories, Properties, And Hint Timing](/learn/categories-properties-and-hints)
- [Client UI And Prompt Behavior](/learn/client-ui-and-prompt-behavior)
- [Common Script Errors And Debugging](/learn/common-script-errors-and-debugging)
- [Filters, Card Objects, and Group Objects](/learn/filters-and-groups)
- [Write Your First Custom Card](/learn/first-custom-card)

::: details More guided lessons (6)

- [First Scripts To Study](/learn/first-scripts)
- [Min/Max Stat Card Selection](/learn/min-max-stat-selection)
- [Normal And Continuous Traps](/learn/normal-and-continuous-traps)
- [Quick-Play Spells](/learn/quick-play-spells)
- [Selection And Group Handling](/learn/selection-and-group-handling)
- [Targeting Flow](/learn/targeting-flow)

:::

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5099** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SelectTarget) with `Duel.SelectTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua) | 1 |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 1 |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua) | 1 |
| [Ultra Polymerization](/examples/cards/76647978) | `76647978` | [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76647978.lua) | 1 |
| [Ashtraja Susanoo](/examples/cards/17020474) | `17020474` | [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17020474.lua) | 1 |
| [Fiendsmith's Sequence](/examples/cards/49867899) | `49867899` | [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49867899.lua) | 1 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11852093.lua) | 1 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 1 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua) | 1 |
| [Mixousia the Confounder](/examples/cards/80843006) | `80843006` | [Scripts/c80843006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80843006.lua) | 1 |
| [Invoked Sorath](/examples/cards/43989315) | `43989315` | [Scripts/c43989315.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43989315.lua) | 1 |
| [Performage Cup Tricker](/examples/cards/6812770) | `6812770` | [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua) | 2 |
| [Spirit Illusion](/examples/cards/71939275) | `71939275` | [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71939275.lua) | 1 |
| [Ghostrick Renovation](/examples/cards/61818176) | `61818176` | [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61818176.lua) | 1 |
| [Hecahands Tartaros](/examples/cards/57809669) | `57809669` | [Scripts/c57809669.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57809669.lua) | 1 |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28454232.lua) | 1 |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua) | 1 |
| [Resurgam Xyz](/examples/cards/49082032) | `49082032` | [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua) | 1 |
| [Tohushaddoll Grysta](/examples/cards/95072744) | `95072744` | [Scripts/c95072744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95072744.lua) | 1 |
| [PSY-Framelord Omega](/examples/cards/74586817) | `74586817` | [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74586817.lua) | 2 |
| [Teleport Fusion](/examples/cards/36494597) | `36494597` | [Scripts/c36494597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36494597.lua) | 1 |
| [Graydle Split](/examples/cards/75361204) | `75361204` | [Scripts/c75361204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75361204.lua) | 1 |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua) | 1 |
| [D/D/D/D Dimensional King Arc Crisis](/examples/cards/71398055) | `71398055` | [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71398055.lua) | 1 |
| ...and 5075 more |  |  |  |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
		and Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_EQUIP)
	Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
	Duel.SetOperationInfo(0,CATEGORY_EQUIP,e:GetHandler(),1,0,0)
end
```

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
	Duel.Hint(HINT_OPSELECTED,1-tp,e:GetDescription())
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
	Duel.SelectTarget(tp,c55795155.atkfilter,tp,LOCATION_MZONE,0,1,1,nil)
end
function c55795155.atkop(e,tp,eg,ep,ev,re,r,rp)
```

### Surprise Fusion (`35167375`)

Source: [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua)

```lua
	if chk==0 then return Duel.IsExistingTarget(s.rafilter,tp,LOCATION_MZONE,0,1,nil) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
	local tc=Duel.SelectTarget(tp,s.rafilter,tp,LOCATION_MZONE,0,1,1,nil):GetFirst()
	local race,att
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RACE)
```
