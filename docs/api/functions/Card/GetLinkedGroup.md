# Card.GetLinkedGroup

## Signature

```lua
Card.GetLinkedGroup(Card c) -> Group
```

## Description

Returns the cards currently occupying zones linked by c.
Use this when an effect cares about the actual cards in zones pointed to by c's Link Markers.

## Parameters

- `c` `Card`

## Returns

- `Group` - Cards currently in c's linked zones.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3419`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **61** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetLinkedGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| R.B. Lambda Blade | `17188206` | [Scripts/c17188206.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17188206.lua) | 56 |
| R.B. Lambda Cannon | `81794107` | [Scripts/c81794107.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81794107.lua) | 56 |
| Cyberse Contract Witch | `37458564` | [Scripts/c37458564.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37458564.lua) | 55 |
| Sylvan Dancepione | `21903613` | [Scripts/c21903613.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21903613.lua) | 54 |
| Cyberse Witch | `11674673` | [Scripts/c11674673.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11674673.lua) | 53 |
| Salamangreat Sunlight Wolf | `87871125` | [Scripts/c87871125.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87871125.lua) | 52 |
| S-Force Justify | `35334193` | [Scripts/c35334193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35334193.lua) | 51 |
| Gergonne's End | `59490397` | [Scripts/c59490397.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59490397.lua) | 51 |
| Saryuja Skull Dread | `74997493` | [Scripts/c74997493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74997493.lua) | 51 |
| Qliphort Genius | `22423493` | [Scripts/c22423493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22423493.lua) | 49 |
| Zerrziel, Ruler of the Evil Eyed | `17739335` | [Scripts/c17739335.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17739335.lua) | 48 |
| Battle Shogun of the Six Samurai | `74752631` | [Scripts/c74752631.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74752631.lua) | 48 |
| Maliss ＜P＞ March Hare | `20938824` | [Scripts/c20938824.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20938824.lua) | 48 |
| Sunavalon Dryatrentiay | `92770064` | [Scripts/c92770064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92770064.lua) | 48 |
| Rustin Mammoth | `3434362` | [Scripts/c3434362.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3434362.lua) | 48 |
| Xtra HERO Wonder Driver | `1948619` | [Scripts/c1948619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1948619.lua) | 47 |
| Flash Charge Dragon | `95372220` | [Scripts/c95372220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95372220.lua) | 47 |
| Puzzlomino, the Drop-n-Deleter | `84271823` | [Scripts/c84271823.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84271823.lua) | 47 |
| Subterror Behemoth Fiendess | `74937659` | [Scripts/c74937659.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74937659.lua) | 45 |
| Trickstar Band Drumatis | `64804137` | [Scripts/c64804137.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64804137.lua) | 45 |
| Junk Connector | `37337327` | [Scripts/c37337327.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37337327.lua) | 44 |
| R.B. VALCan Rocket | `79436874` | [Scripts/c79436874.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79436874.lua) | 43 |
| R.B. Ga10 Driller | `6043161` | [Scripts/c6043161.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6043161.lua) | 43 |
| Cyberse Wicckid | `52698008` | [Scripts/c52698008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52698008.lua) | 43 |
| ...and 37 more |  |  |  |

## Script Examples

### R.B. Lambda Blade (`17188206`)

Source: [Scripts/c17188206.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17188206.lua)

```lua
	local lg2=Group.CreateGroup()
	for lc in aux.Next(lg) do
		lg2:Merge(lc:GetLinkedGroup())
	end
	return lg2 and lg2:IsContains(e:GetHandler()) and Duel.GetTurnPlayer()==1-tp
```

### R.B. Lambda Cannon (`81794107`)

Source: [Scripts/c81794107.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81794107.lua)

```lua
	local lg2=Group.CreateGroup()
	for lc in aux.Next(lg) do
		lg2:Merge(lc:GetLinkedGroup())
	end
	return lg2 and lg2:IsContains(e:GetHandler())
```

### Cyberse Contract Witch (`37458564`)

Source: [Scripts/c37458564.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37458564.lua)

```lua
function s.thcfilter(c,ec)
	if c:IsLocation(LOCATION_MZONE) then
		return ec:GetLinkedGroup():IsContains(c)
	else
		return bit.extract(ec:GetLinkedZone(c:GetPreviousControler()),c:GetPreviousSequence())~=0
```
