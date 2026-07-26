# Card.IsLinkState

## Signature

```lua
Card.IsLinkState(Card c) -> bool
```

## Description

Checks whether c is currently in linked state.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3428`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **14** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsLinkState`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Knightmare Gryphon | `65330383` | [Scripts/c65330383.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65330383.lua) | 1 |
| Sunseed Shadow | `30013902` | [Scripts/c30013902.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30013902.lua) | 1 |
| Longirsu, the Orcust Orchestrator | `76145142` | [Scripts/c76145142.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76145142.lua) | 2 |
| Orcustrion | `3134857` | [Scripts/c3134857.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3134857.lua) | 2 |
| Codebreaker Virus Berserker | `48736598` | [Scripts/c48736598.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48736598.lua) | 1 |
| World Legacy's Heart | `97648103` | [Scripts/c97648103.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97648103.lua) | 1 |
| Full Active Duplex | `4483598` | [Scripts/c4483598.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4483598.lua) | 1 |
| World Chalice Guardragon | `84899094` | [Scripts/c84899094.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84899094.lua) | 1 |
| SIMM Tablir | `67218327` | [Scripts/c67218327.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67218327.lua) | 1 |
| Tri-Brigade Rendezvous | `96378317` | [Scripts/c96378317.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96378317.lua) | 2 |
| Geonator Transverser | `52119435` | [Scripts/c52119435.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52119435.lua) | 1 |
| Cynet Storm | `42461852` | [Scripts/c42461852.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42461852.lua) | 1 |
| Break Off Trap Hole | `56526564` | [Scripts/c56526564.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56526564.lua) | 1 |
| Pentestag | `72336818` | [Scripts/c72336818.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72336818.lua) | 1 |

## Script Examples

### Knightmare Gryphon (`65330383`)

Source: [Scripts/c65330383.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65330383.lua)

```lua
function c65330383.aclimit(e,re,tp)
	local tc=re:GetHandler()
	return tc:IsLocation(LOCATION_MZONE) and tc:IsSummonType(SUMMON_TYPE_SPECIAL) and not tc:IsLinkState() and re:IsActiveType(TYPE_MONSTER)
end
```

### Sunseed Shadow (`30013902`)

Source: [Scripts/c30013902.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30013902.lua)

```lua
end
function c30013902.tgfilter(c,e,tp)
	return c:IsType(TYPE_LINK) and c:IsSetCard(0x1158,0x2158) and c:IsLinkBelow(2) and c:IsLinkState()
		and Duel.IsExistingMatchingCard(c30013902.spfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp,c:GetCode())
end
```

### Longirsu, the Orcust Orchestrator (`76145142`)

Source: [Scripts/c76145142.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76145142.lua)

```lua
end
function c76145142.indcon(e)
	return e:GetHandler():IsLinkState()
end
function c76145142.tdcon1(e,tp,eg,ep,ev,re,r,rp)
```
