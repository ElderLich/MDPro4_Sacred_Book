# RushDuel.CanRecover

Alias: `RD.CanRecover`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanRecover(any desc, any player, any recover, any break_effect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可选操作: 回复
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `recover` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:606`

```lua
function RushDuel.CanRecover(desc, player, recover, break_effect)
    if recover > 0 and Duel.SelectYesNo(player, desc) then
        if break_effect then
            Duel.BreakEffect()
        end
        return Duel.Recover(player, recover, REASON_EFFECT)
    end
    return 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CanRecover) with `RushDuel.CanRecover`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Tamabot King Golem | `120285039` | [Rush/Scripts/c120285039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285039.lua) | 1 |
| JAM:P Check! | `120228054` | [Rush/Scripts/c120228054.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228054.lua) | 1 |
| Chemical Cure Purple | `120196030` | [Rush/Scripts/c120196030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120196030.lua) | 1 |
| Absurd Void Hole | `120260021` | [Rush/Scripts/c120260021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260021.lua) | 1 |
| Cosmic Sucker | `120294021` | [Rush/Scripts/c120294021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294021.lua) | 1 |
| Dream Drummer | `120189012` | [Rush/Scripts/c120189012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120189012.lua) | 1 |
| Helpful Items | `120306054` | [Rush/Scripts/c120306054.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306054.lua) | 1 |
| Psypickupper | `120199014` | [Rush/Scripts/c120199014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199014.lua) | 1 |

## Script Examples

### Tamabot King Golem (`120285039`)

Source: [Rush/Scripts/c120285039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285039.lua)

```lua
		local c=e:GetHandler()
		if RD.IsSpecialSummonMainPhase(c,SUMMON_TYPE_FUSION) then
			RD.CanRecover(aux.Stringid(m,3),tp,2000,true)
		end
	end)
```

### JAM:P Check! (`120228054`)

Source: [Rush/Scripts/c120228054.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228054.lua)

```lua
			if Duel.Destroy(sg,REASON_EFFECT)~=0
				and Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_MZONE,0,1,nil) then
				RD.CanRecover(aux.Stringid(m,1),tp,1000)
			end
		end
```

### Chemical Cure Purple (`120196030`)

Source: [Rush/Scripts/c120196030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120196030.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	if RD.Draw()~=0 then
		RD.CanRecover(aux.Stringid(m,1),tp,900,true)
	end
end
```
