# Duel.NegateSummon

## Signature

```lua
Duel.NegateSummon(Card|Group targets) -> void
```

## Description

Negates a current Normal Summon, Flip Summon, or Special Summon for targets.
targets may be a Card or Group. Normal and Flip Summon negation require a single card; Special Summon negation can process a group and only negates cards whose Summon is negatable by the current reason effect. The core raises the matching *_SUMMON_NEGATED event and returns no Lua value.
This is Summon negation, not Chain activation negation; pass the Summoned card or Group, not a Chain Link number.

## How To Use It

Use this for effects that negate a Summon before it becomes successful.

```lua
local g=eg
Duel.NegateSummon(g)
Duel.Destroy(g,REASON_EFFECT)
```

This is separate from Chain negation. It expects the Card or Group being Summoned, not a Chain Link number.

## Related Functions

- [Duel.GetCurrentChain](/api/functions/Duel/GetCurrentChain)
- [Duel.NegateActivation](/api/functions/Duel/NegateActivation)
- [Duel.Destroy](/api/functions/Duel/Destroy)

## Parameters

- `targets` `Card|Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4932`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **50** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.NegateSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Stardust Warrior | `74892653` | [Scripts/c74892653.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74892653.lua) | 50 |
| Jurrac Astero | `52553102` | [Scripts/c52553102.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52553102.lua) | 46 |
| Number C79: Battlin' Boxer General Kaiser | `10300821` | [Scripts/c10300821.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10300821.lua) | 45 |
| The Weather Painter Rainbow | `54178659` | [Scripts/c54178659.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54178659.lua) | 44 |
| Cosmic Blazar Dragon | `21123811` | [Scripts/c21123811.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21123811.lua) | 43 |
| Axon Kicker Oracle | `33171768` | [Scripts/c33171768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33171768.lua) | 42 |
| Infernoid Flood | `34446231` | [Scripts/c34446231.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34446231.lua) | 42 |
| T.G. Halberd Cannon/Assault Mode | `47027714` | [Scripts/c47027714.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47027714.lua) | 41 |
| Borreload Riot Dragon | `7987191` | [Scripts/c7987191.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7987191.lua) | 41 |
| T.G. Halberd Cannon | `97836203` | [Scripts/c97836203.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97836203.lua) | 40 |
| Koa'ki Meiru Overload | `14309486` | [Scripts/c14309486.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14309486.lua) | 39 |
| Predaplant Triphyoverutum | `79864860` | [Scripts/c79864860.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79864860.lua) | 37 |
| Varar, Vaalmonican Concord | `1340142` | [Scripts/c1340142.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1340142.lua) | 37 |
| El Shaddoll Grysta | `48424886` | [Scripts/c48424886.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48424886.lua) | 37 |
| Dark World Punishment | `3167439` | [Scripts/c3167439.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3167439.lua) | 36 |
| Paradox Fusion | `57355219` | [Scripts/c57355219.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57355219.lua) | 36 |
| Herald of Ultimateness | `48546368` | [Scripts/c48546368.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48546368.lua) | 35 |
| Angel Statue - Azurune | `44822037` | [Scripts/c44822037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44822037.lua) | 34 |
| Elemental Grace Doriado | `32965616` | [Scripts/c32965616.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32965616.lua) | 34 |
| Primite Scream | `27556460` | [Scripts/c27556460.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27556460.lua) | 32 |
| Seed-Spitting Saplings | `35263180` | [Scripts/c35263180.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35263180.lua) | 32 |
| Bending Destiny | `94662235` | [Scripts/c94662235.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94662235.lua) | 32 |
| Sauravis, the Ancient and Ascended | `4810828` | [Scripts/c4810828.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4810828.lua) | 31 |
| Gravity Collapse | `7811875` | [Scripts/c7811875.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7811875.lua) | 31 |
| ...and 26 more |  |  |  |

## Script Examples

### Stardust Warrior (`74892653`)

Source: [Scripts/c74892653.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74892653.lua)

```lua
end
function c74892653.operation(e,tp,eg,ep,ev,re,r,rp)
	Duel.NegateSummon(eg)
	Duel.Destroy(eg,REASON_EFFECT)
	e:GetHandler():RegisterFlagEffect(74892653,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,0,1)
```

### Jurrac Astero (`52553102`)

Source: [Scripts/c52553102.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52553102.lua)

```lua
end
function s.disop(e,tp,eg,ep,ev,re,r,rp)
	Duel.NegateSummon(eg)
	Duel.Destroy(eg,REASON_EFFECT)
end
```

### Number C79: Battlin' Boxer General Kaiser (`10300821`)

Source: [Scripts/c10300821.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10300821.lua)

```lua
	local c=e:GetHandler()
	if c:IsRelateToChain() and c:RemoveOverlayCard(tp,2,2,REASON_EFFECT)>0 then
		Duel.NegateSummon(eg)
		Duel.Destroy(eg,REASON_EFFECT)
	end
```
