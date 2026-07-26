# Card.GetFirstCardTarget

## Signature

```lua
Card.GetFirstCardTarget(Card c) -> Card|nil
```

## Description

Returns c's first persistent card target, or nil.

## Parameters

- `c` `Card`

## Returns

- `Card|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3541`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **29** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetFirstCardTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Goblin Freefall Squad | `85123771` | [Scripts/c85123771.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85123771.lua) | 48 |
| Altergeist Manifestation | `35146019` | [Scripts/c35146019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35146019.lua) | 45 |
| Phantom Knights' Sword | `61936647` | [Scripts/c61936647.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61936647.lua) | 43 |
| Ninjitsu Art of Shadow Sealing | `13629812` | [Scripts/c13629812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13629812.lua) | 42 |
| Borrel Regenerator | `6556178` | [Scripts/c6556178.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6556178.lua) | 42 |
| Phantom Knights' Fog Blade | `25542642` | [Scripts/c25542642.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25542642.lua) | 40 |
| Galaxy Zero | `97617181` | [Scripts/c97617181.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97617181.lua) | 40 |
| Dimension Mirage | `80560728` | [Scripts/c80560728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80560728.lua) | 40 |
| Dimension Sphinx | `17787975` | [Scripts/c17787975.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17787975.lua) | 39 |
| Follow Wing | `42776855` | [Scripts/c42776855.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42776855.lua) | 36 |
| Moon Dance Ritual | `14005031` | [Scripts/c14005031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14005031.lua) | 35 |
| Nightmare Wheel | `54704216` | [Scripts/c54704216.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54704216.lua) | 35 |
| Vain Betrayer | `94933468` | [Scripts/c94933468.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94933468.lua) | 34 |
| Brainwashing Beam | `59258334` | [Scripts/c59258334.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59258334.lua) | 34 |
| Cyber Phoenix | `3370104` | [Scripts/c3370104.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3370104.lua) | 34 |
| Mask of Dispel | `20765952` | [Scripts/c20765952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20765952.lua) | 34 |
| Fulfillment of the Contract | `48206762` | [Scripts/c48206762.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48206762.lua) | 34 |
| Re-Fusion | `74694807` | [Scripts/c74694807.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74694807.lua) | 34 |
| Evil Eye Mesmerism | `42899204` | [Scripts/c42899204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42899204.lua) | 33 |
| Limit Reverse | `27551` | [Scripts/c27551.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27551.lua) | 32 |
| Symbol of Heritage | `45305419` | [Scripts/c45305419.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45305419.lua) | 32 |
| Shattered Axe | `12117532` | [Scripts/c12117532.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12117532.lua) | 32 |
| Gradius' Option | `14291024` | [Scripts/c14291024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14291024.lua) | 31 |
| Premature Burial | `70828912` | [Scripts/c70828912.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70828912.lua) | 31 |
| ...and 5 more |  |  |  |

## Script Examples

### Goblin Freefall Squad (`85123771`)

Source: [Scripts/c85123771.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85123771.lua)

```lua
function s.reop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local tc=c:GetFirstCardTarget()
	Card.CancelCardTarget(c,tc)
end
```

### Altergeist Manifestation (`35146019`)

Source: [Scripts/c35146019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35146019.lua)

```lua
	if e:GetLabelObject():GetLabel()~=0 then return end
	local c=e:GetHandler()
	local tc=c:GetFirstCardTarget()
	if tc and tc:IsLocation(LOCATION_MZONE) then
		Duel.Destroy(tc,REASON_EFFECT)
```

### Phantom Knights' Sword (`61936647`)

Source: [Scripts/c61936647.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61936647.lua)

```lua
	local c=e:GetHandler()
	if c:IsStatus(STATUS_DESTROY_CONFIRMED) then return false end
	local tc=c:GetFirstCardTarget()
	return tc and eg:IsContains(tc)
end
```
