# RushDuel.CanSelectAndSpecialSummon

Alias: `RD.CanSelectAndSpecialSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanSelectAndSpecialSummon(int desc, function filter, int tp, int s_range, int o_range, int min, int max, Card|Group|nil expect, Effect e, int pos, [bool break_effect], [int target_player]) -> int
```

## Description

Optional action version of SelectAndSpecialSummon. If capacity and candidates exist, asks yes/no before selecting and summoning. Declining returns 0; canceling card selection returns to the yes/no question.
This performs work and belongs in resolution, not chk==0. It uses the same filter arguments, destination rules and actual numeric summon count as SelectAndSpecialSummon.

## Parameters

- `desc` `int`: Yes/no prompt description identifier.
- `filter` `function`: Candidate predicate; receives card,e,tp,pos,break_effect,target_player. Include per-card summon legality.
- `tp` `int`: Selecting and summoning player.
- `s_range` `int`: Source locations on tp side.
- `o_range` `int`: Source locations on the opponent side.
- `min` `int`: Minimum selected count.
- `max` `int`: Maximum count, capped by the destination zone count.
- `expect` `Card|Group|nil`: Excluded Card(s), or nil.
- `e` `Effect`: Source effect passed to the filter.
- `pos` `int`: Required summon position mask.
- `break_effect` `bool` (optional): Call Duel.BreakEffect immediately before summoning; default false.
- `target_player` `int` (optional): Destination player; defaults to tp. Does not change which player makes the choice.

## Returns

- `int`: Actual summon count, or 0 when declined/unavailable.

## Source

`Rush/Utilities/RDAction.lua:131`

```lua
function RushDuel.CanSelectAndSpecialSummon(desc, filter, tp, s_range, o_range, min, max, expect, e, pos, break_effect, target_player)
    local ct = RushDuel.GetMZoneCount(target_player or tp, max)
    if ct >= min then
        return RushDuel._private_action_can_select_match(desc, HINTMSG_SPSUMMON, filter, tp, s_range, o_range, min, ct, expect, false, false, RushDuel._special_summon, e, tp, pos, break_effect,
            target_player)
    end
    return 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **154** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CanSelectAndSpecialSummon) with `RushDuel.CanSelectAndSpecialSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Dark-Guiding Kuriboh](/examples/rush-cards/120280009) | `120280009` | [Rush/Scripts/c120280009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120280009.lua) | 1 |
| [Major Breaking News!](/examples/rush-cards/120304060) | `120304060` | [Rush/Scripts/c120304060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304060.lua) | 1 |
| [Dark Renewal](/examples/rush-cards/120285066) | `120285066` | [Rush/Scripts/c120285066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285066.lua) | 1 |
| [Magical Retribution](/examples/rush-cards/120254028) | `120254028` | [Rush/Scripts/c120254028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254028.lua) | 1 |
| [Gold Rush](/examples/rush-cards/120247059) | `120247059` | [Rush/Scripts/c120247059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247059.lua) | 1 |
| [Curse of the Magiclad Dragon](/examples/rush-cards/120304061) | `120304061` | [Rush/Scripts/c120304061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304061.lua) | 1 |
| [Lullalabind](/examples/rush-cards/120246073) | `120246073` | [Rush/Scripts/c120246073.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246073.lua) | 1 |
| [Star Protector Recapture](/examples/rush-cards/120306063) | `120306063` | [Rush/Scripts/c120306063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306063.lua) | 1 |
| [Chemicalizer Wing](/examples/rush-cards/120272057) | `120272057` | [Rush/Scripts/c120272057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272057.lua) | 1 |
| Dark Matter Transcend Dragon | `120272044` | [Rush/Scripts/c120272044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272044.lua) | 1 |
| Fusionic Revivern | `120109030` | [Rush/Scripts/c120109030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109030.lua) | 1 |
| Dicemite Gyame Double-Up Chirori | `120272040` | [Rush/Scripts/c120272040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272040.lua) | 1 |
| The Flame Dragon Haunting the Temple | `120309047` | [Rush/Scripts/c120309047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309047.lua) | 1 |
| Hysteric Party | `120279035` | [Rush/Scripts/c120279035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120279035.lua) | 1 |
| Multiple Adapter Unit | `120231030` | [Rush/Scripts/c120231030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231030.lua) | 1 |
| Ever-Grace Princess Hina | `120290038` | [Rush/Scripts/c120290038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290038.lua) | 1 |
| Takeout Attack | `120290060` | [Rush/Scripts/c120290060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290060.lua) | 1 |
| OuTerverSe Burst Oblivion | `120290008` | [Rush/Scripts/c120290008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290008.lua) | 1 |
| Iris the Rare Shadow Flower | `120228018` | [Rush/Scripts/c120228018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228018.lua) | 1 |
| Whispurring Fairy | `120277047` | [Rush/Scripts/c120277047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277047.lua) | 1 |
| Flip Dragon | `120253007` | [Rush/Scripts/c120253007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253007.lua) | 1 |
| The Ultimate Flag | `120294019` | [Rush/Scripts/c120294019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294019.lua) | 1 |
| Legendary Hunter | `120271046` | [Rush/Scripts/c120271046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271046.lua) | 1 |
| Abysslayer Apsaras | `120239028` | [Rush/Scripts/c120239028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239028.lua) | 1 |
| ...and 130 more |  |  |  |

## Script Examples

### Dark-Guiding Kuriboh (`120280009`)

Source: [Rush/Scripts/c120280009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120280009.lua)

```lua
			tc:RegisterFlagEffect(FLAG_CANNOT_ATTACK_NEXT_TURN,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END+RESET_OPPO_TURN,0,1)
		end
		RD.CanSelectAndSpecialSummon(aux.Stringid(m,3),aux.NecroValleyFilter(cm.spfilter),tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEDOWN_DEFENSE)
	end)
end
```

### Major Breaking News! (`120304060`)

Source: [Rush/Scripts/c120304060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304060.lua)

```lua
	RD.SelectAndDoAction(HINTMSG_TODECK,aux.NecroValleyFilter(Card.IsAbleToDeck),tp,0,LOCATION_GRAVE,2,2,nil,function(g)
		if RD.SendToDeckTop(g,e,tp,REASON_EFFECT)~=0 then
			RD.CanSelectAndSpecialSummon(aux.Stringid(m,1),cm.spfilter,tp,LOCATION_HAND,0,1,2,nil,e,POS_FACEUP_DEFENSE,true)
		end
	end)
```

### Dark Renewal (`120285066`)

Source: [Rush/Scripts/c120285066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285066.lua)

```lua
		Duel.HintSelection(sg)
		if Duel.Destroy(sg,REASON_EFFECT)~=0 then
			RD.CanSelectAndSpecialSummon(aux.Stringid(m,1),aux.NecroValleyFilter(cm.spfilter),tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEUP,true)
		end
	end
```
