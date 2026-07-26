# Duel.ChangeTargetCard

## Signature

```lua
Duel.ChangeTargetCard(int chainc, Group g) -> void
```

## Description

Replaces the target card group recorded for Chain Link chainc with g.

## Parameters

- `chainc` `int`
- `g` `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4924`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **29** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.ChangeTargetCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Chaos Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua) | 1 |
| Nerva the Power Patron of Creation | `53589300` | [Scripts/c53589300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53589300.lua) | 1 |
| Dyna Tank | `75780818` | [Scripts/c75780818.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75780818.lua) | 1 |
| Artifact Durendal | `69840739` | [Scripts/c69840739.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69840739.lua) | 1 |
| Mermail Abysstrite | `59170782` | [Scripts/c59170782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59170782.lua) | 1 |
| Subterror Nemesis Defender | `68823957` | [Scripts/c68823957.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68823957.lua) | 1 |
| Blackwing Tamer - Obsidian Hawk Joe | `81983656` | [Scripts/c81983656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81983656.lua) | 1 |
| Samsara D Lotus | `62318994` | [Scripts/c62318994.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62318994.lua) | 1 |
| Grapha, Dragon Overlord of Dark World | `39552584` | [Scripts/c39552584.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39552584.lua) | 1 |
| Exosister Karmael | `77675029` | [Scripts/c77675029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77675029.lua) | 1 |
| Prototype Sky Striker Ace - Amatsu | `25072579` | [Scripts/c25072579.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25072579.lua) | 1 |
| Centur-Ion Chimerea | `81696879` | [Scripts/c81696879.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81696879.lua) | 1 |
| World Legacy's Mind Meld | `27705190` | [Scripts/c27705190.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27705190.lua) | 1 |
| Abyss Playhouse - Fantastic Theater | `77297908` | [Scripts/c77297908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77297908.lua) | 1 |
| Phantom of Yubel | `80453041` | [Scripts/c80453041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80453041.lua) | 1 |
| Number 75: Bamboozling Gossip Shadow | `71166481` | [Scripts/c71166481.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71166481.lua) | 1 |
| Fairy Tail - Sleeper | `42921475` | [Scripts/c42921475.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42921475.lua) | 1 |
| Shipping Error | `58761791` | [Scripts/c58761791.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58761791.lua) | 1 |
| Cairngorgon, Antiluminescent Knight | `21501505` | [Scripts/c21501505.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21501505.lua) | 1 |
| Dark World Brainwashing | `10131855` | [Scripts/c10131855.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10131855.lua) | 1 |
| Shift | `59560625` | [Scripts/c59560625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59560625.lua) | 1 |
| Vortex of Time | `42138622` | [Scripts/c42138622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42138622.lua) | 1 |
| Fabled Dianaira | `53199020` | [Scripts/c53199020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53199020.lua) | 1 |
| Generaider Boss Room | `64325438` | [Scripts/c64325438.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64325438.lua) | 1 |
| ...and 5 more |  |  |  |

## Script Examples

### Chaos Hats (`2372506`)

Source: [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua)

```lua
	Duel.ShuffleSetCard(sg)
	local tg=Group.CreateGroup()
	Duel.ChangeTargetCard(ev,tg)
	Duel.ChangeChainOperation(ev,s.repop)
end
```

### Nerva the Power Patron of Creation (`53589300`)

Source: [Scripts/c53589300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53589300.lua)

```lua
function s.chop(e,tp,eg,ep,ev,re,r,rp)
	local g=Group.CreateGroup()
	Duel.ChangeTargetCard(ev,g)
	Duel.ChangeChainOperation(ev,s.repop)
end
```

### Dyna Tank (`75780818`)

Source: [Scripts/c75780818.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75780818.lua)

```lua
	local tc=Duel.GetFirstTarget()
	if tc:IsRelateToEffect(e) then
		Duel.ChangeTargetCard(ev,Group.FromCards(tc))
	end
end
```
