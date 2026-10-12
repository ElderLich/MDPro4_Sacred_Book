# RushDuel.EnableContactFusion

Alias: `RD.EnableContactFusion`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.EnableContactFusion(any card, any desc) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可以进行接触融合术
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:253`

```lua
function RushDuel.EnableContactFusion(card, desc)
    local e = Effect.CreateEffect(card)
    e:SetDescription(desc)
    e:SetType(EFFECT_TYPE_FIELD)
    e:SetCode(EFFECT_SPSUMMON_PROC)
    e:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e:SetRange(LOCATION_EXTRA)
    e:SetCondition(RushDuel.ContactFusionCondition)
    e:SetTarget(RushDuel.ContactFusionTarget)
    e:SetOperation(RushDuel.ContactFusionOperation)
    e:SetValue(SUMMON_TYPE_FUSION)
    card:RegisterEffect(e)
    return e
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **41** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.EnableContactFusion) with `RushDuel.EnableContactFusion`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Voidvelg Beyond Probe | `120300031` | [Rush/Scripts/c120300031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300031.lua) | 1 |
| Dark Matter Transcend Dragon | `120272044` | [Rush/Scripts/c120272044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272044.lua) | 1 |
| Harpie Lady Feather Duster | `120279002` | [Rush/Scripts/c120279002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120279002.lua) | 1 |
| Harpie Regina Splendid Armor | `120279004` | [Rush/Scripts/c120279004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120279004.lua) | 1 |
| Whispurring Fairy | `120277047` | [Rush/Scripts/c120277047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277047.lua) | 1 |
| Excutie Leya Frontier | `120293069` | [Rush/Scripts/c120293069.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293069.lua) | 1 |
| Dark Matter Requiem | `120264039` | [Rush/Scripts/c120264039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264039.lua) | 1 |
| Tune Ophiclaymore the Music Princess | `120290031` | [Rush/Scripts/c120290031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290031.lua) | 1 |
| Dark Matter Requiem Omega | `120264040` | [Rush/Scripts/c120264040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264040.lua) | 1 |
| Celeb Rose Incognito Magician | `120272041` | [Rush/Scripts/c120272041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272041.lua) | 1 |
| Bikuribot | `120109043` | [Rush/Scripts/c120109043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109043.lua) | 1 |
| Roadstar Gladimagia | `120272042` | [Rush/Scripts/c120272042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272042.lua) | 1 |
| Voidvelg Forbidden Requiem | `120277044` | [Rush/Scripts/c120277044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277044.lua) | 1 |
| Harpie Lady 3 &amp; 1 | `120285044` | [Rush/Scripts/c120285044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285044.lua) | 1 |
| Pupating Larvae Moth | `120298033` | [Rush/Scripts/c120298033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298033.lua) | 1 |
| Blue-Fang Concurrent Burst Dragon | `120109046` | [Rush/Scripts/c120109046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109046.lua) | 1 |
| Lightclad Dragon Egg | `120304041` | [Rush/Scripts/c120304041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304041.lua) | 1 |
| Harpie Cara Charming Dress | `120279005` | [Rush/Scripts/c120279005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120279005.lua) | 1 |
| Harpie Cielo Light Skirt | `120283039` | [Rush/Scripts/c120283039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120283039.lua) | 1 |
| Duordoll the Adorable Star | `120294043` | [Rush/Scripts/c120294043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294043.lua) | 1 |
| Dark Matter Emperor Dragon | `120264038` | [Rush/Scripts/c120264038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264038.lua) | 1 |
| Excutie Lumière Frontier | `120264048` | [Rush/Scripts/c120264048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264048.lua) | 1 |
| Draco the Doubly Tiny | `120294039` | [Rush/Scripts/c120294039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294039.lua) | 1 |
| Elemental HERO Earth Neos | `120306068` | [Rush/Scripts/c120306068.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306068.lua) | 1 |
| ...and 17 more |  |  |  |

## Script Examples

### Voidvelg Beyond Probe (`120300031`)

Source: [Rush/Scripts/c120300031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300031.lua)

```lua
	RD.AddFusionProcedure(c,list[1],cm.matfilter)
	--Contact Fusion
	RD.EnableContactFusion(c,aux.Stringid(m,0))
	--Destroy
	local e1=Effect.CreateEffect(c)
```

### Dark Matter Transcend Dragon (`120272044`)

Source: [Rush/Scripts/c120272044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272044.lua)

```lua
	RD.AddFusionProcedure(c,list[1],list[2],cm.matfilter)
	--Contact Fusion
	RD.EnableContactFusion(c,aux.Stringid(m,0))
	--Discard Deck
	local e1=Effect.CreateEffect(c)
```

### Harpie Lady Feather Duster (`120279002`)

Source: [Rush/Scripts/c120279002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120279002.lua)

```lua
	RD.SetFusionMaterial(c,{list[1]},2,2)
	--Contact Fusion
	RD.EnableContactFusion(c,aux.Stringid(m,0))
	--Change Code
	local e1=Effect.CreateEffect(c)
```
