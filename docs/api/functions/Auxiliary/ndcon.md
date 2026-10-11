# Auxiliary.ndcon

## Signature

```lua
Auxiliary.ndcon(int tp, Effect re) -> bool
```

## Description

Condition helper for effects that negate an activation and return the activating card to the Deck. It accepts Spell/Trap activations, unrelated cards, or related cards that can be returned to the Deck.

## Parameters

- `tp` `int`
- `re` `Effect`

## Returns

- `bool` - true if the activation can be negated and the card can be returned to the Deck if needed.

## Source

- `Utilities/utility.lua:1485`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.ndcon) with `Auxiliary.ndcon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Rebirth of Parshath | `42444868` | [Scripts/c42444868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42444868.lua) | 1 |
| Nine Pillars of Yang Zing | `57831349` | [Scripts/c57831349.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57831349.lua) | 1 |
| Stall Turn | `86060749` | [Scripts/c86060749.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86060749.lua) | 1 |
| Cash Back | `59957503` | [Scripts/c59957503.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59957503.lua) | 1 |

## Script Examples

### Rebirth of Parshath (`42444868`)

Source: [Scripts/c42444868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42444868.lua)

```lua
end
function c42444868.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return aux.ndcon(tp,re) end
	Duel.SetOperationInfo(0,CATEGORY_NEGATE,eg,1,0,0)
	if re:GetHandler():IsRelateToEffect(re) then
```

### Nine Pillars of Yang Zing (`57831349`)

Source: [Scripts/c57831349.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57831349.lua)

```lua
end
function c57831349.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return aux.ndcon(tp,re) end
	Duel.SetOperationInfo(0,CATEGORY_NEGATE,eg,1,0,0)
	if re:GetHandler():IsRelateToEffect(re) then
```

### Stall Turn (`86060749`)

Source: [Scripts/c86060749.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86060749.lua)

```lua
function c86060749.target(e,tp,eg,ep,ev,re,r,rp,chk)
	local rc=re:GetHandler()
	if chk==0 then return aux.ndcon(tp,re) end
	Duel.SetOperationInfo(0,CATEGORY_NEGATE,eg,1,0,0)
	if rc:IsRelateToEffect(re) then
```
