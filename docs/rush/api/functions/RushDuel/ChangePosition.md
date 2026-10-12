# RushDuel.ChangePosition

Alias: `RD.ChangePosition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ChangePosition(any target, any effect, any player, any reason, any pos) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 改变表示形式
```

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `effect` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `reason` `any`: Type and behavior are not yet reviewed; see the source.
- `pos` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:236`

```lua
function RushDuel.ChangePosition(target, effect, player, reason, pos)
    local hints = Group.CreateGroup()
    local group = RushDuel.ToGroup(target):Filter(RushDuel.FilterChangePositionTarget, nil, effect, player, reason, hints)
    local tc = hints:GetFirst()
    if tc then
        Duel.Hint(HINT_CARD, 0, tc:GetOriginalCode())
    end
    if group:GetCount() > 0 then
        if pos == nil then
            return Duel.ChangePosition(group, POS_FACEUP_DEFENSE, POS_FACEUP_DEFENSE, POS_FACEUP_ATTACK, POS_FACEUP_ATTACK)
        else
            return Duel.ChangePosition(group, pos)
        end
    else
        return 0
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **178** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ChangePosition) with `RushDuel.ChangePosition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Valkyrian Guard](/examples/rush-cards/120231066) | `120231066` | [Rush/Scripts/c120231066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231066.lua) | 1 |
| [Freshberry Collaboration](/examples/rush-cards/120301071) | `120301071` | [Rush/Scripts/c120301071.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301071.lua) | 1 |
| [Fuden Issen](/examples/rush-cards/120309034) | `120309034` | [Rush/Scripts/c120309034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309034.lua) | 1 |
| [Sparkhearts Makma](/examples/rush-cards/120298023) | `120298023` | [Rush/Scripts/c120298023.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298023.lua) | 1 |
| [Imaginary Arc Turbulence](/examples/rush-cards/120196013) | `120196013` | [Rush/Scripts/c120196013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120196013.lua) | 1 |
| [Necromaid Trickment](/examples/rush-cards/120294063) | `120294063` | [Rush/Scripts/c120294063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294063.lua) | 1 |
| [Spice Cross Secret Recipe](/examples/rush-cards/120261060) | `120261060` | [Rush/Scripts/c120261060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261060.lua) | 1 |
| [Curse of the Magiclad Dragon](/examples/rush-cards/120304061) | `120304061` | [Rush/Scripts/c120304061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304061.lua) | 1 |
| [Shannah the Clad Dragon Researcher](/examples/rush-cards/120304017) | `120304017` | [Rush/Scripts/c120304017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304017.lua) | 1 |
| [Galactica Lost Oblivion](/examples/rush-cards/120277042) | `120277042` | [Rush/Scripts/c120277042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277042.lua) | 1 |
| [Heavenly Bliss](/examples/rush-cards/120203033) | `120203033` | [Rush/Scripts/c120203033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120203033.lua) | 1 |
| [Lullalabind](/examples/rush-cards/120246073) | `120246073` | [Rush/Scripts/c120246073.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246073.lua) | 1 |
| [Evolution Result Flash](/examples/rush-cards/120290063) | `120290063` | [Rush/Scripts/c120290063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290063.lua) | 1 |
| [Lovely Wolf](/examples/rush-cards/120260046) | `120260046` | [Rush/Scripts/c120260046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260046.lua) | 1 |
| [Animagica Majesty](/examples/rush-cards/120277063) | `120277063` | [Rush/Scripts/c120277063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277063.lua) | 1 |
| [False Sun](/examples/rush-cards/120264033) | `120264033` | [Rush/Scripts/c120264033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264033.lua) | 1 |
| [Void Veil](/examples/rush-cards/120227029) | `120227029` | [Rush/Scripts/c120227029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120227029.lua) | 1 |
| Plasmatic Model Smart Owl | `120285019` | [Rush/Scripts/c120285019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285019.lua) | 1 |
| Blaze Fiend Overlord Zebulth | `120287033` | [Rush/Scripts/c120287033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287033.lua) | 1 |
| Transam Scride | `120109036` | [Rush/Scripts/c120109036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109036.lua) | 1 |
| Hysteric Eyes | `120304063` | [Rush/Scripts/c120304063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304063.lua) | 1 |
| Yamiterasu the Divine Ruler | `120199036` | [Rush/Scripts/c120199036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199036.lua) | 1 |
| Ether Escape | `120235062` | [Rush/Scripts/c120235062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235062.lua) | 1 |
| Intercepting Gaia | `120249061` | [Rush/Scripts/c120249061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249061.lua) | 1 |
| ...and 154 more |  |  |  |

## Script Examples

### Valkyrian Guard (`120231066`)

Source: [Rush/Scripts/c120231066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231066.lua)

```lua
		local filter=RD.Filter(cm.posfilter,e,tp)
		RD.CanSelectGroupAndDoAction(aux.Stringid(m,1),HINTMSG_POSCHANGE,filter,cm.poscheck,tp,LOCATION_MZONE,0,1,3,nil,function(g)
			if RD.ChangePosition(g,e,tp,REASON_EFFECT,POS_FACEUP_DEFENSE)~=0 then
				local og=Duel.GetOperatedGroup()
				og:ForEach(function(tc)
```

### Freshberry Collaboration (`120301071`)

Source: [Rush/Scripts/c120301071.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301071.lua)

```lua
	local filter=RD.Filter(cm.filter,e,tp)
	RD.SelectAndDoAction(HINTMSG_POSCHANGE,filter,tp,LOCATION_MZONE,0,1,1,nil,function(g)
		if RD.ChangePosition(g,e,tp,REASON_EFFECT,POS_FACEUP_DEFENSE)~=0 and e:GetLabel()==1 then
			RD.CanSelectAndDoAction(aux.Stringid(m,1),HINTMSG_DESTROY,cm.desfilter,tp,0,LOCATION_MZONE,1,1,nil,function(sg)
				Duel.Destroy(sg,REASON_EFFECT)
```

### Fuden Issen (`120309034`)

Source: [Rush/Scripts/c120309034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309034.lua)

```lua
	local filter=RD.Filter(cm.filter,e,tp)
	RD.SelectAndDoAction(HINTMSG_SET,filter,tp,0,LOCATION_MZONE,1,1,nil,function(g)
		if RD.ChangePosition(g,e,tp,REASON_EFFECT,POS_FACEDOWN_DEFENSE)~=0
			and Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_MZONE,0,1,nil)
			and Duel.SelectEffectYesNo(tp,g:GetFirst(),aux.Stringid(m,1)) then
```
