# RushDuel.CreateCannotActivateEffect

Alias: `RD.CreateCannotActivateEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateCannotActivateEffect(any e, any desc, any value, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 不能把效果发动
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:310`

```lua
function RushDuel.CreateCannotActivateEffect(e, desc, value, player, s_range, o_range, reset)
    return RushDuel.CreateCannotActivateMix(e, desc, player, s_range, o_range, reset, value)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **25** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateCannotActivateEffect) with `RushDuel.CreateCannotActivateEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Elemental Circulation](/examples/rush-cards/120263030) | `120263030` | [Rush/Scripts/c120263030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263030.lua) | 1 |
| [Pot of Duality](/examples/rush-cards/120271002) | `120271002` | [Rush/Scripts/c120271002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271002.lua) | 1 |
| [Ember the Ultra Assistant](/examples/rush-cards/120283035) | `120283035` | [Rush/Scripts/c120283035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283035.lua) | 1 |
| [Tubardiche the Music Princess](/examples/rush-cards/120247025) | `120247025` | [Rush/Scripts/c120247025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247025.lua) | 1 |
| [Voidvelg Gehennamagia](/examples/rush-cards/120109048) | `120109048` | [Rush/Scripts/c120109048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109048.lua) | 1 |
| [Red-Eyes Mars Dragon](/examples/rush-cards/120306034) | `120306034` | [Rush/Scripts/c120306034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306034.lua) | 1 |
| Hysteric Eyes | `120304063` | [Rush/Scripts/c120304063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304063.lua) | 1 |
| Celeb Rose Rich Magicians | `120287040` | [Rush/Scripts/c120287040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287040.lua) | 1 |
| Jointech Nesstrydar Tank | `120257017` | [Rush/Scripts/c120257017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257017.lua) | 1 |
| Voidalfr Buprestruve | `120300003` | [Rush/Scripts/c120300003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300003.lua) | 1 |
| Moonforce Piyopi | `120300011` | [Rush/Scripts/c120300011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300011.lua) | 1 |
| The Secret of Manifestation | `120257051` | [Rush/Scripts/c120257051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257051.lua) | 1 |
| Animagica Coin | `120277056` | [Rush/Scripts/c120277056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277056.lua) | 1 |
| Marsphlox the Planetairy | `120293050` | [Rush/Scripts/c120293050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293050.lua) | 1 |
| Healthie Olivia | `120306023` | [Rush/Scripts/c120306023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306023.lua) | 1 |
| Strange Attractor | `120260017` | [Rush/Scripts/c120260017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260017.lua) | 1 |
| Jointech Spike Centipede | `120249007` | [Rush/Scripts/c120249007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249007.lua) | 1 |
| Prime Call | `120257048` | [Rush/Scripts/c120257048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257048.lua) | 1 |
| Jointech Cobra | `120249002` | [Rush/Scripts/c120249002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249002.lua) | 1 |
| Yewearth the Planetairy | `120293051` | [Rush/Scripts/c120293051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293051.lua) | 1 |
| Moonforce Rifet | `120300012` | [Rush/Scripts/c120300012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300012.lua) | 1 |
| Lore Leimey | `120294037` | [Rush/Scripts/c120294037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294037.lua) | 1 |
| Animagica Leader | `120260074` | [Rush/Scripts/c120260074.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260074.lua) | 1 |
| Phantasmal Triangular Scale | `120264054` | [Rush/Scripts/c120264054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264054.lua) | 1 |
| ...and 1 more |  |  |  |

## Script Examples

### Elemental Circulation (`120263030`)

Source: [Rush/Scripts/c120263030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263030.lua)

```lua
	end
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateCannotActivateEffect(e,aux.Stringid(m,2),cm.aclimit,tp,1,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```

### Pot of Duality (`120271002`)

Source: [Rush/Scripts/c120271002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271002.lua)

```lua
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateCannotSpecialSummonEffect(e,aux.Stringid(m,1),nil,tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateCannotActivateEffect(e,aux.Stringid(m,2),cm.aclimit,tp,1,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```

### Ember the Ultra Assistant (`120283035`)

Source: [Rush/Scripts/c120283035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283035.lua)

```lua
	end
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateCannotActivateEffect(e,aux.Stringid(m,2),cm.aclimit,tp,1,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```
