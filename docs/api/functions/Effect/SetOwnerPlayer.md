# Effect.SetOwnerPlayer

## Signature

```lua
Effect.SetOwnerPlayer(Effect e, int player) -> void
```

## Description

Sets e's owner player to player.
Only player values 0 and 1 are accepted; any other value leaves the effect unchanged.

## Parameters

- `e` `Effect`
- `player` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:630`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **52** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Effect.SetOwnerPlayer`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua) | 69 |
| Fallen Paradise of the Sacred Beasts | `65861210` | [Scripts/c65861210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65861210.lua) | 56 |
| Thunder Dragonlord | `5206415` | [Scripts/c5206415.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5206415.lua) | 54 |
| Raviel, Lord of Phantasms - Shimmering Scraper | `28651380` | [Scripts/c28651380.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28651380.lua) | 51 |
| Deep Sea Prima Donna | `50793215` | [Scripts/c50793215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50793215.lua) | 46 |
| Mystical Elf - White Lightning | `15613529` | [Scripts/c15613529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15613529.lua) | 45 |
| Marincess Bubble Ring | `19712214` | [Scripts/c19712214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19712214.lua) | 45 |
| Marincess Snow | `80627281` | [Scripts/c80627281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80627281.lua) | 45 |
| The Breaking Ruin God | `85182315` | [Scripts/c85182315.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85182315.lua) | 44 |
| Gagaga Head | `67120578` | [Scripts/c67120578.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67120578.lua) | 43 |
| Armed Dragon Thunderbolt | `57605303` | [Scripts/c57605303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57605303.lua) | 43 |
| Phantasm Spiral Assault | `97795930` | [Scripts/c97795930.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97795930.lua) | 43 |
| Noctovision Dragon | `70333910` | [Scripts/c70333910.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70333910.lua) | 42 |
| Aiwass, the Magistus Spell Spirit | `35877582` | [Scripts/c35877582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35877582.lua) | 42 |
| Dimension Fusion Destruction | `89190953` | [Scripts/c89190953.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89190953.lua) | 41 |
| Future Drive | `12508268` | [Scripts/c12508268.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12508268.lua) | 41 |
| Meklord Deflection | `66594927` | [Scripts/c66594927.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66594927.lua) | 41 |
| Battlin' Boxer King Dempsey | `46804536` | [Scripts/c46804536.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46804536.lua) | 40 |
| Gagaku-P.U.N.K. Crash Beat | `17691568` | [Scripts/c17691568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17691568.lua) | 40 |
| Gouki Iron Claw | `71555408` | [Scripts/c71555408.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71555408.lua) | 40 |
| Silent Sword Slash | `18563744` | [Scripts/c18563744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18563744.lua) | 40 |
| Attack of the Cornered Rat | `84389640` | [Scripts/c84389640.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84389640.lua) | 40 |
| Decode Destruction | `33062423` | [Scripts/c33062423.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33062423.lua) | 39 |
| Marincess Wave | `52945066` | [Scripts/c52945066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52945066.lua) | 39 |
| ...and 28 more |  |  |  |

## Script Examples

### Accel Synchro Stardust Dragon (`30983281`)

Source: [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua)

```lua
			e1:SetValue(c30983281.immval)
			e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			e1:SetOwnerPlayer(tp)
			tc:RegisterEffect(e1,true)
			tc:CompleteProcedure()
```

### Fallen Paradise of the Sacred Beasts (`65861210`)

Source: [Scripts/c65861210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65861210.lua)

```lua
				e1:SetReset(RESET_EVENT+RESETS_STANDARD)
				e1:SetValue(s.efilter)
				e1:SetOwnerPlayer(tp)
				tc:RegisterEffect(e1,true)
				if flag then
```

### Thunder Dragonlord (`5206415`)

Source: [Scripts/c5206415.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5206415.lua)

```lua
		e1:SetValue(c5206415.tgoval)
		e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		e1:SetOwnerPlayer(tp)
		tc:RegisterEffect(e1)
	end
```
