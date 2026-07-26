# Duel.CheckTribute

## Signature

```lua
Duel.CheckTribute(Card c, int min, [int max], [Group|nil mg], [int toplayer], [int zone]) -> bool
```

## Description

Checks whether there is a valid Tribute set for Normal Summoning or Setting c.
max defaults to min, mg can restrict the candidate pool, toplayer defaults to c's current controller, and zone defaults to the current extra-summon zone limit when present or 0x1f otherwise.

## Parameters

- `c` `Card`
- `min` `int`
- `max` `int` optional - default: min
- `mg` `Group|nil` optional
- `toplayer` `int` optional - default: c's controller
- `zone` `int` optional - default: current extra-summon zone limit or 0x1f

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4982`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **74** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.CheckTribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua) | 1 |
| Union Activation | `38527680` | [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua) | 1 |
| Koa'ki Meiru Rooklord | `10060427` | [Scripts/c10060427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10060427.lua) | 1 |
| Erebus the Underworld Monarch | `23064604` | [Scripts/c23064604.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23064604.lua) | 1 |
| Metaltron XII, the True Dracombatant | `57761191` | [Scripts/c57761191.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57761191.lua) | 6 |
| Clown Crew Biancaviso | `82159583` | [Scripts/c82159583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82159583.lua) | 1 |
| Egyptian God Slime | `42166000` | [Scripts/c42166000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42166000.lua) | 1 |
| Doodle Beast - Tyranno | `67725394` | [Scripts/c67725394.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67725394.lua) | 1 |
| The Winged Dragon of Ra - Sphere Mode | `10000080` | [Scripts/c10000080.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10000080.lua) | 2 |
| Primite Imperial Dragon | `81418467` | [Scripts/c81418467.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81418467.lua) | 1 |
| Dark Alligator | `34479658` | [Scripts/c34479658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34479658.lua) | 1 |
| Zaborg the Mega Monarch | `87602890` | [Scripts/c87602890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87602890.lua) | 1 |
| Bahalutiya, the Grand Radiance | `53318263` | [Scripts/c53318263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53318263.lua) | 1 |
| Caius the Mega Monarch | `87288189` | [Scripts/c87288189.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87288189.lua) | 1 |
| Raiza the Mega Monarch | `69327790` | [Scripts/c69327790.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69327790.lua) | 1 |
| Master Peace, the True Dracoverlord | `12800564` | [Scripts/c12800564.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12800564.lua) | 1 |
| Blackwing - Simoon the Poison Wind | `81470373` | [Scripts/c81470373.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81470373.lua) | 1 |
| Gravekeeper's Oracle | `25524823` | [Scripts/c25524823.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25524823.lua) | 2 |
| Slifer the Sky Dragon | `10000020` | [Scripts/c10000020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10000020.lua) | 1 |
| Twilight Ninja Getsuga, the Shogun | `76930964` | [Scripts/c76930964.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76930964.lua) | 1 |
| Behemoth the King of a Hundred Battles | `13836592` | [Scripts/c13836592.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13836592.lua) | 1 |
| Cosmic Horror Gangi'el | `51192573` | [Scripts/c51192573.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51192573.lua) | 1 |
| Leo Wizard the Dark Fiend | `55423549` | [Scripts/c55423549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55423549.lua) | 1 |
| Thestalos the Mega Monarch | `69230391` | [Scripts/c69230391.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69230391.lua) | 1 |
| ...and 50 more |  |  |  |

## Script Examples

### Ehther the Heavenly Monarch (`96570609`)

Source: [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua)

```lua
	if c==nil then return true end
	local mg=Duel.GetMatchingGroup(c96570609.otfilter,0,LOCATION_MZONE,LOCATION_MZONE,nil)
	return c:IsLevelAbove(7) and minc<=1 and Duel.CheckTribute(c,1,1,mg)
end
function c96570609.otop(e,tp,eg,ep,ev,re,r,rp,c)
```

### Union Activation (`38527680`)

Source: [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua)

```lua
		end
	else
		if not Duel.CheckTribute(c,minc,maxc) then return false end
	end
	if c:IsHasEffect(EFFECT_CANNOT_SUMMON,c:GetControler()) then
```

### Koa'ki Meiru Rooklord (`10060427`)

Source: [Scripts/c10060427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10060427.lua)

```lua
	local tp=c:GetControler()
	local mg=Duel.GetMatchingGroup(c10060427.otfilter,tp,LOCATION_MZONE,LOCATION_MZONE,nil,tp)
	return c:IsLevelAbove(7) and minc<=1 and Duel.CheckTribute(c,1,1,mg)
end
function c10060427.otop(e,tp,eg,ep,ev,re,r,rp,c)
```
