# Card.IsHasEffect

## Signature

```lua
Card.IsHasEffect(Card c, int code, [int player]) -> Effect,...?
```

## Description

Check if c is affected by the effect type

## Parameters

- `c` `Card`
- `code` `int`
- `player` `int` optional

## Returns

- `Effect`
- `...?` - Effect

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3549`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **223** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsHasEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua) | 78 |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua) | 69 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 68 |
| [Favorite HERO Flame Wingman](/examples/cards/13243124) | `13243124` | [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13243124.lua) | 66 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27693363.lua) | 65 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44509529.lua) | 65 |
| [Dark End Evaporation Dragon](/examples/cards/62002838) | `62002838` | [Scripts/c62002838.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62002838.lua) | 63 |
| [Junoldo the Shadespirit Power Patron](/examples/cards/10266279) | `10266279` | [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10266279.lua) | 62 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62714453.lua) | 62 |
| [Light End Sublimation Dragon](/examples/cards/35614780) | `35614780` | [Scripts/c35614780.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35614780.lua) | 61 |
| [El Shaddoll Meshachrer](/examples/cards/32467459) | `32467459` | [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua) | 61 |
| [Prank-Kids Rocket Ride](/examples/cards/18514525) | `18514525` | [Scripts/c18514525.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18514525.lua) | 61 |
| [Jupredo the Shademachine Power Patron](/examples/cards/43871165) | `43871165` | [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43871165.lua) | 60 |
| D/D Extra Surveyor | `74387963` | [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74387963.lua) | 60 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5148778.lua) | 60 |
| Flame Swordsrealm | `73714736` | [Scripts/c73714736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73714736.lua) | 58 |
| Meteonis Drytron | `22398665` | [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22398665.lua) | 58 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua) | 58 |
| Prank-Kids Bow-Wow-Bark | `43886072` | [Scripts/c43886072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43886072.lua) | 58 |
| Union Activation | `38527680` | [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua) | 57 |
| Ursarctic Grand Chariot | `80086070` | [Scripts/c80086070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80086070.lua) | 57 |
| Lunalight Masquerade | `2344618` | [Scripts/c2344618.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2344618.lua) | 57 |
| Amazoness Secret Arts | `86758746` | [Scripts/c86758746.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86758746.lua) | 57 |
| Nervedo the Shadebeast Power Patron | `17473466` | [Scripts/c17473466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17473466.lua) | 56 |
| ...and 199 more |  |  |  |

## Script Examples

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
function s.getrg(tp,sc)
	local rg=Duel.GetReleaseGroup(tp,true,REASON_SPSUMMON)
	local mrg=rg:Filter(Card.IsHasEffect,nil,EFFECT_EXTRA_RELEASE)
	if mrg:GetCount()>0 then
		return mrg:Filter(s.spfilter,nil,tp,sc)
```

### Accel Synchro Stardust Dragon (`30983281`)

Source: [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua)

```lua
end
function c30983281.excostfilter(c,tp)
	return c:IsAbleToRemoveAsCost() and c:IsHasEffect(84012625,tp)
end
function c30983281.syncheck(g,tp,syncard)
```

### El Shaddoll Apkallone (`50907446`)

Source: [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua)

```lua
	local fc=Duel.GetFieldCard(tp,LOCATION_FZONE,0)
	local exg=nil
	if fc and fc:IsHasEffect(81788994) and fc:IsCanRemoveCounter(tp,0x16,3,REASON_EFFECT) then
		local fe=fc:IsHasEffect(81788994)
		exg=Duel.GetMatchingGroup(c50907446.FShaddollExFilter,tp,0,LOCATION_MZONE,mg,c,fe)
```
