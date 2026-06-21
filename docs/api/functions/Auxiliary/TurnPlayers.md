# Auxiliary.TurnPlayers

## Signature

```lua
Auxiliary.TurnPlayers() -> function
```

## Description

Returns an iterator that yields the current turn player first, then the other player.

## Returns

- `function` - Iterator that yields the turn player, then the other player.

## Source

- `Utilities/utility.lua:68`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.TurnPlayers`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Radiant Typhoon Varuroon, the Marine Eidolon](/examples/cards/39341885) | `39341885` | [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39341885.lua) | 61 |
| Plunder Patrollship Jord | `85969517` | [Scripts/c85969517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85969517.lua) | 58 |
| S:P Little Knight | `29301450` | [Scripts/c29301450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29301450.lua) | 58 |
| Cynet Refresh | `36368606` | [Scripts/c36368606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36368606.lua) | 49 |
| Bone Temple Block | `47778083` | [Scripts/c47778083.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47778083.lua) | 46 |
| The Revived Sky God | `59094601` | [Scripts/c59094601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59094601.lua) | 39 |
| Dark Magical Curtain | `41350417` | [Scripts/c41350417.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41350417.lua) | 38 |
| Dice Dungeon | `11808215` | [Scripts/c11808215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11808215.lua) | 31 |
| Destructive Daruma Karma Cannon | `30748475` | [Scripts/c30748475.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30748475.lua) | 20 |

## Script Examples

### Radiant Typhoon Varuroon, the Marine Eidolon (`39341885`)

Source: [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39341885.lua)

```lua
	local tg=g:Filter(Card.IsRelateToEffect,nil,e):Filter(s.mvfilter2,nil,e)
	local pg=Group.CreateGroup()
	for p in aux.TurnPlayers() do
		local sg=tg:Filter(s.isowner,nil,p)
		local ct=Duel.GetLocationCount(p,LOCATION_SZONE)
```

### Plunder Patrollship Jord (`85969517`)

Source: [Scripts/c85969517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85969517.lua)

```lua
		return
	end
	for p in aux.TurnPlayers() do
		local token=Duel.CreateToken(tp,id+o)
		local e1=Effect.CreateEffect(c)
```

### S:P Little Knight (`29301450`)

Source: [Scripts/c29301450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29301450.lua)

```lua
	if #g<=0 then return end
	Duel.Hint(HINT_CARD,0,id)
	for p in aux.TurnPlayers() do
		local tg=g:Filter(Card.IsPreviousControler,nil,p)
		local ft=Duel.GetLocationCount(p,LOCATION_MZONE)
```
