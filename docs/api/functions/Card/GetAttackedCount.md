# Card.GetAttackedCount

## Signature

```lua
Card.GetAttackedCount(Card c) -> int
```

## Description

Returns c's attack count for the current turn.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3586`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetAttackedCount) with `Card.GetAttackedCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| ZW - Leo Arms | `60992364` | [Scripts/c60992364.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60992364.lua) | 1 |
| Crystal Beast Emerald Tortoise | `68215963` | [Scripts/c68215963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68215963.lua) | 1 |
| Ancient Forest | `87624166` | [Scripts/c87624166.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87624166.lua) | 1 |
| Ape Fighter | `41098335` | [Scripts/c41098335.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41098335.lua) | 1 |

## Script Examples

### ZW - Leo Arms (`60992364`)

Source: [Scripts/c60992364.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60992364.lua)

```lua
function c60992364.attg(e,tp,eg,ep,ev,re,r,rp,chk)
	local eqc=e:GetHandler():GetEquipTarget()
	if chk==0 then return eqc and eqc:GetAttackedCount()==1 and eqc:GetEffectCount(EFFECT_EXTRA_ATTACK)==0 end
	Duel.SetTargetCard(e:GetLabelObject())
end
```

### Crystal Beast Emerald Tortoise (`68215963`)

Source: [Scripts/c68215963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68215963.lua)

```lua
end
function c68215963.filter(c)
	return c:IsAttackPos() and c:GetAttackedCount()>0 and c:IsCanChangePosition()
end
function c68215963.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Ancient Forest (`87624166`)

Source: [Scripts/c87624166.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87624166.lua)

```lua
end
function c87624166.desfilter(c)
	return c:GetAttackedCount()>0
end
function c87624166.destg(e,tp,eg,ep,ev,re,r,rp,chk)
```
