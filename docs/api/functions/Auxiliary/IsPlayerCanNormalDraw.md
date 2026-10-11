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

- `Utilities/utility.lua:1859`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **17** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.IsPlayerCanNormalDraw) with `Auxiliary.IsPlayerCanNormalDraw`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Rank-Up-Magic Astral Force | `45950291` | [Scripts/c45950291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45950291.lua) | 1 |
| Black Luster Soldier - Legendary Swordsman | `70551291` | [Scripts/c70551291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70551291.lua) | 2 |
| Legacy of the Duelist | `88851326` | [Scripts/c88851326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88851326.lua) | 2 |
| Tachyon Chaos Hole | `59650656` | [Scripts/c59650656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59650656.lua) | 1 |
| Fandora, the Flying Furtress | `64400161` | [Scripts/c64400161.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64400161.lua) | 2 |
| Dark General Freed | `70676581` | [Scripts/c70676581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70676581.lua) | 2 |
| Spirit Burner | `50418970` | [Scripts/c50418970.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50418970.lua) | 2 |
| Gearbreed | `27979109` | [Scripts/c27979109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27979109.lua) | 1 |
| Freed the Matchless General | `49681811` | [Scripts/c49681811.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49681811.lua) | 2 |
| Infernity Pawn | `82434071` | [Scripts/c82434071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82434071.lua) | 1 |
| Meteor Flare | `56856951` | [Scripts/c56856951.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56856951.lua) | 2 |
| Sylvan Waterslide | `49838105` | [Scripts/c49838105.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49838105.lua) | 1 |
| Magical Blast | `91819979` | [Scripts/c91819979.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91819979.lua) | 2 |
| Malefic World | `27564031` | [Scripts/c27564031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27564031.lua) | 1 |
| Iron Core of Koa'ki Meiru | `36623431` | [Scripts/c36623431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36623431.lua) | 2 |
| Flying Saucer Muusik'i | `97697678` | [Scripts/c97697678.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97697678.lua) | 2 |
| Flame Tiger | `66499018` | [Scripts/c66499018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66499018.lua) | 1 |

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
