# Duel.ShuffleSetCard

## Signature

```lua
Duel.ShuffleSetCard(Group g) -> void
```

## Description

Randomly reorders the Set cards in g, used for effects such as Magical Hats.

## Parameters

- `g` `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4918`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.ShuffleSetCard) with `Duel.ShuffleSetCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Chaos Magical Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua) | 1 |
| Magical Hats | `81210420` | [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81210420.lua) | 1 |
| Morphing Jar #2 | `79106360` | [Scripts/c79106360.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79106360.lua) | 2 |
| Wandering Mummy | `42994702` | [Scripts/c42994702.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42994702.lua) | 1 |
| Shifting Shadows | `59237154` | [Scripts/c59237154.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59237154.lua) | 1 |

## Script Examples

### Chaos Magical Hats (`2372506`)

Source: [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua)

```lua
	Duel.ConfirmCards(1-tp,sg)
	sg:AddCard(tc)
	Duel.ShuffleSetCard(sg)
	local tg=Group.CreateGroup()
	Duel.ChangeTargetCard(ev,tg)
```

### Magical Hats (`81210420`)

Source: [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81210420.lua)

```lua
	Duel.ConfirmCards(1-tp,sg)
	sg:AddCard(tc)
	Duel.ShuffleSetCard(sg)
	sg:RemoveCard(tc)
	sg:KeepAlive()
```

### Morphing Jar #2 (`79106360`)

Source: [Scripts/c79106360.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79106360.lua)

```lua
	if ct2>0 then g2=c79106360.sp(e,1-tp,ct2) end
	Duel.SpecialSummonComplete()
	if g1 then Duel.ShuffleSetCard(g1) end
	if g2 then Duel.ShuffleSetCard(g2) end
end
```
