# Duel.CheckLocation

## Signature

```lua
Duel.CheckLocation(int player, int location, int sequence) -> bool
```

## Description

Checks whether player can use the given sequence in location.
For Pendulum Zone checks, use LOCATION_PZONE with sequence 0 for the left Pendulum Zone or sequence 1 for the right Pendulum Zone.

## Parameters

- `player` `int`
- `location` `int` - Location constant to inspect, such as LOCATION_MZONE, LOCATION_SZONE, or LOCATION_PZONE.
- `sequence` `int` - Sequence inside that location.

## Returns

- `bool` - true if that exact location sequence is usable.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4944`

## Guided Examples

Learn how to use this function in context:

- [Pendulum Procedure Guide](/learn/pendulum-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **104** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.CheckLocation) with `Duel.CheckLocation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [D/D/D/D Dimensional King Arc Crisis](/examples/cards/71398055) | `71398055` | [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71398055.lua) | 2 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6218704.lua) | 6 |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93729065.lua) | 2 |
| Chef de Nouvelles | `29251488` | [Scripts/c29251488.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29251488.lua) | 2 |
| Vaylantz Genesis Grand Duke | `76075139` | [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76075139.lua) | 4 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5148778.lua) | 2 |
| Plunder Patrollship Jord | `85969517` | [Scripts/c85969517.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85969517.lua) | 4 |
| D/D/D Deviser King Deus Machinex | `46593546` | [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46593546.lua) | 2 |
| Arktos XII - Chronochasm Vaylantz | `50687050` | [Scripts/c50687050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50687050.lua) | 4 |
| Odd-Eyes Rebellion Dragon Overlord | `98452268` | [Scripts/c98452268.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98452268.lua) | 2 |
| Nirvana High Paladin | `80896940` | [Scripts/c80896940.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80896940.lua) | 2 |
| Angello Vaalmonica | `3048768` | [Scripts/c3048768.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3048768.lua) | 4 |
| Supreme King Z-ARC - Synchro Universe | `48654267` | [Scripts/c48654267.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48654267.lua) | 2 |
| Clear Wing Fast Dragon | `90036274` | [Scripts/c90036274.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90036274.lua) | 2 |
| Mamonaka the Vaylantz United | `40680521` | [Scripts/c40680521.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40680521.lua) | 6 |
| Supreme King Gate Zero | `96227613` | [Scripts/c96227613.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c96227613.lua) | 2 |
| Dimonno Vaalmonica | `30432463` | [Scripts/c30432463.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30432463.lua) | 4 |
| Supreme King Gate Infinity | `22211622` | [Scripts/c22211622.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22211622.lua) | 2 |
| Magister of Endymion | `66104644` | [Scripts/c66104644.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66104644.lua) | 2 |
| D/D/D Super Doom King Bright Armageddon | `72402069` | [Scripts/c72402069.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72402069.lua) | 2 |
| Master Spirit Tech Force - Pendulum Ruler | `68508433` | [Scripts/c68508433.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c68508433.lua) | 2 |
| Majespecter Draco - Ryu | `3594985` | [Scripts/c3594985.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3594985.lua) | 2 |
| Pendulum Witch | `43502497` | [Scripts/c43502497.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43502497.lua) | 2 |
| Supreme King Z-ARC | `13331639` | [Scripts/c13331639.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13331639.lua) | 2 |
| ...and 80 more |  |  |  |

## Script Examples

### D/D/D/D Dimensional King Arc Crisis (`71398055`)

Source: [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71398055.lua)

```lua
end
function s.pentg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.CheckLocation(tp,LOCATION_PZONE,0) or Duel.CheckLocation(tp,LOCATION_PZONE,1) end
	local c=e:GetHandler()
	if c:IsLocation(LOCATION_GRAVE) then
```

### Odd-Eyes Arcray Dragon (`6218704`)

Source: [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6218704.lua)

```lua
end
function c6218704.settg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return (Duel.CheckLocation(tp,LOCATION_PZONE,0) or Duel.CheckLocation(tp,LOCATION_PZONE,1))
		and Duel.IsExistingMatchingCard(c6218704.setfilter,tp,LOCATION_DECK,0,1,nil) end
end
```

### Starving Venemy Dragon (`93729065`)

Source: [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93729065.lua)

```lua
end
function c93729065.pentg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.CheckLocation(tp,LOCATION_PZONE,0) or Duel.CheckLocation(tp,LOCATION_PZONE,1) end
end
function c93729065.penop(e,tp,eg,ep,ev,re,r,rp)
```
