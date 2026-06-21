# Card.GetHandSynchro

## Signature

```lua
Card.GetHandSynchro(Card c) -> nil|Effect,function|nil,int|nil,int|nil
```

## Description

If card c is affected by the hand Synchro effect EFFECT_HAND_SYNCHRO, return Effect e, function target, int min, int max; otherwise return nil

## Parameters

- `c` `Card`

## Returns

- `nil|Effect`
- `function|nil`
- `int|nil`
- `int|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3547`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetHandSynchro`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua) | 69 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua) | 61 |
| Saiba the Soldier Swordsmith | `36608728` | [Scripts/c36608728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36608728.lua) | 57 |
| Naturia Blessing | `34813545` | [Scripts/c34813545.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34813545.lua) | 54 |
| Stand Up Centur-Ion! | `41371602` | [Scripts/c41371602.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41371602.lua) | 49 |
| Re-dyce-cle | `85704698` | [Scripts/c85704698.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85704698.lua) | 48 |
| Etude of the Branded | `45675980` | [Scripts/c45675980.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45675980.lua) | 44 |
| Yang Zing Unleashed | `77783947` | [Scripts/c77783947.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77783947.lua) | 36 |

## Script Examples

### Accel Synchro Stardust Dragon (`30983281`)

Source: [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua)

```lua
	if not (c:IsCode(44508094) and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_SYNCHRO,tp,false,false)) then return false end
	local mg=Duel.GetSynchroMaterial(tp)
	if mg:IsExists(Card.GetHandSynchro,1,nil) then
		local mg2=Duel.GetMatchingGroup(nil,tp,LOCATION_HAND,0,nil)
		if mg2:GetCount()>0 then mg:Merge(mg2) end
```

### Yummy★Snatchy (`30581601`)

Source: [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua)

```lua
		if not Duel.IsPlayerCanSpecialSummon(tp) then return false end
		local mg=Duel.GetSynchroMaterial(tp)
		if mg:IsExists(Card.GetHandSynchro,1,nil) then
			local mg2=Duel.GetMatchingGroup(nil,tp,LOCATION_HAND,0,nil)
			if mg2:GetCount()>0 then mg:Merge(mg2) end
```

### Saiba the Soldier Swordsmith (`36608728`)

Source: [Scripts/c36608728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36608728.lua)

```lua
		if not Duel.IsPlayerCanSpecialSummon(tp) then return false end
		local mg=Duel.GetSynchroMaterial(tp)
		if mg:IsExists(Card.GetHandSynchro,1,nil) then
			local mg2=Duel.GetMatchingGroup(nil,tp,LOCATION_HAND,0,nil)
			if mg2:GetCount()>0 then mg:Merge(mg2) end
```
