# RushDuel.AttachLevel

Alias: `RD.AttachLevel`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachLevel(any e, any card, any level, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 等级升降
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `level` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:14`

```lua
function RushDuel.AttachLevel(e, card, level, reset, forced)
    return RushDuel.CreateSingleEffect(e, nil, card, EFFECT_UPDATE_LEVEL, level, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **44** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachLevel) with `RushDuel.AttachLevel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Preferlyre](/examples/rush-cards/120283046) | `120283046` | [Rush/Scripts/c120283046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283046.lua) | 1 |
| Pholus the Star Knight | `120203020` | [Rush/Scripts/c120203020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203020.lua) | 1 |
| Ice Age Pounder | `120304027` | [Rush/Scripts/c120304027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304027.lua) | 2 |
| Fiarma the Ally Spark | `120298025` | [Rush/Scripts/c120298025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298025.lua) | 1 |
| Peit the Ally Spark | `120298024` | [Rush/Scripts/c120298024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298024.lua) | 1 |
| Condurglar the Assisting Anthem | `120293064` | [Rush/Scripts/c120293064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293064.lua) | 1 |
| Tribute Kaiser | `120260073` | [Rush/Scripts/c120260073.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260073.lua) | 1 |
| Royal Rebel's Great Mixer | `120306004` | [Rush/Scripts/c120306004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306004.lua) | 1 |
| Transam Assault Linac | `120272035` | [Rush/Scripts/c120272035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272035.lua) | 1 |
| Hungry Special Coupon | `120300055` | [Rush/Scripts/c120300055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300055.lua) | 1 |
| Dedicated Gaia The Fierce Knight | `120293032` | [Rush/Scripts/c120293032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293032.lua) | 1 |
| Kyoshee of the Forbidden Fist | `120297005` | [Rush/Scripts/c120297005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120297005.lua) | 1 |
| Drahe the Wyrm Vassal | `120291004` | [Rush/Scripts/c120291004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120291004.lua) | 1 |
| Fusionic Tribevern | `120261036` | [Rush/Scripts/c120261036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261036.lua) | 1 |
| Dragonic Scout | `120246028` | [Rush/Scripts/c120246028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246028.lua) | 1 |
| Chaos Material | `120293034` | [Rush/Scripts/c120293034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293034.lua) | 1 |
| Soen the Molten Martial Machine | `120304036` | [Rush/Scripts/c120304036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304036.lua) | 1 |
| Delirium Polynea | `120277033` | [Rush/Scripts/c120277033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277033.lua) | 1 |
| Jointech Prime Rex | `120109041` | [Rush/Scripts/c120109041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109041.lua) | 1 |
| Executie Mates | `120283050` | [Rush/Scripts/c120283050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283050.lua) | 1 |
| Royal Wisdom Guards | `120261031` | [Rush/Scripts/c120261031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261031.lua) | 1 |
| Archfiend Shaman | `120277020` | [Rush/Scripts/c120277020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277020.lua) | 1 |
| Glacies the Snowmeister of Sacred Splendor | `120253034` | [Rush/Scripts/c120253034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253034.lua) | 1 |
| Transam Linac Overwrite | `120245001` | [Rush/Scripts/c120245001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120245001.lua) | 1 |
| ...and 20 more |  |  |  |

## Script Examples

### Preferlyre (`120283046`)

Source: [Rush/Scripts/c120283046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283046.lua)

```lua
		if c:IsFaceup() and c:IsRelateToEffect(e) then
			Duel.BreakEffect()
			RD.AttachLevel(e,c,2,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			RD.CanSelectAndDoAction(aux.Stringid(m,2),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),tp,LOCATION_GRAVE,0,1,1,nil,function(g)
				RD.SendToHandAndExists(g,e,tp,REASON_EFFECT)
```

### Pholus the Star Knight (`120203020`)

Source: [Rush/Scripts/c120203020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203020.lua)

```lua
			Duel.BreakEffect()
			sg:ForEach(function(tc)
				RD.AttachLevel(e,tc,-4,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			end)
		end
```

### Ice Age Pounder (`120304027`)

Source: [Rush/Scripts/c120304027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304027.lua)

```lua
		local g=Duel.GetOperatedGroup()
		g:ForEach(function(tc)
			RD.AttachLevel(e,tc,1,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		end)
		RD.CanSelectAndDoAction(aux.Stringid(m,1),aux.Stringid(m,2),cm.filter,tp,LOCATION_MZONE,0,1,1,nil,function(sg)
```
