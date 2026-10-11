# RushDuel.IsPreviousControler

Alias: `RD.IsPreviousControler`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPreviousControler(any card, any player) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 位置变化前的控制者
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:190`

```lua
function RushDuel.IsPreviousControler(card, player)
    return card:GetPreviousControler() == player
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **36** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPreviousControler) with `RushDuel.IsPreviousControler`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Heavenly Bliss](/examples/rush-cards/120203033) | `120203033` | [Rush/Scripts/c120203033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203033.lua) | 2 |
| [Sunset Rebirth](/examples/rush-cards/120257066) | `120257066` | [Rush/Scripts/c120257066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257066.lua) | 1 |
| Hysteric Party | `120279035` | [Rush/Scripts/c120279035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120279035.lua) | 1 |
| Critical Service | `120260022` | [Rush/Scripts/c120260022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260022.lua) | 1 |
| Executie Emergency! | `120231040` | [Rush/Scripts/c120231040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231040.lua) | 1 |
| Earth Pressure Explosion | `120155058` | [Rush/Scripts/c120155058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155058.lua) | 1 |
| Looter Force | `120228064` | [Rush/Scripts/c120228064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228064.lua) | 1 |
| Phantom Roar | `120235065` | [Rush/Scripts/c120235065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235065.lua) | 1 |
| Gagaga Guts | `120199060` | [Rush/Scripts/c120199060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199060.lua) | 1 |
| Dark Ruler Sword Swipe | `120188030` | [Rush/Scripts/c120188030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120188030.lua) | 1 |
| RB Dragophone | `120225032` | [Rush/Scripts/c120225032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120225032.lua) | 1 |
| Collapsing Chairs | `120150041` | [Rush/Scripts/c120150041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150041.lua) | 1 |
| Transam Alive | `120216028` | [Rush/Scripts/c120216028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120216028.lua) | 1 |
| Explosive Destructor Wyrm Dangerous Bakhamut | `120247038` | [Rush/Scripts/c120247038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247038.lua) | 1 |
| Breaking News! | `120199063` | [Rush/Scripts/c120199063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199063.lua) | 1 |
| Dark Nebula | `120235059` | [Rush/Scripts/c120235059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235059.lua) | 1 |
| Resurrection of the Blaze Fiends | `120231017` | [Rush/Scripts/c120231017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231017.lua) | 1 |
| Archfiend's Revival | `120170062` | [Rush/Scripts/c120170062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170062.lua) | 1 |
| Climax Clash | `120208060` | [Rush/Scripts/c120208060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208060.lua) | 1 |
| Imaginary Arc Turnback | `120196014` | [Rush/Scripts/c120196014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120196014.lua) | 1 |
| Soul of a Reporter | `120145054` | [Rush/Scripts/c120145054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120145054.lua) | 1 |
| Maid's Baneful Gift | `120205065` | [Rush/Scripts/c120205065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205065.lua) | 1 |
| Requesting 9 | `120199061` | [Rush/Scripts/c120199061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199061.lua) | 1 |
| Counter Back | `120203031` | [Rush/Scripts/c120203031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203031.lua) | 1 |
| ...and 12 more |  |  |  |

## Script Examples

### Heavenly Bliss (`120203033`)

Source: [Rush/Scripts/c120203033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203033.lua)

```lua
--Activate
function cm.confilter(c,tp,rp)
	return RD.IsPreviousControler(c,tp) and c:IsPreviousLocation(LOCATION_MZONE)
		and ((rp==1-tp and c:IsReason(REASON_EFFECT)) or c==Duel.GetAttackTarget())
end
```

### Sunset Rebirth (`120257066`)

Source: [Rush/Scripts/c120257066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257066.lua)

```lua
cm.indval=RD.ValueEffectIndesType(0,TYPE_MONSTER+TYPE_SPELL+TYPE_TRAP)
function cm.confilter(c,tp)
	return RD.IsPreviousControler(c,tp) and c:IsPreviousLocation(LOCATION_MZONE)
		and c:IsReason(REASON_EFFECT)
end
```

### Hysteric Party (`120279035`)

Source: [Rush/Scripts/c120279035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120279035.lua)

```lua
--Activate
function cm.confilter(c,tp)
	return RD.IsPreviousControler(c,tp) and c==Duel.GetAttackTarget()
end
function cm.spfilter(c,e,tp)
```
