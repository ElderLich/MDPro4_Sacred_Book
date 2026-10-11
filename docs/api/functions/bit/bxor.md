# bit.bxor

## Signature

```lua
bit.bxor(int a, int b) -> int
```

## Description

Returns the bitwise XOR of a and b.

## Parameters

- `a` `int`
- `b` `int`

## Returns

- `int`

## Source

- `Utilities/utility.lua:21`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=bit.bxor) with `bit.bxor`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| S-Force Justify | `35334193` | [Scripts/c35334193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35334193.lua) | 1 |
| Parallel Panzer | `93394164` | [Scripts/c93394164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93394164.lua) | 2 |
| Dark Infant @Ignister | `74567889` | [Scripts/c74567889.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74567889.lua) | 1 |
| Procession of the Tea Jar | `12612470` | [Scripts/c12612470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12612470.lua) | 1 |
| Gouki The Solid Ogre | `22510667` | [Scripts/c22510667.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22510667.lua) | 1 |
| Link Back | `3567660` | [Scripts/c3567660.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3567660.lua) | 1 |
| Yajiro Invader | `10852583` | [Scripts/c10852583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10852583.lua) | 1 |
| Staring Contest | `97729135` | [Scripts/c97729135.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97729135.lua) | 2 |

## Script Examples

### S-Force Justify (`35334193`)

Source: [Scripts/c35334193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35334193.lua)

```lua
		if tc:IsDisabled() and tc:IsControler(1-tp) and Duel.GetLocationCount(1-tp,LOCATION_MZONE,PLAYER_NONE,0,zone)>0 and Duel.SelectYesNo(tp,aux.Stringid(35334193,2)) then
			local s=0
			local flag=bit.bxor(zone,0xff)*0x10000
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOZONE)
			s=Duel.SelectDisableField(tp,1,0,LOCATION_MZONE,flag)/0x10000
```

### Parallel Panzer (`93394164`)

Source: [Scripts/c93394164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93394164.lua)

```lua
		local s=0
		if ec:IsControler(tp) then
			local flag=bit.bxor(zone,0xff)
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOZONE)
			s=Duel.SelectDisableField(tp,1,LOCATION_MZONE,0,flag)
```

### Dark Infant @Ignister (`74567889`)

Source: [Scripts/c74567889.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74567889.lua)

```lua
	local s=zone
	if s&(s-1)~=0 then
		local flag=bit.bxor(zone,0xff)
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOZONE)
		s=Duel.SelectDisableField(tp,1,LOCATION_MZONE,0,flag)
```
