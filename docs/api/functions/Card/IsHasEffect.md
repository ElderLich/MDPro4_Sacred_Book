# Card.IsHasEffect

## Signature

```lua
Card.IsHasEffect(Card c, int code, [int player]) -> Effect|nil,... Effect
```

## Description

Returns the effects currently affecting c with effect code code, or nil if none match.
When player is supplied, only effects whose count limit can still be used by that player are returned. Multiple matching effects are returned as multiple Lua return values.

## Parameters

- `c` `Card`
- `code` `int`
- `player` `int` optional

## Returns

- `Effect|nil`
- `... Effect` - Additional matching effects, if any.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3604`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **230** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsHasEffect) with `Card.IsHasEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74631897.lua) | 1 |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua) | 3 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua) | 3 |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30983281.lua) | 2 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50907446.lua) | 4 |
| [Favorite HERO Flame Wingman](/examples/cards/13243124) | `13243124` | [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13243124.lua) | 1 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27693363.lua) | 4 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44509529.lua) | 2 |
| [Dark End Evaporation Dragon](/examples/cards/62002838) | `62002838` | [Scripts/c62002838.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62002838.lua) | 1 |
| [Junoldo the Shadespirit Power Patron](/examples/cards/10266279) | `10266279` | [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10266279.lua) | 2 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62714453.lua) | 4 |
| [Light End Sublimation Dragon](/examples/cards/35614780) | `35614780` | [Scripts/c35614780.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35614780.lua) | 1 |
| El Shaddoll Meshachrer | `32467459` | [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c32467459.lua) | 8 |
| Prank-Kids Rocket Ride | `18514525` | [Scripts/c18514525.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18514525.lua) | 3 |
| Jupredo the Shademachine Power Patron | `43871165` | [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43871165.lua) | 2 |
| D/D Extra Surveyor | `74387963` | [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74387963.lua) | 1 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5148778.lua) | 1 |
| Flame Swordsrealm | `73714736` | [Scripts/c73714736.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73714736.lua) | 1 |
| Meteonis Drytron | `22398665` | [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22398665.lua) | 1 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93053159.lua) | 2 |
| Prank-Kids Bow-Wow-Bark | `43886072` | [Scripts/c43886072.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43886072.lua) | 2 |
| Union Activation | `38527680` | [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38527680.lua) | 7 |
| Ursarctic Grand Chariot | `80086070` | [Scripts/c80086070.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80086070.lua) | 4 |
| Lunalight Masquerade | `2344618` | [Scripts/c2344618.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2344618.lua) | 2 |
| ...and 206 more |  |  |  |

## Script Examples

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
function s.getrg(tp,sc)
	local rg=Duel.GetReleaseGroup(tp,true,REASON_SPSUMMON)
	local mrg=rg:Filter(Card.IsHasEffect,nil,EFFECT_EXTRA_RELEASE)
	if mrg:GetCount()>0 then
		return mrg:Filter(s.spfilter,nil,tp,sc)
```

### Levia-Dragoon - Daedalus (`78579058`)

Source: [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua)

```lua
	if c:IsOnField() and c:IsFacedown() then return false end
	if not c:IsCanBeLinkMaterial(lc) or f and not f(c) then return false end
	local le={c:IsHasEffect(EFFECT_EXTRA_LINK_MATERIAL,tp)}
	for _,te in pairs(le) do
		local tf=te:GetValue()
```

### Azure Ocean Dragon Lord - Neo-Daedalus Rage (`41570943`)

Source: [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua)

```lua
	if c:IsOnField() and c:IsFacedown() then return false end
	if not c:IsCanBeLinkMaterial(lc) or f and not f(c) then return false end
	local le={c:IsHasEffect(EFFECT_EXTRA_LINK_MATERIAL,tp)}
	for _,te in pairs(le) do
		local tf=te:GetValue()
```
