# Effect.IsHasType

## Signature

```lua
Effect.IsHasType(Effect e, int type) -> bool
```

## Description

Checks whether e's effect type contains at least one flag from type.

## Parameters

- `e` `Effect`
- `type` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:652`

## Guided Examples

Learn how to use this function in context:

- [Counter Traps](/learn/counter-traps)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **744** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Effect.IsHasType) with `Effect.IsHasType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ultra Polymerization](/examples/cards/76647978) | `76647978` | [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76647978.lua) | 1 |
| [Future Fusion Nova](/examples/cards/92058902) | `92058902` | [Scripts/c92058902.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92058902.lua) | 2 |
| [DoSolfachord Coolia](/examples/cards/80776622) | `80776622` | [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80776622.lua) | 1 |
| [Radiant Typhoon Varuroon, the Marine Eidolon](/examples/cards/39341885) | `39341885` | [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39341885.lua) | 1 |
| Aroma Blend | `25861589` | [Scripts/c25861589.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25861589.lua) | 1 |
| Chaos Magical Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2372506.lua) | 1 |
| Super Duper Polymerization | `44886582` | [Scripts/c44886582.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44886582.lua) | 1 |
| Fusion Destiny | `52947044` | [Scripts/c52947044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52947044.lua) | 1 |
| A-to-Z-Dragon Buster Cannon | `65172015` | [Scripts/c65172015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65172015.lua) | 1 |
| Frightfur March | `74416026` | [Scripts/c74416026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74416026.lua) | 1 |
| Phantom Knights' Rank-Up-Magic Force | `88504133` | [Scripts/c88504133.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88504133.lua) | 1 |
| Clown Crew Soiree Operations | `70058649` | [Scripts/c70058649.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70058649.lua) | 1 |
| Amazement Administrator Arlekino | `94821366` | [Scripts/c94821366.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94821366.lua) | 1 |
| Divine Serpent Apophis | `97800311` | [Scripts/c97800311.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97800311.lua) | 1 |
| D/D/D Deviser King Deus Machinex | `46593546` | [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46593546.lua) | 1 |
| Clown Crew Malabarisme | `83232904` | [Scripts/c83232904.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83232904.lua) | 1 |
| Abyss-steam | `63941169` | [Scripts/c63941169.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63941169.lua) | 1 |
| Toadally Awesome | `90809975` | [Scripts/c90809975.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90809975.lua) | 1 |
| Horn of Olifant | `55749927` | [Scripts/c55749927.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55749927.lua) | 1 |
| Arcana Force EX - The Light Ruler | `5861892` | [Scripts/c5861892.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5861892.lua) | 1 |
| Genex Ally Triforce | `52709508` | [Scripts/c52709508.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52709508.lua) | 1 |
| Spirit Poacher | `85150300` | [Scripts/c85150300.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85150300.lua) | 1 |
| PSY-Framegear Alpha | `75425043` | [Scripts/c75425043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75425043.lua) | 1 |
| The Continuing Epic of Charles | `11802691` | [Scripts/c11802691.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11802691.lua) | 1 |
| ...and 720 more |  |  |  |

## Script Examples

### Ultra Polymerization (`76647978`)

Source: [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76647978.lua)

```lua
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_EXTRA)
	if e:IsHasType(EFFECT_TYPE_ACTIVATE) then
		Duel.SetChainLimit(aux.FALSE)
	end
```

### Future Fusion Nova (`92058902`)

Source: [Scripts/c92058902.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92058902.lua)

```lua
		fid=c:GetFieldID()
		tc:RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,0,1,fid)
		if c:IsOnField() and e:IsHasType(EFFECT_TYPE_ACTIVATE) and c:IsRelateToChain() then
			local e1=Effect.CreateEffect(c)
			e1:SetType(EFFECT_TYPE_CONTINUOUS+EFFECT_TYPE_SINGLE)
```

### DoSolfachord Coolia (`80776622`)

Source: [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80776622.lua)

```lua
end
function c80776622.chainlm(e,ep,tp)
	return ep==tp or e:IsActiveType(TYPE_SPELL+TYPE_TRAP) and not e:IsHasType(EFFECT_TYPE_ACTIVATE)
end
function c80776622.rfilter(c,tp)
```
