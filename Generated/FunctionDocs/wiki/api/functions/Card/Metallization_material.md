# Card.Metallization_material

## Signature

```lua
Card.Metallization_material(int ft, int lv, int race, int att) -> bool
```

## Description

Card-script callback used by the Metalmorph Summon procedure to test the released monster's properties.
Eligible monster scripts assign this callback on their card table. The procedure in `Scripts/c89812483.lua` passes the material-availability flag plus the released monster's Level, Race, and Attribute.

## Parameters

- `ft` `int` - Material-availability flag: 1 when a released monster is being checked, otherwise 0.
- `lv` `int` - Level of the released monster.
- `race` `int` - Race mask of the released monster.
- `att` `int` - Attribute mask of the released monster.

## Returns

- `bool` - True if this monster accepts those material properties for the procedure.

## Source

- `Define/def.lua:90`
