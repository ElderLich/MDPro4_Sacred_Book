# RushDuel.CanSelectAndDoAction

Alias: `RD.CanSelectAndDoAction`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanSelectAndDoAction(int desc, int hint, function filter, int tp, int s_range, int o_range, int min, int max, Card|Group|nil expect, function action) -> any
```

## Description

Optional resolution action: finds candidates, asks a yes/no question, then selects a Group and calls action(selected_group). Despite its name, this helper performs selection and the action; do not use it as a legality predicate or inside chk==0.
Declining the yes/no question, having too few candidates, or selecting an empty Group returns numeric 0 without running action. Canceling card selection returns to the yes/no question through RD.CanSelect. Once the player completes a nonempty selection, every callback return value is forwarded unchanged, including no values.
Like RD.SelectAndDoAction, it creates no activation target relation, passes no extra arguments to the filter/action, and emits a selection hint for public-location searches.

## Parameters

- `desc` `int`: Yes/no question description identifier.
- `hint` `int`: Card-selection prompt identifier.
- `filter` `function`: Card predicate including required action-legality checks.
- `tp` `int`: Selecting player; 0 or 1.
- `s_range` `int`: Locations on tp's side.
- `o_range` `int`: Locations on the opponent's side.
- `min` `int`: Minimum selected count.
- `max` `int`: Maximum selected count.
- `expect` `Card|Group|nil`: Card(s) excluded from matching; pass nil for none.
- `action` `function`: Called as action(selected_group) after the player accepts and completes selection.

## Returns

- `any`: Exactly the callback's return values when invoked; otherwise numeric 0. A callback may return no values.

## Source

`Rush/Utilities/RDAction.lua:107`

```lua
function RushDuel.CanSelectAndDoAction(desc, hint, filter, tp, s_range, o_range, min, max, expect, action)
    local hint_selection = RushDuel._private_is_include_public(s_range, o_range)
    return RushDuel._private_action_can_select_match(desc, hint, filter, tp, s_range, o_range, min, max, expect, hint_selection, false, action)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **509** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CanSelectAndDoAction) with `RushDuel.CanSelectAndDoAction`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lufer the Symbol of the Devils](/examples/rush-cards/120309059) | `120309059` | [Rush/Scripts/c120309059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309059.lua) | 1 |
| [Moonforce Ziggy](/examples/rush-cards/120300014) | `120300014` | [Rush/Scripts/c120300014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300014.lua) | 1 |
| [Freshberry Collaboration](/examples/rush-cards/120301071) | `120301071` | [Rush/Scripts/c120301071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301071.lua) | 1 |
| [Brassdes of the Wicked Wheels](/examples/rush-cards/120304033) | `120304033` | [Rush/Scripts/c120304033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304033.lua) | 1 |
| [Star Protector's Protection](/examples/rush-cards/120253065) | `120253065` | [Rush/Scripts/c120253065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253065.lua) | 1 |
| [Sparkhearts Makma](/examples/rush-cards/120298023) | `120298023` | [Rush/Scripts/c120298023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298023.lua) | 1 |
| [Imaginary Arc Turbulence](/examples/rush-cards/120196013) | `120196013` | [Rush/Scripts/c120196013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120196013.lua) | 1 |
| [Fairy of the Stars](/examples/rush-cards/120305016) | `120305016` | [Rush/Scripts/c120305016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305016.lua) | 1 |
| [Spice Cross Secret Recipe](/examples/rush-cards/120261060) | `120261060` | [Rush/Scripts/c120261060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261060.lua) | 1 |
| [Rising Protect](/examples/rush-cards/120304055) | `120304055` | [Rush/Scripts/c120304055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304055.lua) | 1 |
| [Curse of the Magiclad Dragon](/examples/rush-cards/120304061) | `120304061` | [Rush/Scripts/c120304061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304061.lua) | 1 |
| [Heavenly Bliss](/examples/rush-cards/120203033) | `120203033` | [Rush/Scripts/c120203033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203033.lua) | 1 |
| [Evolution Result Flash](/examples/rush-cards/120290063) | `120290063` | [Rush/Scripts/c120290063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290063.lua) | 1 |
| [Dimension Oper](/examples/rush-cards/120309025) | `120309025` | [Rush/Scripts/c120309025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309025.lua) | 1 |
| [Lovely Wolf](/examples/rush-cards/120260046) | `120260046` | [Rush/Scripts/c120260046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260046.lua) | 1 |
| [False Sun](/examples/rush-cards/120264033) | `120264033` | [Rush/Scripts/c120264033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264033.lua) | 1 |
| [Void Veil](/examples/rush-cards/120227029) | `120227029` | [Rush/Scripts/c120227029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120227029.lua) | 1 |
| [Preferlyre](/examples/rush-cards/120283046) | `120283046` | [Rush/Scripts/c120283046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283046.lua) | 1 |
| [Fist the Contractor of the Imprisoned Dragon](/examples/rush-cards/120306037) | `120306037` | [Rush/Scripts/c120306037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306037.lua) | 1 |
| [Lovely Rabbit](/examples/rush-cards/120300018) | `120300018` | [Rush/Scripts/c120300018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300018.lua) | 1 |
| [Botonaginata the Music Princess](/examples/rush-cards/120290009) | `120290009` | [Rush/Scripts/c120290009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290009.lua) | 1 |
| Sevens Road Ultima Witch | `120261045` | [Rush/Scripts/c120261045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261045.lua) | 1 |
| Daigyakutenno Megami | `120203019` | [Rush/Scripts/c120203019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203019.lua) | 1 |
| Fusionic Defense | `120257064` | [Rush/Scripts/c120257064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257064.lua) | 1 |
| ...and 485 more |  |  |  |

## Script Examples

### Lufer the Symbol of the Devils (`120309059`)

Source: [Rush/Scripts/c120309059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309059.lua)

```lua
		end)
		if Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_GRAVE,0,1,nil) then
			RD.CanSelectAndDoAction(aux.Stringid(m,5),HINTMSG_RTOHAND,cm.thfilter,tp,0,LOCATION_MZONE,1,1,nil,function(sg)
				RD.SendToHandAndExists(sg,e,tp,REASON_EFFECT)
			end)
```

### Moonforce Ziggy (`120300014`)

Source: [Rush/Scripts/c120300014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300014.lua)

```lua
		if not tc:IsImmuneToEffect(e) then
			tc:RegisterFlagEffect(FLAG_CANNOT_ATTACK_NEXT_TURN,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END+RESET_OPPO_TURN,0,1)
			RD.CanSelectAndDoAction(aux.Stringid(m,3),HINTMSG_TODECK,aux.NecroValleyFilter(cm.tdfilter),tp,LOCATION_GRAVE,0,1,1,nil,function(g)
				local c=e:GetHandler()
				if RD.SendToDeckBottom(g,e,tp,REASON_EFFECT)~=0
```

### Freshberry Collaboration (`120301071`)

Source: [Rush/Scripts/c120301071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301071.lua)

```lua
	RD.SelectAndDoAction(HINTMSG_POSCHANGE,filter,tp,LOCATION_MZONE,0,1,1,nil,function(g)
		if RD.ChangePosition(g,e,tp,REASON_EFFECT,POS_FACEUP_DEFENSE)~=0 and e:GetLabel()==1 then
			RD.CanSelectAndDoAction(aux.Stringid(m,1),HINTMSG_DESTROY,cm.desfilter,tp,0,LOCATION_MZONE,1,1,nil,function(sg)
				Duel.Destroy(sg,REASON_EFFECT)
			end)
```
