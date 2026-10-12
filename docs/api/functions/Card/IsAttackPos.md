# Card.IsAttackPos

## Signature

```lua
Card.IsAttackPos(Card c) -> bool
```

## Description

Checks whether c's current position contains POS_ATTACK.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3657`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **154** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsAttackPos) with `Card.IsAttackPos`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Hushed Psychic Cleric | `25343017` | [Scripts/c25343017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25343017.lua) | 2 |
| Buerillabaisse de Nouvelles | `26223582` | [Scripts/c26223582.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26223582.lua) | 1 |
| Floowandereeze &amp; Empen | `80611581` | [Scripts/c80611581.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80611581.lua) | 1 |
| Angry Burger | `28306253` | [Scripts/c28306253.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28306253.lua) | 1 |
| Goblin Freefall Squad | `85123771` | [Scripts/c85123771.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85123771.lua) | 2 |
| Lancea, Ancestral Dragon of the Ice Mountain | `96402918` | [Scripts/c96402918.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c96402918.lua) | 1 |
| Baelgrill de Nouvelles | `88890658` | [Scripts/c88890658.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88890658.lua) | 1 |
| Vylon Disigma | `39987164` | [Scripts/c39987164.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39987164.lua) | 2 |
| Dinowrestler King T Wrextle | `77967790` | [Scripts/c77967790.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77967790.lua) | 3 |
| Dillingerous Dragon | `23732205` | [Scripts/c23732205.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23732205.lua) | 1 |
| The Phantom Knights of Umbrage Veil | `85257384` | [Scripts/c85257384.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85257384.lua) | 1 |
| Shell Knight | `10163855` | [Scripts/c10163855.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10163855.lua) | 1 |
| Balameuniere de Nouvelles | `52495649` | [Scripts/c52495649.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52495649.lua) | 1 |
| Metamorphortress | `43959432` | [Scripts/c43959432.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43959432.lua) | 1 |
| Crossroad Sonic Chick | `80054655` | [Scripts/c80054655.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80054655.lua) | 1 |
| Protecting Spirit Loagaeth | `84339249` | [Scripts/c84339249.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84339249.lua) | 1 |
| Foie Glasya de Nouvelles | `15001940` | [Scripts/c15001940.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15001940.lua) | 1 |
| Ace★Spades Speculation | `10796448` | [Scripts/c10796448.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10796448.lua) | 2 |
| Confiras de Nouvelles | `53618197` | [Scripts/c53618197.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53618197.lua) | 1 |
| Morphtronic Converter | `90659259` | [Scripts/c90659259.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90659259.lua) | 3 |
| Phantasm Spiral Crash | `48308134` | [Scripts/c48308134.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48308134.lua) | 1 |
| Layer 19 "Sudden Incursion! Super Quantum Black!!" | `98349765` | [Scripts/c98349765.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98349765.lua) | 2 |
| Puppet Rook | `77590412` | [Scripts/c77590412.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77590412.lua) | 2 |
| Dual Avatar Fists - Armored Ah-Gyo | `60237530` | [Scripts/c60237530.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60237530.lua) | 3 |
| ...and 130 more |  |  |  |

## Script Examples

### Hushed Psychic Cleric (`25343017`)

Source: [Scripts/c25343017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25343017.lua)

```lua
end
function c25343017.potg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsAttackPos() end
	Duel.SetOperationInfo(0,CATEGORY_POSITION,e:GetHandler(),1,0,0)
end
```

### Buerillabaisse de Nouvelles (`26223582`)

Source: [Scripts/c26223582.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26223582.lua)

```lua
end
function s.relfilter(c,tp,ec)
	return c:IsReleasableByEffect() and c:IsAttackPos()
		and Duel.GetMZoneCount(tp,Group.FromCards(c,ec))>0
end
```

### Floowandereeze & Empen (`80611581`)

Source: [Scripts/c80611581.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80611581.lua)

```lua
	local rc=re:GetHandler()
	return rc:IsLocation(LOCATION_MZONE) and re:IsActiveType(TYPE_MONSTER)
		and rc:IsAttackPos() and rc:IsSummonType(SUMMON_TYPE_SPECIAL)
end
function c80611581.atkcon(e,tp,eg,ep,ev,re,r,rp)
```
