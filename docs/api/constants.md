# Constants

Generated from `Utilities/constant.lua`, with English comments carried forward from the project cache where possible.

## Min/Max Values

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `MIN_ID` | `128` | 4 digits, by DataManager::GetDesc() | 0x80, by DataManager::GetDesc() |
| `MAX_ID` | `268435455` | 28 bits, by DataManager::GetDesc() | 28 bits, by DataManager::GetDesc() |
| `MAX_COUNTER` | `65535` | max number for adding/removing counters, by card::add_counter(), field::remove_counter() | max number for adding/removing counters, by card::add_counter(), field::remove_counter() |
| `MAX_PARAMETER` | `0xffff` | Maximum parameter value |  |
| `MAX_XYZ_LEVEL` | `0x0fff` | Maximum Xyz Level value |  |

## Locations

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `LOCATION_DECK` | `0x01` | Deck | 卡组 |
| `LOCATION_HAND` | `0x02` | Hand | 手牌 |
| `LOCATION_MZONE` | `0x04` | Monster Zone | 主要怪兽区(0-4)+额外怪兽区(5-6) |
| `LOCATION_SZONE` | `0x08` | Spell & Trap Zone (0-4) + Field Zone (5) | 魔陷区(0-4)+场地区(5) |
| `LOCATION_GRAVE` | `0x10` | Graveyard | 墓地 |
| `LOCATION_REMOVED` | `0x20` | Banished Zone | 除外区 |
| `LOCATION_EXTRA` | `0x40` | Extra Deck | 额外 |
| `LOCATION_OVERLAY` | `0x80` | Xyz Material | 超量素材 |
| `LOCATION_ONFIELD` | `0x0c` | Field (LOCATION_MZONE + LOCATION_SZONE) | 场上（LOCATION_MZONE+LOCATION_SZONE） |

## Locations (for redirect)

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `LOCATION_DECKBOT` | `0x10001` | Return to the bottom of the Deck | 弹回卡组底部 |
| `LOCATION_DECKSHF` | `0x20001` | Return to the Deck and shuffle | 弹回卡组并洗牌 |

## Sequences (for Duel.SendtoDeck)

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `SEQ_DECKTOP` | `0` | Return to the top of the Deck | 弹回卡组顶端 |
| `SEQ_DECKBOTTOM` | `1` | Return to the bottom of the Deck | 弹回卡组底端 |
| `SEQ_DECKSHUFFLE` | `2` | Return to the Deck and shuffle (temporarily placed at the bottom before shuffling) | 弹回卡组并洗牌（洗牌前暂时放在底端） |

## Locations of Spell Cards

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `LOCATION_FZONE` | `0x100` | Field Zone | 场地区 |
| `LOCATION_PZONE` | `0x200` | Pendulum Zone | 灵摆区 |

## Positions

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `POS_FACEUP_ATTACK` | `0x1` | Face-up Attack Position | 表侧攻击 |
| `POS_FACEDOWN_ATTACK` | `0x2` | (reserved) | (reserved) |
| `POS_FACEUP_DEFENSE` | `0x4` | Face-up Defense Position | 表侧守备 |
| `POS_FACEDOWN_DEFENSE` | `0x8` | Face-down Defense Position | 里侧守备 |
| `POS_FACEUP` | `0x5` | Face-up | 正面表示 |
| `POS_FACEDOWN` | `0xa` | Face-down | 背面表示 |
| `POS_ATTACK` | `0x3` | Attack Position | 攻击表示 |
| `POS_DEFENSE` | `0xc` | Defense Position | 守备表示 |
| `NO_FLIP_EFFECT` | `0x10000` | Does not activate Flip Effects | 不发动反转效果 |

## Card Types

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `TYPE_MONSTER` | `0x1` | Monster Card | 怪兽卡 |
| `TYPE_SPELL` | `0x2` | Spell Card | 魔法卡 |
| `TYPE_TRAP` | `0x4` | Trap Card | 陷阱卡 |
| `TYPE_NORMAL` | `0x10` | Normal Monster | 通常怪兽 |
| `TYPE_EFFECT` | `0x20` | Effect Monster | 效果 |
| `TYPE_FUSION` | `0x40` | Fusion Monster | 融合 |
| `TYPE_RITUAL` | `0x80` | Ritual Monster | 仪式 |
| `TYPE_TRAPMONSTER` | `0x100` | Trap Monster | 陷阱怪兽 |
| `TYPE_SPIRIT` | `0x200` | Spirit Monster | 灵魂 |
| `TYPE_UNION` | `0x400` | Union Monster | 同盟 |
| `TYPE_DUAL` | `0x800` | Gemini Monster | 二重 |
| `TYPE_TUNER` | `0x1000` | Tuner Monster | 调整 |
| `TYPE_SYNCHRO` | `0x2000` | Synchro Monster | 同调 |
| `TYPE_TOKEN` | `0x4000` | Token | 衍生物 |
| `TYPE_QUICKPLAY` | `0x10000` | Quick-Play Spell | 速攻 |
| `TYPE_CONTINUOUS` | `0x20000` | Continuous Spell/Trap | 永续 |
| `TYPE_EQUIP` | `0x40000` | Equip Spell | 装备 |
| `TYPE_FIELD` | `0x80000` | Field Spell | 场地 |
| `TYPE_COUNTER` | `0x100000` | Counter Trap | 反击 |
| `TYPE_FLIP` | `0x200000` | Flip Monster | 翻转 |
| `TYPE_TOON` | `0x400000` | Toon Monster | 卡通 |
| `TYPE_XYZ` | `0x800000` | Xyz Monster | 超量 |
| `TYPE_PENDULUM` | `0x1000000` | Pendulum Monster | 灵摆 |
| `TYPE_SPSUMMON` | `0x2000000` | Special Summon Monster | 特殊召唤 |
| `TYPE_LINK` | `0x4000000` | Link Monster | 连接 |

## Combined Types

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `TYPES_TOKEN_MONSTER` | `0x4011` | Token Monster |  |
| `TYPES_NORMAL_TRAP_MONSTER` | `0x111` | Normal Trap Monster |  |
| `TYPES_EFFECT_TRAP_MONSTER` | `0x121` | Effect Trap Monster |  |

## Attributes

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `ATTRIBUTE_ALL` | `0x7f` | All Attributes | All |
| `ATTRIBUTE_EARTH` | `0x01` | Earth | 地 |
| `ATTRIBUTE_WATER` | `0x02` | Water | 水 |
| `ATTRIBUTE_FIRE` | `0x04` | Fire | 炎 |
| `ATTRIBUTE_WIND` | `0x08` | Wind | 风 |
| `ATTRIBUTE_LIGHT` | `0x10` | Light | 光 |
| `ATTRIBUTE_DARK` | `0x20` | Dark | 暗 |
| `ATTRIBUTE_DIVINE` | `0x40` | Divine | 神 |

## Races

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `RACE_ALL` | `0x3ffffff` | All Races | 全种族 |
| `RACE_WARRIOR` | `0x1` | Warrior | 战士 |
| `RACE_SPELLCASTER` | `0x2` | Spellcaster | 魔法师 |
| `RACE_FAIRY` | `0x4` | Fairy | 天使 |
| `RACE_FIEND` | `0x8` | Fiend | 恶魔 |
| `RACE_ZOMBIE` | `0x10` | Zombie | 不死 |
| `RACE_MACHINE` | `0x20` | Machine | 机械 |
| `RACE_AQUA` | `0x40` | Aqua | 水 |
| `RACE_PYRO` | `0x80` | Pyro | 炎 |
| `RACE_ROCK` | `0x100` | Rock | 岩石 |
| `RACE_WINDBEAST` | `0x200` | Winged Beast | 鸟兽 |
| `RACE_PLANT` | `0x400` | Plant | 植物 |
| `RACE_INSECT` | `0x800` | Insect | 昆虫 |
| `RACE_THUNDER` | `0x1000` | Thunder | 雷 |
| `RACE_DRAGON` | `0x2000` | Dragon | 龙 |
| `RACE_BEAST` | `0x4000` | Beast | 兽 |
| `RACE_BEASTWARRIOR` | `0x8000` | Beast-Warrior | 兽战士 |
| `RACE_DINOSAUR` | `0x10000` | Dinosaur | 恐龙 |
| `RACE_FISH` | `0x20000` | Fish | 鱼 |
| `RACE_SEASERPENT` | `0x40000` | Sea Serpent | 海龙 |
| `RACE_REPTILE` | `0x80000` | Reptile | 爬虫类 |
| `RACE_PSYCHO` | `0x100000` | Psychic | 念动力 |
| `RACE_DIVINE` | `0x200000` | Divine-Beast | 幻神兽 |
| `RACE_CREATORGOD` | `0x400000` | Creator God | 创造神 |
| `RACE_WYRM` | `0x800000` | Wyrm | 幻龙 |
| `RACE_CYBERSE` | `0x1000000` | Cyberse | 电子界 |
| `RACE_ILLUSION` | `0x2000000` | Illusion | 幻想魔 |

## Reasons

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `REASON_DESTROY` | `0x1` | Destroyed | 破坏 |
| `REASON_RELEASE` | `0x2` | Tributed | 解放 |
| `REASON_TEMPORARY` | `0x4` | Temporary | 暂时 |
| `REASON_MATERIAL` | `0x8` | Used as Fusion/Synchro/Xyz Material, Ritual Material, or as a Tribute for a Tribute Summon | 作为融合/同调/超量素材或用於儀式/升級召喚 |
| `REASON_SUMMON` | `0x10` | Summoned | 召唤 |
| `REASON_BATTLE` | `0x20` | Destroyed by battle | 战斗破坏 |
| `REASON_EFFECT` | `0x40` | Affected by effect | 效果 |
| `REASON_COST` | `0x80` | Used as cost or destroyed due to inability to pay cost | 用於代價或無法支付代價而破壞 |
| `REASON_ADJUST` | `0x100` | Adjusted (e.g., Imperial Custom) | 调整（御前试合） |
| `REASON_LOST_TARGET` | `0x200` | Lost equip target | 失去装备对象 |
| `REASON_RULE` | `0x400` | By game rule | 规则 |
| `REASON_SPSUMMON` | `0x800` | Special Summoned | 特殊召唤 |
| `REASON_DISSUMMON` | `0x1000` | Summon negated | 召唤失败 |
| `REASON_FLIP` | `0x2000` | Flipped | 翻转 |
| `REASON_DISCARD` | `0x4000` | Discarded | 丢弃 |
| `REASON_RDAMAGE` | `0x8000` | Damage converted from recovery | 回復轉換後的傷害 |
| `REASON_RRECOVER` | `0x10000` | Recovery converted from damage | 傷害轉換後的回復 |
| `REASON_RETURN` | `0x20000` | Returned to Graveyard | 回到墓地 |
| `REASON_FUSION` | `0x40000` | Used for Fusion Summon | 用於融合召喚 |
| `REASON_SYNCHRO` | `0x80000` | Used for Synchro Summon | 用於同调召喚 |
| `REASON_RITUAL` | `0x100000` | Used for Ritual Summon | 用於仪式召喚 |
| `REASON_XYZ` | `0x200000` | Used for Xyz Summon | 用於超量召喚 |
| `REASON_REPLACE` | `0x1000000` | Replaced | 代替 |
| `REASON_DRAW` | `0x2000000` | Drawn | 抽卡 |
| `REASON_REDIRECT` | `0x4000000` | Redirected (e.g., Macro Cosmos, Plague Spreader) | 改变去向（大宇宙，带菌等） |
| `REASON_REVEAL` | `0x8000000` | Revealed from Deck (e.g., Sylvan) | 翻开卡组（森罗） |
| `REASON_LINK` | `0x10000000` | Used for Link Summon | 用于连接召唤 |
| `REASON_LOST_OVERLAY` | `0x20000000` | Xyz Material lost when Xyz Monster leaves the field | 超量素材随着超量怪兽离场 |
| `REASON_MAINTENANCE` | `0x40000000` | Maintenance cost | 维持代价 |
| `REASON_ACTION` | `0x80000000` | Action timing, such as attack declaration | 攻击宣言之际等 |

## Location Reasons

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `LOCATION_REASON_TOFIELD` | `0x1` | Default value for Duel.GetLocationCount(), e.g., Kaiser Colosseum | Duel.GetLocationCount()預設值,凱薩競技場 |
| `LOCATION_REASON_CONTROL` | `0x2` | Used by Card.IsControlerCanBeChanged() | Card.IsControlerCanBeChanged()使用 |

## Summon Types

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `SUMMON_TYPE_NORMAL` | `0x10000000` | Normal Summon (can modify value with EFFECT_SUMMON_PROC, EFFECT_SET_PROC) | 通常召唤(EFFECT_SUMMON_PROC,EFFECT_SET_PROC 可用Value修改數值) |
| `SUMMON_TYPE_ADVANCE` | `0x11000000` | Tribute Summon | 上级召唤 |
| `SUMMON_TYPE_DUAL` | `0x12000000` | Gemini Summon (re-summon) | 再度召唤（二重） |
| `SUMMON_TYPE_FLIP` | `0x20000000` | Flip Summon | 翻转召唤 |
| `SUMMON_TYPE_SPECIAL` | `0x40000000` | Special Summon (can modify value with EFFECT_SPSUMMON_PROC, EFFECT_SPSUMMON_PROC_G) | 特殊召唤(EFFECT_SPSUMMON_PROC,EFFECT_SPSUMMON_PROC_G 可用Value修改數值) |
| `SUMMON_TYPE_FUSION` | `0x43000000` | Fusion Summon | 融合召唤 |
| `SUMMON_TYPE_RITUAL` | `0x45000000` | Ritual Summon | 仪式召唤 |
| `SUMMON_TYPE_SYNCHRO` | `0x46000000` | Synchro Summon | 同调召唤 |
| `SUMMON_TYPE_XYZ` | `0x49000000` | Xyz Summon | 超量召唤 |
| `SUMMON_TYPE_PENDULUM` | `0x4a000000` | Pendulum Summon | 灵摆召唤 |
| `SUMMON_TYPE_LINK` | `0x4c000000` | Link Summon | 连接召唤 |

