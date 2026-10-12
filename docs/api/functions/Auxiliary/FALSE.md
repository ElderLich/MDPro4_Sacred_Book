# Auxiliary.FALSE

## Signature

```lua
Auxiliary.FALSE() -> void
```

## Description

Returns false.

## Source

- `Utilities/utility.lua:94`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **126** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.FALSE) with `Auxiliary.FALSE`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua) | 1 |
| [Eternal Favorite](/examples/cards/87532344) | `87532344` | [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87532344.lua) | 2 |
| [Ultra Polymerization](/examples/cards/76647978) | `76647978` | [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76647978.lua) | 1 |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16306932.lua) | 1 |
| [Enlightenment Dragon](/examples/cards/46186135) | `46186135` | [Scripts/c46186135.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46186135.lua) | 1 |
| Super Duper Polymerization | `44886582` | [Scripts/c44886582.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44886582.lua) | 1 |
| Exosisters Magnifica | `59242457` | [Scripts/c59242457.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59242457.lua) | 1 |
| Phara the Primordial Goddess | `82344137` | [Scripts/c82344137.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82344137.lua) | 1 |
| Chaos Emperor Dragon - Envoy of the End | `82301904` | [Scripts/c82301904.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82301904.lua) | 1 |
| Ma'at | `18631392` | [Scripts/c18631392.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18631392.lua) | 1 |
| Blackwing - Aurora the Northern Lights | `4068622` | [Scripts/c4068622.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4068622.lua) | 1 |
| King's Resonance | `17269895` | [Scripts/c17269895.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17269895.lua) | 1 |
| Royal Straight Slasher | `11020863` | [Scripts/c11020863.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11020863.lua) | 1 |
| Destiny HERO - Plasma | `83965310` | [Scripts/c83965310.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83965310.lua) | 1 |
| Myutant Fusion | `42577802` | [Scripts/c42577802.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42577802.lua) | 1 |
| Super Polymerization | `48130397` | [Scripts/c48130397.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48130397.lua) | 1 |
| Chaos End Ruler - Ruler of the Beginning and the End | `41424250` | [Scripts/c41424250.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41424250.lua) | 1 |
| Knight Armed Dragon, the Armored Knight Dragon | `98007437` | [Scripts/c98007437.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98007437.lua) | 1 |
| Uria, Lord of Searing Flames | `6007213` | [Scripts/c6007213.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6007213.lua) | 1 |
| The Winged Dragon of Ra - Immortal Phoenix | `10000090` | [Scripts/c10000090.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10000090.lua) | 1 |
| Raviel, Lord of Phantasms | `69890967` | [Scripts/c69890967.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69890967.lua) | 1 |
| Lunalight Scarlet Tiger | `11876803` | [Scripts/c11876803.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11876803.lua) | 1 |
| Slifer the Sky Dragon | `10000020` | [Scripts/c10000020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10000020.lua) | 1 |
| Malefic Truth Dragon | `37115575` | [Scripts/c37115575.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37115575.lua) | 1 |
| ...and 102 more |  |  |  |

## Script Examples

### Levia-Dragoon - Daedalus (`78579058`)

Source: [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua)

```lua
	Duel.SetOperationInfo(0,CATEGORY_HANDES_OPPO,nil,0,1-tp,1)
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,1-tp,1)
	Duel.SetChainLimit(aux.FALSE)
end
function s.drop(e,tp,eg,ep,ev,re,r,rp)
```

### Eternal Favorite (`87532344`)

Source: [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87532344.lua)

```lua
	e:SetLabel(1)
	if Duel.GetCurrentChain()==0 then
		Duel.SetChainLimitTillChainEnd(aux.FALSE)
	elseif Duel.GetCurrentChain()==1 then
		e:GetHandler():RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD,0,1)
```

### Ultra Polymerization (`76647978`)

Source: [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76647978.lua)

```lua
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_EXTRA)
	if e:IsHasType(EFFECT_TYPE_ACTIVATE) then
		Duel.SetChainLimit(aux.FALSE)
	end
end
```
