# Card.IsReleasable

## Signature

```lua
Card.IsReleasable(Card c, [int reason]) -> bool
```

## Description

Checks whether c can be Released for a non-Summon reason by the current reason player.
reason defaults to REASON_COST. The core rejects cards being Summoned, Xyz Materials, cards in the GY or banished, Spell/Trap Cards in the hand, cards the player cannot release, and cards affected by EFFECT_UNRELEASABLE_NONSUM.

## Parameters

- `c` `Card`
- `reason` `int` optional - default: REASON_COST

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3650`

## Guided Examples

Learn how to use this function in context:

- [Tribute Summon Materials](/learn/tribute-summon-materials)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **123** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsReleasable) with `Card.IsReleasable`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer, the Starfrost Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua) | 2 |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30983281.lua) | 1 |
| [Ultimate Crystal Rainbow Dragon Overdrive](/examples/cards/84544192) | `84544192` | [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84544192.lua) | 1 |
| [Tellusion the Magna Warrior](/examples/cards/24431911) | `24431911` | [Scripts/c24431911.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24431911.lua) | 1 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62714453.lua) | 1 |
| Kuribeh | `34419588` | [Scripts/c34419588.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34419588.lua) | 1 |
| Divine Serpent Apophis | `97800311` | [Scripts/c97800311.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97800311.lua) | 1 |
| Arktos XII - Chronochasm Vaylantz | `50687050` | [Scripts/c50687050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50687050.lua) | 1 |
| All-Eyes Phantom Dragon | `70335319` | [Scripts/c70335319.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70335319.lua) | 1 |
| Metaltron XII, the True Dracombatant | `57761191` | [Scripts/c57761191.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57761191.lua) | 1 |
| Galaxy-Eyes Photon Change Dragon | `54725177` | [Scripts/c54725177.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54725177.lua) | 1 |
| Abyssrhine, the Atlantean Spirit | `17080584` | [Scripts/c17080584.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17080584.lua) | 1 |
| Red-Eyes Black Dragon Exceed | `17242022` | [Scripts/c17242022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17242022.lua) | 1 |
| Black-Winged Assault Dragon | `73218989` | [Scripts/c73218989.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73218989.lua) | 1 |
| Predaplant Daredevil | `82370493` | [Scripts/c82370493.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82370493.lua) | 2 |
| Egyptian God Slime | `42166000` | [Scripts/c42166000.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42166000.lua) | 1 |
| Dawn Angel Kambi | `12500059` | [Scripts/c12500059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12500059.lua) | 2 |
| Hrimnir the Divine Follower | `49904658` | [Scripts/c49904658.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49904658.lua) | 1 |
| Solfachord Solfegia | `84693918` | [Scripts/c84693918.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84693918.lua) | 3 |
| Supreme King Dragon Odd-Eyes | `96733134` | [Scripts/c96733134.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c96733134.lua) | 1 |
| Destiny HERO - Dreadnought Master | `54641720` | [Scripts/c54641720.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54641720.lua) | 1 |
| Bramble Rose Dragon | `6560411` | [Scripts/c6560411.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6560411.lua) | 1 |
| Sky Striker Ace = Zero | `76072561` | [Scripts/c76072561.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76072561.lua) | 1 |
| Crossrose Dragon | `72218246` | [Scripts/c72218246.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72218246.lua) | 1 |
| ...and 99 more |  |  |  |

## Script Examples

### Astrograph Sorcerer, the Starfrost Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
end
function s.fsptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsReleasable(REASON_EFFECT) end
	Duel.SetOperationInfo(0,CATEGORY_RELEASE,e:GetHandler(),1,0,0)
end
```

### Accel Synchro Stardust Dragon (`30983281`)

Source: [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30983281.lua)

```lua
	local g=Group.CreateGroup()
	if c:IsSetCard(0xa3) then g:Merge(Duel.GetMatchingGroup(c30983281.excostfilter,tp,LOCATION_GRAVE,0,nil,tp)) end
	local chkrel=c:IsReleasable()
	local chknotrel=g:GetCount()>0
	local b1=chkrel and Duel.IsExistingMatchingCard(c30983281.scfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp,c,chkrel,nil)
```

### Ultimate Crystal Rainbow Dragon Overdrive (`84544192`)

Source: [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84544192.lua)

```lua
function s.tdcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:GetBattledGroupCount()==0 and c:IsReleasable() end
	Duel.Release(c,REASON_COST)
end
```
