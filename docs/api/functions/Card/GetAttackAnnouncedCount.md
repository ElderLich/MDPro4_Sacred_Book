# Card.GetAttackAnnouncedCount

## Signature

```lua
Card.GetAttackAnnouncedCount(Card c) -> int
```

## Description

Returns c's attack declaration count.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3537`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **18** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetAttackAnnouncedCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Toon Black Luster Soldier | `28711704` | [Scripts/c28711704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28711704.lua) | 1 |
| Blaze Cannon | `4059313` | [Scripts/c4059313.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4059313.lua) | 1 |
| Infernoid Patrulea | `89423971` | [Scripts/c89423971.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89423971.lua) | 1 |
| Infernoid Harmadik | `52038272` | [Scripts/c52038272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52038272.lua) | 1 |
| Voloferniges, the Darkest Dragon Doomrider | `38694052` | [Scripts/c38694052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38694052.lua) | 1 |
| Dinowrestler King T Wrextle | `77967790` | [Scripts/c77967790.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77967790.lua) | 1 |
| Black Luster Soldier - Envoy of the Beginning | `72989439` | [Scripts/c72989439.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72989439.lua) | 1 |
| Dillingerous Dragon | `23732205` | [Scripts/c23732205.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23732205.lua) | 1 |
| GMX - ALLOS | `56311997` | [Scripts/c56311997.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56311997.lua) | 1 |
| Protector Whelp of the Destruction Swordsman | `47158777` | [Scripts/c47158777.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47158777.lua) | 1 |
| Blue-Eyes Alternative Ultimate Dragon | `43228023` | [Scripts/c43228023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43228023.lua) | 1 |
| Abyss Actor - Funky Comedian | `99634927` | [Scripts/c99634927.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99634927.lua) | 1 |
| Link Bumper | `67231737` | [Scripts/c67231737.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67231737.lua) | 1 |
| Arcana Force EX - The Dark Ruler | `69831560` | [Scripts/c69831560.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69831560.lua) | 1 |
| Combination Attack | `8964854` | [Scripts/c8964854.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8964854.lua) | 2 |
| Laval Judgment Lord | `14047624` | [Scripts/c14047624.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14047624.lua) | 1 |
| Savage Colosseum | `32391631` | [Scripts/c32391631.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32391631.lua) | 1 |
| Red Dragon Archfiend | `70902743` | [Scripts/c70902743.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70902743.lua) | 1 |

## Script Examples

### Toon Black Luster Soldier (`28711704`)

Source: [Scripts/c28711704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28711704.lua)

```lua
function c28711704.rmcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:GetAttackAnnouncedCount()==0 end
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_SINGLE)
```

### Blaze Cannon (`4059313`)

Source: [Scripts/c4059313.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4059313.lua)

```lua
end
function c4059313.atkfilter(c,tp)
	return c:GetAttackAnnouncedCount()==0 and c:GetTextAttack()>0 and (c:IsControler(tp) or c:IsFaceup())
end
function c4059313.atkcost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Infernoid Patrulea (`89423971`)

Source: [Scripts/c89423971.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89423971.lua)

```lua
function c89423971.descost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:GetAttackAnnouncedCount()==0 end
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_SINGLE)
```
