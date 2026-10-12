# RushDuel.TargetDamage

Alias: `RD.TargetDamage`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.TargetDamage(any player, any damage) -> any
```

## Description

Rush Duel helper declared in `RDTarget.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
对玩家效果: 伤害 - 对象
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `damage` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDTarget.lua:17`

```lua
function RushDuel.TargetDamage(player, damage)
    Duel.SetTargetPlayer(player)
    Duel.SetTargetParam(damage)
    Duel.SetOperationInfo(0, CATEGORY_DAMAGE, nil, 0, player, damage)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **49** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.TargetDamage) with `RushDuel.TargetDamage`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Spiral Geyser | `120199064` | [Rush/Scripts/c120199064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199064.lua) | 1 |
| Pitch-Dark Eradicator Sorcerer | `120309008` | [Rush/Scripts/c120309008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309008.lua) | 1 |
| Supreme Railartillery Magnum Overlord \[R\] | `120239003` | [Rush/Scripts/c120239003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239003.lua) | 1 |
| CAN:D LIVE | `120199035` | [Rush/Scripts/c120199035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199035.lua) | 1 |
| Cannon Soljersey | `120228016` | [Rush/Scripts/c120228016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228016.lua) | 1 |
| Terrorphone Number | `120217087` | [Rush/Scripts/c120217087.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217087.lua) | 1 |
| Breaking News! | `120199063` | [Rush/Scripts/c120199063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199063.lua) | 1 |
| Amusi Annoyance | `120249063` | [Rush/Scripts/c120249063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249063.lua) | 1 |
| Burst Ray Blaster | `120222022` | [Rush/Scripts/c120222022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120222022.lua) | 1 |
| Dragonic Domination | `120261064` | [Rush/Scripts/c120261064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261064.lua) | 1 |
| Space Bud Exploit | `120260015` | [Rush/Scripts/c120260015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260015.lua) | 1 |
| Defrostrooper Mk-II | `120261039` | [Rush/Scripts/c120261039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261039.lua) | 1 |
| Climax Clash | `120208060` | [Rush/Scripts/c120208060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120208060.lua) | 1 |
| Agent Mishap | `120257022` | [Rush/Scripts/c120257022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257022.lua) | 1 |
| Voidvelg Hecatoncheir | `120227007` | [Rush/Scripts/c120227007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120227007.lua) | 1 |
| Endless Romance Blitz | `120205034` | [Rush/Scripts/c120205034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120205034.lua) | 1 |
| Hiita the Fire Spiritualist | `120301011` | [Rush/Scripts/c120301011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301011.lua) | 1 |
| Accel Wonder Flare | `120186010` | [Rush/Scripts/c120186010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120186010.lua) | 1 |
| Sigurstate Sol | `120191004` | [Rush/Scripts/c120191004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120191004.lua) | 1 |
| Rolled Hot Arrow | `120151047` | [Rush/Scripts/c120151047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120151047.lua) | 1 |
| Reporting from the Scene! | `120199062` | [Rush/Scripts/c120199062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199062.lua) | 1 |
| Extra Spice the Elite Noodle Ninja | `120145033` | [Rush/Scripts/c120145033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120145033.lua) | 1 |
| Thunderbeetle Gift | `120150033` | [Rush/Scripts/c120150033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120150033.lua) | 1 |
| Vulcan Ignite Hyperdrive | `120205045` | [Rush/Scripts/c120205045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120205045.lua) | 1 |
| ...and 25 more |  |  |  |

## Script Examples

### Spiral Geyser (`120199064`)

Source: [Rush/Scripts/c120199064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199064.lua)

```lua
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	RD.TargetDamage(1-tp,400)
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
```

### Pitch-Dark Eradicator Sorcerer (`120309008`)

Source: [Rush/Scripts/c120309008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309008.lua)

```lua
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	RD.TargetDamage(1-tp,500)
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
```

### Supreme Railartillery Magnum Overlord [R] (`120239003`)

Source: [Rush/Scripts/c120239003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239003.lua)

```lua
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	RD.TargetDamage(1-tp,500)
	if RD.IsMaximumMode(e:GetHandler()) then
		Duel.Hint(HINT_OPSELECTED,1-tp,e:GetDescription())
```