## Summon Values

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `SUMMON_VALUE_SELF` | `0x1` | By own effect or condition | 自身效果或条件 |
| `SUMMON_VALUE_SYNCHRO_MATERIAL` | `0x11` | Special Summoned and used as Synchro Material (e.g., Blackwing - Shura the Blue Flame check) | 特殊召唤并作为同调素材（黑羽-东云之东风检查） |
| `SUMMON_VALUE_DARK_SANCTUARY` | `0x12` | Dark Sanctuary | 暗黑圣域 |
| `SUMMON_VALUE_MONSTER_REBORN` | `0x13` | Monster Reborn (e.g., Thousand-Eyes Restrict) | 死者苏生（千年的启示） |
| `SUMMON_VALUE_MASK_CHANGE` | `0x14` | Mask Change summon value |  |
| `SUMMON_VALUE_ASSAULT_MODE` | `0x15` | Assault Mode summon value |  |
| `SUMMON_VALUE_LV` | `0x1000` | Corresponds to LV Monster effects | 对应LV怪兽的效果 |
| `SUMMON_VALUE_GLADIATOR` | `0x2000` | Gladiator Beast | 剑斗兽 |
| `SUMMON_VALUE_EVOLTILE` | `0x4000` | Evoltile | 进化虫 |
| `SUMMON_VALUE_DARK_FUSION` | `SUMMON_TYPE_FUSION|0x16` | Dark Fusion summon value |  |
| `SUMMON_VALUE_FOSSIL_FUSION` | `SUMMON_TYPE_FUSION|0x17` | Fossil Fusion summon value |  |
| `SUMMON_VALUE_FUTURE_FUSION` | `SUMMON_TYPE_FUSION|0x18` | Future Fusion summon value |  |

## Status

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `STATUS_DISABLED` | `0x0001` | Effect negated | 效果被无效 |
| `STATUS_TO_ENABLE` | `0x0002` | Will become enabled | 将变成有效 |
| `STATUS_TO_DISABLE` | `0x0004` | Will become disabled | 将变成无效 |
| `STATUS_PROC_COMPLETE` | `0x0008` | Completed proper summon (bypasses revival restrictions) | 完成正规召唤（解除苏生限制） |
| `STATUS_SET_TURN` | `0x0010` | Set this turn | 在本回合覆盖 |
| `STATUS_NO_LEVEL` | `0x0020` | No Level | 无等级 |
| `STATUS_BATTLE_RESULT` | `0x0040` | Monster expected to be destroyed due to damage calculation | 傷害計算結果預計要破壞的怪獸 |
| `STATUS_SPSUMMON_STEP` | `0x0080` | In Special Summon process | 效果特召處理中 |
| `STATUS_CANNOT_CHANGE_FORM` | `0x0100` | The turn player cannot manually change battle position | 回合玩家不能手动改变表示形式 |
| `STATUS_SUMMONING` | `0x0200` | In summon process | 召唤中 |
| `STATUS_EFFECT_ENABLED` | `0x0400` | Card ready (not moving, summoning, or activating Spell/Trap) | 卡片準備就緒(不在移動、召喚、魔法陷阱發動中) |
| `STATUS_SUMMON_TURN` | `0x0800` | Summoned/Set this turn | 在本回合召喚/SET |
| `STATUS_DESTROY_CONFIRMED` | `0x1000` | Destruction confirmed | 预定被破坏 |
| `STATUS_LEAVE_CONFIRMED` | `0x2000` | Spell/Trap sent to Graveyard after chain resolution | 連鎖處理完後送去墓地的魔法陷阱 |
| `STATUS_BATTLE_DESTROYED` | `0x4000` | Confirmed destroyed by battle, not yet moved | 战斗破坏确定後尚未移動 |
| `STATUS_COPYING_EFFECT` | `0x8000` | Copying effect | 正在复制效果 |
| `STATUS_CHAINING` | `0x10000` | In chain | 正在連鎖串中 |
| `STATUS_SUMMON_DISABLED` | `0x20000` | Summon negated, not yet moved | 召唤无效後尚未移動 |
| `STATUS_ACTIVATE_DISABLED` | `0x40000` | Activation negated, not yet moved | 发动无效後尚未移動 |
| `STATUS_EFFECT_REPLACED` | `0x80000` | Effect replaced (e.g., Crimson Nova Trinity) | 效果被替代(红莲霸权) |
| `STATUS_FLIP_SUMMONING` | `0x100000` | Being Flip Summoned | 反转召唤中 |
| `STATUS_ATTACK_CANCELED` | `0x200000` | Attack canceled if this card is the attacker | 若其為攻擊者，則攻擊中止 |
| `STATUS_INITIALIZING` | `0x400000` | Initializing | 正在初始化 |
| `STATUS_TO_HAND_WITHOUT_CONFIRM` | `0x800000` | Non-public card added to hand by effect without opponent confirmation | 非公开的卡被效果加入手卡但未给对方确认 |
| `STATUS_JUST_POS` | `0x1000000` | Position changed (used for STATUS_CONTINUOUS_POS check) | 已改變表示形式(用於STATUS_CONTINUOUS_POS判定) |
| `STATUS_CONTINUOUS_POS` | `0x2000000` | Changed to another position after initial change | 改變後再次設定成其他表示形式 |
| `STATUS_FORBIDDEN` | `0x4000000` | Cannot be played | 不能play |
| `STATUS_ACT_FROM_HAND` | `0x8000000` | Activated from hand | 從手牌发动 |
| `STATUS_OPPO_BATTLE` | `0x10000000` | Battled an opponent's monster | 和對手的怪兽戰鬥 |
| `STATUS_FLIP_SUMMON_TURN` | `0x20000000` | Flip Summoned this turn | 在本回合反转召唤 |
| `STATUS_SPSUMMON_TURN` | `0x40000000` | Special Summoned this turn | 在本回合特殊召唤 |
| `STATUS_FLIP_SUMMON_DISABLED` | `0x80000000` | Flip Summon negated | 反转召唤被无效 |

## Assume

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `ASSUME_CODE` | `1` | Card Code |  |
| `ASSUME_TYPE` | `2` | Card Type |  |
| `ASSUME_LEVEL` | `3` | Level |  |
| `ASSUME_RANK` | `4` | Rank |  |
| `ASSUME_ATTRIBUTE` | `5` | Attribute |  |
| `ASSUME_RACE` | `6` | Race |  |
| `ASSUME_ATTACK` | `7` | Attack |  |
| `ASSUME_DEFENSE` | `8` | Defense |  |

## Link Markers

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `LINK_MARKER_BOTTOM_LEFT` | `0x001` | Bottom-Left (↙) | ↙ |
| `LINK_MARKER_BOTTOM` | `0x002` | Bottom (↓) | ↓ |
| `LINK_MARKER_BOTTOM_RIGHT` | `0x004` | Bottom-Right (↘) | ↘ |
| `LINK_MARKER_LEFT` | `0x008` | Left (←) | ← |
| `LINK_MARKER_RIGHT` | `0x020` | Right (→) | → |
| `LINK_MARKER_TOP_LEFT` | `0x040` | Top-Left (↖) | ↖ |
| `LINK_MARKER_TOP` | `0x080` | Top (↑) | ↑ |
| `LINK_MARKER_TOP_RIGHT` | `0x100` | Top-Right (↗) | ↗ |

## Counters

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `COUNTER_WITHOUT_PERMIT` | `0x1000` | Counter that can be placed on non-specific targets | 可以放置在非特定對象的指示物 |
| `COUNTER_NEED_ENABLE` | `0x2000` | N/A | N/A |

## Phases

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `PHASE_DRAW` | `0x01` | Draw Phase | 抽卡阶段 |
| `PHASE_STANDBY` | `0x02` | Standby Phase | 准备阶段 |
| `PHASE_MAIN1` | `0x04` | Main Phase 1 | 主要阶段1 |
| `PHASE_BATTLE_START` | `0x08` | Battle Phase Start | 战斗阶段开始 |
| `PHASE_BATTLE_STEP` | `0x10` | Battle Step | 战斗步驟 |
| `PHASE_DAMAGE` | `0x20` | Damage Step | 伤害步驟 |
| `PHASE_DAMAGE_CAL` | `0x40` | Damage Calculation | 伤害计算时 |
| `PHASE_BATTLE` | `0x80` | Battle Phase End | 战斗阶段結束 |
| `PHASE_MAIN2` | `0x100` | Main Phase 2 | 主要阶段2 |
| `PHASE_END` | `0x200` | End Phase | 结束阶段 |

## Players

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `PLAYER_NONE` | `2` | Neither player | 2个玩家都不是 |
| `PLAYER_ALL` | `3` | Both players | 2个玩家都是 |

## Chain Info

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `CHAININFO_CHAIN_COUNT` | `0x01` | Chain number | 连锁数 |
| `CHAININFO_TRIGGERING_EFFECT` | `0x02` | Effect of the chain | 连锁的效果 |
| `CHAININFO_TRIGGERING_PLAYER` | `0x04` | Player who activated the chain | 连锁的玩家 |
| `CHAININFO_TRIGGERING_CONTROLER` | `0x08` | Controller of the card in the chain | 连锁的卡的控制者 |
| `CHAININFO_TRIGGERING_LOCATION` | `0x10` | Location of the chain | 连锁的位置 |
| `CHAININFO_TRIGGERING_SEQUENCE` | `0x20` | Sequence number of the chain's location (Monster or Spell/Trap Zone) | 连锁的位置的编号（指怪兽和魔陷区的格子） |
| `CHAININFO_TARGET_CARDS` | `0x40` | Target cards of the chain effect (the next 3 must be set in the target function) | 连锁的效果的对象（以下3个需要在target函数里设置） |
| `CHAININFO_TARGET_PLAYER` | `0x80` | Target player of the chain effect | 连锁的效果的对象（玩家） |
| `CHAININFO_TARGET_PARAM` | `0x100` | Parameter value of the chain effect | 连锁的效果的参数值 |
| `CHAININFO_DISABLE_REASON` | `0x200` | Reason for negation | 无效的原因效果 |
| `CHAININFO_DISABLE_PLAYER` | `0x400` | Player who negated the chain | 无效的玩家 |
| `CHAININFO_CHAIN_ID` | `0x800` | Chain ID | 连锁ID |
| `CHAININFO_TYPE` | `0x1000` | Chain type | 连锁类型 |
| `CHAININFO_EXTTYPE` | `0x2000` | Chain extra type | 连锁额外类型 |
| `CHAININFO_TRIGGERING_POSITION` | `0x4000` | Position when the chain occurred | 连锁发生时的表示形式 |
| `CHAININFO_TRIGGERING_CODE` | `0x8000` | Code when the chain occurred | 连锁发生时的密码 |
| `CHAININFO_TRIGGERING_CODE2` | `0x10000` | Other code when the chain occurred | 连锁发生时的其他密码 |
| `CHAININFO_TRIGGERING_LEVEL` | `0x40000` | Level when the chain occurred | 连锁发生时的等级 |
| `CHAININFO_TRIGGERING_RANK` | `0x80000` | Rank when the chain occurred | 连锁发生时的阶级 |
| `CHAININFO_TRIGGERING_ATTRIBUTE` | `0x100000` | Attribute when the chain occurred | 连锁发生时的属性 |
| `CHAININFO_TRIGGERING_RACE` | `0x200000` | Race when the chain occurred | 连锁发生时的种族 |
| `CHAININFO_TRIGGERING_ATTACK` | `0x400000` | Attack when the chain occurred | 连锁发生时的攻击力 |
| `CHAININFO_TRIGGERING_DEFENSE` | `0x800000` | Defense when the chain occurred | 连锁发生时的守备力 |

## Summon Info

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `SUMMON_INFO_CODE` | `0x01` | Summon info: code |  |
| `SUMMON_INFO_CODE2` | `0x02` | Summon info: secondary code |  |
| `SUMMON_INFO_TYPE` | `0x04` | Summon info: type |  |
| `SUMMON_INFO_LEVEL` | `0x08` | Summon info: Level |  |
| `SUMMON_INFO_RANK` | `0x10` | Summon info: Rank |  |
| `SUMMON_INFO_ATTRIBUTE` | `0x20` | Summon info: Attribute |  |
| `SUMMON_INFO_RACE` | `0x40` | Summon info: Race |  |
| `SUMMON_INFO_ATTACK` | `0x80` | Summon info: ATK |  |
| `SUMMON_INFO_DEFENSE` | `0x100` | Summon info: DEF |  |
| `SUMMON_INFO_REASON_EFFECT` | `0x200` | Summon info: reason Effect |  |
| `SUMMON_INFO_REASON_PLAYER` | `0x400` | Summon info: reason player |  |

