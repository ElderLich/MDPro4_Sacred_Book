# Duel.SetOperationInfo

## Signature

```lua
Duel.SetOperationInfo(int chainc, int category, [Card|Group|nil|0 targets], int count, int target_player, int target_param) -> void
```

## Description

操作信息：效果处理中确定要处理的分类
比如潜行狙击手需要设置CATEGORY_DICE，但是不能设置CATEGORY_DESTROY，因为不确定
对于破坏效果，targets需要设置成发动时可能成为连锁的影响对象的卡，
并设置count为发动时确定的要处理的卡的数量
比如黑洞发动时，targets需要设定为场上的所有怪兽，count设置成场上的怪的数量
对于需要移动卡片位置的CATEGORY_SPECIAL_SUMMON,CATEGORY_TOHAND,CATEGORY_TODECK等分类，
如果要处理的卡是确定的（比如取对象），则设置targets为这些卡，count为数量，
如果要处理的卡是不确定的（效果处理时才能确定，一般是不取对象的效果），
则设置targets为nil，count为预计要处理的卡的数量，
target_player为预计要处理的卡的持有者（不确定就为0）
target_param为预计要处理的卡的位置
例如增援：SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
操作信息用于很多效果的发动的检测，例如星尘龙，王家长眠之谷等
设置连锁chainc的category分类的操作信息， chainc=0 则是表示当前连锁

## Parameters

- `chainc` `int`
- `category` `int`
- `targets` `Card|Group|nil|0` optional
- `count` `int`
- `target_player` `int`
- `target_param` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5008`
