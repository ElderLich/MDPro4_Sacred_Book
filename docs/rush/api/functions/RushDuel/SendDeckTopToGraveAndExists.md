# RushDuel.SendDeckTopToGraveAndExists

Alias: `RD.SendDeckTopToGraveAndExists`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendDeckTopToGraveAndExists(any player, any card_count, any filter, any count, any expect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 从卡组上面把卡送去墓地
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `card_count` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:304`

```lua
function RushDuel.SendDeckTopToGraveAndExists(player, card_count, filter, count, expect)
    return Duel.DiscardDeck(player, card_count, REASON_EFFECT) ~= 0 and RushDuel.IsOperatedGroupExists(filter, count, expect)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **120** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SendDeckTopToGraveAndExists) with `RushDuel.SendDeckTopToGraveAndExists`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Vapor Lancer the Super Graphagas](/examples/rush-cards/120260063) | `120260063` | [Rush/Scripts/c120260063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260063.lua) | 1 |
| [Shannah the Clad Dragon Researcher](/examples/rush-cards/120304017) | `120304017` | [Rush/Scripts/c120304017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304017.lua) | 1 |
| Daigyakutenno Megami | `120203019` | [Rush/Scripts/c120203019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120203019.lua) | 1 |
| Galactica Dejavu | `120244003` | [Rush/Scripts/c120244003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244003.lua) | 1 |
| Transam Scride | `120109036` | [Rush/Scripts/c120109036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109036.lua) | 1 |
| Grace Princess Emaki | `120300021` | [Rush/Scripts/c120300021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300021.lua) | 1 |
| Dimension Pramma | `120309026` | [Rush/Scripts/c120309026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309026.lua) | 1 |
| Voidvelg Chrysaor | `120244008` | [Rush/Scripts/c120244008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244008.lua) | 1 |
| Ritche of Hope | `120287072` | [Rush/Scripts/c120287072.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287072.lua) | 1 |
| Destructor Soldier Bokka | `120285015` | [Rush/Scripts/c120285015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285015.lua) | 1 |
| Quick Attack Knight | `120293037` | [Rush/Scripts/c120293037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293037.lua) | 1 |
| Wooly Wonderland Naptime | `120293029` | [Rush/Scripts/c120293029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293029.lua) | 1 |
| Awakened Stegoceratops | `120277018` | [Rush/Scripts/c120277018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277018.lua) | 1 |
| Rainbow-Eyes Star Cat | `120264010` | [Rush/Scripts/c120264010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264010.lua) | 1 |
| Lovely Connect | `120300054` | [Rush/Scripts/c120300054.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300054.lua) | 1 |
| Slay the Star Protector's Gunslinger | `120306010` | [Rush/Scripts/c120306010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306010.lua) | 1 |
| RB Dragophone | `120225032` | [Rush/Scripts/c120225032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120225032.lua) | 1 |
| Koumori Dragon the Magical Dragon | `120309011` | [Rush/Scripts/c120309011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309011.lua) | 1 |
| Animagica Gardna | `120277027` | [Rush/Scripts/c120277027.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277027.lua) | 1 |
| Voidvelg Cataphract | `120235008` | [Rush/Scripts/c120235008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235008.lua) | 1 |
| Wroughtwyvern | `120263011` | [Rush/Scripts/c120263011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120263011.lua) | 1 |
| Lovely Dove | `120260047` | [Rush/Scripts/c120260047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260047.lua) | 1 |
| Constructor Desk Worker Tarasque | `120264014` | [Rush/Scripts/c120264014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264014.lua) | 1 |
| Firefall Wall | `120226032` | [Rush/Scripts/c120226032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120226032.lua) | 1 |
| ...and 96 more |  |  |  |

## Script Examples

### Vapor Lancer the Super Graphagas (`120260063`)

Source: [Rush/Scripts/c120260063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260063.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	if RD.SendDeckTopToGraveAndExists(tp,3) then
		local g=Duel.GetOperatedGroup():Filter(cm.exfilter,nil)
		local ct=g:GetClassCount(Card.GetRace)
```

### Shannah the Clad Dragon Researcher (`120304017`)

Source: [Rush/Scripts/c120304017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304017.lua)

```lua
		if RD.ChangePosition(g,e,tp,REASON_EFFECT,POS_FACEDOWN_DEFENSE) then
			Duel.BreakEffect()
			if RD.SendDeckTopToGraveAndExists(tp,1,cm.exfilter,1,nil) then
				local tc=Duel.GetOperatedGroup():GetFirst()
				if Duel.SelectEffectYesNo(tp,tc,aux.Stringid(m,1)) then
```

### Daigyakutenno Megami (`120203019`)

Source: [Rush/Scripts/c120203019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120203019.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	local p=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER)
	if RD.Draw()~=0 and RD.SendDeckTopToGraveAndExists(p,1,cm.exfilter,1,nil) then
		local tc=Duel.GetOperatedGroup():GetFirst()
		local filter=RD.Filter(cm.desfilter,tc:GetRace())
```
