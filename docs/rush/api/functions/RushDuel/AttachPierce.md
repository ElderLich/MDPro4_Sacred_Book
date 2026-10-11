# RushDuel.AttachPierce

Alias: `RD.AttachPierce`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachPierce(any e, any card, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 贯通
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:22`

```lua
function RushDuel.AttachPierce(e, card, desc, reset, forced)
    return RushDuel.CreateSingleEffect(e, desc, card, EFFECT_PIERCE, nil, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **67** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachPierce) with `RushDuel.AttachPierce`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dark Matter Transcend Dragon | `120272044` | [Rush/Scripts/c120272044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272044.lua) | 1 |
| Transam Scride | `120109036` | [Rush/Scripts/c120109036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109036.lua) | 1 |
| Super Princess of the Flock - Max Mutton \[L\] | `120293007` | [Rush/Scripts/c120293007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293007.lua) | 1 |
| Sevens Road Charmy Witch | `120260062` | [Rush/Scripts/c120260062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260062.lua) | 1 |
| Steel Mech Lord Mirror Innovator | `120155015` | [Rush/Scripts/c120155015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155015.lua) | 1 |
| Steel Mech Lord Mirror Innovator | `120239059` | [Rush/Scripts/c120239059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239059.lua) | 1 |
| Abyssal Sea Dragon Abyss Kraken \[R\] | `120239018` | [Rush/Scripts/c120239018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239018.lua) | 1 |
| Divinebreath the Orchestral Music Fiend | `120247018` | [Rush/Scripts/c120247018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247018.lua) | 1 |
| Roaring Firestorm Volcalize Phoenix | `120249016` | [Rush/Scripts/c120249016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249016.lua) | 1 |
| Prey Archfiend | `120304034` | [Rush/Scripts/c120304034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304034.lua) | 1 |
| Mega Jointech Fortrex \[L\] | `120249003` | [Rush/Scripts/c120249003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249003.lua) | 1 |
| Transam Lika | `120109024` | [Rush/Scripts/c120109024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109024.lua) | 1 |
| Dark Matter Freya | `120261027` | [Rush/Scripts/c120261027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261027.lua) | 1 |
| Dark Matter Requiem | `120264039` | [Rush/Scripts/c120264039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264039.lua) | 1 |
| Dimension Riletta | `120309024` | [Rush/Scripts/c120309024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309024.lua) | 1 |
| Einvy the Irreverent | `120285031` | [Rush/Scripts/c120285031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285031.lua) | 1 |
| Star Replete of the Star Sanctuary | `120305015` | [Rush/Scripts/c120305015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305015.lua) | 1 |
| Transam Assault Linac | `120272035` | [Rush/Scripts/c120272035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272035.lua) | 1 |
| Dual Space Yggdrago | `120260008` | [Rush/Scripts/c120260008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260008.lua) | 1 |
| Hungry Special Coupon | `120300055` | [Rush/Scripts/c120300055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300055.lua) | 1 |
| Roadstar Gladimagia | `120272042` | [Rush/Scripts/c120272042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272042.lua) | 1 |
| Alchemicalize Orb | `120272037` | [Rush/Scripts/c120272037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272037.lua) | 1 |
| Elemental HERO Plasma Vice | `120300066` | [Rush/Scripts/c120300066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300066.lua) | 1 |
| Soen the Molten Martial Machine | `120304036` | [Rush/Scripts/c120304036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304036.lua) | 1 |
| ...and 43 more |  |  |  |

## Script Examples

### Dark Matter Transcend Dragon (`120272044`)

Source: [Rush/Scripts/c120272044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272044.lua)

```lua
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.AttachExtraAttackMonster(e,c,2,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.AttachPierce(e,c,aux.Stringid(m,3),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.CanSelectAndSpecialSummon(aux.Stringid(m,4),aux.NecroValleyFilter(cm.spfilter),tp,0,LOCATION_GRAVE,1,3,nil,e,POS_FACEDOWN_DEFENSE,false,1-tp)
	end
```

### Transam Scride (`120109036`)

Source: [Rush/Scripts/c120109036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109036.lua)

```lua
		RD.CanSelectAndDoAction(aux.Stringid(m,1),aux.Stringid(m,2),cm.filter,tp,LOCATION_MZONE,0,1,3,nil,function(g)
			g:ForEach(function(tc)
				RD.AttachPierce(e,tc,aux.Stringid(m,3),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			end)
			local filter=RD.Filter(cm.posfilter,e,tp)
```

### Super Princess of the Flock - Max Mutton [L] (`120293007`)

Source: [Rush/Scripts/c120293007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293007.lua)

```lua
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		local reset=RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END
		RD.AttachPierce(e,c,aux.Stringid(m,1),reset)
		if RD.IsMaximumMode(c) then
			RD.AttachAtkDef(e,c,1000,0,reset)
```
