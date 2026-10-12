# Card.IsAbleToGraveAsCost

## Signature

```lua
Card.IsAbleToGraveAsCost(Card c) -> bool
```

## Description

Checks whether c can be sent to the Graveyard as a cost.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3648`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **705** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsAbleToGraveAsCost) with `Card.IsAbleToGraveAsCost`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua) | 1 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua) | 1 |
| [Eternal Favorite](/examples/cards/87532344) | `87532344` | [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87532344.lua) | 1 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27693363.lua) | 1 |
| [Barian's Chaos Draw](/examples/cards/97769122) | `97769122` | [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97769122.lua) | 1 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62714453.lua) | 1 |
| [Transonic Bird](/examples/cards/34072799) | `34072799` | [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34072799.lua) | 1 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21140872.lua) | 1 |
| Regenesis Birth | `27781371` | [Scripts/c27781371.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27781371.lua) | 2 |
| Isolde, Two Tales of the Noble Knights | `59934749` | [Scripts/c59934749.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59934749.lua) | 1 |
| Black Dragon Ninja | `56562619` | [Scripts/c56562619.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56562619.lua) | 2 |
| Flame Swordsrealm | `73714736` | [Scripts/c73714736.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73714736.lua) | 1 |
| Power Tool Braver Dragon | `63265554` | [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63265554.lua) | 1 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93053159.lua) | 1 |
| Meklord Astro Mekanikle | `63468625` | [Scripts/c63468625.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63468625.lua) | 2 |
| Ursarctic Grand Chariot | `80086070` | [Scripts/c80086070.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80086070.lua) | 1 |
| Zoroa, the Magistus Verethragna | `37260677` | [Scripts/c37260677.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37260677.lua) | 1 |
| Koa'ki Meiru Rooklord | `10060427` | [Scripts/c10060427.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10060427.lua) | 1 |
| Emperor Charles the Great | `97864322` | [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97864322.lua) | 1 |
| Toadally Awesome | `90809975` | [Scripts/c90809975.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90809975.lua) | 1 |
| Ojamatch | `38395123` | [Scripts/c38395123.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38395123.lua) | 1 |
| Witchcrafter Pittore | `95245544` | [Scripts/c95245544.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95245544.lua) | 2 |
| Witchcrafter Genni | `64756282` | [Scripts/c64756282.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64756282.lua) | 2 |
| All-Eyes Phantom Dragon | `70335319` | [Scripts/c70335319.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70335319.lua) | 1 |
| ...and 681 more |  |  |  |

## Script Examples

### Levia-Dragoon - Daedalus (`78579058`)

Source: [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua)

```lua
end
function s.costfilter(c)
	return c:IsFaceup() and c:IsCode(22702055) and c:IsAbleToGraveAsCost()
end
function s.drcon(e,tp,eg,ep,ev,re,r,rp)
```

### Azure Ocean Dragon Lord - Neo-Daedalus Rage (`41570943`)

Source: [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua)

```lua
end
function s.costfilter(c)
	return c:IsFaceup() and c:IsCode(22702055) and c:IsAbleToGraveAsCost()
end
function s.tgcost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Eternal Favorite (`87532344`)

Source: [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87532344.lua)

```lua
	local c=e:GetHandler()
	if chk==0 then return Duel.IsExistingMatchingCard(Card.IsDiscardable,tp,LOCATION_HAND,0,1,e:GetHandler())
		and c:IsAbleToGraveAsCost() and c:IsStatus(STATUS_EFFECT_ENABLED) end
	Duel.DiscardHand(tp,Card.IsDiscardable,1,1,REASON_COST+REASON_DISCARD)
	Duel.SendtoGrave(c,REASON_COST)
```
