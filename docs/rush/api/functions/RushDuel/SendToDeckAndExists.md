# RushDuel.SendToDeckAndExists

Alias: `RD.SendToDeckAndExists`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendToDeckAndExists(any target, any effect, any player, any reason, any filter, any count, any expect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 返回卡组
```

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `effect` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `reason` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:372`

```lua
function RushDuel.SendToDeckAndExists(target, effect, player, reason, filter, count, expect)
    local hints = Group.CreateGroup()
    local group = RushDuel.ToGroup(target):Filter(RushDuel.FilterToDeckTarget, nil, effect, player, reason, hints)
    local g = RushDuel.ToMaximunGroup(group)
    local tc = hints:GetFirst()
    if tc then
        Duel.Hint(HINT_CARD, 0, tc:GetOriginalCode())
    end
    if #g == 0 then
        return false
    end
    return Duel.SendtoDeck(g, nil, SEQ_DECKSHUFFLE, REASON_EFFECT) ~= 0 and RushDuel.IsOperatedGroupExists(filter, count, expect)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **103** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SendToDeckAndExists) with `RushDuel.SendToDeckAndExists`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Analyze Phlogiston](/examples/rush-cards/120226001) | `120226001` | [Rush/Scripts/c120226001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120226001.lua) | 1 |
| [Exchange of the Sheep](/examples/rush-cards/120293030) | `120293030` | [Rush/Scripts/c120293030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293030.lua) | 1 |
| [Mega Jointech Fortrex \[R\]](/examples/rush-cards/120249005) | `120249005` | [Rush/Scripts/c120249005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249005.lua) | 1 |
| [Red-Reboot Enhanced Boost Dragon](/examples/rush-cards/120253037) | `120253037` | [Rush/Scripts/c120253037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253037.lua) | 1 |
| Sevens Road Ultima Witch | `120261045` | [Rush/Scripts/c120261045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261045.lua) | 1 |
| Abysskite Liem | `120249025` | [Rush/Scripts/c120249025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249025.lua) | 1 |
| Qadi of the Monumenthes | `120300009` | [Rush/Scripts/c120300009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300009.lua) | 1 |
| Rising HERO Argent F | `120304043` | [Rush/Scripts/c120304043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304043.lua) | 1 |
| Supreme Railartillery Magnum Overlord \[L\] | `120239001` | [Rush/Scripts/c120239001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239001.lua) | 2 |
| The Trinity Dragiastar | `120109031` | [Rush/Scripts/c120109031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109031.lua) | 1 |
| Poet Fairy | `120208021` | [Rush/Scripts/c120208021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208021.lua) | 2 |
| Destructor Emperor Bakhakaiser | `120264045` | [Rush/Scripts/c120264045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264045.lua) | 1 |
| Steel Mech Lord Mirror Innovator | `120155015` | [Rush/Scripts/c120155015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155015.lua) | 1 |
| Steel Mech Lord Mirror Innovator | `120239059` | [Rush/Scripts/c120239059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239059.lua) | 1 |
| Advance Form | `120261032` | [Rush/Scripts/c120261032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261032.lua) | 1 |
| Excutie Lumière | `120231031` | [Rush/Scripts/c120231031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231031.lua) | 1 |
| Prophecy Flail the Colors of Nature | `120257043` | [Rush/Scripts/c120257043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257043.lua) | 1 |
| Axe Shredder | `120228021` | [Rush/Scripts/c120228021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228021.lua) | 1 |
| CAN - Melo:D | `120203010` | [Rush/Scripts/c120203010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203010.lua) | 1 |
| Guardian Eatos | `120290065` | [Rush/Scripts/c120290065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290065.lua) | 1 |
| Ring of Storms | `120235055` | [Rush/Scripts/c120235055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235055.lua) | 2 |
| Amulet Dragon | `120309085` | [Rush/Scripts/c120309085.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309085.lua) | 1 |
| Fusion Cancel | `120253066` | [Rush/Scripts/c120253066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253066.lua) | 1 |
| Back Jersey | `120228063` | [Rush/Scripts/c120228063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228063.lua) | 1 |
| ...and 79 more |  |  |  |

## Script Examples

### Analyze Phlogiston (`120226001`)

Source: [Rush/Scripts/c120226001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120226001.lua)

```lua
	local check=RD.Check(cm.check,lv)
	RD.SelectGroupAndDoAction(HINTMSG_TODECK,aux.NecroValleyFilter(cm.filter),check,tp,LOCATION_GRAVE,0,3,3,nil,function(sg)
		if RD.SendToDeckAndExists(sg,e,tp,REASON_EFFECT) then
			Duel.BreakEffect()
			Duel.Destroy(g,REASON_EFFECT)
```

### Exchange of the Sheep (`120293030`)

Source: [Rush/Scripts/c120293030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293030.lua)

```lua
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	local mg=Duel.GetMatchingGroup(aux.NecroValleyFilter(Card.IsAbleToDeck),tp,LOCATION_GRAVE,LOCATION_GRAVE,nil)
	if RD.SendToDeckAndExists(mg,e,tp,REASON_EFFECT) then
		if Duel.IsPlayerCanDraw(tp,1) and Duel.SelectYesNo(tp,aux.Stringid(m,1)) then
			local tc=Duel.GetDecktopGroup(tp,1):GetFirst()
```

### Mega Jointech Fortrex [R] (`120249005`)

Source: [Rush/Scripts/c120249005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249005.lua)

```lua
		RD.SelectAndDoAction(HINTMSG_TODECK,aux.NecroValleyFilter(cm.tdfilter),1-tp,0,LOCATION_GRAVE,3,3,nil,function(sg)
			g:Merge(sg)
			if RD.SendToDeckAndExists(g,e,tp,REASON_EFFECT) and c:IsFaceup() and c:IsRelateToEffect(e) and RD.IsMaximumMode(c) then
				local og=Duel.GetOperatedGroup():Filter(cm.exfilter,nil)
				local atk=og:GetSum(Card.GetLevel)*100
```
