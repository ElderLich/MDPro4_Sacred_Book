# Auxiliary.IsPlayerCanNormalDraw

## Signature

```lua
Auxiliary.IsPlayerCanNormalDraw(int tp) -> bool
```

## Description

Checks whether tp can perform a normal draw: draw count is positive, the Deck is not empty, and FLAG_ID_NO_NORMAL_DRAW is not set.

## Parameters

- `tp` `int`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:1854`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **17** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.IsPlayerCanNormalDraw`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Rank-Up-Magic Astral Force | `45950291` | [Scripts/c45950291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45950291.lua) | 58 |
| Black Luster Soldier - Legendary Swordsman | `70551291` | [Scripts/c70551291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70551291.lua) | 47 |
| Legacy of the Duelist | `88851326` | [Scripts/c88851326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88851326.lua) | 44 |
| Tachyon Chaos Hole | `59650656` | [Scripts/c59650656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59650656.lua) | 42 |
| Fandora, the Flying Furtress | `64400161` | [Scripts/c64400161.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64400161.lua) | 40 |
| Dark General Freed | `70676581` | [Scripts/c70676581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70676581.lua) | 40 |
| Spirit Burner | `50418970` | [Scripts/c50418970.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50418970.lua) | 38 |
| Gearbreed | `27979109` | [Scripts/c27979109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27979109.lua) | 37 |
| Freed the Matchless General | `49681811` | [Scripts/c49681811.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49681811.lua) | 35 |
| Infernity Pawn | `82434071` | [Scripts/c82434071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82434071.lua) | 33 |
| Meteor Flare | `56856951` | [Scripts/c56856951.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56856951.lua) | 29 |
| Sylvan Waterslide | `49838105` | [Scripts/c49838105.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49838105.lua) | 27 |
| Magical Blast | `91819979` | [Scripts/c91819979.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91819979.lua) | 27 |
| Malefic World | `27564031` | [Scripts/c27564031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27564031.lua) | 27 |
| Iron Core of Koa'ki Meiru | `36623431` | [Scripts/c36623431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36623431.lua) | 26 |
| Flying Saucer Muusik'i | `97697678` | [Scripts/c97697678.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97697678.lua) | 24 |
| Flame Tiger | `66499018` | [Scripts/c66499018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66499018.lua) | 23 |

## Script Examples

### Rank-Up-Magic Astral Force (`45950291`)

Source: [Scripts/c45950291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45950291.lua)

```lua
end
function c45950291.thcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return aux.IsPlayerCanNormalDraw(tp) and Duel.GetActivityCount(tp,ACTIVITY_SPSUMMON)==0 end
	local c=e:GetHandler()
	local e1=Effect.CreateEffect(c)
```

### Black Luster Soldier - Legendary Swordsman (`70551291`)

Source: [Scripts/c70551291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70551291.lua)

```lua
end
function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return aux.IsPlayerCanNormalDraw(tp) and Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,1,nil) end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
end
```

### Legacy of the Duelist (`88851326`)

Source: [Scripts/c88851326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88851326.lua)

```lua
end
function c88851326.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return aux.IsPlayerCanNormalDraw(tp) and Duel.IsExistingMatchingCard(c88851326.thfilter,tp,LOCATION_GRAVE,0,1,nil) end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_GRAVE)
end
```
