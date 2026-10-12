# RushDuel.IsCanBeSpecialSummoned

Alias: `RD.IsCanBeSpecialSummoned`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanBeSpecialSummoned(Card card, Effect effect, int player, int position) -> bool
```

## Description

Calls card:IsCanBeSpecialSummoned(effect,0,player,false,false,position). This is a legality predicate for an ordinary effect Special Summon to that player, with neither summoning conditions nor revive limits bypassed.
It does not check or reserve a free zone. If the destination player differs from the summoning player, use the native Card.IsCanBeSpecialSummoned arguments that match the later operation.

## Parameters

- `card` `Card`: Monster to check.
- `effect` `Effect`: Summoning effect.
- `player` `int`: Summoning player and default destination player.
- `position` `int`: Position mask to match the later summon.

## Returns

- `bool`: Whether the native per-card summon check passes.

## Source

`Rush/Utilities/RDCondition.lua:126`

```lua
function RushDuel.IsCanBeSpecialSummoned(card, effect, player, position)
    return card:IsCanBeSpecialSummoned(effect, 0, player, false, false, position)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **449** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanBeSpecialSummoned) with `RushDuel.IsCanBeSpecialSummoned`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Nativity of the Monarchs](/examples/rush-cards/120244063) | `120244063` | [Rush/Scripts/c120244063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244063.lua) | 1 |
| [Instant Gift](/examples/rush-cards/120306059) | `120306059` | [Rush/Scripts/c120306059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306059.lua) | 2 |
| [Valkyrian Guard](/examples/rush-cards/120231066) | `120231066` | [Rush/Scripts/c120231066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231066.lua) | 1 |
| [Dark-Guiding Kuriboh](/examples/rush-cards/120280009) | `120280009` | [Rush/Scripts/c120280009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120280009.lua) | 1 |
| [Major Breaking News!](/examples/rush-cards/120304060) | `120304060` | [Rush/Scripts/c120304060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304060.lua) | 1 |
| [Exchange of the Sheep](/examples/rush-cards/120293030) | `120293030` | [Rush/Scripts/c120293030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293030.lua) | 1 |
| [Dark Renewal](/examples/rush-cards/120285066) | `120285066` | [Rush/Scripts/c120285066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285066.lua) | 1 |
| [Magical Retribution](/examples/rush-cards/120254028) | `120254028` | [Rush/Scripts/c120254028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254028.lua) | 1 |
| [Gold Rush](/examples/rush-cards/120247059) | `120247059` | [Rush/Scripts/c120247059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247059.lua) | 1 |
| [Curse of the Magiclad Dragon](/examples/rush-cards/120304061) | `120304061` | [Rush/Scripts/c120304061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304061.lua) | 1 |
| [Hybridrive Back Fusion](/examples/rush-cards/120261052) | `120261052` | [Rush/Scripts/c120261052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261052.lua) | 1 |
| [Jinzo the Machine Menace](/examples/rush-cards/120257028) | `120257028` | [Rush/Scripts/c120257028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257028.lua) | 1 |
| [Rescue Rabbit](/examples/rush-cards/120109057) | `120109057` | [Rush/Scripts/c120109057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109057.lua) | 1 |
| [Lullalabind](/examples/rush-cards/120246073) | `120246073` | [Rush/Scripts/c120246073.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246073.lua) | 1 |
| [YXZ-Cannon Dragon](/examples/rush-cards/120305004) | `120305004` | [Rush/Scripts/c120305004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305004.lua) | 1 |
| [Evolution Result Flash](/examples/rush-cards/120290063) | `120290063` | [Rush/Scripts/c120290063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290063.lua) | 1 |
| [Star Protector Recapture](/examples/rush-cards/120306063) | `120306063` | [Rush/Scripts/c120306063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306063.lua) | 1 |
| [Devil Foolish](/examples/rush-cards/120244026) | `120244026` | [Rush/Scripts/c120244026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244026.lua) | 1 |
| [Sunset Rebirth](/examples/rush-cards/120257066) | `120257066` | [Rush/Scripts/c120257066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257066.lua) | 1 |
| [Grace Princess Hina](/examples/rush-cards/120287020) | `120287020` | [Rush/Scripts/c120287020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287020.lua) | 1 |
| [Necromaid Timer](/examples/rush-cards/120294014) | `120294014` | [Rush/Scripts/c120294014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294014.lua) | 1 |
| [Chemicalizer Wing](/examples/rush-cards/120272057) | `120272057` | [Rush/Scripts/c120272057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272057.lua) | 1 |
| [Star Cat Destronya](/examples/rush-cards/120235037) | `120235037` | [Rush/Scripts/c120235037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235037.lua) | 1 |
| [Road Servant Flare](/examples/rush-cards/120109050) | `120109050` | [Rush/Scripts/c120109050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109050.lua) | 1 |
| ...and 425 more |  |  |  |

## Script Examples

### Nativity of the Monarchs (`120244063`)

Source: [Rush/Scripts/c120244063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244063.lua)

```lua
end
function cm.spfilter(c,e,tp)
	return c:IsLevelAbove(5) and RD.IsDefense(c,1000) and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP_ATTACK)
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```

### Instant Gift (`120306059`)

Source: [Rush/Scripts/c120306059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306059.lua)

```lua
function cm.chkfilter(c,e,tp,fc)
	return aux.IsMaterialListCode(fc,c:GetFusionCode())
		and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP)
end
function cm.spfilter(c,e,tp,code)
```

### Valkyrian Guard (`120231066`)

Source: [Rush/Scripts/c120231066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231066.lua)

```lua
end
function cm.spfilter(c,e,tp)
	return c:IsLevel(4) and c:IsRace(RACE_SPELLCASTER) and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP_ATTACK)
end
function cm.posfilter(c,e,tp)
```
