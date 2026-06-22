# Function Translation Review

This queue tracks function pages whose English should be reviewed by hand. It is stricter than the generator backlog: imported English can be technically present but still read like a rough machine translation.

## Summary

- Total functions: **998**
- Functions used by current scripts: **753**
- Functions with raw Chinese text in English fields: **0**
- Functions queued for natural-English review: **485**

## English Status Counts

| Status | Count |
| --- | ---: |
| `imported_from_dataeditorx` | 485 |
| `translated_exact` | 513 |

## Priority Review Queue

Sorted by current script usage count so the most visible function pages are reviewed first.

| Function | Status | Script Uses | Current English Preview |
| --- | --- | ---: | --- |
| [`Effect.GetOperation`](/api/functions/Effect/GetOperation) | `imported_from_dataeditorx` | 253 | Returns the operation attribute |
| [`Effect.GetTarget`](/api/functions/Effect/GetTarget) | `imported_from_dataeditorx` | 253 | Returns the target attribute |
| [`Card.GetType`](/api/functions/Card/GetType) | `imported_from_dataeditorx` | 246 | Returns the current type of c |
| [`Effect.GetType`](/api/functions/Effect/GetType) | `imported_from_dataeditorx` | 246 | Returns the Type property |
| [`Card.CheckFusionMaterial`](/api/functions/Card/CheckFusionMaterial) | `imported_from_dataeditorx` | 244 | Check if g contains a set of fusion material that c needs [must contain gc] |
| [`Duel.CreateToken`](/api/functions/Duel/CreateToken) | `imported_from_dataeditorx` | 239 | Creates a new Token with the passed in parameter value and returns |
| [`Group.FilterSelect`](/api/functions/Group/FilterSelect) | `imported_from_dataeditorx` | 239 | Filter function, allowing players to choose from the g player min-max sheets meet the screening conditions f and not equal to the ex card Starting with the 7th argumen... |
| [`Effect.GetValue`](/api/functions/Effect/GetValue) | `imported_from_dataeditorx` | 238 | Returns the value attribute |
| [`Auxiliary.tgoval`](/api/functions/Auxiliary/tgoval) | `imported_from_dataeditorx` | 234 | Simplified method for the filter function preventing being targeted by opponent's card effects, used in effect registration for SetValue function aux.tgoval(e, re, rp)... |
| [`Duel.GetTurnCount`](/api/functions/Duel/GetTurnCount) | `imported_from_dataeditorx` | 231 | Returns the current number of turns |
| [`Card.IsFusionSetCard`](/api/functions/Card/IsFusionSetCard) | `imported_from_dataeditorx` | 229 | Check the c as a fusion material can be used as a name setname card |
| [`Card.IsPublic`](/api/functions/Card/IsPublic) | `imported_from_dataeditorx` | 229 | Check if c is open |
| [`Card.IsHasEffect`](/api/functions/Card/IsHasEffect) | `imported_from_dataeditorx` | 223 | Check if c is affected by the effect type |
| [`Card.IsPosition`](/api/functions/Card/IsPosition) | `imported_from_dataeditorx` | 222 | Check whether c is the representation pos |
| [`Duel.SelectFusionMaterial`](/api/functions/Duel/SelectFusionMaterial) | `imported_from_dataeditorx` | 222 | Let the player player from the g to select a group [must contain gc] fusion fusion monster c material |
| [`Group.DeleteGroup`](/api/functions/Group/DeleteGroup) | `imported_from_dataeditorx` | 221 | Delete the card group g |
| [`Card.GetFlagEffectLabel`](/api/functions/Card/GetFlagEffectLabel) | `imported_from_dataeditorx` | 217 | The type of c is the label that identifies the effect of code, and returns nil if it does not |
| [`Card.GetMaterial`](/api/functions/Card/GetMaterial) | `imported_from_dataeditorx` | 214 | Returns the material used for the appearance of c |
| [`Duel.GetChainMaterial`](/api/functions/Duel/GetChainMaterial) | `imported_from_dataeditorx` | 212 | Returns the effect of the chained material that is played by the player. This function is only used to blend the effect of a class card |
| [`Duel.NegateRelatedChain`](/api/functions/Duel/NegateRelatedChain) | `imported_from_dataeditorx` | 210 | So that card c has launched the chain are invalid, reset event occurs reset |
| [`Card.IsSummonLocation`](/api/functions/Card/IsSummonLocation) | `imported_from_dataeditorx` | 206 | Check if card c's Normal Summon or Special Summon location is loc |
| [`Card.GetFieldID`](/api/functions/Card/GetFieldID) | `imported_from_dataeditorx` | 187 | Returns the time stamp of the transition to the current position This value is unique, the smaller the c is the earlier appear in that position Opening the card from t... |
| [`Effect.GetFieldID`](/api/functions/Effect/GetFieldID) | `imported_from_dataeditorx` | 187 | Gets the id of the effect e |
| [`Effect.IsHasProperty`](/api/functions/Effect/IsHasProperty) | `imported_from_dataeditorx` | 187 | Check if the effect contains the flags prop1 [and prop2] |
| [`Card.CheckUniqueOnField`](/api/functions/Card/CheckUniqueOnField) | `imported_from_dataeditorx` | 186 | Check the uniqueness of c in the check_player field |
| [`Duel.GetDecktopGroup`](/api/functions/Duel/GetDecktopGroup) | `imported_from_dataeditorx` | 185 | Returns the count card at the top of the player's deck |
| [`Duel.GetFusionMaterial`](/api/functions/Duel/GetFusionMaterial) | `imported_from_dataeditorx` | 181 | Return the group of cards available to player for Fusion Summon materials Includes monsters in hand, on the field, and cards affected by EFFECT_EXTRA_FUSION_MATERIAL |
| [`Card.EnableCounterPermit`](/api/functions/Card/EnableCounterPermit) | `imported_from_dataeditorx` | 178 | Allow c [to be placed in the location location] that can be placed "can be placed on the counter countertype The default value of location depends on the type of c, an... |
| [`Card.IsCanTurnSet`](/api/functions/Card/IsCanTurnSet) | `imported_from_dataeditorx` | 174 | Check whether c can turn into the inside of that |
| [`Duel.AddCustomActivityCounter`](/api/functions/Duel/AddCustomActivityCounter) | `imported_from_dataeditorx` | 173 | Set the action type to activity_type, code counter_id counter, placed in the initial_effect function F for the filter function, the card type parameters, the return va... |
| [`Card.IsAttackBelow`](/api/functions/Card/IsAttackBelow) | `imported_from_dataeditorx` | 172 | Check whether c is attack power atk below (at least 0) |
| [`Duel.GetCustomActivityCount`](/api/functions/Duel/GetCustomActivityCount) | `imported_from_dataeditorx` | 172 | Counter number counter_id count, the number of players to return to the following (currently up to 1) The activity_type is of the following type ACTIVITY_SUMMON call (... |
| [`Auxiliary.IsCodeListed`](/api/functions/Auxiliary/IsCodeListed) | `imported_from_dataeditorx` | 170 | Check if card c lists card code in its card_code_list |
| [`Card.IsCanOverlay`](/api/functions/Card/IsCanOverlay) | `imported_from_dataeditorx` | 169 | Check if c can be used as Xyz Material |
| [`Card.GetReasonPlayer`](/api/functions/Card/GetReasonPlayer) | `imported_from_dataeditorx` | 167 | Returns the player that caused the position of c to change |
| [`Group.SelectUnselect`](/api/functions/Group/SelectUnselect) | `imported_from_dataeditorx` | 167 | Have player select 1 card from cg to add to sg and return the selected card btok indicates whether the confirm selection button is available, cancelable indicates whet... |
| [`Card.GetAttribute`](/api/functions/Card/GetAttribute) | `imported_from_dataeditorx` | 166 | Returns the current attribute of c Note: For some multi-attribute monsters such as light and dark dragon, the return value of this function may be a combination of sev... |
| [`Effect.GetOwnerPlayer`](/api/functions/Effect/GetOwnerPlayer) | `imported_from_dataeditorx` | 165 | Returns the OwnerPlayer property, which is typically the controller of the Owner |
| [`Card.GetOriginalType`](/api/functions/Card/GetOriginalType) | `imported_from_dataeditorx` | 162 | Returns the type of card entry for c |
| [`Card.IsAttack`](/api/functions/Card/IsAttack) | `imported_from_dataeditorx` | 161 | Check if card c's ATK is atk1 [, or atk2...], returns false if c is not a monster card or not in LOCATION_MZONE |
| [`Duel.GetCurrentChain`](/api/functions/Duel/GetCurrentChain) | `imported_from_dataeditorx` | 161 | Returns the chain number currently being processed |
| [`Auxiliary.ExceptThisCard`](/api/functions/Auxiliary/ExceptThisCard) | `imported_from_dataeditorx` | 160 | If e:GetHandler() is related to effect e, return e:GetHandler(); otherwise return nil function aux.ExceptThisCard(e) local c=e:GetHandler() if c:IsRelateToEffect(e) th... |
| [`Group.CreateGroup`](/api/functions/Group/CreateGroup) | `imported_from_dataeditorx` | 160 | Create a new empty deck |
| [`Card.GetReasonCard`](/api/functions/Card/GetReasonCard) | `imported_from_dataeditorx` | 157 | Returns the card that caused the position of c to change This function is only valid when a card is destroyed by a battle, because the superior call is released, or be... |
| [`Card.GetOverlayGroup`](/api/functions/Card/GetOverlayGroup) | `imported_from_dataeditorx` | 154 | Returns the currently stacked deck |
| [`Card.IsAttackPos`](/api/functions/Card/IsAttackPos) | `imported_from_dataeditorx` | 154 | Check whether c is an attack |
| [`Card.IsCanChangePosition`](/api/functions/Card/IsCanChangePosition) | `imported_from_dataeditorx` | 153 | Check if c can have its battle position changed by an effect |
| [`Duel.ConfirmDecktop`](/api/functions/Duel/ConfirmDecktop) | `imported_from_dataeditorx` | 151 | Confirm the player card group above count cards |
| [`Card.GetEquipTarget`](/api/functions/Card/GetEquipTarget) | `imported_from_dataeditorx` | 150 | Returns the current artefact object |
| [`Auxiliary.MustMaterialCheck`](/api/functions/Auxiliary/MustMaterialCheck) | `imported_from_dataeditorx` | 147 | Check if value contains cards or a group affected by player's effect type code Currently involved codes are: EFFECT_MUST_BE_SMATERIAL EFFECT_MUST_BE_XMATERIAL EFFECT_M... |
| [`Effect.IsActivated`](/api/functions/Effect/IsActivated) | `imported_from_dataeditorx` | 147 | Check the effect of e is the effect of starting (chassis) |
| [`Group.GetSum`](/api/functions/Group/GetSum) | `imported_from_dataeditorx` | 142 | Calculates the sum of the values ​​of all cards in g, f is the value function for each card, starting with the third parameter as an additional parameter |
| [`Card.AddCounter`](/api/functions/Card/AddCounter) | `imported_from_dataeditorx` | 141 | Place count count counter type c for c, singly true to add one to the upper limit |
| [`Duel.MoveSequence`](/api/functions/Duel/MoveSequence) | `imported_from_dataeditorx` | 140 | Move the serial number of c, usually used to change the grid in the field or in the card group to move to the top or bottom |
| [`Auxiliary.AddFusionProcFun2`](/api/functions/Auxiliary/AddFusionProcFun2) | `imported_from_dataeditorx` | 139 | For the c to specify conditions for the f1 and f2 monsters for the fusion material |
| [`Group.RandomSelect`](/api/functions/Group/RandomSelect) | `imported_from_dataeditorx` | 139 | Let the player player randomly select count cards from g Because it is a random choice, so the basic parameter useless player, randomly selected by the system |
| [`Card.IsAttackAbove`](/api/functions/Card/IsAttackAbove) | `imported_from_dataeditorx` | 137 | Check whether c is more than attack power atk |
| [`Card.IsLinkRace`](/api/functions/Card/IsLinkRace) | `imported_from_dataeditorx` | 136 | Check if card c, when used as Link Material [for a Link Summon by player], has Race race |
| [`Auxiliary.SelectFromOptions`](/api/functions/Auxiliary/SelectFromOptions) | `imported_from_dataeditorx` | 135 | Duel.SelectOption with option condition Return value starts from 1, different from Duel.SelectOption |
| [`Card.IsCanBeFusionMaterial`](/api/functions/Card/IsCanBeFusionMaterial) | `imported_from_dataeditorx` | 132 | Check whether c can become a [fusion monster fc] fusion material, ignore_mon = true does not check whether c is a monster |
| [`Card.IsLinkType`](/api/functions/Card/IsLinkType) | `imported_from_dataeditorx` | 132 | Check if card c, when used as Link Material, has type type (unlike IsType, for monster cards in the Spell/Trap Zone, it uses their original type for judgment) |
| [`Card.IsLinkSetCard`](/api/functions/Card/IsLinkSetCard) | `imported_from_dataeditorx` | 131 | Check if card c, when used as Link Material, can be treated as a card with setname in its name |
| [`Auxiliary.AddFusionProcFunRep`](/api/functions/Auxiliary/AddFusionProcFunRep) | `imported_from_dataeditorx` | 128 | For the c designated cc meet the same conditions f monster for the fusion material |
| [`Card.IsControlerCanBeChanged`](/api/functions/Card/IsControlerCanBeChanged) | `imported_from_dataeditorx` | 125 | Check whether the control of c can be changed Note: This function appends the space on the field to the Card.IsAbleToChangeControler |
| [`Duel.NegateAttack`](/api/functions/Duel/NegateAttack) | `imported_from_dataeditorx` | 124 | Invalid This attack, the return value indicates whether the success This attack has been invalidated by other effects or cause the attack card can not attack is false |
| [`Card.GetCounter`](/api/functions/Card/GetCounter) | `imported_from_dataeditorx` | 121 | Returns the number of countertype types on c |
| [`Card.GetDefense`](/api/functions/Card/GetDefense) | `imported_from_dataeditorx` | 121 | Returns the current defense of c, the return value is negative that is "?" |
| [`Card.IsDefensePos`](/api/functions/Card/IsDefensePos) | `imported_from_dataeditorx` | 121 | Check whether c is a defensive representation |
| [`Card.IsReleasable`](/api/functions/Card/IsReleasable) | `imported_from_dataeditorx` | 121 | Check whether c can be liberated (non-superior call) |
| [`Card.SetCardTarget`](/api/functions/Card/SetCardTarget) | `imported_from_dataeditorx` | 121 | C2 as the perpetual object of c1 C1 and c2 of the contact will c1 or c2 any one card to leave or become the side of that reset |
| [`Auxiliary.exccon`](/api/functions/Auxiliary/exccon) | `imported_from_dataeditorx` | 116 | Simplified method for the condition that this card cannot activate its effect during the turn it was sent to the Graveyard, used for SetCondition function aux.exccon(e... |
| [`Card.GetOriginalLevel`](/api/functions/Card/GetOriginalLevel) | `imported_from_dataeditorx` | 115 | Returns the rank of the card in c |
| [`Group.RemoveCard`](/api/functions/Group/RemoveCard) | `imported_from_dataeditorx` | 115 | Remove c from g |
| [`Auxiliary.AddFusionProcCode2`](/api/functions/Auxiliary/AddFusionProcCode2) | `imported_from_dataeditorx` | 114 | For the c designated card number for the code1 and code2 monster for the fusion material Sub that can use fusion instead of material, insf that can be summoned with a... |
| [`Duel.IsEnvironment`](/api/functions/Duel/IsEnvironment) | `imported_from_dataeditorx` | 114 | Check whether the player player is the source code of the venue code The site code refers to the code of the venue card in effect, or the value of the effect of the ve... |
| [`Auxiliary.indoval`](/api/functions/Auxiliary/indoval) | `imported_from_dataeditorx` | 111 | Simplified method for the filter function preventing destruction by opponent's card effects, used in effect registration for SetValue function aux.indoval(e, re, rp) r... |
| [`Duel.RaiseEvent`](/api/functions/Duel/RaiseEvent) | `imported_from_dataeditorx` | 110 | To eg, ep, ev, re, r, rp trigger a point in time |
| [`Auxiliary.GCheckAdditional`](/api/functions/Auxiliary/GCheckAdditional) | `imported_from_dataeditorx` | 106 | Subgroup check function |
| [`Card.IsRank`](/api/functions/Card/IsRank) | `imported_from_dataeditorx` | 106 | Check if card c is Rank rank1 [, or rank2...] |
| [`Card.GetTextAttack`](/api/functions/Card/GetTextAttack) | `imported_from_dataeditorx` | 105 | Returns the attack power recorded on card c |
| [`Duel.CheckLocation`](/api/functions/Duel/CheckLocation) | `imported_from_dataeditorx` | 104 | Check if the player's player field is seq in the location of the space is available |
| [`Card.GetRank`](/api/functions/Card/GetRank) | `imported_from_dataeditorx` | 99 | Returns the current class of c |
| [`Card.GetOriginalCode`](/api/functions/Card/GetOriginalCode) | `imported_from_dataeditorx` | 97 | Returns the code number of the card in c |
| [`Card.IsDefense`](/api/functions/Card/IsDefense) | `imported_from_dataeditorx` | 97 | Check if c's DEF is def1 [, or def2...]; returns false if c is not a monster card or not in LOCATION_MZONE |
| [`Auxiliary.fuslimit`](/api/functions/Auxiliary/fuslimit) | `imported_from_dataeditorx` | 89 | Simplified method for the filter function preventing summoning (broadly) by methods other than Fusion Summon, used in effect registration for SetValue se is the effect... |
| [`Card.IsAbleToChangeControler`](/api/functions/Card/IsAbleToChangeControler) | `imported_from_dataeditorx` | 88 | Check whether c can change the control Note: This function returns false only if the card receives the effect of "Can not change control" |
| [`Group.Sub`](/api/functions/Group/Sub) | `imported_from_dataeditorx` | 88 | Remove the card from g1 that belongs to g2 Note: g2 itself does not change |
| [`Card.IsFusionType`](/api/functions/Card/IsFusionType) | `imported_from_dataeditorx` | 87 | Check if card c, when used as Fusion Material, has type type (unlike IsType, for monster cards in the Spell/Trap Zone, it uses their original type for judgment) |
| [`Duel.ReturnToField`](/api/functions/Duel/ReturnToField) | `imported_from_dataeditorx` | 87 | To return the form c to the field pos, pos default value is the expression before leaving the field, the return value indicates whether the success C must be a REASON_... |
| [`Duel.SetChainLimit`](/api/functions/Duel/SetChainLimit) | `imported_from_dataeditorx` | 87 | Set the chain conditions, f function prototype for bool f (e, ep, tp) E said to limit the effect of chain, ep said to limit the chain of players, tp that launched the... |
| [`Card.CheckRemoveOverlayCard`](/api/functions/Card/CheckRemoveOverlayCard) | `imported_from_dataeditorx` | 86 | Check the player player can be reason for the reason, at least remove the c stacked count cards |
| [`Card.IsDestructable`](/api/functions/Card/IsDestructable) | `imported_from_dataeditorx` | 86 | Check whether c is destructible |
| [`Card.RemoveOverlayCard`](/api/functions/Card/RemoveOverlayCard) | `imported_from_dataeditorx` | 86 | For reason reason, let players player remove c stacked min-max card, the return value that is successful |
| [`Duel.GetFirstMatchingCard`](/api/functions/Duel/GetFirstMatchingCard) | `imported_from_dataeditorx` | 85 | Filter function to return to the specified location to meet the filter condition f and not equal to the first card ex The sixth parameter starts as an extra parameter |
| [`Card.IsFusionAttribute`](/api/functions/Card/IsFusionAttribute) | `imported_from_dataeditorx` | 84 | Check if card c, when used as Fusion Material [for a Fusion Summon by player], has Attribute attribute |
| [`Duel.GetActivityCount`](/api/functions/Duel/GetActivityCount) | `imported_from_dataeditorx` | 83 | Returns the number of times the player performed the corresponding activity_type operation The activity_type is of the following type ACTIVITY_SUMMON call (not includi... |
| [`Effect.UseCountLimit`](/api/functions/Effect/UseCountLimit) | `imported_from_dataeditorx` | 83 | Manually reduce player p's available activation count for effect e by count [oath_only indicates whether the effect is EFFECT_FLAG_OATH] |
| [`Card.GetOriginalRace`](/api/functions/Card/GetOriginalRace) | `imported_from_dataeditorx` | 82 | Returns the c of the card record race |
| [`Card.GetOverlayCount`](/api/functions/Card/GetOverlayCount) | `imported_from_dataeditorx` | 82 | Returns the number of cards currently stacked |
| [`Card.IsCanAddCounter`](/api/functions/Card/IsCanAddCounter) | `imported_from_dataeditorx` | 82 | Check if c can place count counters of type countertype [singly = true] |
| [`Duel.SetLP`](/api/functions/Duel/SetLP) | `imported_from_dataeditorx` | 82 | Set the player's current LP to lp |
| [`Auxiliary.AddFusionProcCodeFun`](/api/functions/Auxiliary/AddFusionProcCodeFun) | `imported_from_dataeditorx` | 80 | For the c designated card number for the code and cc meet the conditions of the monster f fusion material |
| [`Duel.AnnounceNumber`](/api/functions/Duel/AnnounceNumber) | `imported_from_dataeditorx` | 77 | Let the player player declare a number Starting with the second argument, each parameter represents a declarable number The first return value is the number of declara... |
| [`Card.GetBaseDefense`](/api/functions/Card/GetBaseDefense) | `imported_from_dataeditorx` | 76 | Return to the original c of the defense |
| [`Card.SetSPSummonOnce`](/api/functions/Card/SetSPSummonOnce) | `imported_from_dataeditorx` | 76 | Set c can only be a round of a special call (they reveal, wave dragon) The same spsummon_code shares 1 number of times |
| [`Card.IsPreviousSetCard`](/api/functions/Card/IsPreviousSetCard) | `imported_from_dataeditorx` | 75 | Check whether the name c contains a setname before the c position changes |
| [`Duel.IsAbleToEnterBP`](/api/functions/Duel/IsAbleToEnterBP) | `imported_from_dataeditorx` | 75 | Check whether the player can enter the combat phase of the round |
| [`Duel.CheckTribute`](/api/functions/Duel/CheckTribute) | `imported_from_dataeditorx` | 74 | Check if there are min [to max] Tributes on the field [or in mg] for Normal Summoning c [to toplayer's field in zone] |
| [`Effect.GetActivateLocation`](/api/functions/Effect/GetActivateLocation) | `imported_from_dataeditorx` | 73 | Returns the firing area of ​​the effect e |
| [`Card.AddMonsterAttribute`](/api/functions/Card/AddMonsterAttribute) | `imported_from_dataeditorx` | 72 | Add the monster value to the trap card Note: Values ​​recorded in the database are treated as the original value, and are set to zero here |
| [`Card.GetPreviousTypeOnField`](/api/functions/Card/GetPreviousTypeOnField) | `imported_from_dataeditorx` | 72 | Returns the type before the c position change |
| [`Duel.GetFieldCard`](/api/functions/Duel/GetFieldCard) | `imported_from_dataeditorx` | 72 | Back to player The player's field is located in the location number seq card, commonly used to obtain the field area · Spirit pendulum area card |
| [`Card.GetOriginalAttribute`](/api/functions/Card/GetOriginalAttribute) | `imported_from_dataeditorx` | 71 | Returns the attributes of the card that c is describing |
| [`Duel.SelectTribute`](/api/functions/Duel/SelectTribute) | `imported_from_dataeditorx` | 71 | Let the player player [from the mg] choose the min-max sacrifices that are normally used to summon c, ex = true to allow the monster on the other side of the field (th... |
| [`Auxiliary.bdocon`](/api/functions/Auxiliary/bdocon) | `imported_from_dataeditorx` | 70 | Check if e:GetHandler() is related to the current battle, typically used for EVENT_BATTLE_DESTROYING and when battling an opponent's monster, as a condition function A... |
| [`Card.IsCanBeXyzMaterial`](/api/functions/Card/IsCanBeXyzMaterial) | `imported_from_dataeditorx` | 69 | Check whether c can become an excessive monster sc excess material |
| [`Card.GetPreviousControler`](/api/functions/Card/GetPreviousControler) | `imported_from_dataeditorx` | 68 | Returns the controller before the position change of c |
| [`Card.GetEquipGroup`](/api/functions/Card/GetEquipGroup) | `imported_from_dataeditorx` | 63 | Returns the current set of cards |
| [`Card.GetLinkedGroup`](/api/functions/Card/GetLinkedGroup) | `imported_from_dataeditorx` | 61 | Return the group of cards in the zones linked to card c |
| [`Card.GetLinkedZone`](/api/functions/Card/GetLinkedZone) | `imported_from_dataeditorx` | 60 | Return the [from player's perspective on the field] Link Zones of card c |
| [`Card.GetPreviousSequence`](/api/functions/Card/GetPreviousSequence) | `imported_from_dataeditorx` | 59 | Returns the sequence number before the c position changes |
| [`Duel.ChainAttack`](/api/functions/Duel/ChainAttack) | `imported_from_dataeditorx` | 59 | So that the attack card [or card c] can be carried out an attack (opening up, the queen of the Queen) |
| [`Duel.IsCanRemoveCounter`](/api/functions/Duel/IsCanRemoveCounter) | `imported_from_dataeditorx` | 59 | Checks whether the player player can remove count objects of the countertype type on the farm for reason reasons S represents the position of the player's own removabl... |
| [`Duel.SortDecktop`](/api/functions/Duel/SortDecktop) | `imported_from_dataeditorx` | 59 | Let the player sort_player on the player target_player card group at the top count card sort |
| [`Duel.RemoveCounter`](/api/functions/Duel/RemoveCounter) | `imported_from_dataeditorx` | 58 | Causes the player player to remove count objects of the countertype type present on the farm for reason reasons. The return value indicates success S represents the po... |
| [`Duel.TossDice`](/api/functions/Duel/TossDice) | `imported_from_dataeditorx` | 58 | Let the player to cast count1 dice[, 1-player to vote count2 dice] (count1 + count2 <= 5) The return value is count1 + count2 results, 1-6 |
| [`Card.IsLinkAttribute`](/api/functions/Card/IsLinkAttribute) | `imported_from_dataeditorx` | 56 | Check if card c, when used as Link Material [for a Link Summon by player], has Attribute attribute |
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
| [`Duel.TossCoin`](/api/functions/Duel/TossCoin) | `imported_from_dataeditorx` | 47 | Let the player player cast count (<= 5) coins, the return value for the count results, 0 or 1. |
| [`Card.GetColumnGroup`](/api/functions/Card/GetColumnGroup) | `imported_from_dataeditorx` | 46 | Return the group of cards in the same column as card c, excluding c, the last two parameters include all cards in the left columns and right columns from c For example... |
| [`Card.GetReason`](/api/functions/Card/GetReason) | `imported_from_dataeditorx` | 46 | Returns the position change reason for c |
| [`Card.IsDefenseBelow`](/api/functions/Card/IsDefenseBelow) | `imported_from_dataeditorx` | 46 | Check whether c is defensive def below (at least 0) |
| [`Card.IsFusionCode`](/api/functions/Card/IsFusionCode) | `imported_from_dataeditorx` | 46 | Check the c as a fusion material can be used as the card number for the code card |
| [`Auxiliary.EnableDualAttribute`](/api/functions/Auxiliary/EnableDualAttribute) | `imported_from_dataeditorx` | 45 | Add double for the c monster attributes |
| [`Card.GetPreviousEquipTarget`](/api/functions/Card/GetPreviousEquipTarget) | `imported_from_dataeditorx` | 45 | Returns the device object before c |
| [`Duel.CheckRemoveOverlayCard`](/api/functions/Duel/CheckRemoveOverlayCard) | `imported_from_dataeditorx` | 45 | Check if the player can remove at least count cards for the specified reason |
| [`Auxiliary.IsMaterialListCode`](/api/functions/Auxiliary/IsMaterialListCode) | `imported_from_dataeditorx` | 44 | Check if card c lists card code as a material in its material list |
| ...and 325 more |  |  |  |

## Raw Chinese In English Fields

No raw Chinese text was detected in English fields during this generation.

## DataEditorX Sync Rule

Sync generated `_functions` and `_function_english` files to DataEditorX only after the reviewed text has been regenerated here. Sacred Book is the source of truth for the next pass.
