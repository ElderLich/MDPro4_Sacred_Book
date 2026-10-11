# RushDuel.AddFusionProcedure

Alias: `RD.AddFusionProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddFusionProcedure(Card card, bool|any sub, bool|any insf, ... int|function|table) -> Effect|nil
```

## Description

Registers a Rush Fusion material procedure using fixed material slots. Each slot may be a card code, a predicate, or a table of alternatives. sub controls substitutes and insf permits non-Fusion special-summon handling; use explicit booleans to make the call unambiguous.

## Parameters

- `card` `Card`: Fusion monster.
- `sub` `bool|any`: Substitute permission; non-booleans are interpreted as the first material slot.
- `insf` `bool|any`: Non-Fusion summon allowance; non-booleans are interpreted as a material slot.
- `...` `int|function|table`: Material slots.

## Returns

- `Effect|nil`: Fusion procedure effect; nil while copying effects.

## Source

`Rush/Utilities/RDFusion.lua:15`

```lua
function RushDuel.AddFusionProcedure(card, sub, insf, ...)
    if card:IsStatus(STATUS_COPYING_EFFECT) then
        return
    end
    local vals = {...}
    -- 简易融合
    if type(insf) ~= "boolean" then
        table.insert(vals, 1, insf)
        insf = true
    end
    -- 融合素材替代
    if type(sub) ~= "boolean" then
        table.insert(vals, 1, sub)
        sub = true
    end
    -- 融合素材
    local codes, funcs = RushDuel.MakeFusionMaterial(card, table.unpack(vals))
    RushDuel.SetFusionMaterialData(card, codes, #funcs, #funcs)
    return RushDuel.CreateFusionProcedure(card, sub, insf, funcs, nil, 0, 0, nil)
end
```

## Guided Examples

Learn how to use this function in context:

- [Rush Maximum, Fusion, And Ritual](/learn/rush-summon-procedures)

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **307** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddFusionProcedure) with `RushDuel.AddFusionProcedure`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Volcalizing Salamandeus](/examples/rush-cards/120272039) | `120272039` | [Rush/Scripts/c120272039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272039.lua) | 1 |
| [Voidalfr Star Mayfly](/examples/rush-cards/120300034) | `120300034` | [Rush/Scripts/c120300034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300034.lua) | 1 |
| [Vapor Lancer the Super Graphagas](/examples/rush-cards/120260063) | `120260063` | [Rush/Scripts/c120260063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260063.lua) | 1 |
| [Fairy of the Stars](/examples/rush-cards/120305016) | `120305016` | [Rush/Scripts/c120305016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305016.lua) | 1 |
| [Galactica Lost Oblivion](/examples/rush-cards/120277042) | `120277042` | [Rush/Scripts/c120277042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277042.lua) | 1 |
| [Bluetech Burst Rex](/examples/rush-cards/120261044) | `120261044` | [Rush/Scripts/c120261044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261044.lua) | 1 |
| [Red-Reboot Enhanced Boost Dragon](/examples/rush-cards/120253037) | `120253037` | [Rush/Scripts/c120253037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253037.lua) | 1 |
| [Voidvelg Gehennamagia](/examples/rush-cards/120109048) | `120109048` | [Rush/Scripts/c120109048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109048.lua) | 1 |
| [Fist the Contractor of the Imprisoned Dragon](/examples/rush-cards/120306037) | `120306037` | [Rush/Scripts/c120306037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306037.lua) | 1 |
| [Star Cat Destronya](/examples/rush-cards/120235037) | `120235037` | [Rush/Scripts/c120235037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235037.lua) | 1 |
| [Thousand Dragon](/examples/rush-cards/120102001) | `120102001` | [Rush/Scripts/c120102001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120102001.lua) | 1 |
| Voidvelg Beyond Probe | `120300031` | [Rush/Scripts/c120300031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300031.lua) | 1 |
| Sevens Road Ultima Witch | `120261045` | [Rush/Scripts/c120261045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261045.lua) | 1 |
| Dark Matter Transcend Dragon | `120272044` | [Rush/Scripts/c120272044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272044.lua) | 1 |
| Yamiterasu the Divine Ruler | `120199036` | [Rush/Scripts/c120199036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199036.lua) | 1 |
| Cosmostar the White Hole Polairy | `120293045` | [Rush/Scripts/c120293045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293045.lua) | 1 |
| Harpie Lady Feather Duster | `120279002` | [Rush/Scripts/c120279002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120279002.lua) | 1 |
| Magical Weapoknight Xeno One | `120306038` | [Rush/Scripts/c120306038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306038.lua) | 1 |
| Rising HERO Argent O | `120304042` | [Rush/Scripts/c120304042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304042.lua) | 1 |
| Rising HERO Argent F | `120304043` | [Rush/Scripts/c120304043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304043.lua) | 1 |
| Dicemite Gyame Double-Up Chirori | `120272040` | [Rush/Scripts/c120272040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272040.lua) | 1 |
| The Trinity Dragiastar | `120109031` | [Rush/Scripts/c120109031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109031.lua) | 1 |
| Celeb Rose Influencers | `120257044` | [Rush/Scripts/c120257044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257044.lua) | 1 |
| The Dragiastar | `120235035` | [Rush/Scripts/c120235035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235035.lua) | 1 |
| ...and 283 more |  |  |  |

## Script Examples

### Volcalizing Salamandeus (`120272039`)

Source: [Rush/Scripts/c120272039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272039.lua)

```lua
	RD.AddCodeList(c,list)
	--Fusion Material
	RD.AddFusionProcedure(c,list[1],cm.matfilter)
	--Atk Down
	local e1=Effect.CreateEffect(c)
```

### Voidalfr Star Mayfly (`120300034`)

Source: [Rush/Scripts/c120300034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300034.lua)

```lua
	RD.AddCodeList(c,list)
	--Fusion Material
	RD.AddFusionProcedure(c,list[1],cm.matfilter)
	--To Hand
	local e1=Effect.CreateEffect(c)
```

### Vapor Lancer the Super Graphagas (`120260063`)

Source: [Rush/Scripts/c120260063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260063.lua)

```lua
	RD.AddCodeList(c,list)
	--Fusion Material
	RD.AddFusionProcedure(c,list[1],list[2])
	--Discard Deck
	local e1=Effect.CreateEffect(c)
```
