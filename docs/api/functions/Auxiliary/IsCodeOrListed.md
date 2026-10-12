# Auxiliary.IsCodeOrListed

## Signature

```lua
Auxiliary.IsCodeOrListed(Card c, int code) -> bool
```

## Description

Returns true if c's current code matches code or code is registered in c's listed-code table.

## Parameters

- `c` `Card`
- `code` `int`

## Returns

- `bool` - true if c has or lists code.

## Source

- `Utilities/utility.lua:550`

## Guided Examples

Learn how to use this function in context:

- [Archetypes and Set Codes](/learn/archetypes-and-setcodes)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **39** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.IsCodeOrListed) with `Auxiliary.IsCodeOrListed`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ecclesia and the Dark Dragon | `78397661` | [Scripts/c78397661.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78397661.lua) | 1 |
| Assault Reboot | `74431740` | [Scripts/c74431740.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74431740.lua) | 1 |
| Protector of The Agents - Moon | `90290572` | [Scripts/c90290572.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90290572.lua) | 1 |
| Arrow of Regulus | `60439482` | [Scripts/c60439482.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60439482.lua) | 1 |
| Dark Magician of Destruction | `59400890` | [Scripts/c59400890.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59400890.lua) | 1 |
| Celestial Knightlord Parshath | `48589580` | [Scripts/c48589580.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48589580.lua) | 1 |
| B.E.S. Derringer Core | `5121528` | [Scripts/c5121528.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5121528.lua) | 1 |
| Junk Signal | `26387390` | [Scripts/c26387390.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26387390.lua) | 2 |
| Psi-Reflector | `74644400` | [Scripts/c74644400.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74644400.lua) | 1 |
| Soul Resonator | `62991792` | [Scripts/c62991792.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62991792.lua) | 1 |
| Pumpking the Great Ghost King | `17856505` | [Scripts/c17856505.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17856505.lua) | 1 |
| Illusion of Chaos | `12266229` | [Scripts/c12266229.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12266229.lua) | 1 |
| Keldo the Sacred Protector | `63542003` | [Scripts/c63542003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63542003.lua) | 1 |
| Wightbaking | `6128460` | [Scripts/c6128460.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6128460.lua) | 1 |
| Soul Servant | `23020408` | [Scripts/c23020408.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23020408.lua) | 2 |
| Fisherman of Legend | `76660178` | [Scripts/c76660178.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76660178.lua) | 1 |
| Fallen Sanctuary | `90312154` | [Scripts/c90312154.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90312154.lua) | 1 |
| Celestial Apparatus Tesea | `54092240` | [Scripts/c54092240.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54092240.lua) | 1 |
| Crimson Blader/Assault Mode | `50604072` | [Scripts/c50604072.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50604072.lua) | 1 |
| Gung-Ho! Springans! | `4079728` | [Scripts/c4079728.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4079728.lua) | 1 |
| Dictator of D. | `66961194` | [Scripts/c66961194.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66961194.lua) | 1 |
| Wight Reanimator | `39848658` | [Scripts/c39848658.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39848658.lua) | 1 |
| Curse of Aramatir | `34690953` | [Scripts/c34690953.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34690953.lua) | 1 |
| Fiend Piece Golem | `56838842` | [Scripts/c56838842.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56838842.lua) | 1 |
| ...and 15 more |  |  |  |

## Script Examples

### Ecclesia and the Dark Dragon (`78397661`)

Source: [Scripts/c78397661.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78397661.lua)

```lua
end
function s.spfilter(c,e,tp)
	return aux.IsCodeOrListed(c,68468459) and c:IsLevelBelow(4) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Assault Reboot (`74431740`)

Source: [Scripts/c74431740.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74431740.lua)

```lua
end
function c74431740.tdfilter(c,e)
	return not c:IsCode(74431740) and aux.IsCodeOrListed(c,80280737) and c:IsAbleToDeck()
		and (not e or c:IsCanBeEffectTarget(e))
end
```

### Protector of The Agents - Moon (`90290572`)

Source: [Scripts/c90290572.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90290572.lua)

```lua
end
function c90290572.tgfilter(c)
	return aux.IsCodeOrListed(c,56433456) and c:IsAbleToGrave()
end
function c90290572.thfilter(c)
```
