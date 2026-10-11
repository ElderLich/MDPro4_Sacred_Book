# Card.AddMonsterAttribute

## Signature

```lua
Card.AddMonsterAttribute(Card c, int type, [int attribute], [int race], [int level], [int atk], [int def]) -> void
```

## Description

Adds temporary monster properties to c through effects.
The binding clears STATUS_NO_LEVEL, applies EFFECT_PRE_MONSTER with type, and applies Attribute, Race, Level, base ATK, and base DEF changes for nonzero supplied values.

## Parameters

- `c` `Card`
- `type` `int`
- `attribute` `int` optional - default: 0
- `race` `int` optional - default: 0
- `level` `int` optional - default: 0
- `atk` `int` optional - default: 0
- `def` `int` optional - default: 0

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3705`
