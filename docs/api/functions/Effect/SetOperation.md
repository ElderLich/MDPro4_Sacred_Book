# Effect.SetOperation

## Signature

```lua
Effect.SetOperation(Effect e, nil|function op_func) -> void
```

## Description

Sets e's operation callback. Passing nil clears the operation.
For activated effects, this callback resolves after the Chain reaches this Link, so it should re-check targets, locations, relation, and other state that may have changed since activation.

## How To Use It

The operation callback performs the effect when the Chain resolves.

For targeted cards, retrieve the target and re-check that it is still related to the resolving effect before applying the action:

```lua
function s.operation(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc and tc:IsRelateToEffect(e) then
        Duel.Destroy(tc,REASON_EFFECT)
    end
end
```

Passing nil to `SetOperation` clears the operation. That is occasionally useful for effects whose category or target data is enough and no resolution callback is needed.

## Related Functions

- [Effect.SetTarget](/api/functions/Effect/SetTarget)
- [Duel.GetFirstTarget](/api/functions/Duel/GetFirstTarget)
- [Duel.GetTargetsRelateToChain](/api/functions/Duel/GetTargetsRelateToChain)

## Parameters

- `e` `Effect` - Effect whose operation callback is replaced or cleared.
- `op_func` `nil|function` - Operation callback, or nil to clear it.

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:629`

## Guided Examples

Learn how to use this function in context:

- [Beginner Script Ladder](/learn/beginner-script-ladder)
- [Effects That Apply Continuously](/learn/continuous-effects)
- [Cost, Target, And Operation Lifecycle](/learn/cost-target-operation-lifecycle)
- [Counter Traps](/learn/counter-traps)
- [Conditions, Costs, Activation Procedures, and Resolution](/learn/effect-callbacks)
- [Creation, Building, and Registration of an Effect Object](/learn/effect-object)

::: details More guided lessons (2)

- [Write Your First Custom Card](/learn/first-custom-card)
- [Quick-Play Spells](/learn/quick-play-spells)

:::

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **12825** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Effect.SetOperation) with `Effect.SetOperation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62091148.lua) | 4 |
| [Astrograph Sorcerer, the Starfrost Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua) | 3 |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74631897.lua) | 4 |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55795155.lua) | 4 |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua) | 3 |
| [Lady's Dragonmaid](/examples/cards/48658295) | `48658295` | [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48658295.lua) | 3 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua) | 3 |
| [Eternal Favorite](/examples/cards/87532344) | `87532344` | [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87532344.lua) | 5 |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35167375.lua) | 2 |
| [Astrograph Sorcerer](/examples/cards/76794549) | `76794549` | [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76794549.lua) | 5 |
| [Spellbook of the Grand Circle](/examples/cards/11911336) | `11911336` | [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11911336.lua) | 5 |
| [Ultra Polymerization](/examples/cards/76647978) | `76647978` | [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76647978.lua) | 2 |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59255742.lua) | 5 |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30983281.lua) | 2 |
| [Melffy Playtime Surprise](/examples/cards/58036097) | `58036097` | [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58036097.lua) | 2 |
| [Ashtraja Susanoo](/examples/cards/17020474) | `17020474` | [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17020474.lua) | 2 |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92171126.lua) | 6 |
| [Destiny HERO - Destro-Dogma](/examples/cards/25158975) | `25158975` | [Scripts/c25158975.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25158975.lua) | 4 |
| [Yomagna the Fire Phantom](/examples/cards/17350692) | `17350692` | [Scripts/c17350692.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17350692.lua) | 3 |
| [Fiendsmith's Sequence](/examples/cards/49867899) | `49867899` | [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49867899.lua) | 2 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11852093.lua) | 2 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50907446.lua) | 3 |
| [Mementotlan Fusion](/examples/cards/66518509) | `66518509` | [Scripts/c66518509.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66518509.lua) | 3 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24166324.lua) | 2 |
| ...and 12801 more |  |  |  |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
	e1:SetCost(s.cost)
	e1:SetTarget(s.target)
	e1:SetOperation(s.operation)
	c:RegisterEffect(e1)
	--
```

### Astrograph Sorcerer, the Starfrost Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
	e1:SetCountLimit(1,id)
	e1:SetTarget(s.ptg)
	e1:SetOperation(s.pop)
	c:RegisterEffect(e1)
	--special summon
```

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
	e0:SetCode(EVENT_SPSUMMON_SUCCESS)
	e0:SetCondition(s.condition)
	e0:SetOperation(s.regop)
	c:RegisterEffect(e0)
	--spsummon condition
```
