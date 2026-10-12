# Duel.GetSynchroMaterial

## Signature

```lua
Duel.GetSynchroMaterial(int player, [bool facedown]) -> Group
```

## Description

Gets the group of cards player can use as Synchro Material.
Face-down cards in the Monster Zone are omitted unless facedown is true.

## Parameters

- `player` `int`
- `facedown` `bool` optional - default: false

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4992`

## Guided Examples

Learn how to use this function in context:

- [Synchro Procedure Guide](/learn/synchro-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **18** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetSynchroMaterial) with `Duel.GetSynchroMaterial`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30983281.lua) | 1 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57261568.lua) | 2 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30581601.lua) | 2 |
| Flower Cardian Willow with Calligrapher | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89818984.lua) | 2 |
| Saiba the Soldier Swordsmith | `36608728` | [Scripts/c36608728.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36608728.lua) | 2 |
| Flower Cardian Moonflowerviewing | `33541430` | [Scripts/c33541430.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33541430.lua) | 2 |
| R-Genex Turing | `61052897` | [Scripts/c61052897.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61052897.lua) | 2 |
| Naturia Blessing | `34813545` | [Scripts/c34813545.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34813545.lua) | 2 |
| Stand Up Centur-Ion! | `41371602` | [Scripts/c41371602.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41371602.lua) | 2 |
| Re-dyce-cle | `85704698` | [Scripts/c85704698.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85704698.lua) | 2 |
| T.G. Cyber Magician | `64910482` | [Scripts/c64910482.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64910482.lua) | 2 |
| Dragunity Whirlwind | `89450409` | [Scripts/c89450409.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89450409.lua) | 1 |
| Etude of the Branded | `45675980` | [Scripts/c45675980.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45675980.lua) | 2 |
| PSY-Frame Circuit | `575512` | [Scripts/c575512.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c575512.lua) | 2 |
| Gold Pride - Leon | `23512906` | [Scripts/c23512906.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23512906.lua) | 2 |
| Tatsunoko | `55863245` | [Scripts/c55863245.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55863245.lua) | 2 |
| Tatsunecro | `3096468` | [Scripts/c3096468.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3096468.lua) | 2 |
| Yang Zing Unleashed | `77783947` | [Scripts/c77783947.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77783947.lua) | 2 |

## Script Examples

### Accel Synchro Stardust Dragon (`30983281`)

Source: [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30983281.lua)

```lua
function c30983281.scfilter(c,e,tp,rc,chkrel,chknotrel,tgchk,opchk)
	if not (c:IsCode(44508094) and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_SYNCHRO,tp,false,false)) then return false end
	local mg=Duel.GetSynchroMaterial(tp)
	if mg:IsExists(Card.GetHandSynchro,1,nil) then
		local mg2=Duel.GetMatchingGroup(nil,tp,LOCATION_HAND,0,nil)
```

### Flower Cardian Peony with Butterfly (`57261568`)

Source: [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57261568.lua)

```lua
	if lv<=c:GetLevel() and lv<=c57261568.cardiansynlevel(c) then return false end
	local g=Group.FromCards(c)
	local mg=Duel.GetSynchroMaterial(tp):Filter(c57261568.synfilter,c,syncard,c,f)
	return mg:IsExists(c57261568.syncheck,1,g,g,mg,tp,lv,syncard,minc,maxc)
end
```

### Yummy★Snatchy (`30581601`)

Source: [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30581601.lua)

```lua
	if chk==0 then
		if not Duel.IsPlayerCanSpecialSummon(tp) then return false end
		local mg=Duel.GetSynchroMaterial(tp)
		if mg:IsExists(Card.GetHandSynchro,1,nil) then
			local mg2=Duel.GetMatchingGroup(nil,tp,LOCATION_HAND,0,nil)
```
