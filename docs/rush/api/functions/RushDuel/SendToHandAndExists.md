# RushDuel.SendToHandAndExists

Alias: `RD.SendToHandAndExists`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendToHandAndExists(Card|Group|Effect target, Effect effect, int player, int reason, [function|nil filter], [int count], [Card|Group|nil expect]) -> bool
```

## Description

Moves the supplied Card/Group/Effect handler toward its owner hand after applying the Rush EFFECT_CANNOT_TO_HAND_EFFECT protection filter and expanding Maximum components. After movement, confirms relevant cards from Deck/GY/banishment to the opponent.
The reason argument is forwarded to the Rush protection checks, but this pinned implementation calls Duel.SendtoHand with REASON_EFFECT unconditionally. It is not a generic cost-payment helper. player controls protection/confirmation context, not a forced hand destination: the native destination argument is nil.
Returns false if the eligible Group is empty or the core movement count is zero. Otherwise returns true when filter is nil, or checks at least count matching cards in Duel.GetOperatedGroup while excluding expect. This is a boolean, not a count, and the default does not prove every selected card reached the hand.

## Parameters

- `target` `Card|Group|Effect`: Cards to move; Effect input means its handler.
- `effect` `Effect`: Source effect used by Rush protection checks; required.
- `player` `int`: Player used for protection and confirmation context.
- `reason` `int`: Reason passed to protection checks; actual movement is always REASON_EFFECT in this snapshot.
- `filter` `function|nil` (optional): Optional predicate checked against the operated Group.
- `count` `int` (optional): Required match count when filter is supplied.
- `expect` `Card|Group|nil` (optional): Exclusion for the operated-Group check.

## Returns

- `bool`: Whether movement was nonzero and the optional operated-Group check passed.

## Source

`Rush/Utilities/RDAction.lua:277`

```lua
function RushDuel.SendToHandAndExists(target, effect, player, reason, filter, count, expect)
    local hints = Group.CreateGroup()
    local group = RushDuel.ToGroup(target):Filter(RushDuel.FilterToHandTarget, nil, effect, player, reason, hints)
    local g = RushDuel.ToMaximunGroup(group)
    local tc = hints:GetFirst()
    if tc then
        Duel.Hint(HINT_CARD, 0, tc:GetOriginalCode())
    end
    if #g == 0 then
        return false
    end
    if Duel.SendtoHand(g, nil, REASON_EFFECT) == 0 then
        return false
    end
    local cg = g:Filter(RushDuel.FilterToHandConfirm, nil, player)
    if #cg > 0 then
        Duel.ConfirmCards(1 - player, cg)
    end
    return RushDuel.IsOperatedGroupExists(filter, count, expect)
