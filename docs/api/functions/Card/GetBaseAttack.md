# Card.GetBaseAttack

## Signature

```lua
Card.GetBaseAttack(Card c) -> int
```

## Description

Return the original attack power of c

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3441`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **321** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetBaseAttack`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Gishki Nekromirror | `36982581` | [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua) | 59 |
| Performapal Celestial Magician | `58092907` | [Scripts/c58092907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58092907.lua) | 58 |
| Number 38: Hope Harbinger Dragon Titanic Galaxy | `63767246` | [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63767246.lua) | 56 |
| Kaiki the Unity Star | `60822251` | [Scripts/c60822251.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60822251.lua) | 55 |
| Spirit Poacher | `85150300` | [Scripts/c85150300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85150300.lua) | 54 |
| Timebreaker Magician | `80335817` | [Scripts/c80335817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80335817.lua) | 54 |
| Madolche Dessert | `51650038` | [Scripts/c51650038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51650038.lua) | 53 |
| Megaroid City | `44139064` | [Scripts/c44139064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44139064.lua) | 53 |
| Meklord Astro the Eradicator | `2992036` | [Scripts/c2992036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2992036.lua) | 53 |
| Sudden Thunder Swamp | `23611122` | [Scripts/c23611122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23611122.lua) | 53 |
| Eternal Bond | `45283341` | [Scripts/c45283341.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45283341.lua) | 53 |
| World Legacy Collapse | `36197902` | [Scripts/c36197902.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36197902.lua) | 53 |
| Salamangreat Sanctuary | `1295111` | [Scripts/c1295111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1295111.lua) | 53 |
| Earthbound Servant Geo Gremlina | `33202303` | [Scripts/c33202303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33202303.lua) | 52 |
| Soul of the Supreme Celestial King | `76840111` | [Scripts/c76840111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76840111.lua) | 52 |
| Argostars - Giantslaying | `30964246` | [Scripts/c30964246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30964246.lua) | 51 |
| Shichi-Go-San | `11035075` | [Scripts/c11035075.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11035075.lua) | 51 |
| Brilliant Fusion | `7394770` | [Scripts/c7394770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7394770.lua) | 51 |
| Keel, Shipwright Fur Hire | `66736884` | [Scripts/c66736884.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66736884.lua) | 50 |
| Blackwing - Aurora the Northern Lights | `4068622` | [Scripts/c4068622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4068622.lua) | 50 |
| Ghost Mourner & Moonlit Chill | `52038441` | [Scripts/c52038441.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52038441.lua) | 50 |
| Mythical Beast Master Cerberus | `53842431` | [Scripts/c53842431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53842431.lua) | 49 |
| Junk Speeder | `77075360` | [Scripts/c77075360.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77075360.lua) | 49 |
| Salamangreat Pyro Phoenix | `31313405` | [Scripts/c31313405.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31313405.lua) | 49 |
| ...and 297 more |  |  |  |

## Script Examples

### Gishki Nekromirror (`36982581`)

Source: [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua)

```lua
		Duel.BreakEffect()
		if Duel.SpecialSummon(tc,SUMMON_TYPE_RITUAL,tp,tp,false,true,POS_FACEUP)>0 then
			Duel.SetLP(tp,Duel.GetLP(tp)-tc:GetBaseAttack())
			tc:CompleteProcedure()
		end
```

### Performapal Celestial Magician (`58092907`)

Source: [Scripts/c58092907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58092907.lua)

```lua
		e3:SetType(EFFECT_TYPE_SINGLE)
		e3:SetCode(EFFECT_SET_ATTACK_FINAL)
		e3:SetValue(c:GetBaseAttack()*2)
		e3:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_DISABLE+RESET_PHASE+PHASE_END)
		c:RegisterEffect(e3)
```

### Number 38: Hope Harbinger Dragon Titanic Galaxy (`63767246`)

Source: [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63767246.lua)

```lua
end
function c63767246.atkfilter1(c,tp)
	return c:IsReason(REASON_BATTLE+REASON_EFFECT) and c:IsType(TYPE_XYZ) and c:GetBaseAttack()>0
		and c:IsPreviousLocation(LOCATION_MZONE) and c:IsPreviousControler(tp)
end
```
