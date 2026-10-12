# RushDuel.IsSpecialSummonMainPhase

Alias: `RD.IsSpecialSummonMainPhase`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsSpecialSummonMainPhase(any card, any type) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 这张卡特殊召唤的自己主要阶段
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `type` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:42`

```lua
function RushDuel.IsSpecialSummonMainPhase(card, type)
    return card:IsReason(REASON_SPSUMMON) and card:IsStatus(STATUS_SPSUMMON_TURN) and card:GetFlagEffect(FLAG_SUMMON_MAIN_PHASE) ~= 0
        and (not type or card:IsSummonType(type))
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **69** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsSpecialSummonMainPhase) with `RushDuel.IsSpecialSummonMainPhase`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Volcalizing Salamandeus](/examples/rush-cards/120272039) | `120272039` | [Rush/Scripts/c120272039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272039.lua) | 1 |
| [Voidalfr Star Mayfly](/examples/rush-cards/120300034) | `120300034` | [Rush/Scripts/c120300034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300034.lua) | 1 |
| [Brassdes of the Wicked Wheels](/examples/rush-cards/120304033) | `120304033` | [Rush/Scripts/c120304033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304033.lua) | 1 |
| [Player #C39: Home Run Smasher V](/examples/rush-cards/120305028) | `120305028` | [Rush/Scripts/c120305028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305028.lua) | 1 |
| [Wako Gozen Riletta](/examples/rush-cards/120309021) | `120309021` | [Rush/Scripts/c120309021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309021.lua) | 1 |
| [YXZ-Cannon Dragon](/examples/rush-cards/120305004) | `120305004` | [Rush/Scripts/c120305004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305004.lua) | 1 |
| [Bluetech Burst Rex](/examples/rush-cards/120261044) | `120261044` | [Rush/Scripts/c120261044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261044.lua) | 1 |
| [Voidvelg Gehennamagia](/examples/rush-cards/120109048) | `120109048` | [Rush/Scripts/c120109048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109048.lua) | 1 |
| [Fist the Contractor of the Imprisoned Dragon](/examples/rush-cards/120306037) | `120306037` | [Rush/Scripts/c120306037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306037.lua) | 1 |
| Voidvelg Beyond Probe | `120300031` | [Rush/Scripts/c120300031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300031.lua) | 1 |
| Dark Matter Transcend Dragon | `120272044` | [Rush/Scripts/c120272044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272044.lua) | 1 |
| Cosmostar the White Hole Polairy | `120293045` | [Rush/Scripts/c120293045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293045.lua) | 1 |
| Harpie Lady Feather Duster | `120279002` | [Rush/Scripts/c120279002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120279002.lua) | 1 |
| Rising HERO Argent F | `120304043` | [Rush/Scripts/c120304043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304043.lua) | 1 |
| Dicemite Gyame Double-Up Chirori | `120272040` | [Rush/Scripts/c120272040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272040.lua) | 1 |
| Celeb Rose Rich Magicians | `120287040` | [Rush/Scripts/c120287040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287040.lua) | 1 |
| Tamabot King Golem | `120285039` | [Rush/Scripts/c120285039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285039.lua) | 1 |
| Ever-Grace Princess Hina | `120290038` | [Rush/Scripts/c120290038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290038.lua) | 1 |
| Divinebreath the Orchestral Music Fiend | `120247018` | [Rush/Scripts/c120247018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247018.lua) | 1 |
| Voidalfr Star Stripe | `120300033` | [Rush/Scripts/c120300033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300033.lua) | 1 |
| Harpie Regina Splendid Armor | `120279004` | [Rush/Scripts/c120279004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120279004.lua) | 1 |
| Whispurring Fairy | `120277047` | [Rush/Scripts/c120277047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277047.lua) | 1 |
| Amulet Dragon | `120309085` | [Rush/Scripts/c120309085.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309085.lua) | 1 |
| Reshef the Dark Being | `120306069` | [Rush/Scripts/c120306069.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306069.lua) | 1 |
| ...and 45 more |  |  |  |

## Script Examples

### Volcalizing Salamandeus (`120272039`)

Source: [Rush/Scripts/c120272039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272039.lua)

```lua
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) 
		and RD.IsSpecialSummonMainPhase(c) and e:GetLabel()==1 then
		RD.AttachExtraAttack(e,c,2,aux.Stringid(m,3),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end
```

### Voidalfr Star Mayfly (`120300034`)

Source: [Rush/Scripts/c120300034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300034.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsSpecialSummonMainPhase(e:GetHandler(),SUMMON_TYPE_FUSION)
end
cm.cost=RD.CostSendGraveSubToDeck(cm.costfilter,cm.check,3,3)
```

### Brassdes of the Wicked Wheels (`120304033`)

Source: [Rush/Scripts/c120304033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304033.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsSpecialSummonMainPhase(e:GetHandler())
end
cm.cost=RD.CostSendDeckTopToGrave(3)
```
