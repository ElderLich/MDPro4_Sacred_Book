# Auxiliary.AddEquipSpellEffect

## Signature

```lua
Auxiliary.AddEquipSpellEffect(Card c, bool is_self, bool is_opponent, function filter, function|nil eqlimit, [bool pause], [bool skip_target]) -> Effect
```

## Description

Creates an Equip Spell activation effect for c and registers the matching EFFECT_EQUIP_LIMIT.
The activation effect is returned; when pause is true it is created but not registered on c.
Use this for ordinary Equip Spells. Write the target and operation manually when the card equips after another action or needs extra state.

## How To Use It

Use this for the normal Equip Spell activation shape: target a face-up monster, equip the handler during resolution, and register the matching `EFFECT_EQUIP_LIMIT` on the Equip Card.

```lua
aux.AddEquipSpellEffect(c,true,true,s.eqfilter,s.eqlimit)
```

Use a manual activation instead when the card Special Summons first, equips cards from another location, equips several cards at once, or needs extra state before `Duel.Equip`.

## Related Functions

- [Auxiliary.EquipSpellTarget](/api/functions/Auxiliary/EquipSpellTarget)
- [Auxiliary.EquipSpellOperation](/api/functions/Auxiliary/EquipSpellOperation)
- [Duel.Equip](/api/functions/Duel/Equip)
- [Card.CheckEquipTarget](/api/functions/Card/CheckEquipTarget)

## Parameters

- `c` `Card`
- `is_self` `bool`
- `is_opponent` `bool`
- `filter` `function`
- `eqlimit` `function|nil`
- `pause` `bool` optional - default: false
- `skip_target` `bool` optional - default: false

## Returns

- `Effect` - Created activation effect.

## Source

- `Utilities/utility.lua:1883`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddEquipSpellEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Tails of the Fairy Tails | `82119326` | [Scripts/c82119326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82119326.lua) | 57 |
| DoomZ Command "D.O.O.M.D.U.R.G." | `68831625` | [Scripts/c68831625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68831625.lua) | 49 |
| Cursed Copycat Noble Arms | `23249029` | [Scripts/c23249029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23249029.lua) | 46 |
| Reincarnation Unveiling Mail | `68663427` | [Scripts/c68663427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68663427.lua) | 45 |
| DoomZ Command "A.D.R.A.S.T.E.I.A." | `84054556` | [Scripts/c84054556.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84054556.lua) | 45 |
| Xyz Lay | `43150717` | [Scripts/c43150717.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43150717.lua) | 38 |
| Orichalcos Sword of Sealing | `847217` | [Scripts/c847217.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c847217.lua) | 38 |
| Dragon Treasure | `1435851` | [Scripts/c1435851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1435851.lua) | 17 |
| Ballista of Rampart Smashing | `242146` | [Scripts/c242146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c242146.lua) | 13 |
| WINDS OF VICTORY | `37301660` | [Scripts/c37301660.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37301660.lua) | 7 |

## Script Examples

### Tails of the Fairy Tails (`82119326`)

Source: [Scripts/c82119326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82119326.lua)

```lua
function s.initial_effect(c)
	aux.AddCodeList(c,19144623)
	aux.AddEquipSpellEffect(c,true,true,Card.IsFaceup,nil)
	--Atk up
	local e1=Effect.CreateEffect(c)
```

### DoomZ Command "D.O.O.M.D.U.R.G." (`68831625`)

Source: [Scripts/c68831625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68831625.lua)

```lua
local s,id,o=GetID()
function s.initial_effect(c)
	aux.AddEquipSpellEffect(c,true,true,Card.IsFaceup,nil)
	--dam
	local e1=Effect.CreateEffect(c)
```

### Cursed Copycat Noble Arms (`23249029`)

Source: [Scripts/c23249029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23249029.lua)

```lua
local s,id,o=GetID()
function s.initial_effect(c)
	aux.AddEquipSpellEffect(c,true,true,Card.IsFaceup,nil)
	--Atk Change
	local e1=Effect.CreateEffect(c)
```
