# Rush Duel constants

These values belong to the Rush bootstrap. `TYPE_LEGEND = 0x8` and `TYPE_MAXIMUM = 0x8000` overlap standard type bits; do not combine the two environments.

## CARD_CODE_OTS

`CARD_CODE_OTS = 120000010`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
外宇宙
```

## RACE_MAGICALKNIGHT

`RACE_MAGICALKNIGHT = 0x4000000`

Magical Knight race.

Upstream comment:

```text
魔导骑士
```

## RACE_HYDRAGON

`RACE_HYDRAGON = 0x8000000`

High Dragon race.

Upstream comment:

```text
多头龙
```

## RACE_OMEGAPSYCHO

`RACE_OMEGAPSYCHO = 0x10000000`

Omega Psychic race.

Upstream comment:

```text
欧米茄念动力
```

## RACE_CELESTIALWARRIOR

`RACE_CELESTIALWARRIOR = 0x20000000`

Celestial Warrior race.

Upstream comment:

```text
天界战士
```

## RACE_GALAXY

`RACE_GALAXY = 0x40000000`

Galaxy race.

Upstream comment:

```text
银河
```

## RACE_CYBORG

`RACE_CYBORG = 0x80000000`

Cyborg race.

Upstream comment:

```text
电子人
```

## RACE_ALL

`RACE_ALL = 0xffffffff`

All 32 race bits used by this Rush helper snapshot.

## EFFECT_LEGEND_CARD

`EFFECT_LEGEND_CARD = 120000000`

Custom Rush Legend marker, separate from the printed Legend type bit.

Upstream comment:

```text
传说卡标识 (改变卡名不影响)
```

## EFFECT_CANNOT_SINGLE_TRIBUTE

`EFFECT_CANNOT_SINGLE_TRIBUTE = 120170045`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
监狱岛 大姐头巨岩 (与下面的效果结合变成不能上级召唤)
```

## EFFECT_CANNOT_DOUBLE_TRIBUTE

`EFFECT_CANNOT_DOUBLE_TRIBUTE = 120120029`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
魔将 雅灭鲁拉 (不能使用：双重解放)
```

## EFFECT_PLAYER_CANNOT_ATTACK

`EFFECT_PLAYER_CANNOT_ATTACK = 120155054`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
幻刃封锁 (对方不能攻击时不能发动)
```

## EFFECT_PLAYER_RACE_CANNOT_ATTACK

`EFFECT_PLAYER_RACE_CANNOT_ATTACK = 120155055`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
幻刃封锁 (不能选择不能攻击的种族)
```

## EFFECT_PLAYER_CANNOT_ACTIVATE_TRAP

`EFFECT_PLAYER_CANNOT_ACTIVATE_TRAP = 120247013`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
三角神迷火花 (整个回合不能发动陷阱)
```

## EFFECT_PLAYER_CANNOT_ACTIVATE_TRAP_BATTLE

`EFFECT_PLAYER_CANNOT_ACTIVATE_TRAP_BATTLE = 120261022`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
暗物质人偶·水母 (战斗阶段不能发动陷阱)
```

## EFFECT_ATTACK_NOT_CHAIN_TRAP

`EFFECT_ATTACK_NOT_CHAIN_TRAP = 120140004`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
不许始末战士 (攻击宣言时, 对方不能把陷阱卡发动)
```

## EFFECT_DOUBLE_FUSION_MATERIAL

`EFFECT_DOUBLE_FUSION_MATERIAL = 120252004`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
青眼幻像龙 (作为2只数量的融合术素材)
```

## EFFECT_ONLY_FUSION_SUMMON

`EFFECT_ONLY_FUSION_SUMMON = 120263031`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
只能融合召唤 (奇迹融合)
```

## EFFECT_MAXIMUM_MODE

`EFFECT_MAXIMUM_MODE = 120272058`

Custom Rush marker for Maximum-mode behavior; interpreted by the Rush helper layer.

Upstream comment:

```text
通过效果变成极大模式 (时间机器)
```

## EFFECT_CANNOT_TO_HAND_EFFECT

