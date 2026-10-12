# Duel.IsExistingMatchingCard

## Signature

```lua
Duel.IsExistingMatchingCard([function|nil f], int player, int s, int o, int count, [Card|Group|nil ex], ... any) -> bool
```

## Description

Checks whether the specified locations contain at least count cards that satisfy filter f and are not excluded by ex.
s is player's own location mask and o is the opponent's location mask from that player's viewpoint. Extra arguments after ex are passed to f.

## How To Use It

Use this for activation checks that only need to know whether matching cards exist.

The filter receives each candidate card first, followed by any extra arguments after `ex`:

```lua
function s.filter(c,e,tp)
    return c:IsFaceup() and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

if chk==0 then
    return Duel.IsExistingMatchingCard(s.filter,tp,LOCATION_GRAVE,0,1,nil,e,tp)
end
```

Use `Duel.IsExistingTarget` instead when the card must become an official target of the activating effect.

## Parameters

- `f` `function|nil` optional
- `player` `int`
- `s` `int`
- `o` `int`
- `count` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4972`

## Guided Examples

Learn how to use this function in context:

- [Methods for Affecting Cards](/learn/affecting-cards)
- [Filters, Card Objects, and Group Objects](/learn/filters-and-groups)
- [First Scripts To Study](/learn/first-scripts)
- [Min/Max Stat Card Selection](/learn/min-max-stat-selection)
- [Selection And Group Handling](/learn/selection-and-group-handling)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **7601** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.IsExistingMatchingCard) with `Duel.IsExistingMatchingCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62091148.lua) | 3 |
| [Astrograph Sorcerer, the Starfrost Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua) | 1 |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74631897.lua) | 4 |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55795155.lua) | 2 |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua) | 2 |
| [Lady's Dragonmaid](/examples/cards/48658295) | `48658295` | [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48658295.lua) | 3 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua) | 2 |
| [Eternal Favorite](/examples/cards/87532344) | `87532344` | [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87532344.lua) | 5 |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35167375.lua) | 3 |
| [Astrograph Sorcerer](/examples/cards/76794549) | `76794549` | [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76794549.lua) | 4 |
| [Spellbook of the Grand Circle](/examples/cards/11911336) | `11911336` | [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11911336.lua) | 2 |
| [Ultra Polymerization](/examples/cards/76647978) | `76647978` | [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76647978.lua) | 2 |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59255742.lua) | 1 |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30983281.lua) | 5 |
| [Melffy Playtime Surprise](/examples/cards/58036097) | `58036097` | [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58036097.lua) | 3 |
| [Ashtraja Susanoo](/examples/cards/17020474) | `17020474` | [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17020474.lua) | 2 |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92171126.lua) | 4 |
| [Destiny HERO - Destro-Dogma](/examples/cards/25158975) | `25158975` | [Scripts/c25158975.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25158975.lua) | 3 |
| [Yomagna the Fire Phantom](/examples/cards/17350692) | `17350692` | [Scripts/c17350692.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17350692.lua) | 2 |
| [Fiendsmith's Sequence](/examples/cards/49867899) | `49867899` | [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49867899.lua) | 2 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11852093.lua) | 2 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50907446.lua) | 1 |
| [Mementotlan Fusion](/examples/cards/66518509) | `66518509` | [Scripts/c66518509.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66518509.lua) | 3 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24166324.lua) | 2 |
| ...and 7577 more |  |  |  |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
		e2:SetReset(RESET_EVENT+RESETS_STANDARD)
		c:RegisterEffect(e2)
		if Duel.IsExistingMatchingCard(s.posfilter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil) and Duel.SelectYesNo(tp,aux.Stringid(id,2)) then
			Duel.BreakEffect()
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
```

### Astrograph Sorcerer, the Starfrost Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
	local c=e:GetHandler()
	if chk==0 then return c:IsDestructable()
		and Duel.IsExistingMatchingCard(s.pfilter,tp,LOCATION_HAND+LOCATION_DECK,0,1,nil,tp) end
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,c,1,0,0)
end
```

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
	if Duel.GetFlagEffect(tp,id)>0 then return false end
	local rg=s.getrg(tp,c)
	return rg:GetCount()>0 and Duel.IsExistingMatchingCard(s.cfilter,tp,LOCATION_HAND,0,1,nil)
end
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk,c)
```
