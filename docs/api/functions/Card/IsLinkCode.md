# Card.IsLinkCode

## Signature

```lua
Card.IsLinkCode(Card c, int code1, [int code2], [... int]) -> bool
```

## Description

Checks whether c matches any supplied code while used as Link Material.
This includes c's current code, second code, and EFFECT_ADD_LINK_CODE values. If no link-code additions apply, the binding falls back to Card.IsCode.

## Parameters

- `c` `Card`
- `code1` `int`
- `code2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3442`

## Guided Examples

Learn how to use this function in context:

- [Link Procedure Guide](/learn/link-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **21** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsLinkCode) with `Card.IsLinkCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Emperor Charles the Great | `97864322` | [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97864322.lua) | 1 |
| Salamangreat Raging Phoenix | `57134592` | [Scripts/c57134592.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57134592.lua) | 1 |
| Salamangreat Sanctuary | `1295111` | [Scripts/c1295111.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1295111.lua) | 1 |
| Salamangreat Sunlight Wolf | `87871125` | [Scripts/c87871125.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87871125.lua) | 1 |
| Code of Soul | `74652966` | [Scripts/c74652966.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74652966.lua) | 1 |
| Salamangreat Pyro Phoenix | `31313405` | [Scripts/c31313405.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c31313405.lua) | 1 |
| Salamangreat Rage | `14934922` | [Scripts/c14934922.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14934922.lua) | 1 |
| Cyberse Enchanter | `60279710` | [Scripts/c60279710.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60279710.lua) | 1 |
| Salamangreat Circle | `52155219` | [Scripts/c52155219.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52155219.lua) | 1 |
| Salamangreat Heatleo | `41463181` | [Scripts/c41463181.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41463181.lua) | 1 |
| Salamangreat Gift | `20788863` | [Scripts/c20788863.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20788863.lua) | 1 |
| Will of the Salamangreat | `64178424` | [Scripts/c64178424.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64178424.lua) | 1 |
| Marincess Crystal Heart | `67712104` | [Scripts/c67712104.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67712104.lua) | 1 |
| Sunavalon Dryas | `93896655` | [Scripts/c93896655.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93896655.lua) | 1 |
| Knightmare Mermaid | `3679218` | [Scripts/c3679218.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3679218.lua) | 1 |
| Backup Supervisor | `97677329` | [Scripts/c97677329.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97677329.lua) | 1 |
| Cyber Dragon Sieger | `46724542` | [Scripts/c46724542.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46724542.lua) | 1 |
| Salamangreat Roar | `51339637` | [Scripts/c51339637.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51339637.lua) | 1 |
| Salamangreat Claw | `88540324` | [Scripts/c88540324.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88540324.lua) | 1 |
| Crusadia Magius | `72228247` | [Scripts/c72228247.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72228247.lua) | 1 |
| Scareclaw Light-Heart | `53776969` | [Scripts/c53776969.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53776969.lua) | 1 |

## Script Examples

### Emperor Charles the Great (`97864322`)

Source: [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97864322.lua)

```lua
end
function s.matfilter(c)
	return c:IsLevel(9) and c:IsLinkCode(77656797) and c:GetEquipCount()>0
end
function s.copycon(e)
```

### Salamangreat Raging Phoenix (`57134592`)

Source: [Scripts/c57134592.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57134592.lua)

```lua
function s.valcheck(e,c)
	local g=c:GetMaterial()
	if g:IsExists(Card.IsLinkCode,1,nil,57134592) then
		e:GetLabelObject():SetLabel(1)
	else
```

### Salamangreat Sanctuary (`1295111`)

Source: [Scripts/c1295111.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1295111.lua)

```lua
end
function c1295111.lmfilter(c,lc,tp,og,lmat)
	return c:IsFaceup() and c:IsCanBeLinkMaterial(lc) and c:IsLinkCode(lc:GetCode()) and c:IsLinkType(TYPE_LINK)
		and Duel.GetLocationCountFromEx(tp,tp,c,lc)>0 and aux.MustMaterialCheck(c,tp,EFFECT_MUST_BE_LMATERIAL)
		and (not og or og:IsContains(c)) and (not lmat or lmat==c)
```
