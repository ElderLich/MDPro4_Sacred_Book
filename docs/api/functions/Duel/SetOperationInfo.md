# Duel.SetOperationInfo

## Signature

```lua
Duel.SetOperationInfo(int chainc, int category, Card|Group|nil targets, int count, int player, int param) -> void
```

## Description

Records operation information for category on chainc.
Use concrete targets and count when the affected cards are known. For unresolved non-targeting movement effects, pass nil targets with the expected count, target player, and target location.
For LP effects, target_player is the affected player and target_param is the amount. This information announces intent; it does not perform the operation or create official card targets.

## How To Use It

Call this in the Target callback when the Chain Link can announce a category, affected cards or players, count, amount, or source location.

Known targets can be passed directly:

```lua
local g=Duel.SelectTarget(tp,s.filter,tp,0,LOCATION_ONFIELD,1,1,nil)
Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,1,0,0)
```

For unresolved movement from a location, pass `nil` for targets and use `target_player` plus `target_param` as the location or amount:

```lua
Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
Duel.SetOperationInfo(0,CATEGORY_DAMAGE,nil,0,1-tp,800)
```

This announces intent; the operation still has to recheck legality and perform the actual action.

## Related Functions

- [Effect.SetCategory](/api/functions/Effect/SetCategory)
- [Duel.GetOperationInfo](/api/functions/Duel/GetOperationInfo)
- [Duel.SetTargetPlayer](/api/functions/Duel/SetTargetPlayer)
- [Duel.SetTargetParam](/api/functions/Duel/SetTargetParam)

## Parameters

- `chainc` `int` - Chain index/count passed to the core chain lookup; scripts commonly use 0 for the current Chain Link.
- `category` `int` - CATEGORY_* operation category to record.
- `targets` `Card|Group|nil` - Known affected cards. Card or Group values are cloned into a read-only Group; nil records only count, player, and param.
- `count` `int` - Expected number of affected cards.
- `player` `int` - Target player stored in the operation info.
- `param` `int` - Category-specific value, commonly a destination location, amount, or other operation parameter.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5008`

## Guided Examples

Learn how to use this function in context:

- [Methods for Affecting Cards](/learn/affecting-cards)
- [Beginner Script Ladder](/learn/beginner-script-ladder)
- [Categories, Properties, And Hint Timing](/learn/categories-properties-and-hints)
- [Chain Timing And Activation Windows](/learn/chain-timing-and-activation-windows)
- [Client UI And Prompt Behavior](/learn/client-ui-and-prompt-behavior)
- [Common Script Errors And Debugging](/learn/common-script-errors-and-debugging)

::: details More guided lessons (11)

- [Counter Traps](/learn/counter-traps)
- [Counters](/learn/counters)
- [Conditions, Costs, Activation Procedures, and Resolution](/learn/effect-callbacks)
- [Write Your First Custom Card](/learn/first-custom-card)
- [LP Recovery and Effect Damage](/learn/lp-recovery-and-damage)
- [Min/Max Stat Card Selection](/learn/min-max-stat-selection)
- [Functions That Move Cards Across Locations](/learn/moving-cards)
- [Player-Targeted Effects](/learn/player-targeted-effects)
- [Quick-Play Spells](/learn/quick-play-spells)
- [Spell Card Patterns](/learn/spell-card-patterns)
- [Targeting Flow](/learn/targeting-flow)

:::

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **10772** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SetOperationInfo) with `Duel.SetOperationInfo`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua) | 3 |
| [Astrograph Sorcerer, the Starfrost Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua) | 3 |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua) | 1 |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 1 |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78579058.lua) | 3 |
| [Lady's Dragonmaid](/examples/cards/48658295) | `48658295` | [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48658295.lua) | 3 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41570943.lua) | 2 |
| [Eternal Favorite](/examples/cards/87532344) | `87532344` | [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87532344.lua) | 2 |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua) | 3 |
| [Astrograph Sorcerer](/examples/cards/76794549) | `76794549` | [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76794549.lua) | 3 |
| [Spellbook of the Grand Circle](/examples/cards/11911336) | `11911336` | [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11911336.lua) | 3 |
| [Ultra Polymerization](/examples/cards/76647978) | `76647978` | [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76647978.lua) | 2 |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 3 |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua) | 2 |
| [Melffy Playtime Surprise](/examples/cards/58036097) | `58036097` | [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua) | 1 |
| [Ashtraja Susanoo](/examples/cards/17020474) | `17020474` | [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17020474.lua) | 3 |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua) | 4 |
| [Destiny HERO - Destro-Dogma](/examples/cards/25158975) | `25158975` | [Scripts/c25158975.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25158975.lua) | 2 |
| [Yomagna the Fire Phantom](/examples/cards/17350692) | `17350692` | [Scripts/c17350692.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17350692.lua) | 1 |
| [Fiendsmith's Sequence](/examples/cards/49867899) | `49867899` | [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49867899.lua) | 4 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11852093.lua) | 3 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 2 |
| [Mementotlan Fusion](/examples/cards/66518509) | `66518509` | [Scripts/c66518509.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66518509.lua) | 4 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua) | 2 |
| ...and 10748 more |  |  |  |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_EQUIP)
	Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
	Duel.SetOperationInfo(0,CATEGORY_EQUIP,e:GetHandler(),1,0,0)
end
function s.posfilter(c)
```

### Astrograph Sorcerer, the Starfrost Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
	if chk==0 then return c:IsDestructable()
		and Duel.IsExistingMatchingCard(s.pfilter,tp,LOCATION_HAND+LOCATION_DECK,0,1,nil,tp) end
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,c,1,0,0)
end
function s.pop(e,tp,eg,ep,ev,re,r,rp)
```

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
	end
	Duel.Hint(HINT_OPSELECTED,1-tp,e:GetDescription())
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_EXTRA)
end
function s.fspop(e,tp,eg,ep,ev,re,r,rp)
```
