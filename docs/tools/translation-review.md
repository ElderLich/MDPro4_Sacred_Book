# Function Translation Review

This queue tracks function pages whose English should be reviewed by hand. It is stricter than the generator backlog: imported English can be technically present but still read like a rough machine translation.

## Summary

- Total functions: **998**
- Functions used by current scripts: **753**
- Functions with raw Chinese text in English fields: **0**
- Functions queued for natural-English review: **528**

## English Status Counts

| Status | Count |
| --- | ---: |
| `imported_from_dataeditorx` | 528 |
| `translated_exact` | 470 |

## Priority Review Queue

Sorted by current script usage count so the most visible function pages are reviewed first.

| Function | Status | Script Uses | Current English Preview |
| --- | --- | ---: | --- |
| [`Card.IsLevel`](/api/functions/Card/IsLevel) | `imported_from_dataeditorx` | 676 | Check if card c is Level level1 [, or level2...] |
| [`Card.SetMaterial`](/api/functions/Card/SetMaterial) | `imported_from_dataeditorx` | 475 | The g of all the cards as the c material (superior summon, special summon) |
| [`Duel.SelectOption`](/api/functions/Duel/SelectOption) | `imported_from_dataeditorx` | 471 | Let the player select the option, starting with the second argument, where each parameter represents an option Returns the serial number of the selected option (0-based) |
| [`Effect.GetDescription`](/api/functions/Effect/GetDescription) | `imported_from_dataeditorx` | 470 | Returns the description of the effect |
| [`Card.GetFlagEffect`](/api/functions/Card/GetFlagEffect) | `imported_from_dataeditorx` | 466 | The type of returned c is the number of identifying effects of the code |
| [`Auxiliary.AddLinkProcedure`](/api/functions/Auxiliary/AddLinkProcedure) | `imported_from_dataeditorx` | 460 | Add a Link Summon procedure for c Use minc-maxc monsters satisfying filter condition f [and within the group satisfying filter condition gf] as Link Materials |
| [`Card.IsSummonType`](/api/functions/Card/IsSummonType) | `imported_from_dataeditorx` | 457 | Check if card c's summon type is sumtype |
| [`Card.CompleteProcedure`](/api/functions/Card/CompleteProcedure) | `imported_from_dataeditorx` | 455 | So that c to complete the formal call procedures |
| [`Card.IsStatus`](/api/functions/Card/IsStatus) | `imported_from_dataeditorx` | 455 | Check whether c contains a status code |
| [`Duel.GetLocationCountFromEx`](/api/functions/Duel/GetLocationCountFromEx) | `imported_from_dataeditorx` | 444 | Return the number of available slots on player's field [after targets leave due to reason_player] for Special Summoning card sc from the Extra Deck in zone |
| [`Duel.CheckReleaseGroup`](/api/functions/Duel/CheckReleaseGroup) | `imported_from_dataeditorx` | 443 | Check if the player has at least count of cards that meet the filter condition f and are not equal to ex (non-superior summons) The fifth parameter starts as an extra... |
| [`Card.GetOwner`](/api/functions/Card/GetOwner) | `imported_from_dataeditorx` | 439 | Returns the holder of c |
| [`Effect.GetOwner`](/api/functions/Effect/GetOwner) | `imported_from_dataeditorx` | 439 | Returns the Owner property |
| [`Card.IsPreviousPosition`](/api/functions/Card/IsPreviousPosition) | `imported_from_dataeditorx` | 438 | Check whether the c position before the change is represented by pos |
| [`Duel.SelectReleaseGroup`](/api/functions/Duel/SelectReleaseGroup) | `imported_from_dataeditorx` | 430 | Filter function, allowing players to choose from the field min-max Zhang is not equal to ex to meet the conditions f can be liberated card (non-superior summon) |
| [`Group.FilterCount`](/api/functions/Group/FilterCount) | `imported_from_dataeditorx` | 425 | Filter function, and Group.Filter is basically the same, the difference is that this function only returns the number of cards to meet the conditions |
| [`Group.FromCards`](/api/functions/Group/FromCards) | `imported_from_dataeditorx` | 420 | Indefinite parameters, the incoming card into a combination of all cards and return |
| [`Auxiliary.TargetBoolFunction`](/api/functions/Auxiliary/TargetBoolFunction) | `imported_from_dataeditorx` | 415 | Used in effect registration, returns a function with a bool return type; additional parameters start from the second parameter function Auxiliary.TargetBoolFunction(f,... |
| [`Duel.GetFieldGroup`](/api/functions/Duel/GetFieldGroup) | `imported_from_dataeditorx` | 411 | Returns the card at the specified location |
| [`Auxiliary.EnablePendulumAttribute`](/api/functions/Auxiliary/EnablePendulumAttribute) | `imported_from_dataeditorx` | 389 | Add Pendulum Monster attributes to c (Pendulum Summon, Pendulum Card activation) If active_effect=false, do not register the Pendulum Card's "card activation" effect |
| [`Duel.NegateActivation`](/api/functions/Duel/NegateActivation) | `imported_from_dataeditorx` | 385 | So that the chain chainc launch invalid, the return value that is successful |
| [`Duel.IsChainNegatable`](/api/functions/Duel/IsChainNegatable) | `imported_from_dataeditorx` | 379 | Check the chain chainc launch can be invalid |
| [`Effect.GetCode`](/api/functions/Effect/GetCode) | `imported_from_dataeditorx` | 358 | Returns the code property |
| [`Card.GetBattleTarget`](/api/functions/Card/GetBattleTarget) | `imported_from_dataeditorx` | 353 | Returns the card that fought with c |
| [`Duel.GetFlagEffect`](/api/functions/Duel/GetFlagEffect) | `imported_from_dataeditorx` | 331 | Returns the number of specific marker effects for the player's player |
| [`Duel.IsPlayerCanSpecialSummonMonster`](/api/functions/Duel/IsPlayerCanSpecialSummonMonster) | `imported_from_dataeditorx` | 330 | Check player player can be pos to the form of special summon the parameters of the monster to the target_player field This function is usually used to determine whethe... |
| [`Duel.RegisterFlagEffect`](/api/functions/Duel/RegisterFlagEffect) | `imported_from_dataeditorx` | 329 | For the player to register the global environment logo effect This effect always affects the player's (EFFECT_FLAG_PLAYER_TARGET) and will not be invalidated The rest... |
| [`Group.AddCard`](/api/functions/Group/AddCard) | `imported_from_dataeditorx` | 327 | Increase g to g |
| [`Card.GetBaseAttack`](/api/functions/Card/GetBaseAttack) | `imported_from_dataeditorx` | 321 | Return the original attack power of c |
| [`Card.IsCanBeEffectTarget`](/api/functions/Card/IsCanBeEffectTarget) | `imported_from_dataeditorx` | 320 | Check whether c can be the object of effect e |
| [`Effect.Reset`](/api/functions/Effect/Reset) | `imported_from_dataeditorx` | 291 | The effect of e reset, reset can not be used after this effect |
| [`Duel.GetOperatedGroup`](/api/functions/Duel/GetOperatedGroup) | `imported_from_dataeditorx` | 285 | This function returns a card set that was actually manipulated before a card operation Duel.Destroy, Duel.Remove, Duel.SendtoGrave, Duel.SendtoHand, Duel.SendtoDeck, D... |
| [`Group.KeepAlive`](/api/functions/Group/KeepAlive) | `imported_from_dataeditorx` | 279 | Let the deck continue, set the deck to effect LabelObject needs to be set |
| [`Auxiliary.Next`](/api/functions/Auxiliary/Next) | `imported_from_dataeditorx` | 273 | Iterator for group g; the pointer starts at the first card and moves to the next card with each call, typically used when operating on cards in g For example: local g=... |
| [`Duel.Recover`](/api/functions/Duel/Recover) | `imported_from_dataeditorx` | 267 | To reason reason players to player value LP, return to the actual response value The return value is 0 if it is affected by an effect such as a return to harm. Is_step... |
| [`Card.IsForbidden`](/api/functions/Card/IsForbidden) | `imported_from_dataeditorx` | 265 | Check whether c is in the declaration prohibition state |
| [`Duel.GetLP`](/api/functions/Duel/GetLP) | `imported_from_dataeditorx` | 265 | Returns the current LP of the player's player |
| [`Duel.SelectEffectYesNo`](/api/functions/Duel/SelectEffectYesNo) | `imported_from_dataeditorx` | 263 | Let players choose whether to launch the card player c effect |
| [`Duel.NegateEffect`](/api/functions/Duel/NegateEffect) | `imported_from_dataeditorx` | 260 | So that the chain chainc invalid effect, the return value that is successful |
| [`Card.IsSummonPlayer`](/api/functions/Card/IsSummonPlayer) | `imported_from_dataeditorx` | 253 | Check if the player who Normal Summoned or Special Summoned card c is player |
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
| [`Duel.IsChainDisablable`](/api/functions/Duel/IsChainDisablable) | `imported_from_dataeditorx` | 156 | Check chainC effect can be invalid |
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
| [`Duel.CheckReleaseGroupEx`](/api/functions/Duel/CheckReleaseGroupEx) | `imported_from_dataeditorx` | 115 | Check whether there are at least count cards that can satisfy the filter condition f and are not equal to ex. (For non-superior summoning) |
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
| ...and 368 more |  |  |  |

## Raw Chinese In English Fields

No raw Chinese text was detected in English fields during this generation.

## DataEditorX Sync Rule

Sync generated `_functions` and `_function_english` files to DataEditorX only after the reviewed text has been regenerated here. Sacred Book is the source of truth for the next pass.
