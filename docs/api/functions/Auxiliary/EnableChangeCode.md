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

## Guided Examples

Learn how to use this function in context:

- [Toon Monsters](/learn/toon-monsters)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **111** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.EnableChangeCode) with `Auxiliary.EnableChangeCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78579058.lua) | 1 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41570943.lua) | 1 |
| Supreme King Z-ARC - Synchro Universe | `48654267` | [Scripts/c48654267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48654267.lua) | 1 |
| Gunkan Suship Shari Red | `63748694` | [Scripts/c63748694.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63748694.lua) | 1 |
| Harpie Conductor | `85696777` | [Scripts/c85696777.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85696777.lua) | 1 |
| Buster Blader, the Destruction Swordmaster | `3428069` | [Scripts/c3428069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3428069.lua) | 1 |
| Frightfur Jar | `18138630` | [Scripts/c18138630.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18138630.lua) | 1 |
| Dark Magician of Destruction | `59400890` | [Scripts/c59400890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59400890.lua) | 1 |
| Sea Stealth II | `58203736` | [Scripts/c58203736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58203736.lua) | 1 |
| Armed Dragon Thunder LV5 | `21546416` | [Scripts/c21546416.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21546416.lua) | 1 |
| Avendread Savior | `91420202` | [Scripts/c91420202.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91420202.lua) | 1 |
| Shiranui Style Samsara | `78765160` | [Scripts/c78765160.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78765160.lua) | 1 |
| Perfect Toon World | `7293697` | [Scripts/c7293697.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7293697.lua) | 1 |
| Ruler of the End of the World | `3739500` | [Scripts/c3739500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3739500.lua) | 1 |
| Shiranui Style Solemnity | `40364916` | [Scripts/c40364916.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40364916.lua) | 1 |
| Armed Dragon Thunder LV10 | `58153103` | [Scripts/c58153103.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58153103.lua) | 1 |
| Monstrous Arms of Atlantis | `37092104` | [Scripts/c37092104.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37092104.lua) | 1 |
| Leviathan of Atlantis - Daedalus | `64603351` | [Scripts/c64603351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64603351.lua) | 1 |
| Eldlich the Mad Golden Lord | `74889525` | [Scripts/c74889525.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74889525.lua) | 1 |
| Berfomet the Mythical King of Phantom Beasts | `69601012` | [Scripts/c69601012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69601012.lua) | 1 |
| Wightbaking | `6128460` | [Scripts/c6128460.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6128460.lua) | 1 |
| Fallen Sanctuary | `90312154` | [Scripts/c90312154.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90312154.lua) | 1 |
| Evil Eye of Gorgoneio | `28957126` | [Scripts/c28957126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28957126.lua) | 1 |
| Scarred Dragon Archfiend | `87451661` | [Scripts/c87451661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87451661.lua) | 1 |
| ...and 87 more |  |  |  |

## Script Examples

### Levia-Dragoon - Daedalus (`78579058`)

Source: [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78579058.lua)

```lua
function s.initial_effect(c)
	aux.AddCodeList(c,38391684,22702055)
	aux.EnableChangeCode(c,22702055)
	--link summon
	c:EnableReviveLimit()
```

### Azure Ocean Dragon Lord - Neo-Daedalus Rage (`41570943`)

Source: [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41570943.lua)

```lua
function s.initial_effect(c)
	aux.AddCodeList(c,38391684,22702055)
	aux.EnableChangeCode(c,22702055)
	--link summon
	c:EnableReviveLimit()
```

### Supreme King Z-ARC - Synchro Universe (`48654267`)

Source: [Scripts/c48654267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48654267.lua)

```lua
function c48654267.initial_effect(c)
	aux.AddCodeList(c,13331639)
	aux.EnableChangeCode(c,13331639,LOCATION_MZONE)
	aux.EnablePendulumAttribute(c)
	c:EnableReviveLimit()
```
