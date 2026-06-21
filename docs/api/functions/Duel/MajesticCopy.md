# Duel.MajesticCopy

## Signature

```lua
Duel.MajesticCopy(Card c1, Card c2) -> void
```

## Description

Salvation Star Dragon dedicated. Copy the effect described in c2 to c1
Forced to launch the effect can choose whether to launch

## Parameters

- `c1` `Card`
- `c2` `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5073`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.MajesticCopy`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Majestic Star Dragon | `7841112` | [Scripts/c7841112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7841112.lua) | 49 |

## Script Examples

### Majestic Star Dragon (`7841112`)

Source: [Scripts/c7841112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7841112.lua)

```lua
		e2:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		tc:RegisterEffect(e2)
		Duel.MajesticCopy(c,tc)
	end
end
```
