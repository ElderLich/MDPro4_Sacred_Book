# Card.IsDefenseAbove

## Signature

```lua
Card.IsDefenseAbove(Card c, int def) -> bool
```

## Description

Checks whether c has current DEF greater than or equal to def.
Link Monsters and cards that are not monsters or currently treated as monsters return false.

## Parameters

- `c` `Card`
- `def` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3624`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **52** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsDefenseAbove`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Dark End Evaporation Dragon](/examples/cards/62002838) | `62002838` | [Scripts/c62002838.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62002838.lua) | 63 |
| [Light End Sublimation Dragon](/examples/cards/35614780) | `35614780` | [Scripts/c35614780.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35614780.lua) | 61 |
| Amaze Attraction Wonder Wheel | `93473606` | [Scripts/c93473606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93473606.lua) | 55 |
| Battlewasp - Hama the Conquering Bow | `80949182` | [Scripts/c80949182.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80949182.lua) | 46 |
| Subterror Final Battle | `74640994` | [Scripts/c74640994.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74640994.lua) | 46 |
| Ancient Gear Ballista | `10547580` | [Scripts/c10547580.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10547580.lua) | 46 |
| Number 3: Cicada King | `4997565` | [Scripts/c4997565.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4997565.lua) | 44 |
| Galaxy Brave | `55168550` | [Scripts/c55168550.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55168550.lua) | 44 |
| Psychic Commander | `21454943` | [Scripts/c21454943.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21454943.lua) | 44 |
| Sacred Scrolls of the Gizmek Legend | `24793135` | [Scripts/c24793135.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24793135.lua) | 43 |
| Mementotlan Cranium Burst | `79600447` | [Scripts/c79600447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79600447.lua) | 43 |
| Alice, Lady of Lament | `14504454` | [Scripts/c14504454.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14504454.lua) | 42 |
| Rise to Full Height | `19254117` | [Scripts/c19254117.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19254117.lua) | 42 |
| Icejade Creation Kingfisher | `66749546` | [Scripts/c66749546.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66749546.lua) | 41 |
| Leo Wizard the Dark Fiend | `55423549` | [Scripts/c55423549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55423549.lua) | 41 |
| Ultimate Great Insect | `87804747` | [Scripts/c87804747.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87804747.lua) | 41 |
| Pig Iron vs. Pen Peg | `46497537` | [Scripts/c46497537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46497537.lua) | 40 |
| Full Force Virus | `4931121` | [Scripts/c4931121.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4931121.lua) | 40 |
| Ahrima, the Wicked Warden | `86377375` | [Scripts/c86377375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86377375.lua) | 39 |
| Bark of Dark Ruler | `41925941` | [Scripts/c41925941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41925941.lua) | 39 |
| Raidraptor - Pain Lanius | `46589034` | [Scripts/c46589034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46589034.lua) | 37 |
| Performage Mirror Conductor | `71578874` | [Scripts/c71578874.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71578874.lua) | 34 |
| Performapal Turn Toad | `4239451` | [Scripts/c4239451.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4239451.lua) | 33 |
| Embrace of the Tistina | `59069885` | [Scripts/c59069885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59069885.lua) | 33 |
| ...and 28 more |  |  |  |

## Script Examples

### Dark End Evaporation Dragon (`62002838`)

Source: [Scripts/c62002838.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62002838.lua)

```lua
	local c=e:GetHandler()
	if chkc then return chkc:IsLocation(LOCATION_MZONE) and chkc~=c and s.atkfilter(chkc) end
	if chk==0 then return c:IsAttackAbove(500) and c:IsDefenseAbove(500) and Duel.IsExistingTarget(s.atkfilter,tp,LOCATION_MZONE,LOCATION_MZONE,1,c) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
	local tc=Duel.SelectTarget(tp,s.atkfilter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,c)
```

### Light End Sublimation Dragon (`35614780`)

Source: [Scripts/c35614780.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35614780.lua)

```lua
function s.atktg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:IsAttackAbove(500) and c:IsDefenseAbove(500) end
end
function s.atkop(e,tp,eg,ep,ev,re,r,rp)
```

### Amaze Attraction Wonder Wheel (`93473606`)

Source: [Scripts/c93473606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93473606.lua)

```lua
function c93473606.swtg(e,tp,eg,ep,ev,re,r,rp,chk)
	local ec=e:GetHandler():GetEquipTarget()
	if chk==0 then return ec and ec:IsDefenseAbove(0) end
end
function c93473606.swop(e,tp,eg,ep,ev,re,r,rp)
```
