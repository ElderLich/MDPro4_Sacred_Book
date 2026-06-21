# Duel.ChangePosition

## Signature

```lua
Duel.ChangePosition(Card|Group targets, int au, [int ad], [int du], [int dd], [bool noflip], [bool setavailable]) -> int
```

## Description

改变targets的表示形式返回实际操作的数量，若只有2个参数，则不管什么表示形式，都变成 第二个参数 代表的形式
表侧攻击表示 = au
里侧攻击表示 = ad
表侧守备表示 = du
里侧守备表示 = dd
如果noflip=true则不触发反转效果（但会触发反转时的诱发效果）
如果setavailable=true则对象之后变成里侧也发动反转效果

## Parameters

- `targets` `Card|Group`
- `au` `int`
- `ad` `int` optional - default: au
- `du` `int` optional - default: au
- `dd` `int` optional - default: au
- `noflip` `bool` optional - default: false
- `setavailable` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4880`
