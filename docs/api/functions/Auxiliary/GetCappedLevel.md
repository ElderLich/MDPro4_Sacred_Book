# Auxiliary.GetCappedLevel

## Signature

```lua
Auxiliary.GetCappedLevel(Card c) -> void
```

## Description

Returns c's current Level, capped at MAX_PARAMETER.

## Parameters

- `c` `Card`

## Source

- `Utilities/utility.lua:1522`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **13** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.GetCappedLevel) with `Auxiliary.GetCappedLevel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Miracle Raven | `18988396` | [Scripts/c18988396.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18988396.lua) | 1 |
| Griffoh | `97462632` | [Scripts/c97462632.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97462632.lua) | 1 |
| Lo, the Prayers of the Voiceless Voice | `25801745` | [Scripts/c25801745.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25801745.lua) | 1 |
| Avance, Swordsman of the Nekroz | `51618973` | [Scripts/c51618973.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51618973.lua) | 1 |
| Emilia, Dance Priestess of the Nekroz | `87003671` | [Scripts/c87003671.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87003671.lua) | 1 |
| Gishki Grimness | `38356857` | [Scripts/c38356857.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38356857.lua) | 1 |
| Gishki Vision | `47106439` | [Scripts/c47106439.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c47106439.lua) | 1 |
| Gishki Shadow | `29888389` | [Scripts/c29888389.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29888389.lua) | 1 |
| Shurit, Strategist of the Nekroz | `90307777` | [Scripts/c90307777.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90307777.lua) | 1 |
| Dragunity Couse | `29253591` | [Scripts/c29253591.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29253591.lua) | 1 |
| Tuningware | `92676637` | [Scripts/c92676637.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92676637.lua) | 1 |
| Yamatako Orochi | `4632019` | [Scripts/c4632019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4632019.lua) | 1 |
| Ritual Raven | `34334692` | [Scripts/c34334692.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34334692.lua) | 1 |

## Script Examples

### Miracle Raven (`18988396`)

Source: [Scripts/c18988396.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18988396.lua)

```lua
function s.rlevel(e,c)
	local ec=e:GetHandler()
	local lv=aux.GetCappedLevel(ec)
	if not ec:IsLocation(LOCATION_MZONE) then return lv end
	local clv=c:GetLevel()
```

### Griffoh (`97462632`)

Source: [Scripts/c97462632.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97462632.lua)

```lua
end
function s.rlevel(e,c)
	local lv=aux.GetCappedLevel(e:GetHandler())
	if c:IsLevel(8) then
		local clv=c:GetLevel()
```

### Lo, the Prayers of the Voiceless Voice (`25801745`)

Source: [Scripts/c25801745.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25801745.lua)

```lua
end
function s.rlevel(e,c)
	local lv=aux.GetCappedLevel(e:GetHandler())
	if c:IsRace(RACE_WARRIOR+RACE_DRAGON) and c:IsAttribute(ATTRIBUTE_LIGHT) then
		local clv=c:GetLevel()
```