`EFFECT_CANNOT_TO_HAND_EFFECT = 120274001`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
不会因效果回到手卡
```

## EFFECT_CANNOT_TO_DECK_EFFECT

`EFFECT_CANNOT_TO_DECK_EFFECT = 120274002`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
不会因效果回到卡组·额外卡组
```

## EFFECT_CANNOT_CHANGE_POSITION_EFFECT

`EFFECT_CANNOT_CHANGE_POSITION_EFFECT = 120277011`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
不会因效果改变表示形式
```

## EFFECT_NO_COST_SEND_HAND_TO_GRAVE

`EFFECT_NO_COST_SEND_HAND_TO_GRAVE = 120294004`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
不需要支付"把手卡送去墓地"的代价
```

## EFFECT_CANNOT_BE_RITUAL_MATERIAL

`EFFECT_CANNOT_BE_RITUAL_MATERIAL = 120294063`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
不能作为仪式术召唤的素材
```

## EFFECT_RITUAL_MATERIAL

`EFFECT_RITUAL_MATERIAL = 120300052`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
额外的仪式素材
```

## EFFECT_UNION_FUSION_MATERIAL

`EFFECT_UNION_FUSION_MATERIAL = 120305005`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
XY-神龙炮 (作为2只不同卡名的融合术素材)
```

## EFFECT_UNION_TARGET

`EFFECT_UNION_TARGET = 120306017`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
同盟怪兽的装备要求
```

## FLAG_SUMMON_TURN

`FLAG_SUMMON_TURN = 120000011`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
召唤·特殊召唤的回合
```

## FLAG_FLIP_TURN

`FLAG_FLIP_TURN = 120000012`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
反转的回合
```

## FLAG_SUMMON_MAIN_PHASE

`FLAG_SUMMON_MAIN_PHASE = 120000013`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
召唤·特殊召唤的主要阶段
```

## FLAG_FLIP_MAIN_PHASE

`FLAG_FLIP_MAIN_PHASE = 120000014`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
反转的主要阶段
```

## FLAG_ATTACK_ANNOUNCED

`FLAG_ATTACK_ANNOUNCED = 120000021`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
已经进行了攻击宣言, 不能向怪兽攻击的效果失效
```

## FLAG_ATTACH_EFFECT

`FLAG_ATTACH_EFFECT = 120000022`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
通过效果赋予的效果, 不能重复叠加
```

## FLAG_CANNOT_ATTACK_NEXT_TURN

`FLAG_CANNOT_ATTACK_NEXT_TURN = 120231059`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
下个回合不能攻击
```

## FLAG_CANNOT_ATTACK_UNTIL_NEXT_TURN

`FLAG_CANNOT_ATTACK_UNTIL_NEXT_TURN = 120247006`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
直到下个回合, 不能攻击
```

## FLAG_HAS_DRAW_IN_MAIN_PHASE

`FLAG_HAS_DRAW_IN_MAIN_PHASE = 120261037`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
已在主要阶段抽卡
```

## FLAG_HAS_DRAW_IN_TURN

`FLAG_HAS_DRAW_IN_TURN = 120294034`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
已在这个回合抽卡
```

## FLAG_SKIP_MAIN_PHASE

`FLAG_SKIP_MAIN_PHASE = 120306067`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
跳过主要阶段, 部分陷阱卡不能发动
```

## FLAG_MAX_ATTACK_TWICE_NEXT_TURN

`FLAG_MAX_ATTACK_TWICE_NEXT_TURN = 120285044`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
下个回合, 对方最多攻击2次
```

## HINTMSG_MAXSUMMON

`HINTMSG_MAXSUMMON = Auxiliary.Stringid(120000000, 0)`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
极大召唤
```

## HINTMSG_MAXMATERIAL

`HINTMSG_MAXMATERIAL = Auxiliary.Stringid(120000000, 1)`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
请选择要极大召唤的怪兽(3只)
```

## HINTMSG_FUSION_MATERIAL

`HINTMSG_FUSION_MATERIAL = Auxiliary.Stringid(120000000, 2)`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
请选择要作为融合术召唤的素材的卡
```

## HINTMSG_RITUAL_MATERIAL

`HINTMSG_RITUAL_MATERIAL = Auxiliary.Stringid(120000000, 3)`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
请选择要作为仪式术召唤的素材的卡
```