## Reset Conditions

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `RESET_SELF_TURN` | `0x10000000` | Reset at the end of your turn's phase | 自己回合的階段重置 |
| `RESET_OPPO_TURN` | `0x20000000` | Reset at the end of opponent's turn's phase | 对方回合的階段重置 |
| `RESET_PHASE` | `0x40000000` | Reset at phase end (typically used with phases above) | 阶段结束重置(一般和上面那些阶段配合使用) |
| `RESET_CHAIN` | `0x80000000` | Reset at chain end | 连锁结束重置 |
| `RESET_EVENT` | `0x1000` | Reset under specified conditions (typically used with events below) | 指定的條件下重置(一般和下面这些事件配合使用) |
| `RESET_CARD` | `0x2000` | Reset effects with a specific card as Owner | 重置Owner為指定卡片的效果 |
| `RESET_CODE` | `0x4000` | Reset single effects with a specific Code (excluding EFFECT_FLAG_SINGLE_RANGE) | 重置指定Code的single效果(不含EFFECT_FLAG_SINGLE_RANGE) |
| `RESET_COPY` | `0x8000` | Reset effects obtained by copying | 重置以复制取得的效果 |
| `RESET_DISABLE` | `0x00010000` | Reset for negated effects (only applies to effects where owner==handler) | 效果无效重置(只適用於owner==handler的效果) |
| `RESET_TURN_SET` | `0x00020000` | Reset when Set (before event triggers) | 变里侧重置(皆為事件觸發前重置) |
| `RESET_TOGRAVE` | `0x00040000` | Reset when sent to Graveyard | 去墓地重置 |
| `RESET_REMOVE` | `0x00080000` | Reset when banished | 除外重置 |
| `RESET_TEMP_REMOVE` | `0x00100000` | Reset when temporarily banished | 暂时除外重置 |
| `RESET_TOHAND` | `0x00200000` | Reset when returned to hand or added to hand | 回手牌或加入手牌重置 |
| `RESET_TODECK` | `0x00400000` | Reset when returned to Deck | 回卡组重置 |
| `RESET_LEAVE` | `0x00800000` | Reset when moving from Monster Zone or Spell/Trap Zone to a different location | 从怪兽区或魔法区到不同区域 |
| `RESET_TOFIELD` | `0x01000000` | Reset when moving to Monster Zone or Spell/Trap Zone from a different location (except returning to field) | 除了返回场上以外，从不同区域移动到怪兽区或魔法区 |
| `RESET_CONTROL` | `0x02000000` | Reset when controller changes | 控制者变更重置 |
| `RESET_OVERLAY` | `0x04000000` | Reset when used as Xyz Material | 超量叠放重置 |
| `RESET_MSCHANGE` | `0x08000000` | Reset when moving from Monster Zone to Spell/Trap Zone or vice versa (e.g., move_to_field(), Gem Beasts) | 从怪兽区到魔法区，或者从魔法区到怪兽区(move_to_field()、寶玉獸) |

## Combined Reset Masks

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `RESETS_STANDARD` | `0x1fe0000` | RESET_TOFIELD + RESET_LEAVE + RESET_TODECK + RESET_TOHAND + RESET_TEMP_REMOVE + RESET_REMOVE + RESET_TOGRAVE + RESET_TURN_SET | RESET_TOFIELD+RESET_LEAVE+RESET_TODECK+RESET_TOHAND+RESET_TEMP_REMOVE+RESET_REMOVE+RESET_TOGRAVE+RESET_TURN_SET |
| `RESETS_REDIRECT` | `0xc7e0000` | RESETS_STANDARD + RESET_OVERLAY + RESET_MSCHANGE - RESET_TOFIELD - RESET_LEAVE (used for EFFECT_LEAVE_FIELD_REDIRECT) | RESETS_STANDARD+RESET_OVERLAY+RESET_MSCHANGE-RESET_TOFIELD-RESET_LEAVE (EFFECT_LEAVE_FIELD_REDIRECT) |
| `RESETS_WITHOUT_TEMP_REMOVE` | `0x56e0000` | RESETS_STANDARD - RESET_TEMP_REMOVE - RESET_LEAVE + RESET_OVERLAY | RESETS_STANDARD-RESET_TEMP_REMOVE-RESET_LEAVE+RESET_OVERLAY |

## Effect Types

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `EFFECT_TYPE_SINGLE` | `0x0001` | Triggered when the card's own status changes | 自己状态变化时触发 |
| `EFFECT_TYPE_FIELD` | `0x0002` | Triggered when any card on the field's status changes | 场上所有卡状态变化时触发 |
| `EFFECT_TYPE_EQUIP` | `0x0004` | Equip effect | 装备效果 |
| `EFFECT_TYPE_ACTIONS` | `0x0008` | Trigger-type, automatically added to the following types (e.g., Confrontation G) | 触发型，以下類型會自動添加此屬性（对峙的G） |
| `EFFECT_TYPE_ACTIVATE` | `0x0010` | Spell/Trap activation | 魔陷发动 |
| `EFFECT_TYPE_FLIP` | `0x0020` | Flip effect | 翻转效果 |
| `EFFECT_TYPE_IGNITION` | `0x0040` | Ignition effect | 起动效果 |
| `EFFECT_TYPE_TRIGGER_O` | `0x0080` | Optional Trigger effect | 诱发选发效果 |
| `EFFECT_TYPE_QUICK_O` | `0x0100` | Quick Optional effect | 诱发即时效果 |
| `EFFECT_TYPE_TRIGGER_F` | `0x0200` | Mandatory Trigger effect | 诱发必发效果 |
| `EFFECT_TYPE_QUICK_F` | `0x0400` | Mandatory Quick effect (e.g., Dragonmaid Tidying) | 诱发即时必发效果（熊猫龙等） |
| `EFFECT_TYPE_CONTINUOUS` | `0x0800` | Auxiliary effect triggered by events / Continuous effect | 由事件觸發的輔助用效果/永續效果 |
| `EFFECT_TYPE_XMATERIAL` | `0x1000` | Effect gained by an Xyz Monster when used as Xyz Material (e.g., Zoodiac) | 作为超量素材时超量怪兽获得的效果（十二兽） |
| `EFFECT_TYPE_GRANT` | `0x2000` | Grants effects to other cards (e.g., Weather Pattern) | 使其他卡片获得效果（天气模样） |
| `EFFECT_TYPE_TARGET` | `0x4000` | Continuous effect with sustained targets (mainly for Spells/Traps) | 影响持续取的对象的效果（基本只用于魔陷） |

## Effect Flags

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `EFFECT_FLAG_INITIAL` | `0x0001` | Can be activated | 卡片记载的效果(internal) |
| `EFFECT_FLAG_FUNC_VALUE` | `0x0002` | The Value property of this effect is a function | 此效果的Value属性是函数(internal) |
| `EFFECT_FLAG_COUNT_LIMIT` | `0x0004` | Activation count limit | 发动次数限制(internal) |
| `EFFECT_FLAG_FIELD_ONLY` | `0x0008` | Registered to the global environment | 此效果是注册给玩家的(internal) |
| `EFFECT_FLAG_CARD_TARGET` | `0x0010` | Targeting effect | 取对象效果 |
| `EFFECT_FLAG_IGNORE_RANGE` | `0x0020` | Affects cards in all zones (e.g., Macro Cosmos) | 影响所有区域的卡（大宇宙） |
| `EFFECT_FLAG_ABSOLUTE_TARGET` | `0x0040` | Target Range fixed to a player's perspective of self/opponent (used with SetAbsoluteRange()) | Target Range固定為某個玩家的視角所見的自己/對方(internal) |
| `EFFECT_FLAG_IGNORE_IMMUNE` | `0x0080` | Ignores effect immunity | 无视效果免疫 |
| `EFFECT_FLAG_SET_AVAILABLE` | `0x0100` | Effect can activate in face-down state, or continuous effect affecting face-down cards on the field | 裡側狀態可發動的效果、影响场上里侧的卡的永續型效果 |
| `EFFECT_FLAG_CAN_FORBIDDEN` | `0x0200` | Effect that can be stopped by Prohibition (used with EFFECT_FLAG_CANNOT_DISABLE) | 可被禁止令停止適用的效果（與EFFECT_FLAG_CANNOT_DISABLE並用） |
| `EFFECT_FLAG_CANNOT_DISABLE` | `0x0400` | Effect cannot be negated | 效果不会被无效 |
| `EFFECT_FLAG_PLAYER_TARGET` | `0x0800` | Has "targeting a player" property (e.g., Mirror of the Spirits), or continuous effect affecting players (SetTargetRange() changed to target players) | 含有"以玩家为对象"的特性（精靈之鏡）、影響玩家的永續型效果(SetTargetRange()改成指定玩家) |
| `EFFECT_FLAG_BOTH_SIDE` | `0x1000` | Usable by both players (e.g., some Field Spells, Imperial Order) | 双方都能使用（部分场地，弹压） |
| `EFFECT_FLAG_COPY` | `0x2000` | Copied effect (internal) | 复制得到的效果(internal) |
| `EFFECT_FLAG_DAMAGE_STEP` | `0x4000` | Can activate during Damage Step | 可以在伤害步骤发动 |
| `EFFECT_FLAG_DAMAGE_CAL` | `0x8000` | Can activate during Damage Calculation | 可以在伤害计算时发动 |
| `EFFECT_FLAG_DELAY` | `0x10000` | Optional trigger effect or used for EFFECT_TYPE_CONTINUOUS continuous effects | 場合型誘發效果、用於永續效果的EFFECT_TYPE_CONTINUOUS |
| `EFFECT_FLAG_SINGLE_RANGE` | `0x20000` | Only affects the card itself | 只对自己有效 |
| `EFFECT_FLAG_UNCOPYABLE` | `0x40000` | Original effect cannot be copied (effect text) | 不能复制的原始效果（效果外文本） |
| `EFFECT_FLAG_OATH` | `0x80000` | Oath effect | 誓约效果 |
| `EFFECT_FLAG_SPSUM_PARAM` | `0x100000` | Specifies position and form for summon/special summon (e.g., Lava Golem) | 指定召喚/规则特殊召唤的位置和表示形式(熔岩魔神) |
| `EFFECT_FLAG_REPEAT` | `0x200000` | N/A | N/A |
| `EFFECT_FLAG_NO_TURN_RESET` | `0x400000` | Effects like "this card can only activate once while on the field" (e.g., Springans) | 发条等“这张卡在场上只能发动一次”的效果 |
| `EFFECT_FLAG_EVENT_PLAYER` | `0x800000` | Treated as opponent's effect (action?) | 发动/处理效果的玩家为触发事件的玩家而不是卡片的持有者，如仪式魔人，万魔殿 |
| `EFFECT_FLAG_OWNER_RELATE` | `0x1000000` | Effect tied to the effect's owner | 与效果owner关联的效果 |
| `EFFECT_FLAG_CANNOT_INACTIVATE` | `0x2000000` | Activation cannot be negated | 發動不會被無效 |
| `EFFECT_FLAG_CLIENT_HINT` | `0x4000000` | Client hint | 客户端提示 |
| `EFFECT_FLAG_CONTINUOUS_TARGET` | `0x8000000` | Continuous Spell/Trap or Equip Spell (excluding early burial types) that establishes continuous targets | 建立持續對象的永續魔法/永續陷阱/早埋系以外的裝備魔法卡 |
| `EFFECT_FLAG_LIMIT_ZONE` | `0x10000000` | Restricts zones where Spell/Trap cards can be activated | 限制魔法·陷阱卡发动时可以放置的区域 |
| `EFFECT_FLAG_ACTIVATE_CONDITION` | `0x20000000` | Check the condition when a Trigger Effect is about to activate; Trigger Effects without this flag, except hand triggers, check when the event occurs | 诱发效果即将发动时检查条件（手卡诱发之外的无此标记的诱发效果为触发事件时检查） |
| `EFFECT_FLAG_CVAL_CHECK` | `0x40000000` | N/A | N/A |
| `EFFECT_FLAG_IMMEDIATELY_APPLY` | `0x80000000` | Effect applies immediately upon card activation | 卡在发动时效果就立即适用 |
| `EFFECT_FLAG_COIN` | `0x100000000` | Effect uses a coin toss |  |
| `EFFECT_FLAG_DICE` | `0x200000000` | Effect uses a die roll |  |
| `EFFECT_FLAG_FUSION_SUMMON` | `0x400000000` | Effect performs a Fusion Summon |  |
| `EFFECT_FLAG2_REPEAT_UPDATE` | `0x0001` | Final calculated ATK increase | 最后计算的攻击力上升 |
| `EFFECT_FLAG2_COF` | `0x0002` | Normal Spell can activate outside Main Phase 1 (special handling for Evil Ritual) | 通常魔法卡在MP1以外发动（邪恶的仪式的特殊处理） |
| `EFFECT_FLAG2_WICKED` | `0x0004` | Attack change for The Wicked Avatar/Dreadroot calculated last | 神之化身/恐惧之源的攻击力变化最后计算 |
| `EFFECT_FLAG2_OPTION` | `0x0008` | Child Machine | 子機 |

