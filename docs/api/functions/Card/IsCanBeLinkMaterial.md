# Card.IsCanBeLinkMaterial

## Signature

```lua
Card.IsCanBeLinkMaterial(Card c, [Card|nil sc]) -> bool
```

## Description

Check if c can be used as Link Material \[for Link Monster sc\]; if sc is not specified, must pass nil

## Parameters

- `c` `Card`
- `sc` `Card|nil` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3643`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsCanBeLinkMaterial`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Salamangreat Sanctuary | `1295111` | [Scripts/c1295111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1295111.lua) | 53 |
| Code of Soul | `74652966` | [Scripts/c74652966.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74652966.lua) | 50 |
| Salamangreat Transcendence | `54529134` | [Scripts/c54529134.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54529134.lua) | 40 |

## Script Examples

### Salamangreat Sanctuary (`1295111`)

Source: [Scripts/c1295111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1295111.lua)

```lua
end
function c1295111.lmfilter(c,lc,tp,og,lmat)
	return c:IsFaceup() and c:IsCanBeLinkMaterial(lc) and c:IsLinkCode(lc:GetCode()) and c:IsLinkType(TYPE_LINK)
		and Duel.GetLocationCountFromEx(tp,tp,c,lc)>0 and aux.MustMaterialCheck(c,tp,EFFECT_MUST_BE_LMATERIAL)
		and (not og or og:IsContains(c)) and (not lmat or lmat==c)
```

### Code of Soul (`74652966`)

Source: [Scripts/c74652966.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74652966.lua)

```lua
end
function c74652966.lmfilter(c,lc,tp,og,lmat)
	return c:IsFaceup() and c:IsCanBeLinkMaterial(lc) and c:IsLinkCode(lc:GetCode()) and c:IsLinkType(TYPE_LINK)
		and Duel.GetLocationCountFromEx(tp,tp,c,lc)>0 and aux.MustMaterialCheck(c,tp,EFFECT_MUST_BE_LMATERIAL)
		and (not og or og:IsContains(c)) and (not lmat or lmat==c)
```

### Salamangreat Transcendence (`54529134`)

Source: [Scripts/c54529134.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54529134.lua)

```lua
end
function c54529134.filter2(c,e,tp,mc)
	return c:IsSetCard(0x119) and c:IsType(TYPE_LINK) and c:IsCode(mc:GetCode()) and mc:IsCanBeLinkMaterial(c)
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_LINK,tp,false,false) and Duel.GetLocationCountFromEx(tp,tp,mc,c)>0
end
```
