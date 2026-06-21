# Card.IsCanBeSpecialSummoned

## Signature

```lua
Card.IsCanBeSpecialSummoned(Card c, Effect e, int sumtype, int sumplayer, bool nocheck, bool nolimit, [int sumpos], [int toplayer], [int zone]) -> bool
```

## Description

检查c是否可以被玩家sumplayer用效果e[以sumtype方式和sumpos表示形式]特殊召唤[到玩家 toplayer 的区域zone]
如果nocheck是true则不检查c的召唤条件，如果nolimit是true则不检查c的苏生限制

## Parameters

- `c` `Card`
- `e` `Effect`
- `sumtype` `int`
- `sumplayer` `int`
- `nocheck` `bool`
- `nolimit` `bool`
- `sumpos` `int` optional - default: POS_FACEUP
- `toplayer` `int` optional - default: sumplayer
- `zone` `int` optional - default: 0xff

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3582`
