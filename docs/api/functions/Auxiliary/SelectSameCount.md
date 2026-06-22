# Auxiliary.SelectSameCount

## Signature

```lua
Auxiliary.SelectSameCount(int tp, Group g1, Group g2, [int min], [int max], [Card|Group|nil except]) -> Group|nil
```

## Description

Lets tp build a selection that contains the same number of cards from g1 and g2.
except is removed from both groups before selection. The result can be nil if min is greater than the computed max.

## Parameters

- `tp` `int`
- `g1` `Group`
- `g2` `Group`
- `min` `int` optional - default: 1
- `max` `int` optional - default: min(#g1, #g2, 127)
- `except` `Card|Group|nil` optional

## Returns

- `Group|nil`

## Source

- `Utilities/utility.lua:1421`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.SelectSameCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Excited Melffys | `79561872` | [Scripts/c79561872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79561872.lua) | 51 |
| Dark Rebellion Xyz Dragon of the Four Heavenly Dragons | `90091224` | [Scripts/c90091224.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90091224.lua) | 50 |
| Mementomictlan Tecuhtlica - Creation King | `14529511` | [Scripts/c14529511.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14529511.lua) | 44 |
| Sky Striker Special Maneuver - Lemnisgate! | `34433770` | [Scripts/c34433770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34433770.lua) | 43 |
| Fire King Sky Burn | `91703676` | [Scripts/c91703676.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91703676.lua) | 32 |

## Script Examples

### Excited Melffys (`79561872`)

Source: [Scripts/c79561872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79561872.lua)

```lua
	if chk==0 then return #g1>0 and #g2>0 end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RTOHAND)
	local sg=aux.SelectSameCount(tp,g1,g2)
	Duel.SetTargetCard(sg)
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,sg,sg:GetCount(),0,0)
```

### Dark Rebellion Xyz Dragon of the Four Heavenly Dragons (`90091224`)

Source: [Scripts/c90091224.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90091224.lua)

```lua
	local g2=g:Filter(Card.IsControler,nil,1-tp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
	local sg=aux.SelectSameCount(tp,g1,g2)
	Duel.SetTargetCard(sg)
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,sg,sg:GetCount(),0,0)
```

### Mementomictlan Tecuhtlica - Creation King (`14529511`)

Source: [Scripts/c14529511.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14529511.lua)

```lua
		and #g1>0 and #g2>0 end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
	local sg=aux.SelectSameCount(tp,g1,g2)
	Duel.SetTargetCard(sg)
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,sg,sg:GetCount(),0,0)
```
