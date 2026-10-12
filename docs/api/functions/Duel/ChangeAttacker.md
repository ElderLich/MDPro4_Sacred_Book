# Duel.ChangeAttacker

## Signature

```lua
Duel.ChangeAttacker(Card c, [bool ignore_count]) -> void
```

## Description

Changes the current attacking monster to attacker.
Unless ignore_count is true, the new attacker gains an attack announcement count, and during the Damage Phase also gains attacked-count and attacked-card records.

## Parameters

- `c` `Card`
- `ignore_count` `bool` optional - default: false

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4919`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.ChangeAttacker) with `Duel.ChangeAttacker`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dark Spirit of the Silent | `93599951` | [Scripts/c93599951.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93599951.lua) | 1 |

## Script Examples

### Dark Spirit of the Silent (`93599951`)

Source: [Scripts/c93599951.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93599951.lua)

```lua
			Duel.ChangePosition(tc,POS_FACEUP_ATTACK)
		end
		Duel.ChangeAttacker(tc)
	end
end
```
