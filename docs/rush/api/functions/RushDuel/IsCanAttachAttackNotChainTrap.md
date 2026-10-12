# RushDuel.IsCanAttachAttackNotChainTrap

Alias: `RD.IsCanAttachAttackNotChainTrap`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachAttackNotChainTrap(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 攻击宣言时, 对方不能把陷阱卡发动
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:341`

```lua
function RushDuel.IsCanAttachAttackNotChainTrap(card)
    local player = 1 - card:GetControler()
    return RushDuel.IsPlayerCanActivateTrapBattle(player) and RushDuel.IsCanAttack(card) and not RushDuel.IsHasAttachEffect(card, EFFECT_ATTACK_NOT_CHAIN_TRAP)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanAttachAttackNotChainTrap) with `RushDuel.IsCanAttachAttackNotChainTrap`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Yurushima Warrior | `120140004` | [Rush/Scripts/c120140004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120140004.lua) | 1 |
| Neutron Blast | `120283038` | [Rush/Scripts/c120283038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120283038.lua) | 1 |

## Script Examples

### Yurushima Warrior (`120140004`)

Source: [Rush/Scripts/c120140004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120140004.lua)

```lua
end
function cm.filter(c)
	return c:IsFaceup() and c:IsRace(RACE_WARRIOR) and RD.IsCanAttachAttackNotChainTrap(c)
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```

### Neutron Blast (`120283038`)

Source: [Rush/Scripts/c120283038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120283038.lua)

```lua
function cm.filter(c)
	return c:IsFaceup() and c:IsCode(list[1])
		and (RD.IsCanAttachAttackNotChainTrap(c) or RD.IsCanAttachExtraAttackMonster(c,2))
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```
