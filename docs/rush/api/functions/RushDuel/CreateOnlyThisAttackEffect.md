# RushDuel.CreateOnlyThisAttackEffect

Alias: `RD.CreateOnlyThisAttackEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateOnlyThisAttackEffect(any e, any code, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 只能用这张卡进行攻击
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:248`

```lua
function RushDuel.CreateOnlyThisAttackEffect(e, code, player, s_range, o_range, reset)
    RushDuel.CreateOnlyThatAttackEffect(e, e:GetHandler(), code, player, s_range, o_range, reset)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateOnlyThisAttackEffect) with `RushDuel.CreateOnlyThisAttackEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Beast Gear King Convoy Liogon | `120145031` | [Rush/Scripts/c120145031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120145031.lua) | 1 |
| Executie Flame | `120235019` | [Rush/Scripts/c120235019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235019.lua) | 1 |
| Voidvelg Transi | `120109018` | [Rush/Scripts/c120109018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109018.lua) | 1 |
| Player #39: Home Run Hitter | `120199028` | [Rush/Scripts/c120199028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199028.lua) | 1 |
| Gingangel, the Deluxe Sushi Fairy | `120155030` | [Rush/Scripts/c120155030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155030.lua) | 1 |
| Galactica Rising Oblivion | `120304038` | [Rush/Scripts/c120304038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304038.lua) | 1 |

## Script Examples

### Beast Gear King Convoy Liogon (`120145031`)

Source: [Rush/Scripts/c120145031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120145031.lua)

```lua
	end
	RD.CreateHintEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateOnlyThisAttackEffect(e,20145031,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
end
function cm.atlimit(e,c)
```

### Executie Flame (`120235019`)

Source: [Rush/Scripts/c120235019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235019.lua)

```lua
	end
	RD.CreateHintEffect(e,aux.Stringid(m,2),tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateOnlyThisAttackEffect(e,20235019,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
end
```

### Voidvelg Transi (`120109018`)

Source: [Rush/Scripts/c120109018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109018.lua)

```lua
	end
	RD.CreateHintEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateOnlyThisAttackEffect(e,20109018,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
end
```
