# Debug.SetPlayerInfo

## Signature

```lua
Debug.SetPlayerInfo(int playerid, int lp, int startcount, int drawcount) -> void
```

## Description

设置玩家信息，基本分为lp，初始手卡为startcount张，每回合抽drawcount张
在残局当中， playerid ：自己=0,对方=1

## Parameters

- `playerid` `int`
- `lp` `int`
- `startcount` `int`
- `drawcount` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libdebug.cpp:204`
