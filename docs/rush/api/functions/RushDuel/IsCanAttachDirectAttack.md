# RushDuel.IsCanAttachDirectAttack

Alias: `RD.IsCanAttachDirectAttack`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachDirectAttack(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 直接攻击
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:239`

```lua
function RushDuel.IsCanAttachDirectAttack(card)
    return RushDuel.IsCanAttack(card) and not card:IsHasEffect(EFFECT_CANNOT_DIRECT_ATTACK) and not RushDuel.IsHasAttachEffect(card, EFFECT_DIRECT_ATTACK)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **17** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanAttachDirectAttack) with `RushDuel.IsCanAttachDirectAttack`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| OuTerverSe Direct Driver | `120109056` | [Rush/Scripts/c120109056.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109056.lua) | 1 |
| UMP Sky Forbia | `120306017` | [Rush/Scripts/c120306017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306017.lua) | 1 |
| Beginning Hiyashi the Sonic Noodle Ninja | `120300035` | [Rush/Scripts/c120300035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300035.lua) | 1 |
| Doushin Kaika the Shadow Flower Full Moon | `120228037` | [Rush/Scripts/c120228037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228037.lua) | 1 |
| Jinzo #7.7 | `120257026` | [Rush/Scripts/c120257026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257026.lua) | 1 |
| Shining Shamaness | `120254082` | [Rush/Scripts/c120254082.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254082.lua) | 1 |
| Gaia, Conqueror of Champions | `120249046` | [Rush/Scripts/c120249046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249046.lua) | 1 |
| Kimeruler the Dark Raider | `120140001` | [Rush/Scripts/c120140001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120140001.lua) | 1 |
| Elemental HERO Mariner | `120272047` | [Rush/Scripts/c120272047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272047.lua) | 1 |
| Shining Shaman | `120105009` | [Rush/Scripts/c120105009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120105009.lua) | 1 |
| Hydro Cannon Big Bluefin | `120130032` | [Rush/Scripts/c120130032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120130032.lua) | 1 |
| Hazy Strike Dragon Miragiastar F | `120205033` | [Rush/Scripts/c120205033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120205033.lua) | 1 |
| Digracheon the Skysavior Radiaknight | `120301036` | [Rush/Scripts/c120301036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301036.lua) | 1 |
| Telepathic Agent | `120140030` | [Rush/Scripts/c120140030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120140030.lua) | 1 |
| Alligator's Sword Dragon | `120206001` | [Rush/Scripts/c120206001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120206001.lua) | 1 |
| Cyber Tutu | `120102004` | [Rush/Scripts/c120102004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120102004.lua) | 1 |
| Kimeterasu the Divine Ruler | `120246040` | [Rush/Scripts/c120246040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246040.lua) | 1 |

## Script Examples

### OuTerverSe Direct Driver (`120109056`)

Source: [Rush/Scripts/c120109056.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109056.lua)

```lua
function cm.filter(c)
	return c:IsFaceup() and c:IsType(TYPE_EFFECT) and c:IsLevel(4) and c:IsRace(RACE_GALAXY)
		and RD.IsCanAttachDirectAttack(c)
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```

### UMP Sky Forbia (`120306017`)

Source: [Rush/Scripts/c120306017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306017.lua)

```lua
	local c=e:GetHandler()
	return Duel.IsAbleToEnterBP()
		and RD.IsCanAttachDirectAttack(c)
		and RD.IsSummonOrSpecialSummonMainPhase(c)
end
```

### Beginning Hiyashi the Sonic Noodle Ninja (`120300035`)

Source: [Rush/Scripts/c120300035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300035.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsAbleToEnterBP() and RD.IsCanAttachDirectAttack(e:GetHandler())
end
cm.cost=RD.CostSendGraveToDeck(cm.costfilter,3,3)
```
