# Auxiliary.EnableChangeCode

## Signature

```lua
Auxiliary.EnableChangeCode(Card c, int code, int location, function condition) -> void
```

## Description

Registers code as a listed code for c and gives c an EFFECT_CHANGE_CODE effect with that value.
If location is omitted, monsters use the Monster Zone and non-monsters use the Spell & Trap Zone. If condition is omitted, the code change is always active.

## Parameters

- `c` `Card`
- `code` `int`
- `location` `int`
- `condition` `function`

## Source

- `Utilities/utility.lua:433`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **103** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.EnableChangeCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Supreme King Z-ARC - Synchro Universe | `48654267` | [Scripts/c48654267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48654267.lua) | 54 |
| Gunkan Suship Shari Red | `63748694` | [Scripts/c63748694.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63748694.lua) | 52 |
| Harpie Conductor | `85696777` | [Scripts/c85696777.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85696777.lua) | 50 |
| Buster Blader, the Destruction Swordmaster | `3428069` | [Scripts/c3428069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3428069.lua) | 49 |
| Frightfur Jar | `18138630` | [Scripts/c18138630.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18138630.lua) | 49 |
| Dark Magician of Destruction | `59400890` | [Scripts/c59400890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59400890.lua) | 48 |
| Sea Stealth II | `58203736` | [Scripts/c58203736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58203736.lua) | 46 |
| Armed Dragon Thunder LV5 | `21546416` | [Scripts/c21546416.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21546416.lua) | 45 |
| Avendread Savior | `91420202` | [Scripts/c91420202.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91420202.lua) | 45 |
| Shiranui Style Samsara | `78765160` | [Scripts/c78765160.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78765160.lua) | 45 |
| Toon World the Perfect World | `7293697` | [Scripts/c7293697.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7293697.lua) | 44 |
| Ruler of the End of the World | `3739500` | [Scripts/c3739500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3739500.lua) | 44 |
| Shiranui Style Solemnity | `40364916` | [Scripts/c40364916.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40364916.lua) | 44 |
| Armed Dragon Thunder LV10 | `58153103` | [Scripts/c58153103.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58153103.lua) | 42 |
| Eldlich the Mad Golden Lord | `74889525` | [Scripts/c74889525.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74889525.lua) | 42 |
| Berfomet the Mythical King of Phantom Beasts | `69601012` | [Scripts/c69601012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69601012.lua) | 41 |
| Wightbaking | `6128460` | [Scripts/c6128460.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6128460.lua) | 41 |
| Fallen Sanctuary | `90312154` | [Scripts/c90312154.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90312154.lua) | 40 |
| Evil Eye of Gorgoneio | `28957126` | [Scripts/c28957126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28957126.lua) | 40 |
| Scarred Dragon Archfiend | `87451661` | [Scripts/c87451661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87451661.lua) | 40 |
| Red-Eyes Soul | `6556909` | [Scripts/c6556909.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6556909.lua) | 39 |
| The Bystial Aluber | `45005708` | [Scripts/c45005708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45005708.lua) | 39 |
| Cyber Dragon Sieger | `46724542` | [Scripts/c46724542.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46724542.lua) | 39 |
| Blue-Eyes Alternative White Dragon | `38517737` | [Scripts/c38517737.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38517737.lua) | 39 |
| ...and 79 more |  |  |  |

## Script Examples

### Supreme King Z-ARC - Synchro Universe (`48654267`)

Source: [Scripts/c48654267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48654267.lua)

```lua
function c48654267.initial_effect(c)
	aux.AddCodeList(c,13331639)
	aux.EnableChangeCode(c,13331639,LOCATION_MZONE)
	aux.EnablePendulumAttribute(c)
	c:EnableReviveLimit()
```

### Gunkan Suship Shari Red (`63748694`)

Source: [Scripts/c63748694.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63748694.lua)

```lua
function c63748694.initial_effect(c)
	--change name
	aux.EnableChangeCode(c,24639891,LOCATION_HAND+LOCATION_DECK+LOCATION_MZONE+LOCATION_GRAVE)
	--spsummon
	local e1=Effect.CreateEffect(c)
```

### Harpie Conductor (`85696777`)

Source: [Scripts/c85696777.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85696777.lua)

```lua
	c:EnableReviveLimit()
	--change name
	aux.EnableChangeCode(c,76812113,LOCATION_MZONE+LOCATION_GRAVE)
	--destroy replace
	local e2=Effect.CreateEffect(c)
```
