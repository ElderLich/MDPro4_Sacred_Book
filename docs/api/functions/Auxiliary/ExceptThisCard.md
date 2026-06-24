# Auxiliary.ExceptThisCard

## Signature

```lua
Auxiliary.ExceptThisCard(Effect e) -> Card|nil
```

## Description

Returns e's handler while that card is still related to the current Chain; otherwise returns nil.

## Parameters

- `e` `Effect`

## Returns

- `Card|nil` - e's handler if it is still related to the current Chain; otherwise nil.

## Source

- `Utilities/utility.lua:1176`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **162** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.ExceptThisCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua) | 64 |
| [Enlightenment Dragon](/examples/cards/46186135) | `46186135` | [Scripts/c46186135.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46186135.lua) | 62 |
| Performapal Celestial Magician | `58092907` | [Scripts/c58092907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58092907.lua) | 58 |
| Fallen Paradise of the Sacred Beasts | `65861210` | [Scripts/c65861210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65861210.lua) | 56 |
| Invoked Transcendence Aeon | `33166263` | [Scripts/c33166263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33166263.lua) | 55 |
| Sosei Ryu-Ge Mistva | `92487128` | [Scripts/c92487128.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92487128.lua) | 54 |
| Shadow Severing Strike | `57232301` | [Scripts/c57232301.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57232301.lua) | 52 |
| Triangle O | `11489642` | [Scripts/c11489642.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11489642.lua) | 52 |
| Immortal Phoenix Gearfried | `22091647` | [Scripts/c22091647.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22091647.lua) | 51 |
| Ruddy Rose Dragon | `40139997` | [Scripts/c40139997.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40139997.lua) | 50 |
| DoomZ Command "D.O.O.M.D.U.R.G." | `68831625` | [Scripts/c68831625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68831625.lua) | 49 |
| Mystic Box of Chaos | `75983808` | [Scripts/c75983808.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75983808.lua) | 49 |
| Clockwork Knight | `41739381` | [Scripts/c41739381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41739381.lua) | 49 |
| Stellarknight Triverr | `42589641` | [Scripts/c42589641.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42589641.lua) | 49 |
| Super Quantum Black Layer | `92034192` | [Scripts/c92034192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92034192.lua) | 48 |
| Crimson Dragon Quetzacoatl | `29053656` | [Scripts/c29053656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29053656.lua) | 48 |
| Maliss ＜P＞ March Hare | `20938824` | [Scripts/c20938824.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20938824.lua) | 48 |
| Infernoid Onuncu | `14799437` | [Scripts/c14799437.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14799437.lua) | 48 |
| Possessed Partnerships | `65046521` | [Scripts/c65046521.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65046521.lua) | 48 |
| Neo Galaxy-Eyes Photon Dragon - Photon Howling | `28331069` | [Scripts/c28331069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28331069.lua) | 47 |
| Topologic Blaster Dragon | `30064423` | [Scripts/c30064423.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30064423.lua) | 47 |
| Sky Striker Ace - Azalea Temperance | `56741506` | [Scripts/c56741506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56741506.lua) | 47 |
| Elemental HERO Thunder Giant - Voltic Thunder | `19222426` | [Scripts/c19222426.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19222426.lua) | 47 |
| DoomZ Raiders | `32442017` | [Scripts/c32442017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32442017.lua) | 47 |
| ...and 138 more |  |  |  |

## Script Examples

### Odd-Eyes Revolution Dragon (`16306932`)

Source: [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua)

```lua
end
function c16306932.tdop(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetMatchingGroup(Card.IsAbleToDeck,tp,LOCATION_ONFIELD+LOCATION_GRAVE,LOCATION_ONFIELD+LOCATION_GRAVE,aux.ExceptThisCard(e))
	if g:GetCount()>0 then
		Duel.SendtoDeck(g,nil,SEQ_DECKSHUFFLE,REASON_EFFECT)
```

### Enlightenment Dragon (`46186135`)

Source: [Scripts/c46186135.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46186135.lua)

```lua
end
function s.reop(e,tp,eg,ep,ev,re,r,rp)
	local sg=Duel.GetMatchingGroup(Card.IsAbleToRemove,tp,LOCATION_ONFIELD+LOCATION_GRAVE,LOCATION_ONFIELD+LOCATION_GRAVE,aux.ExceptThisCard(e))
	Duel.Remove(sg,POS_FACEUP,REASON_EFFECT)
end
```

### Performapal Celestial Magician (`58092907`)

Source: [Scripts/c58092907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58092907.lua)

```lua
function c58092907.meop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local g=Duel.GetMatchingGroup(c58092907.mefilter1,tp,LOCATION_MZONE,0,aux.ExceptThisCard(e))
	local b1=c:IsRelateToEffect(e) and g:IsExists(c58092907.cfilter,1,nil,TYPE_FUSION)
	local b2=g:IsExists(c58092907.cfilter,1,nil,TYPE_SYNCHRO)
```
