# Duel.NegateAttack

## Signature

```lua
Duel.NegateAttack() -> bool
```

## Description

Attempts to negate the current attack and returns whether the attack was successfully negated.
The core fails if there is no valid current attacker, if the attacker moved or changed field ID, if the attacker cannot attack, if the Damage Step state blocks attack negation, or if the attacker is not affected by the resolving effect.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4960`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **124** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.NegateAttack`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Magnet Warrior Sigma Minus | `87814728` | [Scripts/c87814728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87814728.lua) | 54 |
| Doodlebook - Uh uh uh! | `94113093` | [Scripts/c94113093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94113093.lua) | 52 |
| Smile Action | `47870325` | [Scripts/c47870325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47870325.lua) | 51 |
| Magician of Hope | `67865534` | [Scripts/c67865534.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67865534.lua) | 50 |
| Performapal Turn Trooper | `220414` | [Scripts/c220414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c220414.lua) | 50 |
| Don Thousand's Throne | `93238626` | [Scripts/c93238626.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93238626.lua) | 49 |
| Shooting Star Dragon T.G. EX | `63180841` | [Scripts/c63180841.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63180841.lua) | 49 |
| Parasite Paranoid | `14457896` | [Scripts/c14457896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14457896.lua) | 48 |
| Summon Reactor ・SK | `89493368` | [Scripts/c89493368.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89493368.lua) | 48 |
| Performapal Odd-Eyes Butler | `56677752` | [Scripts/c56677752.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56677752.lua) | 47 |
| Red Nova Dragon/Assault Mode | `82323997` | [Scripts/c82323997.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82323997.lua) | 47 |
| Amaze Attraction Viking Vortex | `97182396` | [Scripts/c97182396.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97182396.lua) | 47 |
| Beetrooper Light Flapper | `88962829` | [Scripts/c88962829.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88962829.lua) | 46 |
| Performapal Duelist Extraordinaire | `92644052` | [Scripts/c92644052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92644052.lua) | 45 |
| Shooting Star Dragon | `24696097` | [Scripts/c24696097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24696097.lua) | 45 |
| Marincess Bubble Ring | `19712214` | [Scripts/c19712214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19712214.lua) | 45 |
| The Door of Destiny | `27062594` | [Scripts/c27062594.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27062594.lua) | 44 |
| Legacy of the Duelist | `88851326` | [Scripts/c88851326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88851326.lua) | 44 |
| Artmage Varnish -Alteration- | `74011784` | [Scripts/c74011784.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74011784.lua) | 43 |
| Cosmic Blazar Dragon | `21123811` | [Scripts/c21123811.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21123811.lua) | 43 |
| Light Law Medium | `52253888` | [Scripts/c52253888.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52253888.lua) | 42 |
| Turn Silence | `5786513` | [Scripts/c5786513.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5786513.lua) | 42 |
| Raging Storm Dragon - Beaufort IX | `8836329` | [Scripts/c8836329.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8836329.lua) | 42 |
| Battlin' Boxer Chief Second | `47921178` | [Scripts/c47921178.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47921178.lua) | 41 |
| ...and 100 more |  |  |  |

## Script Examples

### Magnet Warrior Sigma Minus (`87814728`)

Source: [Scripts/c87814728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87814728.lua)

```lua
end
function s.atkop(e,tp,eg,ep,ev,re,r,rp)
	Duel.NegateAttack()
end
```

### Doodlebook - Uh uh uh! (`94113093`)

Source: [Scripts/c94113093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94113093.lua)

```lua
end
function c94113093.negop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.NegateAttack() then
		local g=Duel.GetMatchingGroup(aux.NecroValleyFilter(c94113093.spfilter),tp,LOCATION_GRAVE,0,nil,e,tp)
		local ct=Duel.GetLocationCount(tp,LOCATION_MZONE)
```

### Smile Action (`47870325`)

Source: [Scripts/c47870325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47870325.lua)

```lua
				if Duel.SendtoGrave(tc,REASON_EFFECT+REASON_DISCARD)~=0 then
					res=true
					Duel.NegateAttack()
				end
			end
```
