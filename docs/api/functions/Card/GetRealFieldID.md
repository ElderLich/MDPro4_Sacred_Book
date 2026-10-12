# Card.GetRealFieldID

## Signature

```lua
Card.GetRealFieldID(Card c) -> int
```

## Description

Returns c's real field ID, the core field identifier used for relation tracking.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3530`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **12** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetRealFieldID) with `Card.GetRealFieldID`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Rise to Full Height | `19254117` | [Scripts/c19254117.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19254117.lua) | 2 |
| Corrupted Keys | `67949763` | [Scripts/c67949763.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67949763.lua) | 1 |
| Number 13: Embodiment of Crime | `69058960` | [Scripts/c69058960.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69058960.lua) | 2 |
| Number 31: Embodiment of Punishment | `95442074` | [Scripts/c95442074.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95442074.lua) | 2 |
| Cyberse Wizard | `36033786` | [Scripts/c36033786.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36033786.lua) | 2 |
| Phonon Pulse Dragon | `67556500` | [Scripts/c67556500.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67556500.lua) | 2 |
| Staunch Defender | `92854392` | [Scripts/c92854392.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92854392.lua) | 2 |
| Guard Penalty | `48653261` | [Scripts/c48653261.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48653261.lua) | 2 |
| Taunt | `90740329` | [Scripts/c90740329.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90740329.lua) | 2 |
| Interplanetary Invader "A" | `14729426` | [Scripts/c14729426.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14729426.lua) | 2 |
| Prohibition | `43711255` | [Scripts/c43711255.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43711255.lua) | 1 |
| Bounzer Guard | `48582558` | [Scripts/c48582558.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48582558.lua) | 2 |

## Script Examples

### Rise to Full Height (`19254117`)

Source: [Scripts/c19254117.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19254117.lua)

```lua
		e1:SetTargetRange(0,LOCATION_MZONE)
		e1:SetValue(c19254117.atklimit)
		e1:SetLabel(tc:GetRealFieldID())
		e1:SetReset(RESET_PHASE+PHASE_END)
		Duel.RegisterEffect(e1,tp)
```

### Corrupted Keys (`67949763`)

Source: [Scripts/c67949763.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67949763.lua)

```lua
	local tc=Duel.GetFirstTarget()
	if Duel.GetLocationCount(tp,LOCATION_MZONE)>2 then
		local rfid=tc:GetRealFieldID()
		local atk=0
		local cr=false
```

### Number 13: Embodiment of Crime (`69058960`)

Source: [Scripts/c69058960.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69058960.lua)

```lua
	if g:GetCount()>0 then
		Duel.ChangePosition(g,POS_FACEUP_ATTACK)
		local fid=c:GetRealFieldID()
		local tc=g:GetFirst()
		while tc do
```
