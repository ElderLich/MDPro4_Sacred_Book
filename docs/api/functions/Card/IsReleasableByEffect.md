# Card.IsReleasableByEffect

## Signature

```lua
Card.IsReleasableByEffect(Card c) -> bool
```

## Description

Checks whether c can be Released by the current resolving effect, using the current reason player and reason effect.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3596`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **43** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsReleasableByEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua) | 73 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua) | 63 |
| Gishki Nekromirror | `36982581` | [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua) | 59 |
| Sosei Ryu-Ge Mistva | `92487128` | [Scripts/c92487128.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92487128.lua) | 54 |
| Megalith Anastasis | `29876299` | [Scripts/c29876299.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29876299.lua) | 54 |
| Subterror Nemesis Warrior | `16719140` | [Scripts/c16719140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16719140.lua) | 51 |
| Clockwork Knight | `41739381` | [Scripts/c41739381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41739381.lua) | 49 |
| Buerillabaisse de Nouvelles | `26223582` | [Scripts/c26223582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26223582.lua) | 48 |
| Angry Burger | `28306253` | [Scripts/c28306253.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28306253.lua) | 48 |
| Renewal of the World | `81306186` | [Scripts/c81306186.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81306186.lua) | 48 |
| V-LAN Hydra | `13536606` | [Scripts/c13536606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13536606.lua) | 48 |
| Baelgrill de Nouvelles | `88890658` | [Scripts/c88890658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88890658.lua) | 47 |
| Neo Galaxy-Eyes Photon Dragon - Photon Howling | `28331069` | [Scripts/c28331069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28331069.lua) | 47 |
| Nibiru, the Primal Being | `27204311` | [Scripts/c27204311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27204311.lua) | 47 |
| Albion the Sanctifire Dragon | `38811586` | [Scripts/c38811586.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38811586.lua) | 46 |
| Balameuniere de Nouvelles | `52495649` | [Scripts/c52495649.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52495649.lua) | 44 |
| Predaplant Ambulomelides | `66309175` | [Scripts/c66309175.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66309175.lua) | 44 |
| Megalith Notrah Plura | `44293356` | [Scripts/c44293356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44293356.lua) | 43 |
| Starving Venom Predapower Fusion Dragon | `39915560` | [Scripts/c39915560.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39915560.lua) | 43 |
| Starry Knight Orbitael | `44818` | [Scripts/c44818.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44818.lua) | 43 |
| Foie Glasya de Nouvelles | `15001940` | [Scripts/c15001940.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15001940.lua) | 42 |
| Confiras de Nouvelles | `53618197` | [Scripts/c53618197.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53618197.lua) | 42 |
| Witchcrafter Marka | `6071005` | [Scripts/c6071005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6071005.lua) | 42 |
| Prima Light | `2507443` | [Scripts/c2507443.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2507443.lua) | 42 |
| ...and 19 more |  |  |  |

## Script Examples

### Surprise Fusion (`35167375`)

Source: [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua)

```lua
end
function s.cfilter(c,tp,chk)
	return c:IsType(TYPE_FUSION) and c:IsReleasableByEffect() and (not chk
		or (Duel.GetMZoneCount(tp,c)>1 and not Duel.IsPlayerAffectedByEffect(tp,59822133)
			and Duel.IsPlayerCanSpecialSummonMonster(tp,id+o,0,TYPES_TOKEN_MONSTER,0,0,c:GetLevel(),RACE_SPELLCASTER,ATTRIBUTE_DARK)))
```

### D/D Count Surveyor (`5997110`)

Source: [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua)

```lua
	local sg=g:Clone()
	sg:Sub(Group.FromCards(c))
	return sg:FilterCount(Card.IsReleasableByEffect,nil)==2
end
function s.crlfilteer(c,e)
```

### Gishki Nekromirror (`36982581`)

Source: [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua)

```lua
end
function c36982581.cfilter(c,e,tp)
	return c:IsFaceup() and not c:IsImmuneToEffect(e) and c:IsReleasableByEffect() and c:IsControler(tp)
end
function c36982581.target(e,tp,eg,ep,ev,re,r,rp,chk)
```
