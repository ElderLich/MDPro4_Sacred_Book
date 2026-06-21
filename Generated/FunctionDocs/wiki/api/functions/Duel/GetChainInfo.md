# Duel.GetChainInfo

## Signature

```lua
Duel.GetChainInfo(int chainc, ... any) -> ...
```

## Description

返回连锁chainc的信息，如果chainc=0，则返回当前正在处理的连锁的信息
此函数根据传入的参数个数按顺序返回相应数量的返回值参数可以是:
CHAININFO_CHAIN_COUNT               连锁序号
CHAININFO_TRIGGERING_EFFECT         连锁的效果
CHAININFO_TRIGGERING_PLAYER         连锁的玩家
CHAININFO_TRIGGERING_CONTROLER      连锁发生位置所属玩家
CHAININFO_TRIGGERING_LOCATION       连锁发生位置
CHAININFO_TRIGGERING_SEQUENCE       连锁发生的位置的序号
CHAININFO_TARGET_CARDS              连锁的对象卡片组
CHAININFO_TARGET_PLAYER             连锁的对象玩家
CHAININFO_TARGET_PARAM              连锁的对象参数
CHAININFO_DISABLE_REASON            连锁被无效的原因效果
CHAININFO_DISABLE_PLAYER            连锁被无效的原因玩家
CHAININFO_CHAIN_ID                  连锁的唯一标识
CHAININFO_TYPE                      连锁卡片的类型（怪兽·魔法·陷阱）
CHAININFO_EXTTYPE                   连锁卡片的具体类型（例如同调怪兽·永续魔法·反击陷阱）
举例：
Duel.GetChainInfo(0,CHAININFO_TRIGGERING_LOCATION,CHAININFO_TARGET_CARDS)
将会返回当前连锁发生的位置和对象卡

## Parameters

- `chainc` `int`
- `...` `any`

## Returns

- `...`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4947`
