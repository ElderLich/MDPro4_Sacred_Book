# Card.ReleaseEffectRelation

## Signature

```lua
Card.ReleaseEffectRelation(Card c, Effect e) -> void
```

## Description

Releases c's relation to effect e.

## Parameters

- `c` `Card`
- `e` `Effect`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3560`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.ReleaseEffectRelation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Chaos Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua) | 59 |
| Bait Doll | `7165085` | [Scripts/c7165085.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7165085.lua) | 45 |
| Double Spell | `24096228` | [Scripts/c24096228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24096228.lua) | 40 |

## Script Examples

### Chaos Hats (`2372506`)

Source: [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua)

```lua
		Duel.ChangePosition(tc,POS_FACEDOWN_DEFENSE)
		local ce=Duel.GetChainInfo(ev,CHAININFO_TRIGGERING_EFFECT)
		tc:ReleaseEffectRelation(ce)
	end
	for sc in aux.Next(sg) do
```

### Bait Doll (`7165085`)

Source: [Scripts/c7165085.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7165085.lua)

```lua
				end
				if operation then operation(te,tep,eg,ep,ev,re,r,rp) end
				tc:ReleaseEffectRelation(te)
				tg=g:GetFirst()
				while tg do
```

### Double Spell (`24096228`)

Source: [Scripts/c24096228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24096228.lua)

```lua
		end
	end
	tc:ReleaseEffectRelation(te)
	etc=g:GetFirst()
	while etc do
```
