# Duel.DisableShuffleCheck

## Signature

```lua
Duel.DisableShuffleCheck([bool disable]) -> void
```

## Description

Disables the automatic shuffle check for the next Deck or hand operation.
Use this before operations that intentionally preserve Deck order or hand order.

## Parameters

- `disable` `bool` optional - default: true

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4912`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **149** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.DisableShuffleCheck) with `Duel.DisableShuffleCheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Junoldo the Shadespirit Power Patron](/examples/cards/10266279) | `10266279` | [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10266279.lua) | 1 |
| Jupredo the Shademachine Power Patron | `43871165` | [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43871165.lua) | 1 |
| D/D Extra Surveyor | `74387963` | [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74387963.lua) | 1 |
| Nervedo the Shadebeast Power Patron | `17473466` | [Scripts/c17473466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17473466.lua) | 1 |
| GMX - VELOX | `82706696` | [Scripts/c82706696.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82706696.lua) | 1 |
| Purrely | `25550531` | [Scripts/c25550531.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25550531.lua) | 1 |
| Sylvan Dancepione | `21903613` | [Scripts/c21903613.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21903613.lua) | 2 |
| Squeeze, the Full Moon of Raise Moon - JACKPOT! | `9484285` | [Scripts/c9484285.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9484285.lua) | 1 |
| Materiactor Meltthrough | `66059345` | [Scripts/c66059345.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66059345.lua) | 1 |
| Mad Tempest Trirealm Rift Ploutonion | `33822112` | [Scripts/c33822112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33822112.lua) | 1 |
| Time Thief Redoer | `55285840` | [Scripts/c55285840.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55285840.lua) | 1 |
| Ma'at | `18631392` | [Scripts/c18631392.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18631392.lua) | 2 |
| Shadowreaver Knight 21 | `95506252` | [Scripts/c95506252.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95506252.lua) | 1 |
| Materiactor Meltdown | `38669664` | [Scripts/c38669664.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38669664.lua) | 2 |
| Super Koi Koi | `66171432` | [Scripts/c66171432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66171432.lua) | 1 |
| Mariamne, the True Dracophoenix | `94160895` | [Scripts/c94160895.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94160895.lua) | 1 |
| Chaos Ruler, the Chaotic Magical Dragon | `3040496` | [Scripts/c3040496.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3040496.lua) | 1 |
| Adamancipator Risen - Leonite | `47674738` | [Scripts/c47674738.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47674738.lua) | 1 |
| Runick Freezing Curses | `30430448` | [Scripts/c30430448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30430448.lua) | 1 |
| Sky Thunder Trirealm Rift Yomi | `61033809` | [Scripts/c61033809.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61033809.lua) | 1 |
| Akashic Magician | `28776350` | [Scripts/c28776350.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28776350.lua) | 2 |
| Kelbek the Ancient Vanguard | `25926710` | [Scripts/c25926710.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25926710.lua) | 1 |
| Trirealm Rift of Emptiness Gehenna | `35761342` | [Scripts/c35761342.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35761342.lua) | 1 |
| Number 104: Masquerade Vain | `16908882` | [Scripts/c16908882.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16908882.lua) | 1 |
| ...and 125 more |  |  |  |

## Script Examples

### Junoldo the Shadespirit Power Patron (`10266279`)

Source: [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10266279.lua)

```lua
		and (not Duel.IsExistingMatchingCard(s.costfilter,tp,LOCATION_GRAVE,0,1,nil,e,tp)
		or not Duel.SelectYesNo(tp,aux.Stringid(99311889,1))) then
		Duel.DisableShuffleCheck()
		Duel.Remove(g,POS_FACEDOWN,REASON_COST)
	else
```

### Jupredo the Shademachine Power Patron (`43871165`)

Source: [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43871165.lua)

```lua
		and (not Duel.IsExistingMatchingCard(s.costfilter,tp,LOCATION_GRAVE,0,1,nil,e,tp)
		or not Duel.SelectYesNo(tp,aux.Stringid(99311889,1))) then
		Duel.DisableShuffleCheck()
		Duel.Remove(g,POS_FACEDOWN,REASON_COST)
	else
```

### D/D Extra Surveyor (`74387963`)

Source: [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74387963.lua)

```lua
	if ct==0 then return end
	local tg=Duel.GetDecktopGroup(1-tp,ct)
	Duel.DisableShuffleCheck()
	local atk=Duel.Remove(tg,POS_FACEUP,REASON_EFFECT)
	if atk>0 and Duel.IsExistingMatchingCard(s.atkfilter,tp,LOCATION_MZONE,0,1,nil)
```
