# Card.IsLinkType

## Signature

```lua
Card.IsLinkType(Card c, int type) -> bool
```

## Description

Checks whether c's type while used as Link Material contains type.

## Parameters

- `c` `Card`
- `type` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3486`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **132** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsLinkType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 61 |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua) | 59 |
| Beyond the Pendulum | `22125101` | [Scripts/c22125101.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22125101.lua) | 56 |
| Enlilgirsu, the Orcust Mekk-Knight | `74820316` | [Scripts/c74820316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74820316.lua) | 56 |
| Neo Super Quantal Mech King Blaster Magna | `95493471` | [Scripts/c95493471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95493471.lua) | 53 |
| Borrelcode Dragon | `67288539` | [Scripts/c67288539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67288539.lua) | 53 |
| Borrelshroud Dragon | `66452432` | [Scripts/c66452432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66452432.lua) | 53 |
| Crystron Halqifibrax Prism | `65400671` | [Scripts/c65400671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65400671.lua) | 53 |
| Worldsea Dragon Zealantis | `45112597` | [Scripts/c45112597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45112597.lua) | 53 |
| Salamangreat Raging Phoenix | `57134592` | [Scripts/c57134592.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57134592.lua) | 53 |
| Salamangreat Sanctuary | `1295111` | [Scripts/c1295111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1295111.lua) | 53 |
| Proxy F Magician | `12450071` | [Scripts/c12450071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12450071.lua) | 53 |
| Salamangreat Sunlight Wolf | `87871125` | [Scripts/c87871125.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87871125.lua) | 52 |
| Rahamu, Envoy of the Sacred Tome | `53904087` | [Scripts/c53904087.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53904087.lua) | 51 |
| S-Force Justify | `35334193` | [Scripts/c35334193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35334193.lua) | 51 |
| Code of Soul | `74652966` | [Scripts/c74652966.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74652966.lua) | 50 |
| Allied Code Talker @Ignister | `39138610` | [Scripts/c39138610.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39138610.lua) | 50 |
| Accesscode Talker | `86066372` | [Scripts/c86066372.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86066372.lua) | 50 |
| Borreload Dragon | `31833038` | [Scripts/c31833038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31833038.lua) | 50 |
| Firewall Dragon Singularity | `21637210` | [Scripts/c21637210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21637210.lua) | 50 |
| Shaddoll Construct | `86938484` | [Scripts/c86938484.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86938484.lua) | 50 |
| Salamangreat Pyro Phoenix | `31313405` | [Scripts/c31313405.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31313405.lua) | 49 |
| Clockwork Knight | `41739381` | [Scripts/c41739381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41739381.lua) | 49 |
| Predaplant Verte Anaconda | `70369116` | [Scripts/c70369116.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70369116.lua) | 49 |
| ...and 108 more |  |  |  |

## Script Examples

### W:P Fancy Ball (`4993187`)

Source: [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua)

```lua
function s.initial_effect(c)
	--link summon
	aux.AddLinkProcedure(c,aux.FilterBoolFunction(Card.IsLinkType,TYPE_EFFECT),2)
	c:EnableReviveLimit()
	--disable
```

### Duel Link Dragon, the Duel Dragon (`60025883`)

Source: [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua)

```lua
end
function c60025883.lcheck(g,lc)
	return g:IsExists(Card.IsLinkType,1,nil,TYPE_SYNCHRO)
end
function c60025883.spcon(e,tp,eg,ep,ev,re,r,rp)
```

### Beyond the Pendulum (`22125101`)

Source: [Scripts/c22125101.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22125101.lua)

```lua
function c22125101.initial_effect(c)
	--link summon
	aux.AddLinkProcedure(c,aux.FilterBoolFunction(Card.IsLinkType,TYPE_EFFECT),2,2,c22125101.lcheck)
	c:EnableReviveLimit()
	--to hand
```
