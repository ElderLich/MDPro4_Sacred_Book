# Duel.SendtoGrave

## Signature

```lua
Duel.SendtoGrave(Card|Group targets, int reason, [int reason_player]) -> int
```

## Description

Sends targets to the GY for reason, optionally treating reason_player as the player that moved them, and returns the number actually moved.
This is not destruction by itself. Use Duel.Destroy for destroy effects, or include the correct discard/material/release reason flags when the card text or mechanic requires them.

## How To Use It

Use this for sending cards to the Graveyard by effect, cost, discard, or material handling.

```lua
if #g>0 then
    Duel.SendtoGrave(g,REASON_EFFECT)
end
```

This is not the same as destroying. A card sent to the Graveyard by `Duel.SendtoGrave` was not destroyed unless the reason and prior action also say it was destroyed.

## Related Functions

- [Card.IsAbleToGrave](/api/functions/Card/IsAbleToGrave)
- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)
- [Duel.Destroy](/api/functions/Duel/Destroy)

## Parameters

- `targets` `Card|Group` - Card or Group to send to the Graveyard.
- `reason` `int` - REASON_* flags recorded for the move.
- `reason_player` `int` optional - Player recorded as the reason player; defaults to the core's current reason player.

## Returns

- `int` - Number of cards actually sent to the Graveyard.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4860`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2387** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SendtoGrave) with `Duel.SendtoGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua) | 2 |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78579058.lua) | 3 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41570943.lua) | 3 |
| [Eternal Favorite](/examples/cards/87532344) | `87532344` | [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87532344.lua) | 2 |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua) | 1 |
| [Spellbook of the Grand Circle](/examples/cards/11911336) | `11911336` | [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11911336.lua) | 1 |
| [Ultra Polymerization](/examples/cards/76647978) | `76647978` | [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76647978.lua) | 1 |
| [Melffy Playtime Surprise](/examples/cards/58036097) | `58036097` | [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua) | 1 |
| [Yomagna the Fire Phantom](/examples/cards/17350692) | `17350692` | [Scripts/c17350692.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17350692.lua) | 1 |
| [Fiendsmith's Sequence](/examples/cards/49867899) | `49867899` | [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49867899.lua) | 1 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11852093.lua) | 1 |
| [Mementotlan Fusion](/examples/cards/66518509) | `66518509` | [Scripts/c66518509.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66518509.lua) | 1 |
| [Favorite HERO Flame Wingman](/examples/cards/13243124) | `13243124` | [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13243124.lua) | 1 |
| [Gem-Knight Dispersion](/examples/cards/24220368) | `24220368` | [Scripts/c24220368.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24220368.lua) | 1 |
| [Performage Cup Tricker](/examples/cards/6812770) | `6812770` | [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua) | 1 |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua) | 1 |
| [Spirit Illusion](/examples/cards/71939275) | `71939275` | [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71939275.lua) | 1 |
| [Pere-Zenet Em Heru](/examples/cards/46273941) | `46273941` | [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46273941.lua) | 1 |
| [Am Duazenet](/examples/cards/45151304) | `45151304` | [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45151304.lua) | 1 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27693363.lua) | 2 |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua) | 1 |
| [Aiwass, Divine Spirit of the Law](/examples/cards/84288367) | `84288367` | [Scripts/c84288367.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84288367.lua) | 1 |
| [Resurgam Xyz](/examples/cards/49082032) | `49082032` | [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua) | 1 |
| [GMX 55th Experiment Report](/examples/cards/38984832) | `38984832` | [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38984832.lua) | 2 |
| ...and 2363 more |  |  |  |

## Script Examples

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
	local dg=g:Filter(s.disfilter,nil)
	g:Sub(dg)
	Duel.SendtoGrave(dg,REASON_SPSUMMON+REASON_DISCARD)
	Duel.Release(g,REASON_SPSUMMON)
	g:DeleteGroup()
```

### Levia-Dragoon - Daedalus (`78579058`)

Source: [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78579058.lua)

```lua
				c:SetMaterial(g)
				s.LExtraMaterialCount(g,c,tp)
				Duel.SendtoGrave(g,REASON_MATERIAL+REASON_LINK)
				g:DeleteGroup()
			end
```

### Azure Ocean Dragon Lord - Neo-Daedalus Rage (`41570943`)

Source: [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41570943.lua)

```lua
				c:SetMaterial(g)
				s.LExtraMaterialCount(g,c,tp)
				Duel.SendtoGrave(g,REASON_MATERIAL+REASON_LINK)
				g:DeleteGroup()
			end
```
