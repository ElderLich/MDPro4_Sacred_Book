# Duel.IsPlayerCanAdditionalSummon

## Signature

```lua
Duel.IsPlayerCanAdditionalSummon(int player) -> bool
```

## Description

Check if player has additional summon counts beyond Normal Summon

## Parameters

- `player` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5059`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **23** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.IsPlayerCanAdditionalSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Synchro Fellowship | `43834302` | [Scripts/c43834302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43834302.lua) | 51 |
| Red-Eyes Retro Dragon | `53485634` | [Scripts/c53485634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53485634.lua) | 50 |
| Gimmick Puppet Fantasix Machinix | `76290637` | [Scripts/c76290637.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76290637.lua) | 47 |
| Swap Frog | `9126351` | [Scripts/c9126351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9126351.lua) | 47 |
| Battlewasp - Sachi the Ceremonial Bow | `71456737` | [Scripts/c71456737.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71456737.lua) | 45 |
| Darkness Resonator | `83445539` | [Scripts/c83445539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83445539.lua) | 45 |
| Ancient Chant | `78665705` | [Scripts/c78665705.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78665705.lua) | 45 |
| Royal Archfiend | `58769832` | [Scripts/c58769832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58769832.lua) | 44 |
| Shadow's Light | `61322713` | [Scripts/c61322713.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61322713.lua) | 44 |
| Maginificent Magikey Mafteal | `15983048` | [Scripts/c15983048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15983048.lua) | 42 |
| Knightmare Goblin | `39064822` | [Scripts/c39064822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39064822.lua) | 42 |
| Scrap Raptor | `80529459` | [Scripts/c80529459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80529459.lua) | 42 |
| U.A. Hyper Stadium | `12931061` | [Scripts/c12931061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12931061.lua) | 39 |
| Yosenju Kodam | `23740893` | [Scripts/c23740893.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23740893.lua) | 37 |
| Mithra the Thunder Vassal | `22404675` | [Scripts/c22404675.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22404675.lua) | 34 |
| Cartorhyn the Hidden Gem of the Seafront | `94076521` | [Scripts/c94076521.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94076521.lua) | 34 |
| Balancer Lord | `8567955` | [Scripts/c8567955.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8567955.lua) | 34 |
| Noble Knight Custennin | `42472002` | [Scripts/c42472002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42472002.lua) | 33 |
| World Legacy - "World Key" | `40441990` | [Scripts/c40441990.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40441990.lua) | 33 |
| Simorgh, Bird of Beginning | `50820852` | [Scripts/c50820852.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50820852.lua) | 32 |
| Vampire's Domain | `5795882` | [Scripts/c5795882.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5795882.lua) | 32 |
| Ice Knight | `99328137` | [Scripts/c99328137.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99328137.lua) | 27 |
| Card Advance | `52112003` | [Scripts/c52112003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52112003.lua) | 25 |

## Script Examples

### Synchro Fellowship (`43834302`)

Source: [Scripts/c43834302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43834302.lua)

```lua
	if chkc then return chkc:IsLocation(LOCATION_MZONE) and s.lvfilter(chkc) end
	if chk==0 then return Duel.IsExistingTarget(s.lvfilter,tp,LOCATION_MZONE,0,1,nil) and Duel.GetFlagEffect(tp,id)==0
		and Duel.IsPlayerCanSummon(tp) and Duel.IsPlayerCanAdditionalSummon(tp)
	end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TARGET)
```

### Red-Eyes Retro Dragon (`53485634`)

Source: [Scripts/c53485634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53485634.lua)

```lua
end
function c53485634.sumtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanSummon(tp) and Duel.IsPlayerCanAdditionalSummon(tp) end
end
function c53485634.sumop(e,tp,eg,ep,ev,re,r,rp)
```

### Gimmick Puppet Fantasix Machinix (`76290637`)

Source: [Scripts/c76290637.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76290637.lua)

```lua
function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,1,nil)
		and Duel.IsPlayerCanSummon(tp) and Duel.IsPlayerCanAdditionalSummon(tp) end
	Duel.Hint(HINT_OPSELECTED,1-tp,e:GetDescription())
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
```
