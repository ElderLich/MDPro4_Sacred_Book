# RushDuel.AttachAtkDef

Alias: `RD.AttachAtkDef`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachAtkDef(any e, any card, any atk, any def, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 攻守升降
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `atk` `any`: Type and behavior are not yet reviewed; see the source.
- `def` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:5`

```lua
function RushDuel.AttachAtkDef(e, card, atk, def, reset, forced)
    if atk ~= nil and atk ~= 0 then
        RushDuel.CreateSingleEffect(e, nil, card, EFFECT_UPDATE_ATTACK, atk, reset, forced)
    end
    if def ~= nil and def ~= 0 and RushDuel.IsCanChangeDef(card) then
        RushDuel.CreateSingleEffect(e, nil, card, EFFECT_UPDATE_DEFENSE, def, reset, forced)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **561** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachAtkDef) with `RushDuel.AttachAtkDef`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Moonforce Ziggy](/examples/rush-cards/120300014) | `120300014` | [Rush/Scripts/c120300014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300014.lua) | 1 |
| [Volcalizing Salamandeus](/examples/rush-cards/120272039) | `120272039` | [Rush/Scripts/c120272039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272039.lua) | 1 |
| [Brassdes of the Wicked Wheels](/examples/rush-cards/120304033) | `120304033` | [Rush/Scripts/c120304033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304033.lua) | 1 |
| [Super Galaxy King Lord of Galactica \[R\]](/examples/rush-cards/120254039) | `120254039` | [Rush/Scripts/c120254039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254039.lua) | 1 |
| [Wako Gozen Riletta](/examples/rush-cards/120309021) | `120309021` | [Rush/Scripts/c120309021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309021.lua) | 1 |
| [Mega Jointech Fortrex \[R\]](/examples/rush-cards/120249005) | `120249005` | [Rush/Scripts/c120249005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249005.lua) | 1 |
| [Insect Taurus](/examples/rush-cards/120300060) | `120300060` | [Rush/Scripts/c120300060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300060.lua) | 1 |
| [Galactica Lost Oblivion](/examples/rush-cards/120277042) | `120277042` | [Rush/Scripts/c120277042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277042.lua) | 1 |
| [Bluetech Burst Rex](/examples/rush-cards/120261044) | `120261044` | [Rush/Scripts/c120261044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261044.lua) | 2 |
| [Red-Reboot Enhanced Boost Dragon](/examples/rush-cards/120253037) | `120253037` | [Rush/Scripts/c120253037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253037.lua) | 1 |
| [Lovely Rabbit](/examples/rush-cards/120300018) | `120300018` | [Rush/Scripts/c120300018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300018.lua) | 1 |
| [Star Cat Destronya](/examples/rush-cards/120235037) | `120235037` | [Rush/Scripts/c120235037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235037.lua) | 1 |
| [Supreme Machine Magnum Overlord \[L\]](/examples/rush-cards/120150001) | `120150001` | [Rush/Scripts/c120150001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150001.lua) | 1 |
| Royal Rebel's Heavy Metal | `120130031` | [Rush/Scripts/c120130031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120130031.lua) | 1 |
| Prophecy Phrase the Colors of the Wind | `120228024` | [Rush/Scripts/c120228024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228024.lua) | 1 |
| Galactica Supreme Oblivion | `120245003` | [Rush/Scripts/c120245003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120245003.lua) | 1 |
| Yamiterasu the Divine Ruler | `120199036` | [Rush/Scripts/c120199036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199036.lua) | 1 |
| Rising HERO Argent F | `120304043` | [Rush/Scripts/c120304043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304043.lua) | 1 |
| Excutie Riding! | `120249064` | [Rush/Scripts/c120249064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249064.lua) | 1 |
| Super Princess of the Flock - Max Mutton \[L\] | `120293007` | [Rush/Scripts/c120293007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293007.lua) | 1 |
| Dicemite Gyame Double-Up Chirori | `120272040` | [Rush/Scripts/c120272040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272040.lua) | 1 |
| Celeb Rose Influencers | `120257044` | [Rush/Scripts/c120257044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257044.lua) | 1 |
| Abyssal Sea Dragon Abyss Kraken \[L\] | `120239016` | [Rush/Scripts/c120239016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239016.lua) | 1 |
| Destructor Emperor Bakhakaiser | `120264045` | [Rush/Scripts/c120264045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264045.lua) | 1 |
| ...and 537 more |  |  |  |

## Script Examples

### Moonforce Ziggy (`120300014`)

Source: [Rush/Scripts/c120300014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300014.lua)

```lua
				if RD.SendToDeckBottom(g,e,tp,REASON_EFFECT)~=0
					and c:IsFaceup() and c:IsRelateToEffect(e) then
					RD.AttachAtkDef(e,c,0,500,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END+RESET_OPPO_TURN)
				end
			end)
```

### Volcalizing Salamandeus (`120272039`)

Source: [Rush/Scripts/c120272039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272039.lua)

```lua
	if g:GetCount()==0 then return end
	g:ForEach(function(tc)
		RD.AttachAtkDef(e,tc,-3000,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end)
	local c=e:GetHandler()
```

### Brassdes of the Wicked Wheels (`120304033`)

Source: [Rush/Scripts/c120304033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304033.lua)

```lua
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.AttachAtkDef(e,c,2000,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END+RESET_OPPO_TURN)
		RD.CanSelectAndDoAction(aux.Stringid(m,1),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),tp,LOCATION_GRAVE,0,1,1,nil,function(g)
			Duel.BreakEffect()
```