end
```

## Guided Examples

Learn how to use this function in context:

- [Rush Special Summons And Result Types](/learn/rush-special-summon-results)

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **496** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SendToHandAndExists) with `RushDuel.SendToHandAndExists`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lufer the Symbol of the Devils](/examples/rush-cards/120309059) | `120309059` | [Rush/Scripts/c120309059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309059.lua) | 1 |
| [Skysavior Watch](/examples/rush-cards/120235053) | `120235053` | [Rush/Scripts/c120235053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235053.lua) | 1 |
| [Voidalfr Star Mayfly](/examples/rush-cards/120300034) | `120300034` | [Rush/Scripts/c120300034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300034.lua) | 1 |
| [Brassdes of the Wicked Wheels](/examples/rush-cards/120304033) | `120304033` | [Rush/Scripts/c120304033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304033.lua) | 1 |
| [Miracle Pick](/examples/rush-cards/120253052) | `120253052` | [Rush/Scripts/c120253052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253052.lua) | 1 |
| [Pot of Duality](/examples/rush-cards/120271002) | `120271002` | [Rush/Scripts/c120271002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271002.lua) | 1 |
| [Vapor Lancer the Super Graphagas](/examples/rush-cards/120260063) | `120260063` | [Rush/Scripts/c120260063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260063.lua) | 1 |
| [Ember the Ultra Assistant](/examples/rush-cards/120283035) | `120283035` | [Rush/Scripts/c120283035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283035.lua) | 1 |
| [Sparkhearts Makma](/examples/rush-cards/120298023) | `120298023` | [Rush/Scripts/c120298023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298023.lua) | 1 |
| [Fairy of the Stars](/examples/rush-cards/120305016) | `120305016` | [Rush/Scripts/c120305016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305016.lua) | 1 |
| [Rising Protect](/examples/rush-cards/120304055) | `120304055` | [Rush/Scripts/c120304055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304055.lua) | 1 |
| [Tubardiche the Music Princess](/examples/rush-cards/120247025) | `120247025` | [Rush/Scripts/c120247025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247025.lua) | 1 |
| [Moonforce Sheila](/examples/rush-cards/120300013) | `120300013` | [Rush/Scripts/c120300013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300013.lua) | 1 |
| [Spiritualization Training](/examples/rush-cards/120301020) | `120301020` | [Rush/Scripts/c120301020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301020.lua) | 1 |
| [Dimension Oper](/examples/rush-cards/120309025) | `120309025` | [Rush/Scripts/c120309025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309025.lua) | 1 |
| [Lovely Wolf](/examples/rush-cards/120260046) | `120260046` | [Rush/Scripts/c120260046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260046.lua) | 1 |
| [False Sun](/examples/rush-cards/120264033) | `120264033` | [Rush/Scripts/c120264033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264033.lua) | 1 |
| [Void Veil](/examples/rush-cards/120227029) | `120227029` | [Rush/Scripts/c120227029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120227029.lua) | 1 |
| [Voidvelg Gehennamagia](/examples/rush-cards/120109048) | `120109048` | [Rush/Scripts/c120109048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109048.lua) | 1 |
| [Preferlyre](/examples/rush-cards/120283046) | `120283046` | [Rush/Scripts/c120283046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283046.lua) | 1 |
| [Handy Girl](/examples/rush-cards/120290012) | `120290012` | [Rush/Scripts/c120290012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290012.lua) | 1 |
| [Botonaginata the Music Princess](/examples/rush-cards/120290009) | `120290009` | [Rush/Scripts/c120290009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290009.lua) | 1 |
| [Soleil, the Fairy of Skysavior](/examples/rush-cards/120235020) | `120235020` | [Rush/Scripts/c120235020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235020.lua) | 1 |
| [Crystal Seer](/examples/rush-cards/120109067) | `120109067` | [Rush/Scripts/c120109067.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109067.lua) | 1 |
| ...and 472 more |  |  |  |

## Script Examples

### Lufer the Symbol of the Devils (`120309059`)

Source: [Rush/Scripts/c120309059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309059.lua)

```lua
		if Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_GRAVE,0,1,nil) then
			RD.CanSelectAndDoAction(aux.Stringid(m,5),HINTMSG_RTOHAND,cm.thfilter,tp,0,LOCATION_MZONE,1,1,nil,function(sg)
				RD.SendToHandAndExists(sg,e,tp,REASON_EFFECT)
			end)
		end
```

### Skysavior Watch (`120235053`)

Source: [Rush/Scripts/c120235053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235053.lua)

```lua
		Duel.DisableShuffleCheck()
		if tc:IsAbleToHand() then
			RD.SendToHandAndExists(sg,e,p,REASON_EFFECT)
			Duel.ShuffleHand(p)
		else
```

### Voidalfr Star Mayfly (`120300034`)

Source: [Rush/Scripts/c120300034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300034.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectAndDoAction(HINTMSG_RTOHAND,cm.filter,tp,0,LOCATION_MZONE,1,3,nil,function(g)
		RD.SendToHandAndExists(g,e,tp,REASON_EFFECT)
	end)
	if Duel.GetFlagEffect(tp,m)~=0 then return end
```
