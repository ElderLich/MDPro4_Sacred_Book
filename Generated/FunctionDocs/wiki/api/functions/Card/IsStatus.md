# Card.IsStatus

## Signature

```lua
Card.IsStatus(Card c, int status) -> bool
```

## Description

Checks whether c currently has at least one status flag from status.
Common legality checks use this for temporary engine states such as STATUS_BATTLE_DESTROYED before allowing a Damage Step Quick Effect.

## Parameters

- `c` `Card` - Card whose current status flags are checked.
- `status` `int` - Status flag or combined status mask, such as STATUS_BATTLE_DESTROYED.

## Returns

- `bool` - true if c has any flag included in status.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3559`
