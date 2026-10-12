# Duel.SetChainLimitTillChainEnd

## Signature

```lua
Duel.SetChainLimitTillChainEnd(function f) -> void
```

## Description

Registers a chain-limit callback that persists until the current chain ends.

## Parameters

- `f` `function` - callback: f(e, chain_player, activating_player)

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4888`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **43** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SetChainLimitTillChainEnd) with `Duel.SetChainLimitTillChainEnd`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Eternal Favorite](/examples/cards/87532344) | `87532344` | [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87532344.lua) | 2 |
| [Spellbook of the Grand Circle](/examples/cards/11911336) | `11911336` | [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11911336.lua) | 2 |
| [DoSolfachord Coolia](/examples/cards/80776622) | `80776622` | [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80776622.lua) | 2 |
| Artmage Pact -Awakening- | `23599634` | [Scripts/c23599634.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23599634.lua) | 2 |
| Magikey Dragon - Andrabime | `71159974` | [Scripts/c71159974.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71159974.lua) | 2 |
| Echelon of the Fire Kings | `38798785` | [Scripts/c38798785.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38798785.lua) | 2 |
| Flame Swordsrealm | `73714736` | [Scripts/c73714736.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73714736.lua) | 2 |
| Link into the VRAINS! | `28827503` | [Scripts/c28827503.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28827503.lua) | 1 |
| Fabled Realm's Revival | `57775790` | [Scripts/c57775790.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57775790.lua) | 2 |
| Abyss Actor - Superstar | `25629622` | [Scripts/c25629622.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25629622.lua) | 2 |
| Clown Crew Meteor | `93172951` | [Scripts/c93172951.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93172951.lua) | 2 |
| LaSolfachord Angelia | `27993919` | [Scripts/c27993919.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27993919.lua) | 2 |
| TiSolfachord Beautia | `54387923` | [Scripts/c54387923.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54387923.lua) | 2 |
| Sweet Dreams, Nemleria | `44843954` | [Scripts/c44843954.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44843954.lua) | 2 |
| Dragonroid | `9069157` | [Scripts/c9069157.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9069157.lua) | 2 |
| Arcana Force V - The Hierophant | `3376703` | [Scripts/c3376703.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3376703.lua) | 2 |
| Chaos End Ruler - Ruler of the Beginning and the End | `41424250` | [Scripts/c41424250.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41424250.lua) | 1 |
| SolSolfachord Gracia | `91598270` | [Scripts/c91598270.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c91598270.lua) | 2 |
| Slifer the Sky Dragon | `10000020` | [Scripts/c10000020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10000020.lua) | 1 |
| GMX Lab #5 | `74378580` | [Scripts/c74378580.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74378580.lua) | 2 |
| Stellarknight Delteros | `56638325` | [Scripts/c56638325.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56638325.lua) | 2 |
| Theorealize Past Lull | `36709484` | [Scripts/c36709484.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36709484.lua) | 1 |
| Tri-Brigade Arms Bucephalus II | `10019086` | [Scripts/c10019086.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10019086.lua) | 2 |
| The Winged Dragon of Ra | `10000010` | [Scripts/c10000010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10000010.lua) | 1 |
| ...and 19 more |  |  |  |

## Script Examples

### Eternal Favorite (`87532344`)

Source: [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87532344.lua)

```lua
	e:SetLabel(1)
	if Duel.GetCurrentChain()==0 then
		Duel.SetChainLimitTillChainEnd(aux.FALSE)
	elseif Duel.GetCurrentChain()==1 then
		e:GetHandler():RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD,0,1)
```

### Spellbook of the Grand Circle (`11911336`)

Source: [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11911336.lua)

```lua
	e:SetLabel(1)
	if Duel.GetCurrentChain()==0 then
		Duel.SetChainLimitTillChainEnd(s.chainlm)
	elseif Duel.GetCurrentChain()==1 then
		e:GetHandler():RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD,0,1)
```

### DoSolfachord Coolia (`80776622`)

Source: [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80776622.lua)

```lua
function c80776622.limop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetCurrentChain()==0 then
		Duel.SetChainLimitTillChainEnd(c80776622.chainlm)
	elseif Duel.GetCurrentChain()==1 then
		e:GetHandler():RegisterFlagEffect(80776622,RESET_EVENT+RESETS_STANDARD,0,1)
```
