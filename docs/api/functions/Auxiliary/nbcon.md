# Auxiliary.nbcon

## Signature

```lua
Auxiliary.nbcon(int tp, Effect re) -> bool
```

## Description

Condition helper for effects that negate an activation and banish the activating card. It requires tp to be able to banish, and the activating card must either no longer be related to its effect or be able to be banished.

## Parameters

- `tp` `int`
- `re` `Effect`

## Returns

- `bool` - true if the activation can be negated and the card can be banished if needed.

## Source

- `Utilities/utility.lua:1467`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.nbcon) with `Auxiliary.nbcon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 1 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 1 |
| Virakam, the Divine Spirit of Artifice | `10673071` | [Scripts/c10673071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10673071.lua) | 1 |
| Linguriboh | `24842059` | [Scripts/c24842059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24842059.lua) | 1 |

## Script Examples

### Shooting Majestic Star Dragon (`40939228`)

Source: [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua)

```lua
function c40939228.negtg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:IsAbleToRemove() and aux.nbcon(tp,re) end
	Duel.SetOperationInfo(0,CATEGORY_NEGATE,eg,1,0,0)
	Duel.SetOperationInfo(0,CATEGORY_REMOVE,c,1,0,0)
```

### W:P Fancy Ball (`4993187`)

Source: [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua)

```lua
end
function s.distg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return aux.nbcon(tp,re) end
	Duel.SetOperationInfo(0,CATEGORY_DISABLE,eg,1,0,0)
	if re:GetHandler():IsRelateToEffect(re) then
```

### Virakam, the Divine Spirit of Artifice (`10673071`)

Source: [Scripts/c10673071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10673071.lua)

```lua
end
function s.discon(e,tp,eg,ep,ev,re,r,rp)
	if not Duel.IsChainDisablable(ev) or not aux.nbcon(tp,re) then return false end
	local te,p=Duel.GetChainInfo(ev-1,CHAININFO_TRIGGERING_EFFECT,CHAININFO_TRIGGERING_PLAYER)
	return te and te:IsActiveType(TYPE_FUSION) and p==tp and rp==1-tp
```
