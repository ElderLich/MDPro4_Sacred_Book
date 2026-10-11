# Duel.SelectField

## Signature

```lua
Duel.SelectField(int player, int count, int location1, int location2, int filter, [int desc]) -> int|nil
```

## Description

Lets player select count field zones from location1/location2 after applying filter as unavailable zones.
When desc is supplied, the core shows it as a selection hint. The return value is a bitmask of selected zones from player's viewpoint.

## Parameters

- `player` `int`
- `count` `int`
- `location1` `int`
- `location2` `int`
- `filter` `int`
- `desc` `int` optional

## Returns

- `int|nil` - Selected zone bitmask, or nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5027`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SelectField) with `Duel.SelectField`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Cynet Circuit | `82886276` | [Scripts/c82886276.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82886276.lua) | 1 |
| Solving for Pendulum | `5208118` | [Scripts/c5208118.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5208118.lua) | 1 |
| Zenet Cataract | `12555008` | [Scripts/c12555008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12555008.lua) | 1 |
| Springans Ship - Exblowrer | `62941499` | [Scripts/c62941499.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62941499.lua) | 1 |
| Codebreaker Virus Berserker | `48736598` | [Scripts/c48736598.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48736598.lua) | 1 |
| Vaylantz Buster Baron | `14418464` | [Scripts/c14418464.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14418464.lua) | 1 |
| Nazuki the Vaylantz Ninja | `41525660` | [Scripts/c41525660.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41525660.lua) | 1 |
| Vaylantz Wakening - Solo Activation | `60095092` | [Scripts/c60095092.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60095092.lua) | 1 |
| Springans Blast! | `10584050` | [Scripts/c10584050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10584050.lua) | 2 |

## Script Examples

### Cynet Circuit (`82886276`)

Source: [Scripts/c82886276.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82886276.lua)

```lua
			end
		end
		local sel_zone=Duel.SelectField(tp,1,LOCATION_MZONE,LOCATION_MZONE,0x00ff00ff&(~avail_zone),sc:GetCode())
		local sump=0
		if sel_zone&0xff>0 then
```

### Solving for Pendulum (`5208118`)

Source: [Scripts/c5208118.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5208118.lua)

```lua
		if flag==0 then return end
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOZONE)
		local ss=Duel.SelectField(tp,1,LOCATION_MZONE,0,~flag)
		local nseq=math.log(ss,2)
		Duel.MoveSequence(tc,nseq)
```

### Zenet Cataract (`12555008`)

Source: [Scripts/c12555008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12555008.lua)

```lua
	if chk==0 then return ct>0 end
	local diss={}
	local dis=Duel.SelectField(tp,math.min(ct,5),0,LOCATION_MZONE,0x60<<16)
	for i=0,4 do
		if dis&(1<<(i+16))~=0 then
```
