# RushDuel.AddContinuousEffect

Alias: `RD.AddContinuousEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddContinuousEffect(any c, ... any) -> any
```

## Description

Rush Duel helper declared in `RDContinuous.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加永续效果列表
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDContinuous.lua:5`

```lua
function RushDuel.AddContinuousEffect(c, ...)
    if c:IsStatus(STATUS_COPYING_EFFECT) then
        return
    end
    if c.continuous_effect == nil then
        local mt = getmetatable(c)
        mt.continuous_effect = {...}
    else
        for _, e in ipairs {...} do
            table.insert(c.continuous_effect, e)
        end
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **203** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddContinuousEffect) with `RushDuel.AddContinuousEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Supreme Machine Magnum Overlord](/examples/rush-cards/120150002) | `120150002` | [Rush/Scripts/c120150002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150002.lua) | 1 |
| Souffraruda the Defiant Soulclad Scripture | `120298002` | [Rush/Scripts/c120298002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298002.lua) | 1 |
| Plandolin-a-la-Mode | `120264042` | [Rush/Scripts/c120264042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264042.lua) | 1 |
| Twin Blaze Fiend Angel Lunael | `120287032` | [Rush/Scripts/c120287032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287032.lua) | 1 |
| Supreme Beasteam Magnum Overlord \[R\] | `120217003` | [Rush/Scripts/c120217003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217003.lua) | 1 |
| Cross Lostream Verdias | `120309035` | [Rush/Scripts/c120309035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309035.lua) | 1 |
| Isyria, Deity of the Monumenthes | `120300037` | [Rush/Scripts/c120300037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300037.lua) | 1 |
| Plasma Saber the Super Graphagas | `120272038` | [Rush/Scripts/c120272038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272038.lua) | 1 |
| Dark Paladin | `120283002` | [Rush/Scripts/c120283002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283002.lua) | 1 |
| Transam Prime Armor Nova | `120257008` | [Rush/Scripts/c120257008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257008.lua) | 1 |
| Exalted Celestial Custodian of the Sacred Summit | `120304100` | [Rush/Scripts/c120304100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304100.lua) | 1 |
| God Maju Garzett | `120261043` | [Rush/Scripts/c120261043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261043.lua) | 1 |
| Ancient Gear Megaton Golem | `120283030` | [Rush/Scripts/c120283030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283030.lua) | 1 |
| Deity of Seven Treasures - Ryozai | `120257036` | [Rush/Scripts/c120257036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257036.lua) | 1 |
| Dark Matter Enigmata | `120261048` | [Rush/Scripts/c120261048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261048.lua) | 1 |
| Dark Matter Deep Badger | `120264004` | [Rush/Scripts/c120264004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264004.lua) | 1 |
| Eternum Voidvelg Requiem | `120300032` | [Rush/Scripts/c120300032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300032.lua) | 1 |
| Draco the Doubly Tiny | `120294039` | [Rush/Scripts/c120294039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294039.lua) | 1 |
| Cuilades the Skysavior Dismal Dark | `120301038` | [Rush/Scripts/c120301038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301038.lua) | 1 |
| Abyssal Sea Dragon Abyss Kraken | `120239017` | [Rush/Scripts/c120239017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239017.lua) | 1 |
| Dark Cavalry | `120283028` | [Rush/Scripts/c120283028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283028.lua) | 1 |
| Speed Major | `120301057` | [Rush/Scripts/c120301057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301057.lua) | 1 |
| Great Moth Alternative | `120298032` | [Rush/Scripts/c120298032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298032.lua) | 1 |
| Dark Sword Magician | `120246080` | [Rush/Scripts/c120246080.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246080.lua) | 1 |
| ...and 179 more |  |  |  |

## Script Examples

### Supreme Machine Magnum Overlord (`120150002`)

Source: [Rush/Scripts/c120150002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150002.lua)

```lua
	c:RegisterEffect(e1)
	--Continuous Effect
	RD.AddContinuousEffect(c,e1)
end
--Indes
```

### Souffraruda the Defiant Soulclad Scripture (`120298002`)

Source: [Rush/Scripts/c120298002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298002.lua)

```lua
	c:RegisterEffect(e2)
	--Continuous Effect
	RD.AddContinuousEffect(c,e1,e2)
end
--Damage
```

### Plandolin-a-la-Mode (`120264042`)

Source: [Rush/Scripts/c120264042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264042.lua)

```lua
	c:RegisterEffect(e1)
	--Continuous Effect
	RD.AddContinuousEffect(c,e1)
end
-- Fusion Expend
```
