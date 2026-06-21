# Duel.SelectTribute

## Signature

```lua
Duel.SelectTribute(int player, Card c, int min, int max, [Group|nil mg], [int|nil toplayer]) -> Group
```

## Description

Let the player player \[from the mg\] choose the min-max sacrifices that are normally used to summon c, ex = true to allow the monster on the other side of the field (the wing of the Sun God-Sphere)

## Parameters

- `player` `int`
- `c` `Card`
- `min` `int`
- `max` `int`
- `mg` `Group|nil` optional
- `toplayer` `int|nil` optional - default: c:GetControler()

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4983`
