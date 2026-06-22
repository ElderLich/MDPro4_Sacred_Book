# Duel.ChainAttack

## Signature

```lua
Duel.ChainAttack([Card c]) -> void
```

## Description

Marks the current attacker so it can make another attack, optionally against card c.
The binding only sets chain-attack state. It returns no Lua value and does nothing if there is no current attacker or the attacker is not affected by the resolving effect.

## Parameters

- `c` `Card` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4961`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **59** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.ChainAttack`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Converging Wishes](/examples/cards/20007374) | `20007374` | [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20007374.lua) | 64 |
| All-Eyes Phantom Dragon | `70335319` | [Scripts/c70335319.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70335319.lua) | 55 |
| Favorite Hero | `11881272` | [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11881272.lua) | 55 |
| Altergeist Memorygant | `23790299` | [Scripts/c23790299.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23790299.lua) | 52 |
| Dinomist Rex | `63251695` | [Scripts/c63251695.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63251695.lua) | 49 |
| Infernoid Attondel | `88301393` | [Scripts/c88301393.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88301393.lua) | 49 |
| Super Strident Blaze | `81193865` | [Scripts/c81193865.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81193865.lua) | 49 |
| Toy Parade | `92607427` | [Scripts/c92607427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92607427.lua) | 46 |
| Number C5: Chaos Chimera Dragon | `69757518` | [Scripts/c69757518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69757518.lua) | 46 |
| Survival of the Fittest | `58272005` | [Scripts/c58272005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58272005.lua) | 46 |
| Black Luster Soldier - Envoy of the Beginning | `72989439` | [Scripts/c72989439.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72989439.lua) | 45 |
| Starry Night, Starry Dragon | `90835938` | [Scripts/c90835938.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90835938.lua) | 45 |
| Cyber Angel Izana | `91668401` | [Scripts/c91668401.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91668401.lua) | 44 |
| Nitro Warrior | `18013090` | [Scripts/c18013090.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18013090.lua) | 44 |
| Armored Xyz | `73046708` | [Scripts/c73046708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73046708.lua) | 44 |
| Beginning Knight | `6628343` | [Scripts/c6628343.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6628343.lua) | 42 |
| Metaphys Tyrant Dragon | `18743376` | [Scripts/c18743376.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18743376.lua) | 42 |
| DMZ Dragon | `98371278` | [Scripts/c98371278.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98371278.lua) | 41 |
| Dragocytos Corrupted Nethersoul Dragon | `21435914` | [Scripts/c21435914.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21435914.lua) | 41 |
| Superheavy Samurai General Coral | `78274190` | [Scripts/c78274190.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78274190.lua) | 40 |
| Dimension Mirage | `80560728` | [Scripts/c80560728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80560728.lua) | 40 |
| DZW - Chimera Clad | `6330307` | [Scripts/c6330307.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6330307.lua) | 39 |
| Endless Bond | `35989913` | [Scripts/c35989913.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35989913.lua) | 39 |
| Vendread Nights | `76871889` | [Scripts/c76871889.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76871889.lua) | 39 |
| ...and 35 more |  |  |  |

## Script Examples

### Converging Wishes (`20007374`)

Source: [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20007374.lua)

```lua
	local ec=c:GetEquipTarget()
	if not ec:IsRelateToBattle() then return end
	Duel.ChainAttack()
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_SINGLE)
```

### All-Eyes Phantom Dragon (`70335319`)

Source: [Scripts/c70335319.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70335319.lua)

```lua
end
function c70335319.atop(e,tp,eg,ep,ev,re,r,rp)
	Duel.ChainAttack()
end
function c70335319.hspfilter(c)
```

### Favorite Hero (`11881272`)

Source: [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11881272.lua)

```lua
end
function c11881272.chaop(e,tp,eg,ep,ev,re,r,rp)
	Duel.ChainAttack()
end
```
