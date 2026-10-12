# Effect.GetCost

## Signature

```lua
Effect.GetCost(Effect e) -> function|nil
```

## Description

Returns e's cost function, or nil when no cost function is set.

## Parameters

- `e` `Effect`

## Returns

- `function|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:643`

## Guided Examples

Learn how to use this function in context:

- [Field Spells](/learn/field-spells)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **27** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Effect.GetCost) with `Effect.GetCost`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ghostrick Renovation](/examples/cards/61818176) | `61818176` | [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61818176.lua) | 1 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27693363.lua) | 1 |
| Sea Stealth Attack | `19089195` | [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19089195.lua) | 1 |
| Favorite Hero | `11881272` | [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11881272.lua) | 1 |
| Triamid Dancer | `69529337` | [Scripts/c69529337.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69529337.lua) | 1 |
| Numeron Wall | `42352091` | [Scripts/c42352091.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42352091.lua) | 1 |
| The Sacred Waters in the Sky | `26684111` | [Scripts/c26684111.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26684111.lua) | 1 |
| Triamid Master | `32912040` | [Scripts/c32912040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c32912040.lua) | 1 |
| Performapal Sky Magician | `73734821` | [Scripts/c73734821.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73734821.lua) | 1 |
| Bait Doll | `7165085` | [Scripts/c7165085.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7165085.lua) | 1 |
| Necrovalley Temple | `56773577` | [Scripts/c56773577.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56773577.lua) | 1 |
| Springans Booty | `7496001` | [Scripts/c7496001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7496001.lua) | 1 |
| Triamid Hunter | `95923441` | [Scripts/c95923441.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95923441.lua) | 1 |
| Double Spell | `24096228` | [Scripts/c24096228.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24096228.lua) | 1 |
| F.A. Overheat | `32036866` | [Scripts/c32036866.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c32036866.lua) | 1 |
| Dream Mirror of Joy | `74665651` | [Scripts/c74665651.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74665651.lua) | 1 |
| Vampire Takeover | `22900598` | [Scripts/c22900598.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22900598.lua) | 1 |
| Dream Mirror of Terror | `1050355` | [Scripts/c1050355.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1050355.lua) | 1 |
| Malefic Territory | `75223115` | [Scripts/c75223115.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75223115.lua) | 1 |
| Ignis Heat, the True Dracowarrior | `22499034` | [Scripts/c22499034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22499034.lua) | 1 |
| Dinomight Knight, the True Dracofighter | `58984738` | [Scripts/c58984738.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58984738.lua) | 1 |
| Metaverse | `89208725` | [Scripts/c89208725.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89208725.lua) | 1 |
| Necroworld Banshee | `66570171` | [Scripts/c66570171.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66570171.lua) | 1 |
| Pop-Up | `15248873` | [Scripts/c15248873.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15248873.lua) | 1 |
| ...and 3 more |  |  |  |

## Script Examples

### Ghostrick Renovation (`61818176`)

Source: [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61818176.lua)

```lua
			te:UseCountLimit(tp,1,true)
			local tep=sc:GetControler()
			local cost=te:GetCost()
			if cost then cost(te,tep,eg,ep,ev,re,r,rp,1) end
			Duel.RaiseEvent(sc,4179255,te,0,tp,tp,Duel.GetCurrentChain())
```

### Ursarctic Polari (`27693363`)

Source: [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27693363.lua)

```lua
		te:UseCountLimit(tp,1,true)
		local tep=tc:GetControler()
		local cost=te:GetCost()
		if cost then cost(te,tep,eg,ep,ev,re,r,rp,1) end
		Duel.RaiseEvent(tc,4179255,te,0,tp,tp,Duel.GetCurrentChain())
```

### Sea Stealth Attack (`19089195`)

Source: [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19089195.lua)

```lua
			te:UseCountLimit(tp,1,true)
			local tep=tc:GetControler()
			local cost=te:GetCost()
			if cost then cost(te,tep,eg,ep,ev,re,r,rp,1) end
			if field then
```
