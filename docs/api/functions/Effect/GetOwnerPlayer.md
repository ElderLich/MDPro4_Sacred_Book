# Effect.GetOwnerPlayer

## Signature

```lua
Effect.GetOwnerPlayer(Effect e) -> int
```

## Description

Returns the player stored as e's owner player.

## Parameters

- `e` `Effect`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:648`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **169** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Effect.GetOwnerPlayer) with `Effect.GetOwnerPlayer`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30983281.lua) | 2 |
| [Melffy Playtime Surprise](/examples/cards/58036097) | `58036097` | [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58036097.lua) | 1 |
| [Enneacraft - Aiza.LEON](/examples/cards/82359538) | `82359538` | [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82359538.lua) | 2 |
| Ancient Gear Duel | `53541822` | [Scripts/c53541822.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53541822.lua) | 1 |
| Dinomorphia Frenzy | `78420796` | [Scripts/c78420796.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78420796.lua) | 1 |
| Miscellaneousaurus | `38572779` | [Scripts/c38572779.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38572779.lua) | 2 |
| Fallen Paradise of the Sacred Beasts | `65861210` | [Scripts/c65861210.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65861210.lua) | 1 |
| Dinomorphia Domain | `26631975` | [Scripts/c26631975.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26631975.lua) | 1 |
| Vanquish Soul Caesar Valius | `91073013` | [Scripts/c91073013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c91073013.lua) | 1 |
| Thunder Dragonlord | `5206415` | [Scripts/c5206415.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5206415.lua) | 1 |
| Chevreuil, Hunting Scout of the Deep Forest | `13023431` | [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13023431.lua) | 1 |
| Cyberdark End Dragon | `37542782` | [Scripts/c37542782.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37542782.lua) | 1 |
| Fairy Tail - Wiccat | `27632520` | [Scripts/c27632520.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27632520.lua) | 1 |
| Red-Eyes Black Dragon Exceed | `17242022` | [Scripts/c17242022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17242022.lua) | 1 |
| Heraldic Beast Stad Whale | `97662494` | [Scripts/c97662494.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97662494.lua) | 1 |
| Black Chaos | `98684220` | [Scripts/c98684220.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98684220.lua) | 1 |
| Raviel, Lord of Phantasms - Shimmering Scraper | `28651380` | [Scripts/c28651380.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28651380.lua) | 1 |
| Shichi-Go-San | `11035075` | [Scripts/c11035075.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11035075.lua) | 1 |
| Exstellarknight Constellar Ptolemy Ω7 | `6195332` | [Scripts/c6195332.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6195332.lua) | 1 |
| Blaze Cannon | `4059313` | [Scripts/c4059313.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4059313.lua) | 1 |
| King's Resonance | `17269895` | [Scripts/c17269895.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17269895.lua) | 1 |
| Combat Wheel | `12501230` | [Scripts/c12501230.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12501230.lua) | 1 |
| Miracle Raven | `18988396` | [Scripts/c18988396.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18988396.lua) | 1 |
| Crystal Clear Wing Synchro Dragon | `59765225` | [Scripts/c59765225.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59765225.lua) | 1 |
| ...and 145 more |  |  |  |

## Script Examples

### Accel Synchro Stardust Dragon (`30983281`)

Source: [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30983281.lua)

```lua
end
function c30983281.immval(e,te)
	return te:GetOwnerPlayer()~=e:GetOwnerPlayer() and te:IsActivated()
end
```

### Melffy Playtime Surprise (`58036097`)

Source: [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58036097.lua)

```lua
end
function s.efilter(e,re)
	return e:GetHandlerPlayer()~=re:GetOwnerPlayer() and re:IsActivated()
end
```

### Enneacraft - Aiza.LEON (`82359538`)

Source: [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82359538.lua)

```lua
	return e:GetHandler():GetFlagEffect(id)>0
		and eg:IsExists(Card.IsControler,1,nil,1-tp) and not Duel.IsChainSolving()
		and re and re:GetOwnerPlayer()==1-tp
end
function s.damop1(e,tp,eg,ep,ev,re,r,rp)
```
