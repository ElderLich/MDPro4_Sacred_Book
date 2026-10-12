# Auxiliary.EnableMulcharmyGlobalCheck

## Signature

```lua
Auxiliary.EnableMulcharmyGlobalCheck() -> void
```

## Description

Installs the shared Mulcharmy activation-count watcher once per Duel process.
The watcher listens to EVENT_CHAINING and registers player flag 84192580 through the End Phase whenever that player activates a monster effect from set 0x1b2.
Mulcharmy monster scripts call this from initial_effect, then check Duel.GetFlagEffect(tp,84192580)&lt;=1 as part of their hand-activation condition.

## Source

- `Utilities/utility.lua:2053`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.EnableMulcharmyGlobalCheck) with `Auxiliary.EnableMulcharmyGlobalCheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Mulcharmy Purulia | `84192580` | [Scripts/c84192580.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84192580.lua) | 1 |
| Mulcharmy Fuwalos | `42141493` | [Scripts/c42141493.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42141493.lua) | 1 |
| Mulcharmy Meowls | `87126721` | [Scripts/c87126721.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87126721.lua) | 1 |

## Script Examples

### Mulcharmy Purulia (`84192580`)

Source: [Scripts/c84192580.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84192580.lua)

```lua
local s,id,o=GetID()
function s.initial_effect(c)
	aux.EnableMulcharmyGlobalCheck()
	--draw
	local e1=Effect.CreateEffect(c)
```

### Mulcharmy Fuwalos (`42141493`)

Source: [Scripts/c42141493.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42141493.lua)

```lua
local s,id,o=GetID()
function s.initial_effect(c)
	aux.EnableMulcharmyGlobalCheck()
	--draw
	local e1=Effect.CreateEffect(c)
```

### Mulcharmy Meowls (`87126721`)

Source: [Scripts/c87126721.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87126721.lua)

```lua
local s,id,o=GetID()
function s.initial_effect(c)
	aux.EnableMulcharmyGlobalCheck()
	--draw
	local e1=Effect.CreateEffect(c)
```
