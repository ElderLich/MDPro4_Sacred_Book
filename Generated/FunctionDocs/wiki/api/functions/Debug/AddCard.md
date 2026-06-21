# Debug.AddCard

## Signature

```lua
Debug.AddCard(int code, int owner, int player, int location, int seq, int pos, [bool proc]) -> Card
```

## Description

添加卡片，将卡号为code的卡片的持有者设置为owner，以表示形式pos放置在player的场上位于location上序号为seq的格子处
proc=true则完成正规召唤程序(即解除苏生限制)

## Parameters

- `code` `int`
- `owner` `int`
- `player` `int`
- `location` `int`
- `seq` `int`
- `pos` `int`
- `proc` `bool` optional - default: false

## Returns

- `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libdebug.cpp:203`
