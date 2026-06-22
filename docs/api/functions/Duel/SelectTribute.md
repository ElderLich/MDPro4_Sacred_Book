# Duel.SelectTribute

## Signature

```lua
Duel.SelectTribute(int player, Card c, int min, int max, [Group|nil mg], [int toplayer]) -> Group
```

## Description

Lets player select min to max Tribute candidates for Normal Summoning or Setting c and returns the selected Group.
mg can restrict the candidate pool. toplayer defaults to player; when toplayer differs, the core builds the extra release list for Tributing to that player's field.

## Parameters

- `player` `int`
- `c` `Card`
- `min` `int`
- `max` `int`
- `mg` `Group|nil` optional
- `toplayer` `int` optional - default: player

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4983`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **71** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.SelectTribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua) | 65 |
| Koa'ki Meiru Rooklord | `10060427` | [Scripts/c10060427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10060427.lua) | 57 |
| Erebus the Underworld Monarch | `23064604` | [Scripts/c23064604.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23064604.lua) | 56 |
| Metaltron XII, the True Dracombatant | `57761191` | [Scripts/c57761191.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57761191.lua) | 54 |
| Clown Crew Biancaviso | `82159583` | [Scripts/c82159583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82159583.lua) | 52 |
| Egyptian God Slime | `42166000` | [Scripts/c42166000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42166000.lua) | 52 |
| Doodle Beast - Tyranno | `67725394` | [Scripts/c67725394.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67725394.lua) | 51 |
| The Winged Dragon of Ra - Sphere Mode | `10000080` | [Scripts/c10000080.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10000080.lua) | 51 |
| Primite Imperial Dragon | `81418467` | [Scripts/c81418467.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81418467.lua) | 50 |
| Dark Alligator | `34479658` | [Scripts/c34479658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34479658.lua) | 50 |
| Zaborg the Mega Monarch | `87602890` | [Scripts/c87602890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87602890.lua) | 50 |
| Bahalutiya, the Grand Radiance | `53318263` | [Scripts/c53318263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53318263.lua) | 49 |
| Caius the Mega Monarch | `87288189` | [Scripts/c87288189.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87288189.lua) | 48 |
| Raiza the Mega Monarch | `69327790` | [Scripts/c69327790.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69327790.lua) | 48 |
| Master Peace, the True Dracoverlord | `12800564` | [Scripts/c12800564.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12800564.lua) | 45 |
| Gravekeeper's Oracle | `25524823` | [Scripts/c25524823.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25524823.lua) | 45 |
| Slifer the Sky Dragon | `10000020` | [Scripts/c10000020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10000020.lua) | 43 |
| Twilight Ninja Getsuga, the Shogun | `76930964` | [Scripts/c76930964.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76930964.lua) | 43 |
| Behemoth the King of a Hundred Battles | `13836592` | [Scripts/c13836592.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13836592.lua) | 42 |
| Cosmic Horror Gangi'el | `51192573` | [Scripts/c51192573.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51192573.lua) | 42 |
| Leo Wizard the Dark Fiend | `55423549` | [Scripts/c55423549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55423549.lua) | 41 |
| Thestalos the Mega Monarch | `69230391` | [Scripts/c69230391.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69230391.lua) | 41 |
| The Tyrant Neptune | `88071625` | [Scripts/c88071625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88071625.lua) | 41 |
| Mobius the Mega Monarch | `23689697` | [Scripts/c23689697.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23689697.lua) | 41 |
| ...and 47 more |  |  |  |

## Script Examples

### Ehther the Heavenly Monarch (`96570609`)

Source: [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua)

```lua
function c96570609.otop(e,tp,eg,ep,ev,re,r,rp,c)
	local mg=Duel.GetMatchingGroup(c96570609.otfilter,0,LOCATION_MZONE,LOCATION_MZONE,nil)
	local sg=Duel.SelectTribute(tp,c,1,1,mg)
	c:SetMaterial(sg)
	Duel.Release(sg,REASON_SUMMON+REASON_MATERIAL)
```

### Koa'ki Meiru Rooklord (`10060427`)

Source: [Scripts/c10060427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10060427.lua)

```lua
function c10060427.otop(e,tp,eg,ep,ev,re,r,rp,c)
	local mg=Duel.GetMatchingGroup(c10060427.otfilter,tp,LOCATION_MZONE,LOCATION_MZONE,nil,tp)
	local sg=Duel.SelectTribute(tp,c,1,1,mg)
	c:SetMaterial(sg)
	Duel.Release(sg,REASON_SUMMON+REASON_MATERIAL)
```

### Erebus the Underworld Monarch (`23064604`)

Source: [Scripts/c23064604.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23064604.lua)

```lua
function c23064604.otop(e,tp,eg,ep,ev,re,r,rp,c)
	local mg=Duel.GetMatchingGroup(c23064604.otfilter,0,LOCATION_MZONE,LOCATION_MZONE,nil)
	local sg=Duel.SelectTribute(tp,c,1,1,mg)
	c:SetMaterial(sg)
	Duel.Release(sg,REASON_SUMMON+REASON_MATERIAL)
```
