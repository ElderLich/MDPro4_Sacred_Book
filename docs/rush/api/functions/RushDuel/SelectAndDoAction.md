# RushDuel.SelectAndDoAction

Alias: `RD.SelectAndDoAction`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SelectAndDoAction(int hint, function filter, int tp, int s_range, int o_range, int min, int max, Card|Group|nil expect, function action) -> any
```

## Description

Finds matching cards in the specified locations, asks tp to select a non-cancelable Group of min to max cards, and immediately calls action(selected_group). Use during resolution, not during a chk==0 legality test. This helper does not select activation targets or store a target relation.
The public wrapper passes only a Card to filter and only the selected Group to action; capture other values in closures or compose a filter with RD.Filter. It emits a selection hint for public-location searches. If there are too few candidates or the selected Group is empty, it returns numeric 0 without calling action.
On a nonempty selection it forwards every return value from action unchanged. A callback with no return makes this helper return no values (nil in a single-value assignment); it does not automatically return the selected count or success.

## Parameters

- `hint` `int`: Selection prompt identifier, such as HINTMSG_TOGRAVE or aux.Stringid(id, n).
- `filter` `function`: Card predicate. Include the needed operation-legality checks.
- `tp` `int`: Selecting player; 0 or 1.
- `s_range` `int`: Locations on tp's side.
- `o_range` `int`: Locations on the opponent's side.
- `min` `int`: Minimum selected count.
- `max` `int`: Maximum selected count.
- `expect` `Card|Group|nil`: Card(s) excluded from matching; pass nil for no exclusion. The upstream parameter is spelled expect.
- `action` `function`: Called as action(selected_group) immediately after a nonempty selection.

## Returns

- `any`: Exactly the callback's return values when invoked; otherwise numeric 0. A callback may return no values.

## Example

```lua
local moved = RD.SelectAndDoAction(HINTMSG_TOGRAVE,
    Card.IsAbleToGrave, tp, LOCATION_MZONE, 0, 1, 1, nil,
    function(g) return Duel.SendtoGrave(g, REASON_EFFECT) end)
if moved > 0 then
    -- The returned movement count is positive.
end
```

## Source

`Rush/Utilities/RDAction.lua:102`

```lua
function RushDuel.SelectAndDoAction(hint, filter, tp, s_range, o_range, min, max, expect, action)
    local hint_selection = RushDuel._private_is_include_public(s_range, o_range)
    return RushDuel._private_action_select_match(hint, filter, tp, s_range, o_range, min, max, expect, hint_selection, false, action)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **988** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SelectAndDoAction) with `RushDuel.SelectAndDoAction`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Elemental Circulation](/examples/rush-cards/120263030) | `120263030` | [Rush/Scripts/c120263030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263030.lua) | 1 |
