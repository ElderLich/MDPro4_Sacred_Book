# Duel.RaiseSingleEvent

## Signature

```lua
Duel.RaiseSingleEvent(Card ec, int code, Effect|nil re, int r, int rp, int ep, int ev) -> void
```

## Description

Raises a single-card event for ec with code, re, r, rp, ep, and ev, then processes single-card events.

## Parameters

- `ec` `Card`
- `code` `int`
- `re` `Effect|nil`
- `r` `int`
- `rp` `int`
- `ep` `int`
- `ev` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4896`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **35** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.RaiseSingleEvent) with `Duel.RaiseSingleEvent`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Performage Cup Tricker](/examples/cards/6812770) | `6812770` | [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua) | 1 |
| Squeeze, the Full Moon of Raise Moon - JACKPOT! | `9484285` | [Scripts/c9484285.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9484285.lua) | 2 |
| Time Thief Redoer | `55285840` | [Scripts/c55285840.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55285840.lua) | 1 |
| Firewall Dragon Singularity | `21637210` | [Scripts/c21637210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21637210.lua) | 1 |
| Angelechy Bastion | `28904860` | [Scripts/c28904860.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28904860.lua) | 2 |
| LeVirtue Dragon | `33113958` | [Scripts/c33113958.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33113958.lua) | 1 |
| Rank-Up-Magic Barian's Force | `47660516` | [Scripts/c47660516.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47660516.lua) | 1 |
| Transcendosaurus Exaraptor | `56818742` | [Scripts/c56818742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56818742.lua) | 1 |
| World of Prophecy | `29146185` | [Scripts/c29146185.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29146185.lua) | 1 |
| Goblin Biker Grand Breakout | `29111045` | [Scripts/c29111045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29111045.lua) | 1 |
| Angelechy Shatranga | `42410161` | [Scripts/c42410161.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42410161.lua) | 2 |
| Firewall Dragon | `5043010` | [Scripts/c5043010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5043010.lua) | 1 |
| Time Thief Double Barrel | `91135480` | [Scripts/c91135480.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91135480.lua) | 1 |
| Angelechy Destrier | `55393975` | [Scripts/c55393975.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55393975.lua) | 2 |
| Van'Dalgyon the Dark Dragon Lord | `24857466` | [Scripts/c24857466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24857466.lua) | 1 |
| Seismic Shockwave | `79569173` | [Scripts/c79569173.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79569173.lua) | 1 |
| Number 71: Rebarian Shark | `59479050` | [Scripts/c59479050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59479050.lua) | 1 |
| Sacred Tree Beast, Hyperyton | `9349094` | [Scripts/c9349094.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9349094.lua) | 1 |
| Heroic Challenger - Ambush Soldier | `92609670` | [Scripts/c92609670.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92609670.lua) | 1 |
| Power-Up Adapter | `78586116` | [Scripts/c78586116.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78586116.lua) | 1 |
| Gagagaga Girl | `88917691` | [Scripts/c88917691.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88917691.lua) | 1 |
| Dragon Gate | `9567495` | [Scripts/c9567495.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9567495.lua) | 1 |
| Black Rose Moonlight Dragon | `33698022` | [Scripts/c33698022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33698022.lua) | 1 |
| Xyz Revenge | `10275411` | [Scripts/c10275411.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10275411.lua) | 1 |
| ...and 11 more |  |  |  |

## Script Examples

### Performage Cup Tricker (`6812770`)

Source: [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua)

```lua
		Duel.Overlay(tc2,sg,false)
		local oc=sg:GetFirst():GetOverlayTarget()
		Duel.RaiseSingleEvent(tc,EVENT_DETACH_MATERIAL,e,0,0,0,0)
		Duel.RaiseEvent(tc,EVENT_DETACH_MATERIAL,e,0,0,0,0)
	end
```

### Squeeze, the Full Moon of Raise Moon - JACKPOT! (`9484285`)

Source: [Scripts/c9484285.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9484285.lua)

```lua
end
function s.ldop1(e,tp,eg,ep,ev,re,r,rp)
	Duel.RaiseSingleEvent(e:GetHandler(),EVENT_CUSTOM+id,e,0,tp,0,0)
end
function s.ldcon2(e,tp,eg,ep,ev,re,r,rp)
```

### Time Thief Redoer (`55285840`)

Source: [Scripts/c55285840.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55285840.lua)

```lua
	if not sg then return end
	Duel.SendtoGrave(sg,REASON_EFFECT)
	Duel.RaiseSingleEvent(c,EVENT_DETACH_MATERIAL,e,0,0,0,0)
	if sg:IsExists(Card.IsType,1,nil,TYPE_MONSTER) then
		Duel.BreakEffect()
```
