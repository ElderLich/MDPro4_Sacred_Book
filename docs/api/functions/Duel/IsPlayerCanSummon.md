# Duel.IsPlayerCanSummon

## Signature

```lua
Duel.IsPlayerCanSummon(int player, [int sumtype], [Card c]) -> bool
```

## Description

With only player, checks whether player is not forbidden from performing a Normal Summon by an untargeted EFFECT_CANNOT_SUMMON.
With sumtype and c, checks player EFFECT_CANNOT_SUMMON restrictions for Normal Summoning c with that sumtype. This binding does not check Summon count, costs, tribute availability, or zone availability.

## Parameters

- `player` `int`
- `sumtype` `int` optional
- `c` `Card` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5047`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **26** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.IsPlayerCanSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Union Activation | `38527680` | [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua) | 1 |
| Rahamu, Envoy of the Sacred Tome | `53904087` | [Scripts/c53904087.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53904087.lua) | 1 |
| Synchro Fellowship | `43834302` | [Scripts/c43834302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43834302.lua) | 2 |
| Red-Eyes Retro Dragon | `53485634` | [Scripts/c53485634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53485634.lua) | 1 |
| Gimmick Puppet Fantasix Machinix | `76290637` | [Scripts/c76290637.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76290637.lua) | 2 |
| Swap Frog | `9126351` | [Scripts/c9126351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9126351.lua) | 1 |
| Battlewasp - Sachi the Ceremonial Bow | `71456737` | [Scripts/c71456737.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71456737.lua) | 1 |
| Darkness Resonator | `83445539` | [Scripts/c83445539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83445539.lua) | 1 |
| Gem-Knight Nepyrim | `51831560` | [Scripts/c51831560.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51831560.lua) | 1 |
| Ancient Chant | `78665705` | [Scripts/c78665705.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78665705.lua) | 2 |
| Royal Archfiend | `58769832` | [Scripts/c58769832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58769832.lua) | 2 |
| Shadow's Light | `61322713` | [Scripts/c61322713.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61322713.lua) | 1 |
| Maginificent Magikey Mafteal | `15983048` | [Scripts/c15983048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15983048.lua) | 1 |
| Knightmare Goblin | `39064822` | [Scripts/c39064822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39064822.lua) | 1 |
| Scrap Raptor | `80529459` | [Scripts/c80529459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80529459.lua) | 2 |
| U.A. Hyper Stadium | `12931061` | [Scripts/c12931061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12931061.lua) | 1 |
| Yosenju Kodam | `23740893` | [Scripts/c23740893.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23740893.lua) | 1 |
| Mithra the Thunder Vassal | `22404675` | [Scripts/c22404675.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22404675.lua) | 1 |
| Cartorhyn the Hidden Gem of the Seafront | `94076521` | [Scripts/c94076521.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94076521.lua) | 1 |
| Balancer Lord | `8567955` | [Scripts/c8567955.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8567955.lua) | 1 |
| Noble Knight Custennin | `42472002` | [Scripts/c42472002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42472002.lua) | 1 |
| World Legacy - "World Key" | `40441990` | [Scripts/c40441990.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40441990.lua) | 1 |
| Simorgh, Bird of Beginning | `50820852` | [Scripts/c50820852.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50820852.lua) | 1 |
| Vampire's Domain | `5795882` | [Scripts/c5795882.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5795882.lua) | 1 |
| ...and 2 more |  |  |  |

## Script Examples

### Union Activation (`38527680`)

Source: [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua)

```lua
function s.thfilter2(c,e,tp)
	local minc,maxc=c:GetTributeRequirement()
	return c:IsAttackAbove(3000) and c:IsSummonable(true,nil) and c:IsSummonableCard() and c:IsAbleToHand() and s.sunthfilter(c,e,tp,minc,maxc) and Duel.IsPlayerCanSummon(tp,SUMMON_TYPE_ADVANCE,c)
end
function s.sunthfilter(c,e,tp,minc,maxc)
```

### Rahamu, Envoy of the Sacred Tome (`53904087`)

Source: [Scripts/c53904087.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53904087.lua)

```lua
end
function s.sumtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanSummon(tp) and Duel.IsExistingMatchingCard(s.sumfilter,tp,LOCATION_HAND+LOCATION_MZONE,0,1,nil) end
	Duel.SetOperationInfo(0,CATEGORY_SUMMON,nil,1,0,0)
end
```

### Synchro Fellowship (`43834302`)

Source: [Scripts/c43834302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43834302.lua)

```lua
	if chkc then return chkc:IsLocation(LOCATION_MZONE) and s.lvfilter(chkc) end
	if chk==0 then return Duel.IsExistingTarget(s.lvfilter,tp,LOCATION_MZONE,0,1,nil) and Duel.GetFlagEffect(tp,id)==0
		and Duel.IsPlayerCanSummon(tp) and Duel.IsPlayerCanAdditionalSummon(tp)
	end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TARGET)
```