| [Moonforce Ziggy](/examples/rush-cards/120300014) | `120300014` | [Rush/Scripts/c120300014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300014.lua) | 1 |
| [Freshberry Collaboration](/examples/rush-cards/120301071) | `120301071` | [Rush/Scripts/c120301071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301071.lua) | 1 |
| [Voidalfr Star Mayfly](/examples/rush-cards/120300034) | `120300034` | [Rush/Scripts/c120300034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300034.lua) | 1 |
| [Player #C39: Home Run Smasher V](/examples/rush-cards/120305028) | `120305028` | [Rush/Scripts/c120305028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305028.lua) | 1 |
| [Invitation to a Delirious Dream](/examples/rush-cards/120261066) | `120261066` | [Rush/Scripts/c120261066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261066.lua) | 1 |
| [Light of Bewitchment](/examples/rush-cards/120301074) | `120301074` | [Rush/Scripts/c120301074.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301074.lua) | 1 |
| [Dark-Guiding Kuriboh](/examples/rush-cards/120280009) | `120280009` | [Rush/Scripts/c120280009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120280009.lua) | 1 |
| [Delirium Lampyris](/examples/rush-cards/120231061) | `120231061` | [Rush/Scripts/c120231061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231061.lua) | 1 |
| [Super Galaxy King Lord of Galactica \[R\]](/examples/rush-cards/120254039) | `120254039` | [Rush/Scripts/c120254039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254039.lua) | 1 |
| [Fuden Issen](/examples/rush-cards/120309034) | `120309034` | [Rush/Scripts/c120309034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309034.lua) | 1 |
| [Wako Gozen Riletta](/examples/rush-cards/120309021) | `120309021` | [Rush/Scripts/c120309021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309021.lua) | 1 |
| [Sparkhearts Makma](/examples/rush-cards/120298023) | `120298023` | [Rush/Scripts/c120298023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298023.lua) | 1 |
| [Imaginary Arc Turbulence](/examples/rush-cards/120196013) | `120196013` | [Rush/Scripts/c120196013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120196013.lua) | 1 |
| [Major Breaking News!](/examples/rush-cards/120304060) | `120304060` | [Rush/Scripts/c120304060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304060.lua) | 1 |
| [Abyssal Dragon Lord Abyss Poseidra \[L\]](/examples/rush-cards/120239013) | `120239013` | [Rush/Scripts/c120239013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239013.lua) | 1 |
| [Wish of the Skysavior](/examples/rush-cards/120253064) | `120253064` | [Rush/Scripts/c120253064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253064.lua) | 1 |
| [Fairy of the Stars](/examples/rush-cards/120305016) | `120305016` | [Rush/Scripts/c120305016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305016.lua) | 1 |
| [Necromaid Trickment](/examples/rush-cards/120294063) | `120294063` | [Rush/Scripts/c120294063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294063.lua) | 1 |
| [Spice Cross Secret Recipe](/examples/rush-cards/120261060) | `120261060` | [Rush/Scripts/c120261060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261060.lua) | 1 |
| [Magical Retribution](/examples/rush-cards/120254028) | `120254028` | [Rush/Scripts/c120254028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254028.lua) | 1 |
| [Nobody Phantom Thief](/examples/rush-cards/120244060) | `120244060` | [Rush/Scripts/c120244060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244060.lua) | 1 |
| [Nobody Phantom Thief](/examples/rush-cards/120273005) | `120273005` | [Rush/Scripts/c120273005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120273005.lua) | 1 |
| [Mega Jointech Fortrex \[R\]](/examples/rush-cards/120249005) | `120249005` | [Rush/Scripts/c120249005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249005.lua) | 2 |
| ...and 964 more |  |  |  |

## Script Examples

### Elemental Circulation (`120263030`)

Source: [Rush/Scripts/c120263030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263030.lua)

```lua
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if RD.Draw()~=0 then
		RD.SelectAndDoAction(HINTMSG_TOGRAVE,Card.IsAbleToGrave,tp,LOCATION_HAND,0,1,1,nil,function(g)
			Duel.BreakEffect()
			Duel.SendtoGrave(g,REASON_EFFECT)
```

### Moonforce Ziggy (`120300014`)

Source: [Rush/Scripts/c120300014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300014.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectAndDoAction(aux.Stringid(m,1),cm.filter,tp,0,LOCATION_MZONE,1,1,nil,function(g)
		local tc=g:GetFirst()
		local e1=Effect.CreateEffect(e:GetHandler())
```

### Freshberry Collaboration (`120301071`)

Source: [Rush/Scripts/c120301071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301071.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	local filter=RD.Filter(cm.filter,e,tp)
	RD.SelectAndDoAction(HINTMSG_POSCHANGE,filter,tp,LOCATION_MZONE,0,1,1,nil,function(g)
		if RD.ChangePosition(g,e,tp,REASON_EFFECT,POS_FACEUP_DEFENSE)~=0 and e:GetLabel()==1 then
			RD.CanSelectAndDoAction(aux.Stringid(m,1),HINTMSG_DESTROY,cm.desfilter,tp,0,LOCATION_MZONE,1,1,nil,function(sg)
```
