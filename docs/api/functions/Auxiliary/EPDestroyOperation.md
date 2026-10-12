# Auxiliary.EPDestroyOperation

## Signature

```lua
Auxiliary.EPDestroyOperation(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Operation for delayed End Phase destruction effects. It destroys the Card or Group stored as e's label object.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `any`
- `re` `Effect`
- `r` `any`
- `rp` `int`

## Source

- `Utilities/utility.lua:1829`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.EPDestroyOperation) with `Auxiliary.EPDestroyOperation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62091148.lua) | 1 |
| R.B. Lambda Blade | `17188206` | [Scripts/c17188206.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17188206.lua) | 1 |
| Instant Fusion | `1845204` | [Scripts/c1845204.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1845204.lua) | 1 |
| Ritual Foregone | `65450690` | [Scripts/c65450690.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65450690.lua) | 1 |
| Onslaught of the Fire Kings | `22993208` | [Scripts/c22993208.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22993208.lua) | 1 |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
		e2:SetLabelObject(tc)
		e2:SetCondition(s.descon)
		e2:SetOperation(aux.EPDestroyOperation)
		Duel.RegisterEffect(e2,tp)
	end
```

### R.B. Lambda Blade (`17188206`)

Source: [Scripts/c17188206.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17188206.lua)

```lua
		e1:SetLabelObject(tc)
		e1:SetCondition(s.descon)
		e1:SetOperation(aux.EPDestroyOperation)
		Duel.RegisterEffect(e1,tp)
	end
```

### Instant Fusion (`1845204`)

Source: [Scripts/c1845204.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1845204.lua)

```lua
		e2:SetLabelObject(tc)
		e2:SetCondition(c1845204.descon)
		e2:SetOperation(aux.EPDestroyOperation)
		Duel.RegisterEffect(e2,tp)
	end
```