## HINTMSG_OPERATE_COUNT

`HINTMSG_OPERATE_COUNT = Auxiliary.Stringid(120000000, 4)`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
请选择要操作的数量
```

## HINTMSG_ANNOUNCE_MONSTER

`HINTMSG_ANNOUNCE_MONSTER = Auxiliary.Stringid(120000001, 0)`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
宣言常规怪兽
```

## HINTMSG_ANNOUNCE_LEGEND

`HINTMSG_ANNOUNCE_LEGEND = Auxiliary.Stringid(120000001, 1)`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
宣言传说怪兽
```

## HINTMSG_SUMMON_TURN

`HINTMSG_SUMMON_TURN = Auxiliary.Stringid(120000002, 0)`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
在这个回合召唤
```

## HINTMSG_SPSUMMON_TURN

`HINTMSG_SPSUMMON_TURN = Auxiliary.Stringid(120000002, 1)`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
在这个回合特殊召唤
```

## HINTMSG_FILP_TURN

`HINTMSG_FILP_TURN = 1071`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
在这个回合反转
```

## HINTMSG_EFFECT_USED

`HINTMSG_EFFECT_USED = Auxiliary.Stringid(120000002, 2)`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
已使用过效果
```

## TYPE_LEGEND

`TYPE_LEGEND = 0x8`

Rush Legend type bit. The value 0x8 has a different meaning in standard formats; use only with Rush data and helpers.

Upstream comment:

```text
传说卡
```

## TYPE_MAXIMUM

`TYPE_MAXIMUM = 0x8000`

Rush Maximum monster type bit. The value 0x8000 overlaps the standard Token bit; use only with Rush data and helpers.

Upstream comment:

```text
极大怪兽
```

## SUMMON_TYPE_MAXIMUM

`SUMMON_TYPE_MAXIMUM = 0x4a000000`

Summon-type identifier used by the pinned Rush Maximum procedure.

Upstream comment:

```text
极大召唤
```

## RITUAL_ORIGINAL_LEVEL_EQUAL

`RITUAL_ORIGINAL_LEVEL_EQUAL = 1`

Ritual material comparison mode: original Level, exact requirement.

## RITUAL_ORIGINAL_LEVEL_GREATER

`RITUAL_ORIGINAL_LEVEL_GREATER = 2`

Ritual material comparison mode: original Level, at least the requirement.

## RITUAL_CURRENT_LEVEL_EQUAL

`RITUAL_CURRENT_LEVEL_EQUAL = 3`

Ritual material comparison mode: current Level, exact requirement.

## RITUAL_CURRENT_LEVEL_GREATER

`RITUAL_CURRENT_LEVEL_GREATER = 4`

Ritual material comparison mode: current Level, at least the requirement.

## RITUAL_ORIGINAL_ATTACK_EQUAL

`RITUAL_ORIGINAL_ATTACK_EQUAL = 5`

Ritual material comparison mode: original/base ATK, exact requirement.

## RITUAL_ORIGINAL_ATTACK_GREATER

`RITUAL_ORIGINAL_ATTACK_GREATER = 6`

Ritual material comparison mode: original/base ATK, at least the requirement.

## RITUAL_CURRENT_ATTACK_EQUAL

`RITUAL_CURRENT_ATTACK_EQUAL = 7`

Ritual material comparison mode: current ATK, exact requirement.

## RITUAL_CURRENT_ATTACK_GREATER

`RITUAL_CURRENT_ATTACK_GREATER = 8`

Ritual material comparison mode: current ATK, at least the requirement.

## SUMMON_VALUE_ZERO

`SUMMON_VALUE_ZERO = 0x20`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
不用解放的妥协召唤
```

## SUMMON_VALUE_ONE

`SUMMON_VALUE_ONE = 0x40`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
解放1只的妥协召唤
```

## SUMMON_VALUE_TWO

`SUMMON_VALUE_TWO = 0x80`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
解放2只的妥协召唤
```

## SUMMON_VALUE_THREE

`SUMMON_VALUE_THREE = 0x100`

Rush-specific constant; see the upstream source comment.

Upstream comment:

```text
解放3只的妥协召唤
```
