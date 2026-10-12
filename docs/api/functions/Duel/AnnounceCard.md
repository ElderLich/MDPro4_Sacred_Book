# Duel.AnnounceCard

## Signature

```lua
Duel.AnnounceCard(int player, [int opcode1], [... int]) -> int
```

## Description

Lets player declare a card code matching the optional opcode/filter expression and returns the selected code.

## Parameters

- `player` `int`
- `opcode1` `int` optional
- `...` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5032`

## Guided Examples

Learn how to use this function in context:

- [Archetypes and Set Codes](/learn/archetypes-and-setcodes)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **32** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.AnnounceCard) with `Duel.AnnounceCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ma'at | `18631392` | [Scripts/c18631392.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18631392.lua) | 3 |
| Mind Scan | `34298391` | [Scripts/c34298391.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34298391.lua) | 2 |
| Gravekeeper's Trap | `98715423` | [Scripts/c98715423.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98715423.lua) | 1 |
| Primite Roar | `92501449` | [Scripts/c92501449.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92501449.lua) | 1 |
| Primite Howl | `41488249` | [Scripts/c41488249.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41488249.lua) | 1 |
| Primite Lordly Lode | `56506740` | [Scripts/c56506740.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56506740.lua) | 1 |
| Artmage Academic Arcane Arts Acropolis | `74733322` | [Scripts/c74733322.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74733322.lua) | 1 |
| Forge a New Future | `27104921` | [Scripts/c27104921.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27104921.lua) | 1 |
| Akashic Magician | `28776350` | [Scripts/c28776350.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28776350.lua) | 1 |
| Alsei, the Sylvan High Protector | `10406322` | [Scripts/c10406322.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10406322.lua) | 1 |
| Exosister Carpedivem | `30802207` | [Scripts/c30802207.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30802207.lua) | 1 |
| Gunkan Suship Catch-of-the-Day | `83008724` | [Scripts/c83008724.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83008724.lua) | 1 |
| Ancient Gear Gadget | `18486927` | [Scripts/c18486927.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18486927.lua) | 1 |
| The Suppression Pluto | `24413299` | [Scripts/c24413299.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24413299.lua) | 1 |
| Engraver of the Mark | `50078320` | [Scripts/c50078320.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50078320.lua) | 2 |
| Goddess Urd's Verdict | `91969909` | [Scripts/c91969909.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c91969909.lua) | 1 |
| Crossout Designator | `65681983` | [Scripts/c65681983.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65681983.lua) | 1 |
| The True Name | `39913299` | [Scripts/c39913299.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39913299.lua) | 1 |
| Dirge of the Lost Dragon | `40971261` | [Scripts/c40971261.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40971261.lua) | 1 |
| Lullaby of Obedience | `39238953` | [Scripts/c39238953.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39238953.lua) | 1 |
| Archfiend's Oath | `22796548` | [Scripts/c22796548.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22796548.lua) | 1 |
| Question | `38723936` | [Scripts/c38723936.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38723936.lua) | 1 |
| The Black Goat Laughs | `49299410` | [Scripts/c49299410.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49299410.lua) | 1 |
| Cloak and Dagger | `8323633` | [Scripts/c8323633.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8323633.lua) | 1 |
| ...and 8 more |  |  |  |

## Script Examples

### Ma'at (`18631392`)

Source: [Scripts/c18631392.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18631392.lua)

```lua
	getmetatable(e:GetHandler()).announce_filter={TYPE_FUSION+TYPE_SYNCHRO+TYPE_XYZ+TYPE_LINK,OPCODE_ISTYPE,OPCODE_NOT}
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CODE)
	local ac1=Duel.AnnounceCard(tp,table.unpack(getmetatable(e:GetHandler()).announce_filter))
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CODE)
	local ac2=Duel.AnnounceCard(tp,table.unpack(getmetatable(e:GetHandler()).announce_filter))
```

### Mind Scan (`34298391`)

Source: [Scripts/c34298391.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34298391.lua)

```lua
		table.insert(afilter,OPCODE_NOT)
		ag:Clear()
		local ac=Duel.AnnounceCard(tp,table.unpack(afilter))
		Duel.SetTargetParam(ac)
		Duel.SetOperationInfo(0,CATEGORY_ANNOUNCE,nil,0,tp,0)
```

### Gravekeeper's Trap (`98715423`)

Source: [Scripts/c98715423.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98715423.lua)

```lua
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CODE)
	getmetatable(e:GetHandler()).announce_filter={TYPE_FUSION+TYPE_SYNCHRO+TYPE_XYZ+TYPE_LINK,OPCODE_ISTYPE,OPCODE_NOT}
	local ac=Duel.AnnounceCard(tp,table.unpack(getmetatable(e:GetHandler()).announce_filter))
	Duel.SetTargetParam(ac)
	Duel.SetOperationInfo(0,CATEGORY_ANNOUNCE,nil,0,tp,0)
```
