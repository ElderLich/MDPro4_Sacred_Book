# Auxiliary.SameValueCheck

## Signature

```lua
Auxiliary.SameValueCheck(Group g, function f) -> bool
```

## Description

Checks whether every card in g shares at least one bit returned by f; groups of 0 or 1 card return true.

## Parameters

- `g` `Group`
- `f` `function`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:1838`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **19** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.SameValueCheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lady's Dragonmaid](/examples/cards/48658295) | `48658295` | [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48658295.lua) | 1 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua) | 2 |
| Cyberse Contract Witch | `37458564` | [Scripts/c37458564.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37458564.lua) | 1 |
| Keel, Shipwright Fur Hire | `66736884` | [Scripts/c66736884.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66736884.lua) | 1 |
| Stellarnova Binding | `69678646` | [Scripts/c69678646.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69678646.lua) | 1 |
| ASHLAN U1000 | `44376395` | [Scripts/c44376395.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44376395.lua) | 2 |
| Akashic Magician | `28776350` | [Scripts/c28776350.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28776350.lua) | 1 |
| Shipping Archfiend | `57256127` | [Scripts/c57256127.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57256127.lua) | 2 |
| Charmer Quartet in Bloom | `27519978` | [Scripts/c27519978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27519978.lua) | 4 |
| Curious, the Lightsworn Dominion | `98095162` | [Scripts/c98095162.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98095162.lua) | 1 |
| Virtual World Phoenix - Fanfan | `27069566` | [Scripts/c27069566.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27069566.lua) | 2 |
| Karma of the Destruction Swordsman | `78348934` | [Scripts/c78348934.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78348934.lua) | 1 |
| Summon Sorceress | `61665245` | [Scripts/c61665245.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61665245.lua) | 1 |
| Herald of Mirage Lights | `46935289` | [Scripts/c46935289.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46935289.lua) | 2 |
| Judgment, the Dragon of Heaven | `41659072` | [Scripts/c41659072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41659072.lua) | 1 |
| Ra'ten, the Heavenly General | `30163008` | [Scripts/c30163008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30163008.lua) | 1 |
| Darkness Metal, the Dragon of Dark Steel | `79266769` | [Scripts/c79266769.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79266769.lua) | 2 |
| Virtual World Dragon - Longlong | `61641818` | [Scripts/c61641818.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61641818.lua) | 2 |
| Resonance Device | `26864586` | [Scripts/c26864586.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26864586.lua) | 2 |

## Script Examples

### Lady's Dragonmaid (`48658295`)

Source: [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48658295.lua)

```lua
end
function s.fselect(g)
	return g:GetClassCount(Card.GetLevel)==2 and aux.SameValueCheck(g,Card.GetFusionAttribute) and g:IsExists(Card.IsLocation,1,nil,LOCATION_ONFIELD) and g:IsExists(Card.IsLocation,1,nil,LOCATION_GRAVE)
end
function s.spcon(e,c)
```

### D/D Count Surveyor (`5997110`)

Source: [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua)

```lua
end
function s.gcheck(g)
	return (Auxiliary.SameValueCheck(g,Card.GetRace) or Auxiliary.SameValueCheck(g,Card.GetAttribute))
		and g:IsExists(s.atkfilter,1,nil,g)
end
```

### Cyberse Contract Witch (`37458564`)

Source: [Scripts/c37458564.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37458564.lua)

```lua
end
function s.lcheck(g)
	return aux.SameValueCheck(g,Card.GetLinkRace)
end
function s.thcon(e,tp,eg,ep,ev,re,r,rp)
```
