# Function Translation Review

This queue tracks function pages whose English should be reviewed by hand. It is stricter than the generator backlog: imported English can be technically present but still read like a rough machine translation.

## Summary

- Total functions: **998**
- Functions used by current scripts: **753**
- Functions with raw Chinese text in English fields: **0**
- Functions queued for natural-English review: **392**

## English Status Counts

| Status | Count |
| --- | ---: |
| `imported_from_dataeditorx` | 392 |
| `translated_exact` | 606 |

## Priority Review Queue

Sorted by current script usage count so the most visible function pages are reviewed first.

| Function | Status | Script Uses | Current English Preview |
| --- | --- | ---: | --- |
| [`Duel.GetFirstMatchingCard`](/api/functions/Duel/GetFirstMatchingCard) | `imported_from_dataeditorx` | 85 | Filter function to return to the specified location to meet the filter condition f and not equal to the first card ex The sixth parameter starts as an extra parameter |
| [`Card.IsFusionAttribute`](/api/functions/Card/IsFusionAttribute) | `imported_from_dataeditorx` | 84 | Check if card c, when used as Fusion Material \[for a Fusion Summon by player\], has Attribute attribute |
| [`Duel.GetActivityCount`](/api/functions/Duel/GetActivityCount) | `imported_from_dataeditorx` | 83 | Returns the number of times the player performed the corresponding activity_type operation The activity_type is of the following type ACTIVITY_SUMMON call (not includi... |
| [`Effect.UseCountLimit`](/api/functions/Effect/UseCountLimit) | `imported_from_dataeditorx` | 83 | Manually reduce player p's available activation count for effect e by count \[oath_only indicates whether the effect is EFFECT_FLAG_OATH\] |
| [`Card.GetOriginalRace`](/api/functions/Card/GetOriginalRace) | `imported_from_dataeditorx` | 82 | Returns the c of the card record race |
| [`Card.GetOverlayCount`](/api/functions/Card/GetOverlayCount) | `imported_from_dataeditorx` | 82 | Returns the number of cards currently stacked |
| [`Card.IsCanAddCounter`](/api/functions/Card/IsCanAddCounter) | `imported_from_dataeditorx` | 82 | Check if c can place count counters of type countertype \[singly = true\] |
| [`Duel.SetLP`](/api/functions/Duel/SetLP) | `imported_from_dataeditorx` | 82 | Set the player's current LP to lp |
| [`Auxiliary.AddFusionProcCodeFun`](/api/functions/Auxiliary/AddFusionProcCodeFun) | `imported_from_dataeditorx` | 80 | For the c designated card number for the code and cc meet the conditions of the monster f fusion material |
| [`Duel.AnnounceNumber`](/api/functions/Duel/AnnounceNumber) | `imported_from_dataeditorx` | 77 | Let the player player declare a number Starting with the second argument, each parameter represents a declarable number The first return value is the number of declara... |
| [`Card.GetBaseDefense`](/api/functions/Card/GetBaseDefense) | `imported_from_dataeditorx` | 76 | Return to the original c of the defense |
| [`Card.SetSPSummonOnce`](/api/functions/Card/SetSPSummonOnce) | `imported_from_dataeditorx` | 76 | Set c can only be a round of a special call (they reveal, wave dragon) The same spsummon_code shares 1 number of times |
| [`Card.IsPreviousSetCard`](/api/functions/Card/IsPreviousSetCard) | `imported_from_dataeditorx` | 75 | Check whether the name c contains a setname before the c position changes |
| [`Duel.IsAbleToEnterBP`](/api/functions/Duel/IsAbleToEnterBP) | `imported_from_dataeditorx` | 75 | Check whether the player can enter the combat phase of the round |
| [`Duel.CheckTribute`](/api/functions/Duel/CheckTribute) | `imported_from_dataeditorx` | 74 | Check if there are min \[to max\] Tributes on the field \[or in mg\] for Normal Summoning c \[to toplayer's field in zone\] |
| [`Effect.GetActivateLocation`](/api/functions/Effect/GetActivateLocation) | `imported_from_dataeditorx` | 73 | Returns the firing area of ​​the effect e |
| [`Card.AddMonsterAttribute`](/api/functions/Card/AddMonsterAttribute) | `imported_from_dataeditorx` | 72 | Add the monster value to the trap card Note: Values ​​recorded in the database are treated as the original value, and are set to zero here |
| [`Card.GetPreviousTypeOnField`](/api/functions/Card/GetPreviousTypeOnField) | `imported_from_dataeditorx` | 72 | Returns the type before the c position change |
| [`Duel.GetFieldCard`](/api/functions/Duel/GetFieldCard) | `imported_from_dataeditorx` | 72 | Back to player The player's field is located in the location number seq card, commonly used to obtain the field area · Spirit pendulum area card |
| [`Card.GetOriginalAttribute`](/api/functions/Card/GetOriginalAttribute) | `imported_from_dataeditorx` | 71 | Returns the attributes of the card that c is describing |
| [`Duel.SelectTribute`](/api/functions/Duel/SelectTribute) | `imported_from_dataeditorx` | 71 | Let the player player \[from the mg\] choose the min-max sacrifices that are normally used to summon c, ex = true to allow the monster on the other side of the field (th... |
| [`Auxiliary.bdocon`](/api/functions/Auxiliary/bdocon) | `imported_from_dataeditorx` | 70 | Check if e:GetHandler() is related to the current battle, typically used for EVENT_BATTLE_DESTROYING and when battling an opponent's monster, as a condition function A... |
| [`Card.IsCanBeXyzMaterial`](/api/functions/Card/IsCanBeXyzMaterial) | `imported_from_dataeditorx` | 69 | Check whether c can become an excessive monster sc excess material |
| [`Card.GetPreviousControler`](/api/functions/Card/GetPreviousControler) | `imported_from_dataeditorx` | 68 | Returns the controller before the position change of c |
| [`Card.GetEquipGroup`](/api/functions/Card/GetEquipGroup) | `imported_from_dataeditorx` | 63 | Returns the current set of cards |
| [`Card.GetLinkedGroup`](/api/functions/Card/GetLinkedGroup) | `imported_from_dataeditorx` | 61 | Return the group of cards in the zones linked to card c |
| [`Card.GetLinkedZone`](/api/functions/Card/GetLinkedZone) | `imported_from_dataeditorx` | 60 | Return the \[from player's perspective on the field\] Link Zones of card c |
| [`Card.GetPreviousSequence`](/api/functions/Card/GetPreviousSequence) | `imported_from_dataeditorx` | 59 | Returns the sequence number before the c position changes |
| [`Duel.ChainAttack`](/api/functions/Duel/ChainAttack) | `imported_from_dataeditorx` | 59 | So that the attack card \[or card c\] can be carried out an attack (opening up, the queen of the Queen) |
| [`Duel.IsCanRemoveCounter`](/api/functions/Duel/IsCanRemoveCounter) | `imported_from_dataeditorx` | 59 | Checks whether the player player can remove count objects of the countertype type on the farm for reason reasons S represents the position of the player's own removabl... |
| [`Duel.SortDecktop`](/api/functions/Duel/SortDecktop) | `imported_from_dataeditorx` | 59 | Let the player sort_player on the player target_player card group at the top count card sort |
| [`Duel.RemoveCounter`](/api/functions/Duel/RemoveCounter) | `imported_from_dataeditorx` | 58 | Causes the player player to remove count objects of the countertype type present on the farm for reason reasons. The return value indicates success S represents the po... |
| [`Duel.TossDice`](/api/functions/Duel/TossDice) | `imported_from_dataeditorx` | 58 | Let the player to cast count1 dice\[, 1-player to vote count2 dice\] (count1 + count2 &lt;= 5) The return value is count1 + count2 results, 1-6 |
| [`Card.IsLinkAttribute`](/api/functions/Card/IsLinkAttribute) | `imported_from_dataeditorx` | 56 | Check if card c, when used as Link Material \[for a Link Summon by player\], has Attribute attribute |
| [`Card.IsOriginalCodeRule`](/api/functions/Card/IsOriginalCodeRule) | `imported_from_dataeditorx` | 56 | Check if card c is treated as code under the rules |
| [`Duel.GetBattleMonster`](/api/functions/Duel/GetBattleMonster) | `imported_from_dataeditorx` | 56 | Return the monster controlled by player currently in battle; returns nil if there is no battle or no target |
| [`Duel.SkipPhase`](/api/functions/Duel/SkipPhase) | `imported_from_dataeditorx` | 56 | Skip player phase phase player, and in a specific stage after reset, reset parameters and the same effect |
| [`Card.GetPreviousRaceOnField`](/api/functions/Card/GetPreviousRaceOnField) | `imported_from_dataeditorx` | 55 | Returns the race before the c position changes |
| [`Card.CreateEffectRelation`](/api/functions/Card/CreateEffectRelation) | `imported_from_dataeditorx` | 54 | For the card c and the effect of e to establish contact |
| [`Card.GetLink`](/api/functions/Card/GetLink) | `imported_from_dataeditorx` | 54 | Return the Link Marker count of card c |
| [`Card.IsAttackable`](/api/functions/Card/IsAttackable) | `imported_from_dataeditorx` | 54 | Check whether c can attack |
| [`Card.SetStatus`](/api/functions/Card/SetStatus) | `imported_from_dataeditorx` | 54 | Set or cancel the status code for c Do not use this function unless you clearly understand the meaning of each status code |
| [`Duel.AnnounceAttribute`](/api/functions/Duel/AnnounceAttribute) | `imported_from_dataeditorx` | 53 | Let the player player declare count attributes from the optional attribute Available is the combined value of all optional attributes |
| [`Group.GetMaxGroup`](/api/functions/Group/GetMaxGroup) | `imported_from_dataeditorx` | 53 | F is the function that returns an interger value, and the card with the largest value of f is selected from g The second return value is the maximum value, starting wi... |
| [`bit.bor`](/api/functions/bit/bor) | `imported_from_dataeditorx` | 52 | A or b |
| [`Card.IsDefenseAbove`](/api/functions/Card/IsDefenseAbove) | `imported_from_dataeditorx` | 52 | Check c is defensive def above |
| [`Effect.SetOwnerPlayer`](/api/functions/Effect/SetOwnerPlayer) | `imported_from_dataeditorx` | 52 | Set the OwnerPlayer property to player |
| [`Auxiliary.imval1`](/api/functions/Auxiliary/imval1) | `imported_from_dataeditorx` | 51 | Simplified method for the filter function preventing a card from being targeted for attacks, used in effect registration for SetValue function aux.imval1(e, c) return... |
| [`Card.GetReasonEffect`](/api/functions/Card/GetReasonEffect) | `imported_from_dataeditorx` | 50 | Returns the effect that causes the position of c to change |
| [`Card.GetTurnID`](/api/functions/Card/GetTurnID) | `imported_from_dataeditorx` | 50 | Return c The round to the current position |
| [`Card.IsDisabled`](/api/functions/Card/IsDisabled) | `imported_from_dataeditorx` | 50 | Check whether c is in an invalid state |
| [`Duel.NegateSummon`](/api/functions/Duel/NegateSummon) | `imported_from_dataeditorx` | 50 | So that the call is being summoned · reverse call special summoned targets invalid |
| [`Duel.SelectDisableField`](/api/functions/Duel/SelectDisableField) | `imported_from_dataeditorx` | 50 | Let the player player select the specified position to meet the marker condition filter count of the available space, and return to select the location of the marker C... |
| [`Duel.IsPlayerCanSpecialSummonCount`](/api/functions/Duel/IsPlayerCanSpecialSummonCount) | `imported_from_dataeditorx` | 49 | Check whether the player player special call count times |
| [`Card.CheckEquipTarget`](/api/functions/Card/CheckEquipTarget) | `imported_from_dataeditorx` | 48 | Check whether c2 is the correct equipment object for c1 |
| [`Card.GetOriginalCodeRule`](/api/functions/Card/GetOriginalCodeRule) | `imported_from_dataeditorx` | 48 | Returns the codename on the c rule (used as a card rule on this card) |
| [`Auxiliary.chainreg`](/api/functions/Auxiliary/chainreg) | `imported_from_dataeditorx` | 47 | Used by Dark Armed Dragon (81059524), equivalent to function aux.chainreg(e, tp, eg, ep, ev, re, r, rp) if e:GetHandler():GetFlagEffect(1)==0 then e:GetHandler():Regis... |
| [`Duel.EnableGlobalFlag`](/api/functions/Duel/EnableGlobalFlag) | `imported_from_dataeditorx` | 47 | Set the global flag global_flag |
| [`Duel.TossCoin`](/api/functions/Duel/TossCoin) | `imported_from_dataeditorx` | 47 | Let the player player cast count (&lt;= 5) coins, the return value for the count results, 0 or 1. |
| [`Card.GetColumnGroup`](/api/functions/Card/GetColumnGroup) | `imported_from_dataeditorx` | 46 | Return the group of cards in the same column as card c, excluding c, the last two parameters include all cards in the left columns and right columns from c For example... |
| [`Card.GetReason`](/api/functions/Card/GetReason) | `imported_from_dataeditorx` | 46 | Returns the position change reason for c |
| [`Card.IsDefenseBelow`](/api/functions/Card/IsDefenseBelow) | `imported_from_dataeditorx` | 46 | Check whether c is defensive def below (at least 0) |
| [`Card.IsFusionCode`](/api/functions/Card/IsFusionCode) | `imported_from_dataeditorx` | 46 | Check the c as a fusion material can be used as the card number for the code card |
| [`Auxiliary.EnableDualAttribute`](/api/functions/Auxiliary/EnableDualAttribute) | `imported_from_dataeditorx` | 45 | Add double for the c monster attributes |
| [`Card.GetPreviousEquipTarget`](/api/functions/Card/GetPreviousEquipTarget) | `imported_from_dataeditorx` | 45 | Returns the device object before c |
| [`Duel.CheckRemoveOverlayCard`](/api/functions/Duel/CheckRemoveOverlayCard) | `imported_from_dataeditorx` | 45 | Check if the player can remove at least count cards for the specified reason |
| [`Auxiliary.IsMaterialListCode`](/api/functions/Auxiliary/IsMaterialListCode) | `imported_from_dataeditorx` | 44 | Check if card c lists card code as a material in its material list |
| [`Card.IsChainAttackable`](/api/functions/Card/IsChainAttackable) | `imported_from_dataeditorx` | 44 | Check whether c can be a continuous attack, c the number of attacks declared&gt; = ac return false Note: This function returns false when c has made multiple attacks due... |
| [`Auxiliary.IsDualState`](/api/functions/Auxiliary/IsDualState) | `imported_from_dataeditorx` | 43 | Check the double monster e: GetHandler () is re-call state Commonly used in the double monster re-summoned to obtain the effect of e Condition attribute |
| [`Auxiliary.mzctcheckrel`](/api/functions/Auxiliary/mzctcheckrel) | `imported_from_dataeditorx` | 43 | Check if there is space in mzone after tp releases g by reason |
| [`Duel.SetChainLimitTillChainEnd`](/api/functions/Duel/SetChainLimitTillChainEnd) | `imported_from_dataeditorx` | 43 | Same as Duel.SetChainLimit, but the chain limit set by this function persists until the chain ends |
| [`Duel.IsDamageCalculated`](/api/functions/Duel/IsDamageCalculated) | `imported_from_dataeditorx` | 42 | Used to check if damage has been calculated during the damage phase |
| [`Duel.RDComplete`](/api/functions/Duel/RDComplete) | `imported_from_dataeditorx` | 42 | In the call Duel.Damage / Duel.Recover, if is_step parameter is true, you need to call this function when the trigger point |
| [`Card.IsReleasableByEffect`](/api/functions/Card/IsReleasableByEffect) | `imported_from_dataeditorx` | 41 | Check whether c can be liberated by the effect |
| [`Duel.AdjustInstantly`](/api/functions/Duel/AdjustInstantly) | `imported_from_dataeditorx` | 40 | Manually refreshing the card's inactive state on card \[affected by card c\] |
| [`Auxiliary.EnableSpiritReturn`](/api/functions/Auxiliary/EnableSpiritReturn) | `imported_from_dataeditorx` | 39 | Add an effect to c for Spirit Monsters to return to the hand during the End Phase of turns when events event1,... occur |
| [`Card.ResetFlagEffect`](/api/functions/Card/ResetFlagEffect) | `imported_from_dataeditorx` | 39 | Manually clear the type of c is the code of the identification effect |
| [`Duel.RemoveOverlayCard`](/api/functions/Duel/RemoveOverlayCard) | `imported_from_dataeditorx` | 39 | Let the player remove the min-max overlay card at the specified location for the reason reason. The return value indicates success |
| [`Effect.IsHasCategory`](/api/functions/Effect/IsHasCategory) | `imported_from_dataeditorx` | 38 | Check whether the effect contains cate |
| [`Card.GetTurnCounter`](/api/functions/Card/GetTurnCounter) | `imported_from_dataeditorx` | 37 | Returns the round counter for c |
| [`Card.IsLink`](/api/functions/Card/IsLink) | `imported_from_dataeditorx` | 37 | Check if card c's Link Marker count is link1 \[, or link2...\] |
| [`Card.IsSynchroType`](/api/functions/Card/IsSynchroType) | `imported_from_dataeditorx` | 37 | Check if card c, when used as Synchro Material, has type type (unlike IsType, for monster cards in the Spell/Trap Zone, it uses their original type for judgment) |
| [`Duel.ClearOperationInfo`](/api/functions/Duel/ClearOperationInfo) | `imported_from_dataeditorx` | 37 | Clear the OperationInfo of chain chainc; used for cases like Fallen Angel copying and using Graveyard effects, where card effects should not be responded to |
| [`Duel.ShuffleExtra`](/api/functions/Duel/ShuffleExtra) | `imported_from_dataeditorx` | 37 | Manually shuffle player's Extra Deck |
| [`Auxiliary.AddRitualProcGreaterCode`](/api/functions/Auxiliary/AddRitualProcGreaterCode) | `imported_from_dataeditorx` | 36 | Add a Ritual Summon effect for c code is the card code of the Ritual Monster; the sum of the Ritual Levels of the materials can exceed the original Level of the Ritual... |
| [`Card.SetTurnCounter`](/api/functions/Card/SetTurnCounter) | `imported_from_dataeditorx` | 36 | Set c of the round counter (light of the sword, etc.) |
| [`Auxiliary.AddSynchroMixProcedure`](/api/functions/Auxiliary/AddSynchroMixProcedure) | `imported_from_dataeditorx` | 35 | Add a Synchro Summon procedure for c f1, f2, f3 are filter conditions satisfied by 1 card each, f4 is a filter condition satisfied by minc \[to maxc\] cards At least one... |
| [`Auxiliary.nzatk`](/api/functions/Auxiliary/nzatk) | `imported_from_dataeditorx` | 35 | Simplified method for the filter function for face-up monsters with non-zero ATK function aux.nzatk(c) return c:IsFaceup() and c:GetAttack()&gt;0 end |
| [`Card.SetCounterLimit`](/api/functions/Card/SetCounterLimit) | `imported_from_dataeditorx` | 35 | Set c to place the upper limit of countertype type counters |
| [`Group.CheckWithSumEqual`](/api/functions/Group/CheckWithSumEqual) | `imported_from_dataeditorx` | 35 | The subset summation decision function, f, is a function that returns an interger value Check whether there is a subset of min-max in g that satisfies that the sum of... |
| [`Duel.IsPlayerCanRemove`](/api/functions/Duel/IsPlayerCanRemove) | `imported_from_dataeditorx` | 32 | Check whether the player player except c |
| [`Duel.AnnounceCard`](/api/functions/Duel/AnnounceCard) | `imported_from_dataeditorx` | 31 | Let players declare a player \[type type\] card code |
| [`Duel.RaiseSingleEvent`](/api/functions/Duel/RaiseSingleEvent) | `imported_from_dataeditorx` | 31 | To eg, ep, ev, re, r, rp for the card ec trigger a single point in time |
| [`Auxiliary.CreateChecks`](/api/functions/Auxiliary/CreateChecks) | `imported_from_dataeditorx` | 30 | Create a table of filter functions |
| [`Auxiliary.RitualCheck`](/api/functions/Auxiliary/RitualCheck) | `imported_from_dataeditorx` | 30 | \|"'Greater'" \|"'Equal'" |
| [`Card.IsXyzSummonable`](/api/functions/Card/IsXyzSummonable) | `imported_from_dataeditorx` | 30 | Check whether mg can be selected in the \[min-max months\] excessive material on the c to call the excess procedure If mg is nil, this function has the same effect as Ca... |
| [`Duel.XyzSummon`](/api/functions/Duel/XyzSummon) | `imported_from_dataeditorx` | 30 | Let the player player \[from the mg\] \[choose min-max a material\] on the c to call the excess procedure Mg is not empty and min is 0 mg directly to all the excess material |
| [`Auxiliary.bdogcon`](/api/functions/Auxiliary/bdogcon) | `imported_from_dataeditorx` | 29 | Check if e:GetHandler() is related to the current battle, typically used for EVENT_BATTLE_DESTROYING, when battling an opponent's monster and destroying it by battle,... |
| [`Card.GetEquipCount`](/api/functions/Card/GetEquipCount) | `imported_from_dataeditorx` | 29 | Returns the number of cards currently loaded |
| [`Card.GetFirstCardTarget`](/api/functions/Card/GetFirstCardTarget) | `imported_from_dataeditorx` | 29 | Returns c the current first persistent object |
| [`Duel.ChangeTargetCard`](/api/functions/Duel/ChangeTargetCard) | `imported_from_dataeditorx` | 29 | The chain chainc the object into g |
| [`Card.RemoveCounter`](/api/functions/Card/RemoveCounter) | `imported_from_dataeditorx` | 28 | Let the player player remove count counters of type c on c with reason |
| [`Duel.CalculateDamage`](/api/functions/Duel/CalculateDamage) | `imported_from_dataeditorx` | 28 | Let c1 and c2 combat damage calculation |
| [`Effect.GetProperty`](/api/functions/Effect/GetProperty) | `imported_from_dataeditorx` | 28 | Returns the Property property |
| [`Auxiliary.SetUnionState`](/api/functions/Auxiliary/SetUnionState) | `imported_from_dataeditorx` | 27 | Add Union Monster attributes to c |
| [`Card.IsLinkAbove`](/api/functions/Card/IsLinkAbove) | `imported_from_dataeditorx` | 27 | Check if card c's Link Marker count is link or higher |
| [`Card.IsSummonableCard`](/api/functions/Card/IsSummonableCard) | `imported_from_dataeditorx` | 27 | Check whether c is a card that can be called normally |
| [`Duel.AnnounceRace`](/api/functions/Duel/AnnounceRace) | `imported_from_dataeditorx` | 27 | Let the player player declare count races from the optional races Available is the combined value of all the optional races |
| [`Duel.ChangeAttackTarget`](/api/functions/Duel/ChangeAttackTarget) | `imported_from_dataeditorx` | 27 | Will attack the object into c, c for nil that direct attack, the return value indicates whether the successful transfer of attack objects |
| [`Duel.IsPlayerCanSpecialSummon`](/api/functions/Duel/IsPlayerCanSpecialSummon) | `imported_from_dataeditorx` | 27 | Check player player can special summon \[c to target_player field to sumtype summation, sumpos form\] If optional parameters are required, they must all be used |
| [`Duel.ResetFlagEffect`](/api/functions/Duel/ResetFlagEffect) | `imported_from_dataeditorx` | 27 | Manually reset the player player's specific logo effect |
| [`Duel.SelectPosition`](/api/functions/Duel/SelectPosition) | `imported_from_dataeditorx` | 27 | Let player player select the representation of c and return |
| [`Effect.GetCost`](/api/functions/Effect/GetCost) | `imported_from_dataeditorx` | 27 | Returns the cost attribute |
| [`Card.GetLeftScale`](/api/functions/Card/GetLeftScale) | `imported_from_dataeditorx` | 26 | Returns the left-hand pendulum scale of c |
| [`Card.GetPreviousAttributeOnField`](/api/functions/Card/GetPreviousAttributeOnField) | `imported_from_dataeditorx` | 26 | Returns the attribute before the c position change |
| [`Card.GetSummonType`](/api/functions/Card/GetSummonType) | `imported_from_dataeditorx` | 26 | Returns the call / special call of c |
| [`Duel.IsPlayerCanSummon`](/api/functions/Duel/IsPlayerCanSummon) | `imported_from_dataeditorx` | 26 | Check player player can usually call \[c, to sumtype\] If optional parameters are required, they must all be used Returns false only if the player receives an effect suc... |
| [`Card.CopyEffect`](/api/functions/Card/CopyEffect) | `imported_from_dataeditorx` | 25 | Adding a card number for c is the replicable effect of the card's code, and adding an additional reset condition The return value is the code id representing the copy... |
| [`Card.GetMaterialCount`](/api/functions/Card/GetMaterialCount) | `imported_from_dataeditorx` | 25 | Returns the amount of material used for c appearance |
| [`Card.IsRankAbove`](/api/functions/Card/IsRankAbove) | `imported_from_dataeditorx` | 25 | Check whether c is above the class rank |
| [`Duel.CheckPhaseActivity`](/api/functions/Duel/CheckPhaseActivity) | `imported_from_dataeditorx` | 25 | Check the player at the current stage whether the operation (whether at the beginning of the stage, such as the Seven King of the sword) |
| [`Auxiliary.Tuner`](/api/functions/Auxiliary/Tuner) | `imported_from_dataeditorx` | 24 | Filter Tuner monsters satisfying a single filter condition f, returning a function with a bool return type; if only Tuner monsters are required, use aux.Tuner(nil) Add... |
| [`Card.GetBattlePosition`](/api/functions/Card/GetBattlePosition) | `imported_from_dataeditorx` | 24 | Returns the representation of c before this battle occurs |
| [`Card.IsXyzType`](/api/functions/Card/IsXyzType) | `imported_from_dataeditorx` | 24 | Check if card c, when used as Xyz Material, has type type (unlike IsType, for monster cards in the Spell/Trap Zone, it uses their original type for judgment) |
| [`Duel.AnnounceLevel`](/api/functions/Duel/AnnounceLevel) | `imported_from_dataeditorx` | 24 | Let the player declare a level |
| [`Duel.GetTargetCount`](/api/functions/Duel/GetTargetCount) | `imported_from_dataeditorx` | 24 | Basic with Duel.GetMatchingGroupCount, the difference lies in the need to add to determine whether the card is currently being processed by the effect of the object |
| [`Duel.IsCanAddCounter`](/api/functions/Duel/IsCanAddCounter) | `imported_from_dataeditorx` | 24 | Check if the player can add count counterstype to card c |
| [`Duel.SendtoExtraP`](/api/functions/Duel/SendtoExtraP) | `imported_from_dataeditorx` | 24 | The reason for the reason the spirit of the swing card targets sent to the player player extra card group, the return value is the actual number of operations If playe... |
| [`Auxiliary.ritlimit`](/api/functions/Auxiliary/ritlimit) | `imported_from_dataeditorx` | 23 | Simplified method for the filter function preventing summoning (broadly) by methods other than Ritual Summon, used in effect registration for SetValue se is the effect... |
| [`Card.GetCurrentScale`](/api/functions/Card/GetCurrentScale) | `imported_from_dataeditorx` | 23 | Return the current Pendulum Scale of card c. If in the Left Pendulum Zone, return the left scale; if in the Right Pendulum Zone or not in a Pendulum Zone, return the r... |
| [`Card.GetLocation`](/api/functions/Card/GetLocation) | `imported_from_dataeditorx` | 23 | Returns the current position of c |
| [`Duel.AnnounceType`](/api/functions/Duel/AnnounceType) | `imported_from_dataeditorx` | 23 | Let the player player declare a card type |
| [`Duel.IsPlayerCanAdditionalSummon`](/api/functions/Duel/IsPlayerCanAdditionalSummon) | `imported_from_dataeditorx` | 23 | Check if player has additional summon counts beyond Normal Summon |
| [`Group.GetMinGroup`](/api/functions/Group/GetMinGroup) | `imported_from_dataeditorx` | 23 | F is a function that returns an interger value, and the card with the smallest value of f is selected from g The second return value is the minimum value, starting at... |
| [`Card.GetPreviousCodeOnField`](/api/functions/Card/GetPreviousCodeOnField) | `imported_from_dataeditorx` | 22 | Returns the card number prior to the c position change |
| [`Card.IsHasCardTarget`](/api/functions/Card/IsHasCardTarget) | `imported_from_dataeditorx` | 22 | Check whether c1 takes c2 as a persistent object |
| [`Duel.GetBattleDamage`](/api/functions/Duel/GetBattleDamage) | `imported_from_dataeditorx` | 22 | Returns the player's player's damage during this battle |
| [`Duel.GetLinkedZone`](/api/functions/Duel/GetLinkedZone) | `imported_from_dataeditorx` | 22 | Return all Link Zones from player's perspective |
| [`Auxiliary.damcon1`](/api/functions/Auxiliary/damcon1) | `imported_from_dataeditorx` | 21 | Simplified method for the condition of player tp taking damage, used in effect registration for SetCondition function aux.damcon1(e, tp, eg, ep, ev, re, r, rp) local e... |
| [`Auxiliary.EnableUnionAttribute`](/api/functions/Auxiliary/EnableUnionAttribute) | `imported_from_dataeditorx` | 21 | add effect to modern union monsters |
| [`Auxiliary.IsUnionState`](/api/functions/Auxiliary/IsUnionState) | `imported_from_dataeditorx` | 21 | Check if the Union Monster e:GetHandler() is in a Union Equip state (used for the Condition property of effects) |
| [`Card.IsLinkCode`](/api/functions/Card/IsLinkCode) | `imported_from_dataeditorx` | 21 | Check if card c, when used as Link Material, can be treated as a card with code, additional parameters are other codes |
| [`Duel.ChangeChainOperation`](/api/functions/Duel/ChangeChainOperation) | `imported_from_dataeditorx` | 21 | The effect of the chain chainc processing function replaced by f, used to achieve "the effect becomes" effect |
| [`Group.Clear`](/api/functions/Group/Clear) | `imported_from_dataeditorx` | 21 | Empty the deck |
| [`Auxiliary.sumreg`](/api/functions/Auxiliary/sumreg) | `imported_from_dataeditorx` | 20 | Used by Yosenju Yamamisaki (39853199) and some other cards (49249907, 93368494), though the purpose of this function is unclear. Card 54109233, while not using this fu... |
| [`Card.GetEffectCount`](/api/functions/Card/GetEffectCount) | `imported_from_dataeditorx` | 20 | Returns the number of effects that c is affected by the type of code |
| [`Card.GetPreviousPosition`](/api/functions/Card/GetPreviousPosition) | `imported_from_dataeditorx` | 20 | Returns the representation of the position before the c position changes |
| [`Card.IsCanRemoveCounter`](/api/functions/Card/IsCanRemoveCounter) | `imported_from_dataeditorx` | 20 | Check if the player player can remove count counters of type c on c for reason |
| [`Card.IsLinkSummonable`](/api/functions/Card/IsLinkSummonable) | `imported_from_dataeditorx` | 20 | Check if card c can be Link Summoned using \[min-max Link Materials\] from cards on the field \[or mg\] If mg is nil, this function is equivalent to c:IsSpecialSummonable(... |
| [`Card.IsRankBelow`](/api/functions/Card/IsRankBelow) | `imported_from_dataeditorx` | 20 | Check whether c is below the rank rank (at least 1) |
| [`Duel.ClearTargetCard`](/api/functions/Duel/ClearTargetCard) | `imported_from_dataeditorx` | 20 | The current processing of the chain of all the objects cleared |
| [`Duel.LinkSummon`](/api/functions/Duel/LinkSummon) | `imported_from_dataeditorx` | 20 | Have player Link Summon pcard using \[minc to maxc cards from mg, excluding lcard\] as materials |
| [`Duel.Win`](/api/functions/Duel/Win) | `imported_from_dataeditorx` | 20 | The current effect is dealt with so players win_reason duel victory |
| [`Auxiliary.AddFusionProcCode3`](/api/functions/Auxiliary/AddFusionProcCode3) | `imported_from_dataeditorx` | 19 | For the c designated card number code1, code2, code3 monster for the fusion material |
| [`Auxiliary.SameValueCheck`](/api/functions/Auxiliary/SameValueCheck) | `imported_from_dataeditorx` | 19 | Check if all cards in g have the same Attribute/Race |
| [`Card.GetLinkCode`](/api/functions/Card/GetLinkCode) | `imported_from_dataeditorx` | 19 | Return the card code(s) of card c when used as Link Material (including c's original card code) |
| [`Card.GetUnionCount`](/api/functions/Card/GetUnionCount) | `imported_from_dataeditorx` | 19 | Returns the number of ally cards for the current device |
| [`Duel.CheckEvent`](/api/functions/Duel/CheckEvent) | `imported_from_dataeditorx` | 19 | Check whether the current event point If get_info = true and is the correct time point also returns the trigger point information eg, ep, ev, re, r, rp |
| [`Duel.SetSelectedCard`](/api/functions/Duel/SetSelectedCard) | `imported_from_dataeditorx` | 19 | Set the card to the selected card for Group.SelectWithSumEqual or Group.SelectWithSumGreater, |
| [`Duel.SwapControl`](/api/functions/Duel/SwapControl) | `imported_from_dataeditorx` | 19 | Exchange c1 and c2 control, the return value that is successful |
| ...and 232 more |  |  |  |

## Raw Chinese In English Fields

No raw Chinese text was detected in English fields during this generation.

## DataEditorX Sync Rule

Sync generated `_functions` and `_function_english` files to DataEditorX only after the reviewed text has been regenerated here. Sacred Book is the source of truth for the next pass.
