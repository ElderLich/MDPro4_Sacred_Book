# Card.GetSummonPlayer

## Signature

```lua
Card.GetSummonPlayer(Card c) -> int
```

## Description

Returns the player recorded as having Summoned c.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3475`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **17** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetSummonPlayer`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 1 |
| [Ultimate Crystal Rainbow Dragon Overdrive](/examples/cards/84544192) | `84544192` | [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84544192.lua) | 1 |
| Red Nova Dragon - Burning Soul | `65541655` | [Scripts/c65541655.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65541655.lua) | 1 |
| King's Resonance | `17269895` | [Scripts/c17269895.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17269895.lua) | 1 |
| Nibiru, the Primal Being | `27204311` | [Scripts/c27204311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27204311.lua) | 1 |
| Exosister Returnia | `197042` | [Scripts/c197042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c197042.lua) | 2 |
| Ghoti of the Deep Beyond | `72309040` | [Scripts/c72309040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72309040.lua) | 1 |
| Dark Contract with Patent License | `33814281` | [Scripts/c33814281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33814281.lua) | 1 |
| Armed Dragon Catapult Cannon | `75906310` | [Scripts/c75906310.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75906310.lua) | 2 |
| Ringowurm, the Dragon Guarding the Hundred Apples | `30765615` | [Scripts/c30765615.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30765615.lua) | 1 |
| Jester Confit | `8487449` | [Scripts/c8487449.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8487449.lua) | 1 |
| Trifortressops | `12275533` | [Scripts/c12275533.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12275533.lua) | 1 |
| Qliphort Monolith | `51194046` | [Scripts/c51194046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51194046.lua) | 1 |
| Oh my Trap Hole! | `10529441` | [Scripts/c10529441.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10529441.lua) | 1 |
| Undaunted Bumpkin Beast | `8700633` | [Scripts/c8700633.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8700633.lua) | 1 |
| Crystolic Potential | `3576031` | [Scripts/c3576031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3576031.lua) | 1 |
| Summon Gate | `29724053` | [Scripts/c29724053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29724053.lua) | 1 |

## Script Examples

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
	local tc=g:GetFirst()
	while tc do
		Duel.RegisterFlagEffect(tc:GetSummonPlayer(),55795155,RESET_PHASE+PHASE_END,0,1)
		tc=g:GetNext()
	end
```

### Ultimate Crystal Rainbow Dragon Overdrive (`84544192`)

Source: [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84544192.lua)

```lua
	for tc in aux.Next(eg) do
		if tc:IsSetCard(0x2034) then
			Duel.RegisterFlagEffect(tc:GetSummonPlayer(),id,0,0,0)
		end
	end
```

### Red Nova Dragon - Burning Soul (`65541655`)

Source: [Scripts/c65541655.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65541655.lua)

```lua
	for tc in aux.Next(eg) do
		if tc:IsCode(70902743) and tc:IsSummonType(SUMMON_TYPE_SYNCHRO) then
			Duel.RegisterFlagEffect(tc:GetSummonPlayer(),id,0,0,0)
		end
	end
```
