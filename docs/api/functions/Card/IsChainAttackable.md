# Card.IsChainAttackable

## Signature

```lua
Card.IsChainAttackable(Card c, [int ac], [bool monsteronly]) -> bool
```

## Description

Check whether c can be a continuous attack, c the number of attacks declared&gt; = ac return false
Note: This function returns false when c has made multiple attacks due to effects such as flashing swords

## Parameters

- `c` `Card`
- `ac` `int` optional
- `monsteronly` `bool` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3599`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **44** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsChainAttackable`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Converging Wishes](/examples/cards/20007374) | `20007374` | [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20007374.lua) | 64 |
| All-Eyes Phantom Dragon | `70335319` | [Scripts/c70335319.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70335319.lua) | 55 |
| Favorite Hero | `11881272` | [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11881272.lua) | 55 |
| Altergeist Memorygant | `23790299` | [Scripts/c23790299.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23790299.lua) | 52 |
| Infernoid Attondel | `88301393` | [Scripts/c88301393.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88301393.lua) | 49 |
| Number C5: Chaos Chimera Dragon | `69757518` | [Scripts/c69757518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69757518.lua) | 46 |
| Survival of the Fittest | `58272005` | [Scripts/c58272005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58272005.lua) | 46 |
| Black Luster Soldier - Envoy of the Beginning | `72989439` | [Scripts/c72989439.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72989439.lua) | 45 |
| Starry Night, Starry Dragon | `90835938` | [Scripts/c90835938.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90835938.lua) | 45 |
| Cyber Angel Izana | `91668401` | [Scripts/c91668401.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91668401.lua) | 44 |
| Nitro Warrior | `18013090` | [Scripts/c18013090.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18013090.lua) | 44 |
| Armored Xyz | `73046708` | [Scripts/c73046708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73046708.lua) | 44 |
| Metaphys Tyrant Dragon | `18743376` | [Scripts/c18743376.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18743376.lua) | 42 |
| DMZ Dragon | `98371278` | [Scripts/c98371278.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98371278.lua) | 41 |
| Dragocytos Corrupted Nethersoul Dragon | `21435914` | [Scripts/c21435914.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21435914.lua) | 41 |
| Superheavy Samurai General Coral | `78274190` | [Scripts/c78274190.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78274190.lua) | 40 |
| DZW - Chimera Clad | `6330307` | [Scripts/c6330307.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6330307.lua) | 39 |
| Vendread Nights | `76871889` | [Scripts/c76871889.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76871889.lua) | 39 |
| Full Armored Utopic Ray Lancer | `1269512` | [Scripts/c1269512.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1269512.lua) | 38 |
| Metamorphosed Insect Queen | `41456841` | [Scripts/c41456841.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41456841.lua) | 38 |
| Neo Blue-Eyes Ultimate Dragon | `56532353` | [Scripts/c56532353.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56532353.lua) | 37 |
| Firewall Dragon Darkfluid | `68934651` | [Scripts/c68934651.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68934651.lua) | 37 |
| White Reincarnation | `91434208` | [Scripts/c91434208.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91434208.lua) | 37 |
| Fossil Warrior Skull Knight | `59531356` | [Scripts/c59531356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59531356.lua) | 37 |
| ...and 20 more |  |  |  |

## Script Examples

### Converging Wishes (`20007374`)

Source: [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20007374.lua)

```lua
	local c=e:GetHandler()
	local ec=c:GetEquipTarget()
	if chk==0 then return ec:IsChainAttackable(0,true) end
end
function c20007374.caop(e,tp,eg,ep,ev,re,r,rp)
```

### All-Eyes Phantom Dragon (`70335319`)

Source: [Scripts/c70335319.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70335319.lua)

```lua
	local at=Duel.GetAttacker()
	return at:IsControler(tp) and Duel.GetAttackTarget()~=nil
		and at:IsRace(RACE_DRAGON) and at:IsType(TYPE_PENDULUM) and at:IsChainAttackable(0)
end
function c70335319.atcost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Favorite Hero (`11881272`)

Source: [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11881272.lua)

```lua
function c11881272.chacon(e,tp,eg,ep,ev,re,r,rp)
	local ec=e:GetHandler():GetEquipTarget()
	return Duel.GetAttacker()==ec and ec:IsRelateToBattle() and ec:IsStatus(STATUS_OPPO_BATTLE) and ec:IsChainAttackable()
end
function c11881272.chacost(e,tp,eg,ep,ev,re,r,rp,chk)
```
