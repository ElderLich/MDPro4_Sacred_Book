# Card.IsAllTypes

## Signature

```lua
Card.IsAllTypes(Card c, int type) -> bool
```

## Description

Checks whether c includes all types in type.

## Parameters

- `c` `Card`
- `type` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3485`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **64** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsAllTypes`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Radiant Typhoon Varuroon, the Marine Eidolon](/examples/cards/39341885) | `39341885` | [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39341885.lua) | 61 |
| [Chef de Nouvelles](/examples/cards/29251488) | `29251488` | [Scripts/c29251488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29251488.lua) | 60 |
| Power Patron DoomZ | `81650695` | [Scripts/c81650695.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81650695.lua) | 58 |
| Dragon Master Magia | `12381100` | [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12381100.lua) | 57 |
| DoomZ XII Zero - Drastea | `92472273` | [Scripts/c92472273.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92472273.lua) | 57 |
| Lunalight Masquerade | `2344618` | [Scripts/c2344618.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2344618.lua) | 57 |
| Zoroa, the Magistus Verethragna | `37260677` | [Scripts/c37260677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37260677.lua) | 57 |
| Darkuriboh | `1035143` | [Scripts/c1035143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1035143.lua) | 55 |
| Cyberse Contract Witch | `37458564` | [Scripts/c37458564.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37458564.lua) | 55 |
| Yummy☆Surprise | `29369059` | [Scripts/c29369059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29369059.lua) | 55 |
| Elfnotes: Rhapsodia of Madness | `24092792` | [Scripts/c24092792.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24092792.lua) | 54 |
| Fydraulis Harmonia | `70088809` | [Scripts/c70088809.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70088809.lua) | 53 |
| Materiactor Meltthrough | `66059345` | [Scripts/c66059345.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66059345.lua) | 53 |
| Sudden Thunder Swamp | `23611122` | [Scripts/c23611122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23611122.lua) | 53 |
| Elfnote Tinia | `59581480` | [Scripts/c59581480.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59581480.lua) | 52 |
| Snake-Eyes Vengeance Dragon | `79415624` | [Scripts/c79415624.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79415624.lua) | 52 |
| Shade the Obscure | `77157846` | [Scripts/c77157846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77157846.lua) | 51 |
| Argostars - Giantslaying | `30964246` | [Scripts/c30964246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30964246.lua) | 51 |
| Black Chaos the Ultimate Magical Swordsman | `98684220` | [Scripts/c98684220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98684220.lua) | 51 |
| Hrimnir the Divine Follower | `49904658` | [Scripts/c49904658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49904658.lua) | 51 |
| Mystic Box of Chaos | `75983808` | [Scripts/c75983808.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75983808.lua) | 49 |
| Nouvelles Recipe Book "Recettes de Nouvellez" | `61944066` | [Scripts/c61944066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61944066.lua) | 49 |
| Skull Archfiend of Chaos | `24088928` | [Scripts/c24088928.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24088928.lua) | 49 |
| Mystical Celtic Sage | `50073633` | [Scripts/c50073633.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50073633.lua) | 49 |
| ...and 40 more |  |  |  |

## Script Examples

### Radiant Typhoon Varuroon, the Marine Eidolon (`39341885`)

Source: [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39341885.lua)

```lua
end
function s.pfilter(c,tp)
	return c:IsAllTypes(TYPE_CONTINUOUS+TYPE_TRAP) and c:IsSetCard(0x1d1)
		and not c:IsForbidden() and c:CheckUniqueOnField(tp)
end
```

### Chef de Nouvelles (`29251488`)

Source: [Scripts/c29251488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29251488.lua)

```lua
end
function s.thfilter(c)
	return not c:IsAllTypes(TYPE_PENDULUM+TYPE_MONSTER) and c:IsSetCard(0x196) and c:IsAbleToHand()
end
function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Power Patron DoomZ (`81650695`)

Source: [Scripts/c81650695.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81650695.lua)

```lua
end
function s.spfilter(c,e,tp,mc)
	return c:IsRank(mc:GetLevel()) and (c:IsSetCard(0x1d2) or c:IsCode(68231287)) and c:IsAllTypes(TYPE_XYZ+TYPE_MONSTER)
		and mc:IsCanBeXyzMaterial(c) and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_XYZ,tp,false,false)
		and Duel.GetLocationCountFromEx(tp,tp,mc,c)>0
```
