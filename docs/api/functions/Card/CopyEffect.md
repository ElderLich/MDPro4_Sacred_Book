# Card.CopyEffect

## Signature

```lua
Card.CopyEffect(Card c, int code, int reset, [int count]) -> int
```

## Description

Copies the initial_effect of card code onto c and returns the generated copy id, or -1 if code belongs to a Normal Monster.
reset defaults to RESETS_STANDARD when 0. count defaults to 1; phase resets without a turn side are normalized to both players' turns. If c is a non-Effect Monster, the core also adds TYPE_EFFECT for the same reset.

## Parameters

- `c` `Card`
- `code` `int`
- `reset` `int`
- `count` `int` optional - default: 1

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3621`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **25** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.CopyEffect) with `Card.CopyEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93729065.lua) | 1 |
| Windwitch - Crystal Bell | `25793414` | [Scripts/c25793414.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25793414.lua) | 1 |
| Emperor Charles the Great | `97864322` | [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97864322.lua) | 1 |
| Odd-Eyes Venom Dragon | `45014450` | [Scripts/c45014450.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45014450.lua) | 1 |
| Masterflare Hyperion | `63101468` | [Scripts/c63101468.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63101468.lua) | 1 |
| Raidraptor - Rising Rebellion Falcon | `71222868` | [Scripts/c71222868.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71222868.lua) | 1 |
| Starving Venom Fusion Dragon | `41209827` | [Scripts/c41209827.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41209827.lua) | 1 |
| Blackwing - Aurora the Northern Lights | `4068622` | [Scripts/c4068622.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4068622.lua) | 1 |
| Hundred Eyes Dragon | `95453143` | [Scripts/c95453143.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95453143.lua) | 1 |
| Supreme King Dragon Starving Venom | `43387895` | [Scripts/c43387895.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43387895.lua) | 1 |
| Dragon Knight Draco-Equiste | `14017402` | [Scripts/c14017402.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14017402.lua) | 1 |
| Number 8: Heraldic King Genom-Heritage | `47387961` | [Scripts/c47387961.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c47387961.lua) | 1 |
| CXyz Barian Hope | `67926903` | [Scripts/c67926903.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67926903.lua) | 1 |
| Symphonic Warrior Synthess | `49919798` | [Scripts/c49919798.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49919798.lua) | 1 |
| Elemental HERO Divine Neos | `31111109` | [Scripts/c31111109.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c31111109.lua) | 1 |
| The Tyrant Neptune | `88071625` | [Scripts/c88071625.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88071625.lua) | 1 |
| Phantom of Chaos | `30312361` | [Scripts/c30312361.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30312361.lua) | 1 |
| Number C69: Heraldry Crest of Horror | `11522979` | [Scripts/c11522979.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11522979.lua) | 1 |
| Gem-Knight Master Diamond | `39512984` | [Scripts/c39512984.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39512984.lua) | 1 |
| Neo-Spacian Dark Panther | `43237273` | [Scripts/c43237273.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43237273.lua) | 1 |
| Legendary Knight Hermos | `84565800` | [Scripts/c84565800.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84565800.lua) | 1 |
| Number 69: Heraldry Crest | `2407234` | [Scripts/c2407234.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2407234.lua) | 1 |
| Pseudo Space | `77584012` | [Scripts/c77584012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77584012.lua) | 1 |
| Infernoid Decatron | `58446973` | [Scripts/c58446973.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58446973.lua) | 1 |
| ...and 1 more |  |  |  |

## Script Examples

### Starving Venemy Dragon (`93729065`)

Source: [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93729065.lua)

```lua
		c:RegisterEffect(e1)
		if not tc:IsType(TYPE_TRAPMONSTER) then
			cid=c:CopyEffect(tc:GetOriginalCode(),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,1)
		end
		local e2=Effect.CreateEffect(c)
```

### Windwitch - Crystal Bell (`25793414`)

Source: [Scripts/c25793414.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25793414.lua)

```lua
		c:RegisterEffect(e1)
		if not tc:IsType(TYPE_TRAPMONSTER) then
			cid=c:CopyEffect(code,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,1)
		end
		local e2=Effect.CreateEffect(c)
```

### Emperor Charles the Great (`97864322`)

Source: [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97864322.lua)

```lua
		c:RegisterEffect(e1)
		if tc:GetOriginalType()&TYPE_EFFECT==TYPE_EFFECT then
			c:CopyEffect(code,RESET_EVENT+RESETS_STANDARD)
		end
		if Duel.GetLocationCount(tp,LOCATION_SZONE)>0 and tc:CheckUniqueOnField(tp) and not tc:IsForbidden() then
```
