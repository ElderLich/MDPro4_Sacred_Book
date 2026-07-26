# bit.extract

## Signature

```lua
bit.extract(int r, int field, [int width]) -> int
```

## Description

Extracts width bits from r starting at bit field. width defaults to 1.

## Parameters

- `r` `int`
- `field` `int`
- `width` `int` optional

## Returns

- `int` - The extracted bit field.

## Source

- `Utilities/utility.lua:40`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **35** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `bit.extract`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Bujinki Ahashima](/examples/cards/71095768) | `71095768` | [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71095768.lua) | 1 |
| Black Garden | `71645242` | [Scripts/c71645242.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71645242.lua) | 2 |
| Cyberse Contract Witch | `37458564` | [Scripts/c37458564.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37458564.lua) | 1 |
| Neo Super Quantal Mech King Blaster Magna | `95493471` | [Scripts/c95493471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95493471.lua) | 1 |
| Cyberse Witch | `11674673` | [Scripts/c11674673.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11674673.lua) | 1 |
| Zefra Metaltron | `85216896` | [Scripts/c85216896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85216896.lua) | 1 |
| Firewall Dragon Singularity | `21637210` | [Scripts/c21637210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21637210.lua) | 1 |
| Qliphort Genius | `22423493` | [Scripts/c22423493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22423493.lua) | 1 |
| Rescue Ferret | `56343672` | [Scripts/c56343672.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56343672.lua) | 1 |
| Battle Shogun of the Six Samurai | `74752631` | [Scripts/c74752631.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74752631.lua) | 1 |
| Transcendosaurus Exaraptor | `56818742` | [Scripts/c56818742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56818742.lua) | 1 |
| Topologic Blaster Dragon | `30064423` | [Scripts/c30064423.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30064423.lua) | 1 |
| Xtra HERO Wonder Driver | `1948619` | [Scripts/c1948619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1948619.lua) | 1 |
| Tindangle Base Gardna | `94365540` | [Scripts/c94365540.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94365540.lua) | 1 |
| Subterror Behemoth Fiendess | `74937659` | [Scripts/c74937659.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74937659.lua) | 1 |
| Firewall Dragon | `5043010` | [Scripts/c5043010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5043010.lua) | 1 |
| GranSolfachord Coolia | `84521924` | [Scripts/c84521924.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84521924.lua) | 1 |
| Cyberse Wicckid | `52698008` | [Scripts/c52698008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52698008.lua) | 1 |
| Topologic Zeroboros | `66403530` | [Scripts/c66403530.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66403530.lua) | 1 |
| Topologic Bomber Dragon | `5821478` | [Scripts/c5821478.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5821478.lua) | 1 |
| Trickstar Crimson Heart | `51011872` | [Scripts/c51011872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51011872.lua) | 1 |
| Pitknight Earlie | `47759571` | [Scripts/c47759571.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47759571.lua) | 1 |
| Gouki Heel Ogre | `10552026` | [Scripts/c10552026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10552026.lua) | 1 |
| Shinobi Insect Hagakuremino | `70709488` | [Scripts/c70709488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70709488.lua) | 1 |
| ...and 11 more |  |  |  |

## Script Examples

### Bujinki Ahashima (`71095768`)

Source: [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71095768.lua)

```lua
	local zone=(c:GetLinkedZone(0) & 0x7f) | ((c:GetLinkedZone(1) & 0x7f)<<0x10)
	local seq=c71095768[2]
	return seq and bit.extract(zone,seq)~=0
end
function c71095768.destg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Black Garden (`71645242`)

Source: [Scripts/c71645242.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71645242.lua)

```lua
	end
	Duel.BreakEffect()
	if bit.extract(ev,tp)~=0 and Duel.GetLocationCount(1-tp,LOCATION_MZONE,tp)>0
		and Duel.IsPlayerCanSpecialSummonMonster(tp,71645243,0,TYPES_TOKEN_MONSTER,800,800,2,RACE_PLANT,ATTRIBUTE_DARK,POS_FACEUP_ATTACK,1-tp) then
		local token=Duel.CreateToken(tp,71645243)
```

### Cyberse Contract Witch (`37458564`)

Source: [Scripts/c37458564.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37458564.lua)

```lua
		return ec:GetLinkedGroup():IsContains(c)
	else
		return bit.extract(ec:GetLinkedZone(c:GetPreviousControler()),c:GetPreviousSequence())~=0
	end
end
```