## Effect Codes

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `EFFECT_IMMUNE_EFFECT` | `1` | Immune to effects | 效果免疫 |
| `EFFECT_DISABLE` | `2` | Negates effects (e.g., Skill Drain) | 效果无效（技能抽取） |
| `EFFECT_CANNOT_DISABLE` | `3` | Effect cannot be negated | 卡的效果不能被无效 |
| `EFFECT_SET_CONTROL` | `4` | Sets control | 设置控制权 |
| `EFFECT_CANNOT_CHANGE_CONTROL` | `5` | Cannot change control | 不能改变控制权 |
| `EFFECT_CANNOT_ACTIVATE` | `6` | Player cannot activate effects | 玩家不能发动效果 |
| `EFFECT_CANNOT_TRIGGER` | `7` | Card cannot trigger effects | 卡不能发动效果 |
| `EFFECT_DISABLE_EFFECT` | `8` | Negates effects (e.g., Forbidden Chalice) | 效果无效（聖杯） |
| `EFFECT_DISABLE_CHAIN` | `9` | Negates in chain (processor.cpp) | 在連鎖串中無效(processor.cpp) |
| `EFFECT_DISABLE_TRAPMONSTER` | `10` | Negates Trap Monsters | 陷阱怪兽无效 |
| `EFFECT_CANNOT_INACTIVATE` | `12` | Activation cannot be negated | 发动不能被无效 |
| `EFFECT_CANNOT_DISEFFECT` | `13` | Cannot be negated during effect processing | 发动的效果不能被无效 |
| `EFFECT_CANNOT_CHANGE_POSITION` | `14` | Cannot change position | 不能改变表示形式 |
| `EFFECT_TRAP_ACT_IN_HAND` | `15` | Trap can activate from hand | 陷阱可以从手牌发动 |
| `EFFECT_TRAP_ACT_IN_SET_TURN` | `16` | Trap can activate in the turn it was Set | 陷阱可以在盖放的回合发动 |
| `EFFECT_REMAIN_FIELD` | `17` | Remains on field for X turns (e.g., Swords of Revealing Light) | X回合内留在场上（光之护封剑等） |
| `EFFECT_MONSTER_SSET` | `18` | Monster can be Set in Spell/Trap Zone | 怪兽可以在魔陷区放置 |
| `EFFECT_CANNOT_SUMMON` | `20` | Cannot Normal Summon monsters | 不能召唤怪兽 |
| `EFFECT_CANNOT_FLIP_SUMMON` | `21` | Cannot Flip Summon monsters | 不能翻转召唤怪兽 |
| `EFFECT_CANNOT_SPECIAL_SUMMON` | `22` | Cannot Special Summon monsters | 不能特殊召唤怪兽 |
| `EFFECT_CANNOT_MSET` | `23` | Cannot Set monsters | 不能覆盖怪兽 |
| `EFFECT_CANNOT_SSET` | `24` | Cannot Set Spells/Traps | 不能覆盖魔陷 |
| `EFFECT_CANNOT_DRAW` | `25` | Cannot draw cards | 不能抽卡 |
| `EFFECT_CANNOT_DISABLE_SUMMON` | `26` | Summon cannot be negated | 召唤不会无效 |
| `EFFECT_CANNOT_DISABLE_SPSUMMON` | `27` | Special Summon cannot be negated | 特殊召唤不会无效 |
| `EFFECT_SET_SUMMON_COUNT_LIMIT` | `28` | Limits Normal Summon count per turn | 设置每回合召唤次数 |
| `EFFECT_EXTRA_SUMMON_COUNT` | `29` | Increases Normal Summon count | 增加召唤（通常召唤）次数 |
| `EFFECT_SPSUMMON_CONDITION` | `30` | Special Summon condition | 特殊召唤条件 |
| `EFFECT_REVIVE_LIMIT` | `31` | Monsters with revival restrictions (Card.EnableReviveLimit()) | 有苏生限制的怪獸(Card.EnableReviveLimit()) |
| `EFFECT_SUMMON_PROC` | `32` | Summon rule effect | 召唤规则效果 |
| `EFFECT_LIMIT_SUMMON_PROC` | `33` | Summon rule restriction | 召唤规则限制 |
| `EFFECT_SPSUMMON_PROC` | `34` | Special Summon rule | 特殊召唤规则 |
| `EFFECT_EXTRA_SET_COUNT` | `35` | Increases Set (Normal Summon) count | 增加盖放（通常召唤）次数 |
| `EFFECT_SET_PROC` | `36` | Set (Normal Summon) rule | 放置（通常召唤）规则 |
| `EFFECT_LIMIT_SET_PROC` | `37` | Set (Normal Summon) rule restriction | 放置（通常召唤）规则限制 |
| `EFFECT_DIVINE_LIGHT` | `38` | Divine Light | 神圣光辉 |
| `EFFECT_CANNOT_DISABLE_FLIP_SUMMON` | `39` | Flip Summon cannot be negated | 翻转召唤不会无效 |
| `EFFECT_INDESTRUCTABLE` | `40` | Cannot be destroyed | 不会被破坏 |
| `EFFECT_INDESTRUCTABLE_EFFECT` | `41` | Cannot be destroyed by effects | 不会被效果破坏 |
| `EFFECT_INDESTRUCTABLE_BATTLE` | `42` | Cannot be destroyed by battle | 不会被战斗破坏 |
| `EFFECT_UNRELEASABLE_SUM` | `43` | Cannot be Tributed for a Tribute Summon | 不能做上级召唤的祭品 |
| `EFFECT_UNRELEASABLE_NONSUM` | `44` | Cannot be Tributed except for a Tribute Summon | 不能做上级召唤以外的祭品 |
| `EFFECT_DESTROY_SUBSTITUTE` | `45` | Mandatory destruction substitute (replace this card's destruction with another card) | 必選的代替破壞(此卡被破壞時用其他卡代替) |
| `EFFECT_CANNOT_RELEASE` | `46` | Cannot perform Tribute actions | 不能进行解放行为 |
| `EFFECT_INDESTRUCTABLE_COUNT` | `47` | Cannot be destroyed X times per turn | 一回合几次不会被破坏 |
| `EFFECT_UNRELEASABLE_EFFECT` | `48` | Cannot be Tributed | 不能被解放 |
| `EFFECT_DESTROY_REPLACE` | `50` | Optional destruction substitute (replace destruction with another action) | 可選的代替破壞(將破壞改成其他動作) |
| `EFFECT_RELEASE_REPLACE` | `51` | Tribute substitute | 代替解放 |
| `EFFECT_SEND_REPLACE` | `52` | Can send to another location instead of the intended one (e.g., Dessert Castle) | 可以不送去XX而送去OO（甜点城堡等） |
| `EFFECT_CANNOT_DISCARD_HAND` | `55` | Cannot discard from hand | 不能丢弃手牌 |
| `EFFECT_CANNOT_DISCARD_DECK` | `56` | Cannot send cards from Deck to Graveyard | 不能把卡组的卡送去墓地 |
| `EFFECT_CANNOT_USE_AS_COST` | `57` | Cannot be used as cost | 不能作为COST使用 |
| `EFFECT_CANNOT_PLACE_COUNTER` | `58` | Cannot place counters | 不能放置counter |
| `EFFECT_CANNOT_TO_GRAVE_AS_COST` | `59` | Cannot be sent to Graveyard as cost | 不能作为COST送去墓地 |
| `EFFECT_LEAVE_FIELD_REDIRECT` | `60` | Redirect destination when leaving field | 离场时重新指定去向 |
| `EFFECT_TO_HAND_REDIRECT` | `61` | Redirect destination when returning to hand | 回手牌时重新指定去向 |
| `EFFECT_TO_DECK_REDIRECT` | `62` | Redirect destination when returning to Deck | 回卡组时重新指定去向 |
| `EFFECT_TO_GRAVE_REDIRECT` | `63` | Redirect destination when sent to Graveyard | 去墓地时重新指定去向 |
| `EFFECT_REMOVE_REDIRECT` | `64` | Redirect destination when banished | 除外时重新指定去向 |
| `EFFECT_CANNOT_TO_HAND` | `65` | Cannot be added to hand | 不能加入手牌 |
| `EFFECT_CANNOT_TO_DECK` | `66` | Cannot be returned to Deck | 不能回卡组 |
| `EFFECT_CANNOT_REMOVE` | `67` | Cannot be banished | 不能除外 |
| `EFFECT_CANNOT_TO_GRAVE` | `68` | Cannot be sent to Graveyard | 不能去墓地 |
| `EFFECT_CANNOT_TURN_SET` | `69` | Cannot be Set face-down | 不能变里侧 |
| `EFFECT_CANNOT_BE_BATTLE_TARGET` | `70` | Cannot be targeted for attacks | 不能成为攻击对象 |
| `EFFECT_CANNOT_BE_EFFECT_TARGET` | `71` | Cannot be targeted by effects | 不能成为效果对象 |
| `EFFECT_IGNORE_BATTLE_TARGET` | `72` | Cannot be targeted for attacks - weak type (e.g., Legendary Fisherman) | 不能成为攻击对象-鶸型（传说的渔人） |
| `EFFECT_CANNOT_DIRECT_ATTACK` | `73` | Cannot attack directly | 不能直接攻击 |
| `EFFECT_DIRECT_ATTACK` | `74` | Can attack directly | 可以直接攻击 |
| `EFFECT_DUAL_STATUS` | `75` | Gemini status | 二重状态 |
| `EFFECT_EQUIP_LIMIT` | `76` | Equip target restriction | 装备对象限制 |
| `EFFECT_DUAL_SUMMONABLE` | `77` | Can be re-summoned (Gemini) | 可以再度召唤 |
| `EFFECT_UNION_LIMIT` | `78` | Union restriction |  |
| `EFFECT_REVERSE_DAMAGE` | `80` | Converts damage to recovery | 伤害变回复 |
| `EFFECT_REVERSE_RECOVER` | `81` | Converts recovery to damage | 回复变伤害 |
| `EFFECT_CHANGE_DAMAGE` | `82` | Changes damage value | 改变伤害数值 |
| `EFFECT_REFLECT_DAMAGE` | `83` | Reflects damage | 反射伤害 |
| `EFFECT_CANNOT_ATTACK` | `85` | Cannot attack | 不能攻击 |
| `EFFECT_CANNOT_ATTACK_ANNOUNCE` | `86` | Cannot declare an attack | 不能攻击宣言 |
| `EFFECT_CANNOT_CHANGE_POS_E` | `87` | Cannot be changed to Defense Position by effects (e.g., Aggro Cloud) | 不会被卡的效果变成守备表示（攻击性云魔物） |
| `EFFECT_ACTIVATE_COST` | `90` | Activation cost (e.g., Magical Shackles) | 发动代价（魔力之枷） |
| `EFFECT_SUMMON_COST` | `91` | Summon cost | 召唤代价 |
| `EFFECT_SPSUMMON_COST` | `92` | Special Summon cost (e.g., Tyrant Dragon) | 特殊召唤代价（暴君龙） |
| `EFFECT_FLIPSUMMON_COST` | `93` | Flip Summon cost | 翻转召唤代价 |
| `EFFECT_MSET_COST` | `94` | Monster Set cost | 怪兽放置代价 |
| `EFFECT_SSET_COST` | `95` | Spell/Trap Set cost | 魔陷放置代价 |
| `EFFECT_ATTACK_COST` | `96` | Attack cost (e.g., Mist Valley Falcon) | 攻击代价（霞之谷猎鹰） |
| `EFFECT_UPDATE_ATTACK` | `100` | Increase/decrease ATK | 增减攻击力 |
| `EFFECT_SET_ATTACK` | `101` | Set ATK, ATK becomes X for Special Summon, or continuously change ATK | 设置自身攻击力、攻击力变成X特殊召唤、持续改变攻击力 |
| `EFFECT_SET_ATTACK_FINAL` | `102` | Temporarily change ATK (all chain-entering effects) | 暂时改变攻击力（所有置入连锁的效果） |
| `EFFECT_SET_BASE_ATTACK` | `103` | Set original ATK or continuously change original ATK | 设置自身原本攻击力、持续改变原本攻击力 |
| `EFFECT_UPDATE_DEFENSE` | `104` | Increase/decrease DEF | 增减守备力 |
| `EFFECT_SET_DEFENSE` | `105` | Set DEF, DEF becomes X for Special Summon, or continuously change DEF | 设置自身守备力、守备力变成X特殊召唤、持续改变守备力 |
| `EFFECT_SET_DEFENSE_FINAL` | `106` | Temporarily change DEF (all chain-entering effects) | 暂时改变守备力（所有置入连锁的效果） |
| `EFFECT_SET_BASE_DEFENSE` | `107` | Set original DEF or continuously change original DEF | 设置自身原本守备力、持续改变原本守备力 |
| `EFFECT_REVERSE_UPDATE` | `108` | Invert ATK/DEF increase/decrease (e.g., Tengu) | 倒置增减攻击力、防御力（天邪鬼） |
| `EFFECT_SWAP_AD` | `109` | Swap ATK and DEF (e.g., Super Crashbug) | 交换攻守(超級漏洞人) |
| `EFFECT_SWAP_BASE_AD` | `110` | Swap original ATK and DEF | 交换原本攻守 |
| `EFFECT_SET_BASE_ATTACK_FINAL` | `111` | Temporarily change original ATK | 暂时改变原本攻击力 |
| `EFFECT_SET_BASE_DEFENSE_FINAL` | `112` | Temporarily change original DEF | 暂时改变原本防御力 |
| `EFFECT_ADD_CODE` | `113` | Add card code | 增加卡名 |
| `EFFECT_CHANGE_CODE` | `114` | Change card code | 改变卡名 |
| `EFFECT_ADD_TYPE` | `115` | Add card type (Types) | 增加卡片种类（types） |
| `EFFECT_REMOVE_TYPE` | `116` | Remove card type | 删除卡片种类 |
| `EFFECT_CHANGE_TYPE` | `117` | Change card type | 改变卡片种类 |
| `EFFECT_ADD_RACE` | `120` | Add race | 增加种族 |
| `EFFECT_REMOVE_RACE` | `121` | Remove race | 删除种族 |
| `EFFECT_CHANGE_RACE` | `122` | Change race | 改变种族 |
| `EFFECT_ADD_ATTRIBUTE` | `125` | Add attribute | 增加属性 |
| `EFFECT_REMOVE_ATTRIBUTE` | `126` | Remove attribute | 删除属性 |
| `EFFECT_CHANGE_ATTRIBUTE` | `127` | Change attribute | 改变属性 |
| `EFFECT_UPDATE_LEVEL` | `130` | Change Level | 改变等级 |
| `EFFECT_CHANGE_LEVEL` | `131` | Set Level | 设置等级 |
| `EFFECT_UPDATE_RANK` | `132` | Change Rank | 改变阶级 |
| `EFFECT_CHANGE_RANK` | `133` | Set Rank | 设置阶级 |
| `EFFECT_UPDATE_LSCALE` | `134` | Change Left Scale | 改变左刻度 |
| `EFFECT_CHANGE_LSCALE` | `135` | Set Left Scale | 设置左刻度 |
| `EFFECT_UPDATE_RSCALE` | `136` | Change Right Scale | 改变右刻度 |
| `EFFECT_CHANGE_RSCALE` | `137` | Set Right Scale | 设置右刻度 |
| `EFFECT_SET_POSITION` | `140` | Set position | 設定表示形式 |
| `EFFECT_SELF_DESTROY` | `141` | Non-chain destruction (e.g., Sin series) | 不入連鎖的破壞（罪系列等） |
| `EFFECT_SELF_TOGRAVE` | `142` | Non-chain send to Graveyard | 不入連鎖的送墓 |
| `EFFECT_DOUBLE_TRIBUTE` | `150` | Can be used as two Tributes | 可以作为2个祭品 |
| `EFFECT_DECREASE_TRIBUTE` | `151` | Decrease Tributes | 减少祭品 |
| `EFFECT_DECREASE_TRIBUTE_SET` | `152` | Decrease Tributes for Setting monsters | 减少放置怪兽的祭品 |
| `EFFECT_EXTRA_RELEASE` | `153` | Mandatory Tribute substitute (e.g., Soul Exchange) | 必須使用的代替解放（灵魂交错） |
| `EFFECT_TRIBUTE_LIMIT` | `154` | Tribute restriction | 祭品限制 |
| `EFFECT_EXTRA_RELEASE_SUM` | `155` | Tribute substitute for summon (e.g., Kaiser Cyclone) | 代替召唤解放（帝王的烈旋） |
| `EFFECT_TRIPLE_TRIBUTE` | `156` | N/A | N/A |
| `EFFECT_ADD_EXTRA_TRIBUTE` | `157` | Add usable Tributes (e.g., True Draco) | 增加可使用的祭品（真龙） |
| `EFFECT_EXTRA_RELEASE_NONSUM` | `158` | Tribute substitute for effect cost (e.g., Dark World) | 代替效果COST的解放（闇黒世界） |
| `EFFECT_PUBLIC` | `160` | Make hand public | 公开手牌 |
| `EFFECT_COUNTER_PERMIT` | `0x10000` | Allow placement of counter type | 允许放置指示物类型 |
| `EFFECT_COUNTER_LIMIT` | `0x20000` | Allow number of counters | 允许放置指示物数量 |
| `EFFECT_RCOUNTER_REPLACE` | `0x30000` | Substitute for removing counters | 代替取除指示物 |
| `EFFECT_LPCOST_CHANGE` | `170` | Change LP cost value | 改变生命值代价數值 |
| `EFFECT_LPCOST_REPLACE` | `171` | Replace LP cost with another action | 以其他動作代替生命值代价 |
| `EFFECT_SKIP_DP` | `180` | Skip Draw Phase | 跳过抽卡阶段 |
| `EFFECT_SKIP_SP` | `181` | Skip Standby Phase | 跳过准备阶段 |
| `EFFECT_SKIP_M1` | `182` | Skip Main Phase 1 | 跳过主要阶段1 |
| `EFFECT_SKIP_BP` | `183` | Skip Battle Phase | 跳过战斗阶段 |
| `EFFECT_SKIP_M2` | `184` | Skip Main Phase 2 | 跳过主要阶段2 |
| `EFFECT_CANNOT_BP` | `185` | Cannot enter Battle Phase | 不能进入战斗阶段 |
| `EFFECT_CANNOT_M2` | `186` | Cannot enter Main Phase 2 | 不能进入主要阶段2 |
| `EFFECT_CANNOT_EP` | `187` | Cannot enter End Phase | 不能进入结束阶段 |
| `EFFECT_SKIP_TURN` | `188` | Skip entire turn | 跳过整个回合 |
| `EFFECT_DEFENSE_ATTACK` | `190` | Can attack in Defense Position | 可以守备表示攻击 |
| `EFFECT_MUST_ATTACK` | `191` | Must attack | 必须攻击 |
| `EFFECT_FIRST_ATTACK` | `192` | Must attack first | 必须第一个攻击 |
| `EFFECT_ATTACK_ALL` | `193` | Can attack all monsters | 可以攻击所有怪兽 |
| `EFFECT_EXTRA_ATTACK` | `194` | Increase attack count | 增加攻击次数 |
| `EFFECT_MUST_BE_ATTACKED` | `195` | N/A | N/A |
| `EFFECT_ONLY_BE_ATTACKED` | `196` | Can only attack this card | 只能攻击此卡 |
| `EFFECT_ATTACK_DISABLED` | `197` | Attack negated (marker for successful Duel.NegateAttack()) | 攻击已被無效(Duel.NegateAttack()成功的標記) |
| `EFFECT_NO_BATTLE_DAMAGE` | `200` | Does not inflict battle damage to opponent | 不会给对方造成战斗伤害 |
| `EFFECT_AVOID_BATTLE_DAMAGE` | `201` | Does not take battle damage | 不会对自己造成战斗伤害 |
| `EFFECT_REFLECT_BATTLE_DAMAGE` | `202` | Opponent takes battle damage instead | 战斗伤害由对方代为承受 |
| `EFFECT_PIERCE` | `203` | Piercing damage | 贯穿伤害 |
| `EFFECT_BATTLE_DESTROY_REDIRECT` | `204` | Redirect destination when destroyed by battle | 战斗破坏时重新指定去向 |
| `EFFECT_BATTLE_DAMAGE_TO_EFFECT` | `205` | Treat battle damage as effect damage | 战斗伤害视为效果伤害 |
| `EFFECT_BOTH_BATTLE_DAMAGE` | `206` | Both players take battle damage | 战斗伤害由双方承受 |
| `EFFECT_ALSO_BATTLE_DAMAGE` | `207` | Opponent also takes battle damage dealt to you | 对自己的战斗伤害让对方也承受 |
| `EFFECT_CHANGE_BATTLE_DAMAGE` | `208` | Change battle damage dealt by this card or received by player | 改变此卡给予的战斗伤害、改变玩家受到的战斗伤害 |
| `EFFECT_TOSS_COIN_REPLACE` | `220` | Replace coin toss | 重新抛硬币 |
| `EFFECT_TOSS_DICE_REPLACE` | `221` | Replace dice roll | 重新掷骰子 |
| `EFFECT_FUSION_MATERIAL` | `230` | Specify Fusion Material conditions | 指定融合素材的條件 |
| `EFFECT_CHAIN_MATERIAL` | `231` | Player affected by Chain Material effect | 改变融合素材选取方法（连锁素材、电子融合支援） |
| `EFFECT_EXTRA_SYNCHRO_MATERIAL` | `232` | Can be treated as your Synchro Material from the hand or opponent's field | 在手卡或对方场上也可以当作自己的同调素材 |
| `EFFECT_XYZ_MATERIAL` | `233` | Can be used as Xyz Material | 在对方场上也可以当作自己的超量素材 |
| `EFFECT_FUSION_SUBSTITUTE` | `234` | Fusion Material substitute | 代替融合素材 |
| `EFFECT_CANNOT_BE_FUSION_MATERIAL` | `235` | Cannot be used as Fusion Material | 不能做融合素材 |
| `EFFECT_CANNOT_BE_SYNCHRO_MATERIAL` | `236` | Cannot be used as Synchro Material | 不能做同调素材 |
| `EFFECT_SYNCHRO_MATERIAL_CUSTOM` | `237` | Custom Tuner Synchro process | 自定义Tuner的同调过程 |
| `EFFECT_CANNOT_BE_XYZ_MATERIAL` | `238` | Cannot be used as Xyz Material | 不能做超量素材 |
| `EFFECT_CANNOT_BE_LINK_MATERIAL` | `239` | Cannot be used as Link Material | 不能做连接素材 |
| `EFFECT_SYNCHRO_LEVEL` | `240` | Level when used as Synchro Material | 做同调素材时的等级 |
| `EFFECT_RITUAL_LEVEL` | `241` | Level when used as Ritual Tribute | 做仪式祭品时的等级 |
| `EFFECT_XYZ_LEVEL` | `242` | Level when used as Xyz Material | 做超量素材时的等级 |
| `EFFECT_EXTRA_RITUAL_MATERIAL` | `243` | Can be used as Ritual Tribute from Graveyard | 在墓地当做仪式祭品 |
| `EFFECT_NONTUNER` | `244` | Treated as non-Tuner monster (e.g., Phantom King Hydride) | 同调召唤时可以当作调整以外的怪兽（幻影王 幽骑） |
| `EFFECT_OVERLAY_REMOVE_REPLACE` | `245` | Substitute for removing Xyz Material | 代替去除超量素材 |
| `EFFECT_SCRAP_CHIMERA` | `246` | Scrap Chimera | 废铁奇美拉 |
| `EFFECT_TUNE_MAGICIAN_X` | `247` | Tuning Magician Xyz Material restriction | 调弦之魔术师超量素材限制 |
| `EFFECT_TUNE_MAGICIAN_F` | `248` | Tuning Magician Fusion Material restriction | 调弦之魔术师融合素材限制 |
| `EFFECT_PRE_MONSTER` | `250` | Access various monster values (used with Card.AddMonsterAttribute()) | 可存取怪獸的各項數值(Card.AddMonsterAttribute()專用) |
| `EFFECT_MATERIAL_CHECK` | `251` | Check materials | 检查素材 |
| `EFFECT_DISABLE_FIELD` | `260` | Disable zones (e.g., Ojama King) | 无效区域（扰乱王等） |
| `EFFECT_USE_EXTRA_MZONE` | `261` | Lock Monster Zones | 怪兽区域封锁 |
| `EFFECT_USE_EXTRA_SZONE` | `262` | Lock Spell/Trap Zones | 魔法区域封锁 |
| `EFFECT_MAX_MZONE` | `263` | Maximum Monster Zone slots | 怪獸区格數上限 |
| `EFFECT_MAX_SZONE` | `264` | Maximum Spell/Trap Zone slots | 魔陷区格數上限 |
| `EFFECT_MUST_USE_MZONE` | `265` | Must use specific Monster Zone slots | 必须使用怪兽区的格子 |
| `EFFECT_HAND_LIMIT` | `270` | Hand size limit | 手牌数量限制 |
| `EFFECT_DRAW_COUNT` | `271` | Number of cards drawn in Draw Phase | 抽卡阶段的抽卡数 |
| `EFFECT_SPIRIT_DONOT_RETURN` | `280` | Spirit Monster does not return to hand | 灵魂怪兽不返回手牌 |
| `EFFECT_SPIRIT_MAYNOT_RETURN` | `281` | Spirit Monster can choose not to return to hand | 灵魂怪兽可以不返回手牌 |
| `EFFECT_CHANGE_ENVIRONMENT` | `290` | Change Field Spell | 改变场地 |
| `EFFECT_NECRO_VALLEY` | `291` | Necrovalley | 王家长眠之谷 |
| `EFFECT_FORBIDDEN` | `292` | Cannot be played (e.g., Forbidden Order) | 不能Play(禁止令) |
| `EFFECT_NECRO_VALLEY_IM` | `293` | Unaffected by Necrovalley | 不受「王家长眠之谷」的影响 |
| `EFFECT_REVERSE_DECK` | `294` | Reverse Deck order | 翻转卡组 |
| `EFFECT_REMOVE_BRAINWASHING` | `295` | Remove brainwashing | 洗脑解除 |
| `EFFECT_BP_TWICE` | `296` | Two Battle Phases | 2次战斗阶段 |
| `EFFECT_UNIQUE_CHECK` | `297` | Only one can exist on field (used with Card.SetUniqueOnField()) | 場上只能存在1張(Card.SetUniqueOnField()專用) |
| `EFFECT_MATCH_KILL` | `300` | Match victory (e.g., Victory Dragon) | Match胜利(胜利龙) |
| `EFFECT_SYNCHRO_CHECK` | `310` | Genomix Fighter | 基因组斗士 |
| `EFFECT_QP_ACT_IN_NTPHAND` | `311` | Activate from hand in opponent's turn (e.g., Ecclesia the Virtuous) | 对方回合从自己手卡发动（失乐的圣女） |
| `EFFECT_MUST_BE_SMATERIAL` | `312` | Must be used as Synchro Material (e.g., Phonon Pulse Dragon) | 必须作为同调素材（波动龙 声子龙） |
| `EFFECT_TO_GRAVE_REDIRECT_CB` | `313` | Redirect destination (e.g., Gem Beasts) | 重新指定去向(寶玉獸) |
| `EFFECT_CHANGE_INVOLVING_BATTLE_DAMAGE` | `314` | Change battle damage caused by this card | 改变此卡的战斗产生的战斗伤害 |
| `EFFECT_CHANGE_RANK_FINAL` | `315` | N/A | N/A |
| `EFFECT_MUST_BE_FMATERIAL` | `316` | Must be used as Fusion Material | 必须作为融合素材 |
| `EFFECT_MUST_BE_XMATERIAL` | `317` | Must be used as Xyz Material | 必须作为超量素材 |
| `EFFECT_MUST_BE_LMATERIAL` | `318` | Must be used as Link Material | 必须作为连接素材 |
| `EFFECT_SPSUMMON_PROC_G` | `320` | Pendulum Summon rule | P召唤规则 |
| `EFFECT_SPSUMMON_COUNT_LIMIT` | `330` | Special Summon count limit | 特殊召唤次数限制 |
| `EFFECT_LEFT_SPSUMMON_COUNT` | `331` | Remaining summon count (e.g., Summon Limit) | 剩餘召喚次數(召喚限制網) |
| `EFFECT_CANNOT_SELECT_BATTLE_TARGET` | `332` | Opponent cannot select as attack target | 對手不能選擇為攻擊對象 |
| `EFFECT_CANNOT_SELECT_EFFECT_TARGET` | `333` | Opponent cannot select as effect target | 對手不能選擇為效果對象 |
| `EFFECT_ADD_SETCODE` | `334` | Treated as specific archetype effect | 视为「XX」字段的效果 |
| `EFFECT_NO_EFFECT_DAMAGE` | `335` | Player affected by "effect damage becomes 0" | 玩家已受到"效果傷害變成0"的效果影響（只用于检查，实际免伤仍需要EFFECT_CHANGE_DAMAGE等） |
| `EFFECT_UNSUMMONABLE_CARD` | `336` | N/A | N/A |
| `EFFECT_DISABLE_CHAIN_FIELD` | `337` | N/A | N/A |
| `EFFECT_DISCARD_COST_CHANGE` | `338` | Change discard cost for Counter Traps (e.g., Ariadne the Absolver) | 反制陷阱捨棄手牌的代價改變(解放之阿里阿德涅) |
| `EFFECT_HAND_SYNCHRO` | `339` | Use hand monsters as Synchro Material | 用手牌的怪獸當作同步素材 |
| `EFFECT_ADD_FUSION_CODE` | `340` | Treated as specific card name for Fusion Material (e.g., Fusion Identification) | 作为融合素材时可以当作某一卡名(融合识别) |
| `EFFECT_ADD_FUSION_SETCODE` | `341` | Treated as specific archetype for Fusion Material (e.g., Toy Parade) | 作为融合素材时可以当作某一字段(魔玩具改造) |
| `EFFECT_RISE_TO_FULL_HEIGHT` | `342` | N/A | N/A |
| `EFFECT_ONLY_ATTACK_MONSTER` | `343` | Can only attack specific monster | 只能攻擊X |
| `EFFECT_MUST_ATTACK_MONSTER` | `344` | Must attack specific monster if attacking | 若攻擊則必須攻擊X |
| `EFFECT_PATRICIAN_OF_DARKNESS` | `345` | Opponent chooses attack target (e.g., Patrician of Darkness) | 由對手選擇攻擊對象(黑暗貴族) |
| `EFFECT_EXTRA_ATTACK_MONSTER` | `346` | Attack a monster X times | 對怪獸攻擊X次 |
| `EFFECT_UNION_STATUS` | `347` | Union status | 同盟状态 |
| `EFFECT_OLDUNION_STATUS` | `348` | Old Union status | 旧同盟状态 |
| `EFFECT_ADD_FUSION_ATTRIBUTE` | `349` | (reserved) | reserve |
| `EFFECT_REMOVE_FUSION_ATTRIBUTE` | `350` | (reserved) | reserve |
| `EFFECT_CHANGE_FUSION_ATTRIBUTE` | `351` | Attribute when used as Fusion Material | 用作融合素材时的属性 |
| `EFFECT_EXTRA_FUSION_MATERIAL` | `352` | Additional Fusion Material (e.g., Omni Alchemist) | 增加融合素材(万溶炼金师) |
| `EFFECT_TUNER_MATERIAL_LIMIT` | `353` | Synchro Material restriction | 同调素材限制 |
| `EFFECT_ADD_LINK_CODE` | `354` | Card name when used as Link Material | 用作连接素材时的卡名 |
| `EFFECT_ADD_LINK_SETCODE` | `355` | (reserved) | reserve |
| `EFFECT_ADD_LINK_ATTRIBUTE` | `356` | Attribute when used as Link Material | 用作连接素材时的属性 |
| `EFFECT_ADD_LINK_RACE` | `357` | Race when used as Link Material | 用作连接素材时的种族 |
| `EFFECT_EXTRA_LINK_MATERIAL` | `358` | Hand as Link Material | 手卡的连接素材 |
| `EFFECT_QP_ACT_IN_SET_TURN` | `359` | Quick-Play Spell can activate in the turn it was Set | 速攻魔法可以在盖放的回合发动 |
| `EFFECT_EXTRA_PENDULUM_SUMMON` | `360` | Additional Pendulum Summon | extra pendulum summon |
| `EFFECT_MATERIAL_LIMIT` | `361` | Material restriction |  |
| `EFFECT_SET_BATTLE_ATTACK` | `362` | Use set ATK for battle damage calculation | 战斗的伤害计算用设置的攻击力进行 |
| `EFFECT_SET_BATTLE_DEFENSE` | `363` | Use set DEF for battle damage calculation | 战斗的伤害计算用设置的守备力进行 |
| `EFFECT_OVERLAY_RITUAL_MATERIAL` | `364` | Xyz Materials can be used for Ritual Summon | 此卡的超量素材也能用于仪式召唤 |
| `EFFECT_CHANGE_GRAVE_ATTRIBUTE` | `365` | Change attribute of cards in Graveyard (e.g., Advanced Shift) | 墓地的卡将会改变属性（升级转变） |
| `EFFECT_CHANGE_GRAVE_RACE` | `366` | Change race of cards in Graveyard (e.g., Advanced Shift) | 墓地的卡将会改变种族（升级转变） |
| `EFFECT_ACTIVATION_COUNT_LIMIT` | `367` | reserve | reserve |
| `EFFECT_LIMIT_SPECIAL_SUMMON_POSITION` | `368` | Cannot Special Summon in specific position | 不能以特定表示形式特殊召唤 |
| `EFFECT_TUNER` | `369` | Can be treated as a Tuner for a Synchro Summon (Hundred Apple Dragon - Apple Wyrm) | 同调召唤时可以当作调整（百檎龙-苹果鳞虫） |
| `EFFECT_KAISER_COLOSSEUM` | `370` | Kaiser Colosseum | 皇帝斗技场 |
| `EFFECT_REPLACE_DAMAGE` | `371` | Damage is replaced by a specific action | 伤害由特定行动代替 |
| `EFFECT_XYZ_MIN_COUNT` | `372` | Can only be used for an Xyz Summon with at least X materials | 只能用在X只以上的超量召唤 |
| `EFFECT_SYNCHRO_LEVEL_EX` | `373` | Allows monsters without Levels to be used as Synchro Material | 支持使用没有等级的怪兽作为同调素材 |
| `EFFECT_RITUAL_LEVEL_EX` | `374` | Allows monsters without Levels to be used as Ritual Material | 支持使用没有等级的怪兽作为仪式素材 |
| `EFFECT_DOUBLE_XMATERIAL` | `375` | Counts as 2 materials when Xyz Summoning a monster that requires 3 or more materials | 召唤需3只以上作素材的超量怪兽时可以作为2只数量的素材 |
| `EFFECT_FLAG_EFFECT` | `0x20000000` | Flag effect created by RegisterFlagEffect() | 标记类效果，即RegisterFlagEffect()创建的效果 |

## Events

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `EVENT_STARTUP` | `1000` | N/A | N/A |
| `EVENT_FLIP` | `1001` | When flipped | 翻转时 |
| `EVENT_FREE_CHAIN` | `1002` | Free Chain timing (e.g., Torrential Tribute, or Quick Effects like Pleiades) | 自由时点（强脱等，还有昴星团等诱发即时效果） |
| `EVENT_DESTROY` | `1010` | Before a confirmed destroyed card moves | 確定被破壞的卡片移動前 |
| `EVENT_REMOVE` | `1011` | When banished | 除外时 |
| `EVENT_TO_HAND` | `1012` | When added to hand | 加入手牌时 |
| `EVENT_TO_DECK` | `1013` | When returned to Deck | 回卡组时 |
| `EVENT_TO_GRAVE` | `1014` | When sent to Graveyard (excluding REASON_RETURN) | 送去墓地时(不含REASON_RETURN) |
| `EVENT_LEAVE_FIELD` | `1015` | When leaving the field | 离场时 |
| `EVENT_CHANGE_POS` | `1016` | When position changes | 表示形式变更时 |
| `EVENT_RELEASE` | `1017` | When Tributed | 解放时 |
| `EVENT_DISCARD` | `1018` | When discarding from hand | 丢弃手牌时 |
| `EVENT_LEAVE_FIELD_P` | `1019` | Before a card leaving the field moves | 離場的卡片移動前 |
| `EVENT_CHAIN_SOLVING` | `1020` | When chain resolution starts (after EVENT_CHAIN_ACTIVATING) | 连锁处理开始时（EVENT_CHAIN_ACTIVATING之後） |
| `EVENT_CHAIN_ACTIVATING` | `1021` | When chain activation is preparing | 连锁处理准备中 |
| `EVENT_CHAIN_SOLVED` | `1022` | When chain resolution ends | 连锁处理结束时 |
| `EVENT_CHAIN_ACTIVATED` | `1023` | N/A | N/A |
| `EVENT_CHAIN_NEGATED` | `1024` | When chain activation is negated (after EVENT_CHAIN_ACTIVATING) | 连锁发动无效时（EVENT_CHAIN_ACTIVATING之後） |
| `EVENT_CHAIN_DISABLED` | `1025` | When chain effect is negated | 连锁效果无效时 |
| `EVENT_CHAIN_END` | `1026` | When chain ends | 连锁串结束时 |
| `EVENT_CHAINING` | `1027` | When an effect is activated | 效果发动时 |
| `EVENT_BECOME_TARGET` | `1028` | When becoming an effect target | 成为效果对象时 |
| `EVENT_DESTROYED` | `1029` | When destroyed | 被破坏时 |
| `EVENT_MOVE` | `1030` | When moving a card (e.g., Urgent Rabbit Horse) | 移動卡片(急兔馬) |
| `EVENT_LEAVE_GRAVE` | `1031` | When leaving the Graveyard | 离开墓地时 |
| `EVENT_LEAVE_DECK` | `1032` | When leaving the Deck or Extra Deck | 离开卡组或额外卡组时 |
| `EVENT_ADJUST` | `1040` | After adjust_all() (e.g., Imperial Custom) | adjust_all()调整後（御前试合） |
| `EVENT_BREAK_EFFECT` | `1050` | When Duel.BreakEffect() is called | Duel.BreakEffect()被调用时 |
| `EVENT_SUMMON_SUCCESS` | `1100` | When Normal Summon succeeds | 通常召唤成功时 |
| `EVENT_FLIP_SUMMON_SUCCESS` | `1101` | When Flip Summon succeeds | 翻转召唤成功时 |
| `EVENT_SPSUMMON_SUCCESS` | `1102` | When Special Summon succeeds | 特殊召唤成功时 |
| `EVENT_SUMMON` | `1103` | During Normal Summon (before monster appears, e.g., Solemn Warning timing) | 召唤之际（怪兽还没上场、神宣等时点） |
| `EVENT_FLIP_SUMMON` | `1104` | During Flip Summon | 翻转召唤之际 |
| `EVENT_SPSUMMON` | `1105` | During Special Summon | 特殊召唤之际 |
| `EVENT_MSET` | `1106` | When Setting a monster | 放置怪兽时 |
| `EVENT_SSET` | `1107` | When Setting a Spell/Trap | 放置魔陷时 |
| `EVENT_BE_MATERIAL` | `1108` | When used as Synchro/Xyz/Link Material, used as Ritual/Fusion Material, or Tributed for a Tribute Summon | 作为同调/超量/连结素材、用于升级召唤的解放、作为仪式/融合召唤的素材 |
| `EVENT_BE_PRE_MATERIAL` | `1109` | When about to be used as Synchro/Xyz/Link Material or Tributed for a Tribute Summon | 将要作为同调/超量/连结素材、用于升级召唤的解放 |
| `EVENT_DRAW` | `1110` | When drawing | 抽卡时 |
| `EVENT_DAMAGE` | `1111` | When dealing battle/effect damage | 造成战斗/效果伤害时 |
| `EVENT_RECOVER` | `1112` | When recovering LP | 回复生命值时 |
| `EVENT_PREDRAW` | `1113` | Before normal draw in Draw Phase | 抽卡阶段通常抽卡前 |
| `EVENT_SUMMON_NEGATED` | `1114` | When Normal Summon is negated | 召唤被无效时 |
| `EVENT_FLIP_SUMMON_NEGATED` | `1115` | When Flip Summon is negated | 反转召唤被无效时 |
| `EVENT_SPSUMMON_NEGATED` | `1116` | When Special Summon is negated | 特殊召唤被无效时 |
| `EVENT_SPSUMMON_SUCCESS_G_P` | `1117` | Before an EFFECT_SPSUMMON_PROC_G Special Summon succeeds (EFFECT_TYPE_CONTINUOUS only) | EFFECT_SPSUMMON_PROC_G特殊召唤成功前(只能使用EFFECT_TYPE_CONTINUOUS) |
| `EVENT_CONTROL_CHANGED` | `1120` | When control changes | 控制权变更 |
| `EVENT_EQUIP` | `1121` | When an Equip Card is equipped | 装备卡装备时 |
| `EVENT_ATTACK_ANNOUNCE` | `1130` | When attack is declared | 攻击宣言时 |
| `EVENT_BE_BATTLE_TARGET` | `1131` | When selected as attack target | 被选为攻击对象时 |
| `EVENT_BATTLE_START` | `1132` | When Damage Step starts (before flipping) | 伤害步骤开始时（反转前） |
| `EVENT_BATTLE_CONFIRM` | `1133` | Before damage calculation (after flipping) | 伤害计算前（反转後） |
| `EVENT_PRE_DAMAGE_CALCULATE` | `1134` | During damage calculation (e.g., Wing Slash) | 伤害计算时（羽斬） |
| `EVENT_DAMAGE_CALCULATING` | `1135` | N/A | N/A |
| `EVENT_PRE_BATTLE_DAMAGE` | `1136` | When battle damage is about to occur (only for EFFECT_TYPE_CONTINUOUS) | 即将产生战斗伤害(只能使用EFFECT_TYPE_CONTINUOUS) |
| `EVENT_BATTLE_END` | `1137` | N/A | N/A |
| `EVENT_BATTLED` | `1138` | After damage calculation (e.g., Alien Girl, same timing as Flip Effects) | 伤害计算后（异女、同反转效果时点） |
| `EVENT_BATTLE_DESTROYING` | `1139` | When destroying a monster by battle and sending it to Graveyard (e.g., Blackwing - Shura the Blue Flame) | 以战斗破坏怪兽送去墓地时（BF-苍炎之修罗） |
| `EVENT_BATTLE_DESTROYED` | `1140` | When destroyed by battle and sent to Graveyard (e.g., Mystic Tomato) | 被战斗破坏送去墓地时（杀人番茄等） |
| `EVENT_DAMAGE_STEP_END` | `1141` | When Damage Step ends | 伤害步骤结束时 |
| `EVENT_ATTACK_DISABLED` | `1142` | When attack is negated (e.g., Double Chance) | 攻击无效时（翻倍机会） |
| `EVENT_BATTLE_DAMAGE` | `1143` | When dealing battle damage | 造成战斗伤害时 |
| `EVENT_TOSS_DICE` | `1150` | After dice roll result | 掷骰子的结果产生后 |
| `EVENT_TOSS_COIN` | `1151` | After coin toss result | 抛硬币的结果产生后 |
| `EVENT_TOSS_COIN_NEGATE` | `1152` | When re-tossing a coin | 重新抛硬币 |
| `EVENT_TOSS_DICE_NEGATE` | `1153` | When re-rolling a dice | 重新掷骰子 |
| `EVENT_LEVEL_UP` | `1200` | When Level increases | 等级上升时 |
| `EVENT_PAY_LPCOST` | `1201` | When paying LP cost | 支付生命值时 |
| `EVENT_DETACH_MATERIAL` | `1202` | When removing Xyz Material | 去除超量素材时 |
| `EVENT_RETURN_TO_GRAVE` | `1203` | When returning to Graveyard | 回到墓地时 |
| `EVENT_TURN_END` | `1210` | When turn ends | 回合结束时 |
| `EVENT_PHASE` | `0x1000` | When phase ends | 阶段结束时 |
| `EVENT_PHASE_START` | `0x2000` | When phase starts | 阶段开始时 |
| `EVENT_ADD_COUNTER` | `0x10000` | When adding a counter | 增加指示物时 |
| `EVENT_REMOVE_COUNTER` | `0x20000` | When removing a counter (A-Counter, Card.RemoveCounter() must manually trigger this event) | 去除指示物时(A指示物)，Card.RemoveCounter()必須手動觸發此事件 |
| `EVENT_CUSTOM` | `0x10000000` | Custom event | 自訂事件 |

## Categories

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `CATEGORY_DESTROY` | `0x1` | Destruction effect | 破坏效果 |
| `CATEGORY_RELEASE` | `0x2` | Tribute effect | 解放效果 |
| `CATEGORY_REMOVE` | `0x4` | Banish effect | 除外效果 |
| `CATEGORY_TOHAND` | `0x8` | Return to hand effect | 回手牌效果 |
| `CATEGORY_TODECK` | `0x10` | Return to Deck effect | 回卡组效果 |
| `CATEGORY_TOGRAVE` | `0x20` | Send to Graveyard effect | 送去墓地效果 |
| `CATEGORY_DECKDES` | `0x40` | Includes sending from Deck to Graveyard or Special Summon effects | 包含從卡组送去墓地或特殊召唤效果 |
| `CATEGORY_HANDES_SELF` | `0x80` | Effect that discards your own hand | 捨棄自身手牌效果 |
| `CATEGORY_SUMMON` | `0x100` | Includes Normal Summon effect | 含召唤的效果 |
| `CATEGORY_SPECIAL_SUMMON` | `0x200` | Includes Special Summon effect | 含特殊召唤的效果 |
| `CATEGORY_TOKEN` | `0x400` | Includes Token effect | 含衍生物效果 |
| `CATEGORY_GRAVE_ACTION` | `0x800` | Includes moving cards in Graveyard other than Special Summon (e.g., House Duston) | 包含特殊召喚以外移動墓地的卡的效果（屋敷わらし） |
| `CATEGORY_POSITION` | `0x1000` | Change position effect | 改变表示形式效果 |
| `CATEGORY_CONTROL` | `0x2000` | Change control effect | 改变控制权效果 |
| `CATEGORY_DISABLE` | `0x4000` | Negate effect | 使效果无效效果 |
| `CATEGORY_DISABLE_SUMMON` | `0x8000` | Negate summon effect | 无效召唤效果 |
| `CATEGORY_DRAW` | `0x10000` | Draw effect | 抽卡效果 |
| `CATEGORY_SEARCH` | `0x20000` | Search Deck effect | 检索卡组效果 |
| `CATEGORY_EQUIP` | `0x40000` | Equip effect | 把自己装备效果（请勿用于把其他卡装备的效果） |
| `CATEGORY_DAMAGE` | `0x80000` | Damage effect | 伤害效果 |
| `CATEGORY_RECOVER` | `0x100000` | Recovery effect | 回复效果 |
| `CATEGORY_ATKCHANGE` | `0x200000` | Change ATK effect | 改变攻击效果 |
| `CATEGORY_DEFCHANGE` | `0x400000` | Change DEF effect | 改变防御效果 |
| `CATEGORY_COUNTER` | `0x800000` | Counter effect | 指示物效果 |
| `CATEGORY_COIN` | `0x1000000` | Coin toss effect | 硬币效果 |
| `CATEGORY_DICE` | `0x2000000` | Dice roll effect | 骰子效果 |
| `CATEGORY_LEAVE_GRAVE` | `0x4000000` | Involves Graveyard effects (e.g., Necrovalley) | 涉及墓地的效果(王家長眠之谷) |
| `CATEGORY_GRAVE_SPSUMMON` | `0x8000000` | Includes Special Summon from Graveyard (e.g., House Duston, Underworld God) | 包含從墓地特殊召喚的效果（屋敷わらし、冥神） |
| `CATEGORY_NEGATE` | `0x10000000` | Negate activation effect | 使发动无效效果 |
| `CATEGORY_ANNOUNCE` | `0x20000000` | Effect that declares a card name upon activation | 發動時宣言卡名的效果 |
| `CATEGORY_FUSION_SUMMON` | `0x40000000` | Fusion Summon effect (e.g., Magical Rampage Array) | 融合召唤效果（暴走魔法阵） |
| `CATEGORY_TOEXTRA` | `0x80000000` | Return to Extra Deck effect | 回额外卡组效果 |
| `CATEGORY_MSET` | `0x100000000` | Effect that includes Setting a monster | 包含盖放怪兽的效果 |
| `CATEGORY_SSET` | `0x200000000` | Effect that includes Setting a Spell/Trap | 包含盖放魔陷的效果 |
| `CATEGORY_HANDES_OPPO` | `0x400000000` | Effect that discards the opponent's hand | 捨棄對方手牌效果 |
| `CATEGORY_HANDES` | `CATEGORY_HANDES_SELF+CATEGORY_HANDES_OPPO` | Discard hand effect |  |

## Hint

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `HINT_EVENT` | `1` | Event hint |  |
| `HINT_MESSAGE` | `2` | Message hint |  |
| `HINT_SELECTMSG` | `3` | Selection message hint |  |
| `HINT_OPSELECTED` | `4` | Opponent selected hint |  |
| `HINT_EFFECT` | `5` | Effect hint |  |
| `HINT_RACE` | `6` | Race hint |  |
| `HINT_ATTRIB` | `7` | Attribute hint |  |
| `HINT_CODE` | `8` | Card code hint |  |
| `HINT_NUMBER` | `9` | Number hint |  |
| `HINT_CARD` | `10` | Card hint |  |
| `HINT_ZONE` | `11` | Zone hint |  |

## Card Hint

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `CHINT_TURN` | `1` | Turn hint |  |
| `CHINT_CARD` | `2` | Card hint |  |
| `CHINT_RACE` | `3` | Race hint |  |
| `CHINT_ATTRIBUTE` | `4` | Attribute hint |  |
| `CHINT_NUMBER` | `5` | Number hint |  |
| `CHINT_DESC` | `6` | Description hint |  |

## Opcode

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `OPCODE_ADD` | `0x40000000` | Addition |  |
| `OPCODE_SUB` | `0x40000001` | Subtraction |  |
| `OPCODE_MUL` | `0x40000002` | Multiplication |  |
| `OPCODE_DIV` | `0x40000003` | Division |  |
| `OPCODE_AND` | `0x40000004` | Logical AND |  |
| `OPCODE_OR` | `0x40000005` | Logical OR |  |
| `OPCODE_NEG` | `0x40000006` | Negation |  |
| `OPCODE_NOT` | `0x40000007` | Logical NOT |  |
| `OPCODE_ISCODE` | `0x40000100` | Check card code |  |
| `OPCODE_ISSETCARD` | `0x40000101` | Check archetype |  |
| `OPCODE_ISTYPE` | `0x40000102` | Check card type |  |
| `OPCODE_ISRACE` | `0x40000103` | Check race |  |
| `OPCODE_ISATTRIBUTE` | `0x40000104` | Check attribute |  |
| `DOUBLE_DAMAGE` | `-2147483648` | Double damage |  |
| `HALF_DAMAGE` | `-2147483647` | Half damage |  |

## Hint Messages

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `HINTMSG_RELEASE` | `500` | Select a card to Tribute | 请选择要解放的卡 |
| `HINTMSG_DISCARD` | `501` | Select a card to discard from hand | 请选择要丢弃的手牌 |
| `HINTMSG_DESTROY` | `502` | Select a card to destroy | 请选择要破坏的卡 |
| `HINTMSG_REMOVE` | `503` | Select a card to banish | 请选择要除外的卡 |
| `HINTMSG_TOGRAVE` | `504` | Select a card to send to the Graveyard | 请选择要送去墓地的卡 |
| `HINTMSG_RTOHAND` | `505` | Select a card to return to the hand | 请选择要返回手牌的卡 |
| `HINTMSG_ATOHAND` | `506` | Select a card to add to the hand | 请选择要加入手牌的卡 |
| `HINTMSG_TODECK` | `507` | Select a card to return to the Deck | 请选择要返回卡组的卡 |
| `HINTMSG_SUMMON` | `508` | Select a card to Normal Summon | 请选择要召唤的卡 |
| `HINTMSG_SPSUMMON` | `509` | Select a card to Special Summon | 请选择要特殊召唤的卡 |
| `HINTMSG_SET` | `510` | Select a card to Set | 请选择要盖放的卡 |
| `HINTMSG_FMATERIAL` | `511` | Select a card to use as Fusion Material | 请选择要作为融合素材的卡 |
| `HINTMSG_SMATERIAL` | `512` | Select a card to use as Synchro Material | 请选择要作为同调素材的卡 |
| `HINTMSG_XMATERIAL` | `513` | Select a card to use as Xyz Material | 请选择要作为超量素材的卡 |
| `HINTMSG_FACEUP` | `514` | Select a face-up card | 请选择表侧表示的卡 |
| `HINTMSG_FACEDOWN` | `515` | Select a face-down card | 请选择里侧表示的卡 |
| `HINTMSG_ATTACK` | `516` | Select an Attack Position monster | 请选择攻击表示的怪兽 |
| `HINTMSG_DEFENSE` | `517` | Select a Defense Position monster | 请选择守备表示的怪兽 |
| `HINTMSG_EQUIP` | `518` | Select a card to equip | 请选择要装备的卡 |
| `HINTMSG_REMOVEXYZ` | `519` | Select an Xyz Material to remove | 请选择要取除的超量素材 |
| `HINTMSG_CONTROL` | `520` | Select a monster to change control of | 请选择要改变控制权的怪兽 |
| `HINTMSG_DESREPLACE` | `521` | Select a card to replace destruction | 请选择要代替破坏的卡 |
| `HINTMSG_FACEUPATTACK` | `522` | Select a face-up Attack Position monster | 请选择表侧攻击表示的怪兽 |
| `HINTMSG_FACEUPDEFENSE` | `523` | Select a face-up Defense Position monster | 请选择表侧守备表示的怪兽 |
| `HINTMSG_FACEDOWNATTACK` | `524` | Select a face-down Attack Position monster | 请选择里侧攻击表示的怪兽 |
| `HINTMSG_FACEDOWNDEFENSE` | `525` | Select a face-down Defense Position monster | 请选择里侧守备表示的怪兽 |
| `HINTMSG_CONFIRM` | `526` | Select a card to confirm to the opponent | 请选择给对方确认的卡 |
| `HINTMSG_TOFIELD` | `527` | Select a card to place on the field | 请选择要放置到场上的卡 |
| `HINTMSG_POSCHANGE` | `528` | Select a monster to change position | 请选择要改变表示形式的怪兽 |
| `HINTMSG_SELF` | `529` | Select your own card | 请选择自己的卡 |
| `HINTMSG_OPPO` | `530` | Select an opponent's card | 请选择对方的卡 |
| `HINTMSG_TRIBUTE` | `531` | Select a monster to Tribute for a Tribute Summon | 请选择上级召唤用需要解放的怪兽 |
| `HINTMSG_DEATTACHFROM` | `532` | Select a monster to remove Xyz Material from | 请选择要取除超量素材的怪兽 |
| `HINTMSG_LMATERIAL` | `533` | Select a card to use as Link Material | 请选择要作为连接素材的卡 |
| `HINTMSG_ATTACKTARGET` | `549` | Select an attack target | 请选择攻击的对象 |
| `HINTMSG_EFFECT` | `550` | Select an effect to activate | 请选择要发动的效果 |
| `HINTMSG_TARGET` | `551` | Select an effect target | 请选择效果的对象 |
| `HINTMSG_COIN` | `552` | Select heads or tails for a coin toss | 请选择硬币的正反面 |
| `HINTMSG_DICE` | `553` | Select a dice roll result | 请选择骰子的结果 |
| `HINTMSG_CARDTYPE` | `554` | Select a card type | 请选择一个种类 |
| `HINTMSG_OPTION` | `555` | Select an option | 请选择一个选项 |
| `HINTMSG_RESOLVEEFFECT` | `556` | Select an effect to activate or resolve | 请选择要发动/处理的效果 |
| `HINTMSG_SELECT` | `560` | Select | 请选择 |
| `HINTMSG_POSITION` | `561` | Select a position | 请选择表示形式 |
| `HINTMSG_ATTRIBUTE` | `562` | Select an attribute to declare | 请选择要宣言的属性 |
| `HINTMSG_RACE` | `563` | Select a race to declare | 请选择要宣言的种族 |
| `HINTMSG_CODE` | `564` | Declare a card name | 请宣言一个卡名 |
| `HINGMSG_NUMBER` | `565` | Select a number | 请选择一个数字 |
| `HINGMSG_LVRANK` | `567` | Declare a Level | 请宣言一个等级 |
| `HINTMSG_RESOLVECARD` | `568` | Select a card to resolve its effect | 请选择要处理效果的卡 |
| `HINTMSG_ZONE` | `569` | Select the position for \[%ls\] | 请选择\[%ls\]的位置 |
| `HINTMSG_DISABLEZONE` | `570` | Select a zone to make unusable | 请选择要变成不能使用的卡片区域 |
| `HINTMSG_TOZONE` | `571` | Select a position to move to | 请选择要移动到的位置 |
| `HINTMSG_COUNTER` | `572` | Select a card to place a counter on | 请选择要放置指示物的卡 |
| `HINTMSG_DISABLE` | `573` | Select a card to negate | 请选择要无效的卡 |
| `HINTMSG_OPERATECARD` | `574` | Select a card to operate | 请选择要操作的卡 |
| `HINTMSG_FIELD_FIRST` | `575` | Select a card on the field (press Cancel to select a card from another zone) | 请选择场上的卡（按取消可选择其他区域的卡） |

## Selection Constants

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `SELECT_HEADS` | `60` | Heads | 正面 |
| `SELECT_TAILS` | `61` | Tails | 反面 |

## Timings

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `TIMING_DRAW_PHASE` | `0x1` | Draw Phase timing | 抽卡阶段时点 |
| `TIMING_STANDBY_PHASE` | `0x2` | Standby Phase timing | 准备阶段时点 |
| `TIMING_MAIN_END` | `0x4` | Main Phase end timing | 主要阶段结束时点 |
| `TIMING_BATTLE_START` | `0x8` | Battle Phase start timing | 战斗阶段开始时点 |
| `TIMING_BATTLE_END` | `0x10` | Battle Phase end timing | 战斗阶段结束时点 |
| `TIMING_END_PHASE` | `0x20` | End Phase timing | 结束阶段时点 |
| `TIMING_SUMMON` | `0x40` | Normal Summon timing | 召唤时点 |
| `TIMING_SPSUMMON` | `0x80` | Special Summon timing | 特殊召唤时点 |
| `TIMING_FLIPSUMMON` | `0x100` | Flip Summon timing | 翻转召唤时点 |
| `TIMING_MSET` | `0x200` | Monster Set timing | 放置怪兽时点 |
| `TIMING_SSET` | `0x400` | Spell/Trap Set timing | 放置魔陷时点 |
| `TIMING_POS_CHANGE` | `0x800` | Position change timing | 表示形式变更时点 |
| `TIMING_ATTACK` | `0x1000` | Attack declaration timing | 攻击宣言时点 |
| `TIMING_DAMAGE_STEP` | `0x2000` | Damage Step timing | 伤害步骤时点 |
| `TIMING_DAMAGE_CAL` | `0x4000` | Damage Calculation timing | 伤害计算时点 |
| `TIMING_CHAIN_END` | `0x8000` | Chain end timing | 连锁结束时点 |
| `TIMING_DRAW` | `0x10000` | Draw timing (not Draw Phase) | 抽卡时点（不是抽卡阶段 |
| `TIMING_DAMAGE` | `0x20000` | Damage dealt timing | 造成伤害时点 |
| `TIMING_RECOVER` | `0x40000` | Recovery timing | 回复时点 |
| `TIMING_DESTROY` | `0x80000` | Destruction timing | 破坏时点 |
| `TIMING_REMOVE` | `0x100000` | Banish timing | 除外时点 |
| `TIMING_TOHAND` | `0x200000` | Add to hand timing (e.g., search, recovery) | 加入手牌时点（检索、回收等） |
| `TIMING_TODECK` | `0x400000` | Return to Deck timing | 回卡组时点 |
| `TIMING_TOGRAVE` | `0x800000` | Send to Graveyard timing | 进墓地时点 |
| `TIMING_BATTLE_PHASE` | `0x1000000` | Battle Phase timing | 战斗阶段时点 |
| `TIMING_EQUIP` | `0x2000000` | Equip timing | 装备时点 |
| `TIMING_BATTLE_STEP_END` | `0x4000000` | Battle Step end timing | 戰鬥步驟結束時 |
| `TIMING_BATTLED` | `0x8000000` | After damage calculation timing | 伤害计算后时点 |

## Combined Timings

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `TIMINGS_CHECK_MONSTER` | `0x1c0` | Monster summoned face-up | 怪兽正面上场 |

## Global Flags

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `GLOBALFLAG_DECK_REVERSE_CHECK` | `0x1` | Deck reverse check | 卡组翻转标记 |
| `GLOBALFLAG_BRAINWASHING_CHECK` | `0x2` | Brainwashing release check | 洗脑解除标记 |
| `GLOBALFLAG_SCRAP_CHIMERA` | `0x4` | Scrap Chimera check | 废铁奇美拉标记 |
| `GLOBALFLAG_DELAYED_QUICKEFFECT` | `0x8` | N/A | N/A |
| `GLOBALFLAG_DETACH_EVENT` | `0x10` | EVENT_DETACH_MATERIAL | EVENT_DETACH_MATERIAL |
| `GLOBALFLAG_MUST_BE_SMATERIAL` | `0x20` | Must be used as Synchro Material (e.g., Phonon Pulse Dragon) | N/A |
| `GLOBALFLAG_SPSUMMON_COUNT` | `0x40` | Player's Special Summon count limit | 玩家的特殊召唤次数限制 |
| `GLOBALFLAG_XMAT_COUNT_LIMIT` | `0x80` | Xyz Material count limit check (e.g., Archlord Kristya) | 超量素材数量限制标记（光天使 天座） |
| `GLOBALFLAG_SELF_TOGRAVE` | `0x100` | Non-chain send to Graveyard check (EFFECT_SELF_TOGRAVE) | 不入連鎖的送墓檢查(EFFECT_SELF_TOGRAVE) |
| `GLOBALFLAG_SPSUMMON_ONCE` | `0x200` | Can Special Summon only once per turn (Card.SetSPSummonOnce()) | 1回合只能特殊召喚1次(Card.SetSPSummonOnce()) |
| `GLOBALFLAG_TUNE_MAGICIAN` | `0x400` | Xyz Material check (e.g., Tuning Magician) | 超量素材检查标记（调弦之魔术师） |

## count_code

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `EFFECT_COUNT_CODE_OATH` | `0x10000000` | Activation count limit (Oath count, negated activations do not count) | 发动次数限制(誓约次数, 发动被无效不计数) |
| `EFFECT_COUNT_CODE_DUEL` | `0x20000000` | Duel usage count | 决斗中使用次数 |
| `EFFECT_COUNT_CODE_CHAIN` | `0x40000000` | Use count within the same Chain | 同一连锁中使用次数 |
| `EFFECT_COUNT_CODE_SINGLE` | `0x1` | Shared count for multiple effects on the same card | 同一张卡的多个效果公共使用次数 |

## Duel Options

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `DUEL_TEST_MODE` | `0x01` | Test mode (currently none) | 测试模式(目前暫無) |
| `DUEL_ATTACK_FIRST_TURN` | `0x02` | First turn can attack (for puzzles) | 第一回合可以攻击(用于残局) |
| `DUEL_OLD_REPLAY` | `0x04` | Old replay | 旧录像 |
| `DUEL_OBSOLETE_RULING` | `0x08` | Use old rules | 使用舊規則 |
| `DUEL_PSEUDO_SHUFFLE` | `0x10` | No shuffling | 不洗牌 |
| `DUEL_TAG_MODE` | `0x20` | Tag Duel | 双打PP |
| `DUEL_SIMPLE_AI` | `0x40` | Simple AI (for puzzles) | AI(用于残局) |
| `DUEL_RETURN_DECK_TOP` | `0x80` | Cards returned to Deck are placed on top (old default behavior in no-shuffle mode) | 回卡组洗切的卡放到卡组最上方（不洗牌模式下曾经的默认行为） |
| `DUEL_REVEAL_DECK_SEQ` | `0x100` | Show the actual order when selecting cards from the Deck (previous default behavior) | 从卡组选卡显示实际顺序（曾经的默认行为） |

## Duel rule (Debug.ReloadFieldBegin)

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `MASTER_RULE3` | `3` | Master Rule 3 (2014) | Master Rule 3 (2014) |
| `NEW_MASTER_RULE` | `4` | New Master Rule (2017) | New Master Rule (2017) |
| `MASTER_RULE_2020` | `5` | Master Rule 2020 | Master Rule 2020 |

## custom: 1-5,7 (binary: 1-5)

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `ACTIVITY_SUMMON` | `1` | Summon (excluding Normal Summon Set) |  |
| `ACTIVITY_NORMALSUMMON` | `2` | Normal Summon (including Normal Summon Set) |  |
| `ACTIVITY_SPSUMMON` | `3` | Special Summon |  |
| `ACTIVITY_FLIPSUMMON` | `4` | Flip Summon |  |
| `ACTIVITY_ATTACK` | `5` | Attack |  |
| `ACTIVITY_BATTLE_PHASE` | `6` | Enter Battle Phase (not available in custom counter) | not available in custom counter |
| `ACTIVITY_CHAIN` | `7` | Effect activation (only available in custom counter) | only available in custom counter |

## Special cards

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `CARD_MARINE_DOLPHIN` | `78734254` | Marine Dolphin (double name) | 海洋海豚(double name) |
| `CARD_TWINKLE_MOSS` | `13857930` | Twinkle Moss (double name) | 光輝苔蘚(double name) |
| `CARD_QUESTION` | `38723936` | Question | 谜题 |

## Special flag effect id

| Name | Value | English | Source comment |
| --- | --- | --- | --- |
| `FLAG_ID_CHAINING` | `1` | Internal flag id: chaining |  |
| `FLAG_ID_UNION` | `2` | Internal flag id: Union |  |
| `FLAG_ID_NO_NORMAL_DRAW` | `3` | Internal flag id: no normal draw |  |
| `FLAG_ID_ALLURE_QUEEN` | `4` | Internal flag id: Allure Queen |  |
| `FLAG_ID_ARCANA_COIN` | `5` | Internal flag id: Arcana Force coin |  |
| `FLAG_ID_REVERSAL_OF_FATE` | `36690018` | Internal flag id: Reversal of Fate |  |
