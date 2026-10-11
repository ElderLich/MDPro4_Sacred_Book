# RushDuel.IsMaximumMode

Alias: `RD.IsMaximumMode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsMaximumMode(Card card) -> bool
```

## Description

Checks that the card is in a Monster Zone, has the Maximum Summon type and still has overlay components. This Card predicate differs from RD.MaximumMode, an Effect condition that checks the Maximum marker.

## Parameters

- `card` `Card`: Card to inspect.

## Returns

- `bool`: Whether the helper's Maximum-mode test passes.

## Source

`Rush/Utilities/RDCondition.lua:13`

```lua
function RushDuel.IsMaximumMode(card)
    return card:IsLocation(LOCATION_MZONE) and card:IsSummonType(SUMMON_TYPE_MAXIMUM) and card:GetOverlayCount() > 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **40** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsMaximumMode) with `RushDuel.IsMaximumMode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Volcalizing Salamandeus](/examples/rush-cards/120272039) | `120272039` | [Rush/Scripts/c120272039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272039.lua) | 1 |
| [Abyssal Dragon Lord Abyss Poseidra \[L\]](/examples/rush-cards/120239013) | `120239013` | [Rush/Scripts/c120239013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239013.lua) | 2 |
| [Mega Jointech Fortrex \[R\]](/examples/rush-cards/120249005) | `120249005` | [Rush/Scripts/c120249005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249005.lua) | 2 |
| Super Princess of the Flock - Max Mutton \[L\] | `120293007` | [Rush/Scripts/c120293007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293007.lua) | 2 |
| Supreme Railartillery Magnum Overlord \[L\] | `120239001` | [Rush/Scripts/c120239001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239001.lua) | 2 |
| Abyssal Sea Dragon Abyss Kraken \[L\] | `120239016` | [Rush/Scripts/c120239016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239016.lua) | 2 |
| Super Galaxy King Lord of Galactica \[L\] | `120254037` | [Rush/Scripts/c120254037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254037.lua) | 1 |
| Roaring Firestorm Volcalize Phoenix \[L\] | `120249015` | [Rush/Scripts/c120249015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249015.lua) | 2 |
| Abyssal Sea Dragon Abyss Kraken \[R\] | `120239018` | [Rush/Scripts/c120239018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239018.lua) | 2 |
| Mega Jointech Fortrex \[L\] | `120249003` | [Rush/Scripts/c120249003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249003.lua) | 1 |
| Reshef the Dark Being | `120306069` | [Rush/Scripts/c120306069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306069.lua) | 1 |
| Roaring Firestorm Volcalize Phoenix \[R\] | `120249017` | [Rush/Scripts/c120249017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249017.lua) | 2 |
| Harpie Lady Sisters | `120247002` | [Rush/Scripts/c120247002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247002.lua) | 2 |
| Super Princess of the Flock - Max Mutton \[R\] | `120293009` | [Rush/Scripts/c120293009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293009.lua) | 2 |
| Shinesteel Ultra Dragon Devastar Okeabyss \[L\] | `120239019` | [Rush/Scripts/c120239019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239019.lua) | 2 |
| Supreme Railartillery Magnum Overlord \[R\] | `120239003` | [Rush/Scripts/c120239003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239003.lua) | 2 |
| Super Princess of the Flock - Max Mutton | `120293008` | [Rush/Scripts/c120293008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293008.lua) | 1 |
| Reporter Wars Scoopies \[R\] | `120304009` | [Rush/Scripts/c120304009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304009.lua) | 1 |
| Doomblaze Fiend Overlord Despairacion | `120231008` | [Rush/Scripts/c120231008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231008.lua) | 2 |
| Mobile Deployment Gear Start | `120272052` | [Rush/Scripts/c120272052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272052.lua) | 1 |
| Volcalize Compound | `120249048` | [Rush/Scripts/c120249048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249048.lua) | 1 |
| Red-Eyes Maxi-Flare Dragon | `120274002` | [Rush/Scripts/c120274002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274002.lua) | 1 |
| Freshberry Swimming | `120264063` | [Rush/Scripts/c120264063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264063.lua) | 1 |
| Dynamail Dino Dynamix \[R\] | `120274033` | [Rush/Scripts/c120274033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274033.lua) | 1 |
| ...and 16 more |  |  |  |

## Script Examples

### Volcalizing Salamandeus (`120272039`)

Source: [Rush/Scripts/c120272039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272039.lua)

```lua
function cm.check(e,c)
	local g=c:GetMaterial()
	if g:IsExists(RD.IsMaximumMode,1,nil) then
		e:GetLabelObject():SetLabel(1)
	else
```

### Abyssal Dragon Lord Abyss Poseidra [L] (`120239013`)

Source: [Rush/Scripts/c120239013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239013.lua)

```lua
	local g=Duel.GetMatchingGroup(nil,tp,0,LOCATION_MZONE,nil)
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,1,0,0)
	if RD.IsMaximumMode(e:GetHandler()) then
		Duel.Hint(HINT_OPSELECTED,1-tp,e:GetDescription())
	end
```

### Mega Jointech Fortrex [R] (`120249005`)

Source: [Rush/Scripts/c120249005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249005.lua)

```lua
		and Duel.IsExistingMatchingCard(cm.tdfilter,tp,LOCATION_GRAVE,0,3,nil) end
	Duel.SetOperationInfo(0,CATEGORY_TODECK,nil,6,PLAYER_ALL,LOCATION_GRAVE)
	if RD.IsMaximumMode(e:GetHandler()) then
		Duel.Hint(HINT_OPSELECTED,1-tp,e:GetDescription())
	end
```
