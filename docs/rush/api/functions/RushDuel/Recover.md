# RushDuel.Recover

Alias: `RD.Recover`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.Recover(any player, any recover) -> any
```

## Description

Rush Duel helper declared in `RDTarget.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
对玩家效果: 恢复 - 结算
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `recover` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDTarget.lua:39`

```lua
function RushDuel.Recover(player, recover)
    local p, d = Duel.GetChainInfo(0, CHAININFO_TARGET_PLAYER, CHAININFO_TARGET_PARAM)
    return Duel.Recover(player or p, recover or d, REASON_EFFECT)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **36** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.Recover) with `RushDuel.Recover`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Grace Princess Kaori | `120287018` | [Rush/Scripts/c120287018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287018.lua) | 1 |
| Prime Dian Keto | `120257007` | [Rush/Scripts/c120257007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257007.lua) | 1 |
| CAN:D LIVE | `120199035` | [Rush/Scripts/c120199035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199035.lua) | 1 |
| Dian Keto the Food Prodigy | `120260064` | [Rush/Scripts/c120260064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260064.lua) | 1 |
| Wooly Wonderland Wave Schaf | `120222026` | [Rush/Scripts/c120222026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120222026.lua) | 1 |
| Lifeline Linac | `120244058` | [Rush/Scripts/c120244058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244058.lua) | 1 |
| Healthie Elizalamilla | `120306041` | [Rush/Scripts/c120306041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306041.lua) | 1 |
| Cosmic Sucker | `120294021` | [Rush/Scripts/c120294021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294021.lua) | 1 |
| Master's Cure | `120217068` | [Rush/Scripts/c120217068.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217068.lua) | 1 |
| Phoenix Dragoon | `120252008` | [Rush/Scripts/c120252008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120252008.lua) | 1 |
| Requesting 9 | `120199061` | [Rush/Scripts/c120199061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199061.lua) | 1 |
| Towline Cattle Healer | `120290026` | [Rush/Scripts/c120290026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290026.lua) | 1 |
| Abysskite Mapping | `120257052` | [Rush/Scripts/c120257052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257052.lua) | 1 |
| Chemical Cure Red | `120196031` | [Rush/Scripts/c120196031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120196031.lua) | 1 |
| Dian Keto the Cleaning Prodigy | `120260065` | [Rush/Scripts/c120260065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260065.lua) | 1 |
| Chemipet Purr | `120249009` | [Rush/Scripts/c120249009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249009.lua) | 1 |
| Offering to Isyria | `120300047` | [Rush/Scripts/c120300047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300047.lua) | 1 |
| Draco the Doctor | `120294003` | [Rush/Scripts/c120294003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294003.lua) | 1 |
| Chemical Cure Blue | `120155017` | [Rush/Scripts/c120155017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120155017.lua) | 1 |
| Double-Doom Dragon | `120235011` | [Rush/Scripts/c120235011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235011.lua) | 1 |
| Hungry Softserve | `120290019` | [Rush/Scripts/c120290019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290019.lua) | 1 |
| Excutie Plawtie | `120231037` | [Rush/Scripts/c120231037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231037.lua) | 1 |
| Party Up | `120217067` | [Rush/Scripts/c120217067.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217067.lua) | 1 |
| Hydration | `120170047` | [Rush/Scripts/c120170047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170047.lua) | 1 |
| ...and 12 more |  |  |  |

## Script Examples

### Grace Princess Kaori (`120287018`)

Source: [Rush/Scripts/c120287018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287018.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	if RD.Recover()~=0 then
		RD.CanSelectAndDoAction(aux.Stringid(m,2),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),tp,LOCATION_GRAVE,0,1,1,nil,function(g)
			Duel.BreakEffect()
```

### Prime Dian Keto (`120257007`)

Source: [Rush/Scripts/c120257007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257007.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	if RD.Recover()~=0 then
		local c=e:GetHandler()
		if c:IsFaceup() and c:IsRelateToEffect(e) then
```

### CAN:D LIVE (`120199035`)

Source: [Rush/Scripts/c120199035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199035.lua)

```lua
end
function cm.operation2(e,tp,eg,ep,ev,re,r,rp)
	if RD.Recover()~=0 then
		RD.CanSelectAndSpecialSummon(aux.Stringid(m,4),aux.NecroValleyFilter(cm.spfilter),tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEUP,true)
	end
```
