# Function Translation Review

This queue tracks function pages whose English should be reviewed by hand. It is stricter than the generator backlog: imported English can be technically present but still read like a rough machine translation.

## Summary

- Total functions: **998**
- Functions used by current scripts: **753**
- Functions with raw Chinese text in English fields: **0**
- Functions queued for natural-English review: **594**

## English Status Counts

| Status | Count |
| --- | ---: |
| `imported_from_dataeditorx` | 594 |
| `translated_exact` | 404 |

## Priority Review Queue

Sorted by current script usage count so the most visible function pages are reviewed first.

| Function | Status | Script Uses | Current English Preview |
| --- | --- | ---: | --- |
| [`Card.IsControler`](/api/functions/Card/IsControler) | `imported_from_dataeditorx` | 4889 | Check whether the current control of c is a controler |
| [`Card.IsRace`](/api/functions/Card/IsRace) | `imported_from_dataeditorx` | 2789 | Check if c is race race |
| [`Card.IsAbleToHand`](/api/functions/Card/IsAbleToHand) | `imported_from_dataeditorx` | 2720 | Check whether c can hand Note: This function returns false only if the card or player is affected by the effect of being unable to join the hand (such as Ray King) |
| [`Card.EnableReviveLimit`](/api/functions/Card/EnableReviveLimit) | `imported_from_dataeditorx` | 2609 | Add a limit to the cs for c |
| [`Duel.ConfirmCards`](/api/functions/Duel/ConfirmCards) | `imported_from_dataeditorx` | 2581 | Identify targets for the player |
| [`Effect.Clone`](/api/functions/Effect/Clone) | `imported_from_dataeditorx` | 2492 | Create a new copy of effect e |
| [`Group.Clone`](/api/functions/Group/Clone) | `imported_from_dataeditorx` | 2491 | Create a new copy of card group g |
| [`Duel.GetChainInfo`](/api/functions/Duel/GetChainInfo) | `imported_from_dataeditorx` | 2166 | Returns the chainc information, if chainc = 0, returns the chain of information currently being processed This function returns the corresponding number of return valu... |
| [`Duel.RegisterEffect`](/api/functions/Duel/RegisterEffect) | `imported_from_dataeditorx` | 2115 | Register the effect e as the player's effect to the global environment |
| [`Duel.BreakEffect`](/api/functions/Duel/BreakEffect) | `imported_from_dataeditorx` | 1927 | Interrupt the current effect, so that after the effect of treatment as not treated simultaneously, this function will cause the wrong time |
| [`Effect.SetHintTiming`](/api/functions/Effect/SetHintTiming) | `imported_from_dataeditorx` | 1837 | Set the prompt point |
| [`Effect.SetLabel`](/api/functions/Effect/SetLabel) | `imported_from_dataeditorx` | 1706 | Sets the Label property |
| [`Effect.GetLabel`](/api/functions/Effect/GetLabel) | `imported_from_dataeditorx` | 1697 | Returns the Label property |
| [`Effect.SetLabelObject`](/api/functions/Effect/SetLabelObject) | `imported_from_dataeditorx` | 1678 | Sets the LabelObject property |
| [`Effect.GetLabelObject`](/api/functions/Effect/GetLabelObject) | `imported_from_dataeditorx` | 1630 | Returns the LabelObject property |
| [`Card.IsAttribute`](/api/functions/Card/IsAttribute) | `imported_from_dataeditorx` | 1441 | Check whether c belongs to attribute attribute |
| [`Auxiliary.NecroValleyFilter`](/api/functions/Auxiliary/NecroValleyFilter) | `imported_from_dataeditorx` | 1314 | Return a new filter condition based on filter condition f: cards that satisfy f and are not affected by Necrovalley function Auxiliary.NecroValleyFilter(f) return func... |
| [`Duel.SelectYesNo`](/api/functions/Duel/SelectYesNo) | `imported_from_dataeditorx` | 1293 | Let player player select Yes or No |
| [`Card.IsReason`](/api/functions/Card/IsReason) | `imported_from_dataeditorx` | 1246 | Check if c contains the reason |
| [`Card.GetControler`](/api/functions/Card/GetControler) | `imported_from_dataeditorx` | 1228 | Returns the current controller of c |
| [`Duel.GetTurnPlayer`](/api/functions/Duel/GetTurnPlayer) | `imported_from_dataeditorx` | 1212 | Returns the current round of players |
| [`Card.IsOnField`](/api/functions/Card/IsOnField) | `imported_from_dataeditorx` | 1094 | Check if c is present Note: This function returns false when the monster summons, reverses the call, and when the summon is successful |
| [`Effect.IsActiveType`](/api/functions/Effect/IsActiveType) | `imported_from_dataeditorx` | 1079 | Check if the effect type of e (monster, magic, trap) has a type |
| [`Card.IsPreviousLocation`](/api/functions/Card/IsPreviousLocation) | `imported_from_dataeditorx` | 1031 | Check if the location before c is location |
| [`bit.band`](/api/functions/bit/band) | `imported_from_dataeditorx` | 970 | A and b with the bit |
| [`Card.IsFacedown`](/api/functions/Card/IsFacedown) | `imported_from_dataeditorx` | 963 | Check whether c is the backside representation |
| [`Effect.GetHandlerPlayer`](/api/functions/Effect/GetHandlerPlayer) | `imported_from_dataeditorx` | 952 | Return to the current, usually Handle controller |
| [`Duel.SetTargetPlayer`](/api/functions/Duel/SetTargetPlayer) | `imported_from_dataeditorx` | 950 | Set the player that is currently handling the chained object to player |
| [`Duel.GetFieldGroupCount`](/api/functions/Duel/GetFieldGroupCount) | `imported_from_dataeditorx` | 938 | Returns the number of cards in the specified location |
| [`Duel.SetTargetParam`](/api/functions/Duel/SetTargetParam) | `imported_from_dataeditorx` | 908 | Sets the object parameters of the chain that is currently being processed into param |
| [`Duel.GetAttacker`](/api/functions/Duel/GetAttacker) | `imported_from_dataeditorx` | 857 | Return the card for this combat attack |
| [`Auxiliary.FilterBoolFunction`](/api/functions/Auxiliary/FilterBoolFunction) | `imported_from_dataeditorx` | 856 | Filter cards satisfying a single filter condition f, returning a function with a bool return type; additional parameters start from the second parameter function Auxil... |
| [`Card.RegisterFlagEffect`](/api/functions/Card/RegisterFlagEffect) | `imported_from_dataeditorx` | 853 | For the registration of a logo with the results Note: The effect of the registration to the card is not used for the system, Even if the code and the built-in effect c... |
| [`Duel.Draw`](/api/functions/Duel/Draw) | `imported_from_dataeditorx` | 826 | Let the player play the count card with the reason, and return the number of cards actually drawn If the reason contains REASON_RULE the draw is not affected by the "c... |
| [`Duel.GetCurrentPhase`](/api/functions/Duel/GetCurrentPhase) | `imported_from_dataeditorx` | 824 | Returns the current stage |
| [`Duel.Damage`](/api/functions/Duel/Damage) | `imported_from_dataeditorx` | 817 | To the reason reason to give players the player caused value damage, the actual value of the damage received The return value is 0 if the damage becomes an effect such... |
| [`Group.IsContains`](/api/functions/Group/IsContains) | `imported_from_dataeditorx` | 802 | Check g for card c |
| [`Card.IsLevelBelow`](/api/functions/Card/IsLevelBelow) | `imported_from_dataeditorx` | 795 | Check whether c is below the level level (at least 1) |
| [`Card.IsAbleToRemove`](/api/functions/Card/IsAbleToRemove) | `imported_from_dataeditorx` | 781 | Check whether c can be player except player |
| [`Card.IsPreviousControler`](/api/functions/Card/IsPreviousControler) | `imported_from_dataeditorx` | 761 | Check if card c's previous controller was player |
| [`Card.IsLevelAbove`](/api/functions/Card/IsLevelAbove) | `imported_from_dataeditorx` | 754 | Check whether c is above level level |
| [`Auxiliary.bfgcost`](/api/functions/Auxiliary/bfgcost) | `imported_from_dataeditorx` | 752 | Simplified method for the filter condition of banishing this card, used in effect registration for cost function aux.bfgcost(e, tp, eg, ep, ev, re, r, rp, chk) if chk=... |
| [`Effect.IsHasType`](/api/functions/Effect/IsHasType) | `imported_from_dataeditorx` | 735 | Check if the effect is of type type |
| [`Duel.HintSelection`](/api/functions/Duel/HintSelection) | `imported_from_dataeditorx` | 731 | Manually displays the animated effect of the selected object for g and records that the card is selected as the object |
| [`Duel.IsPlayerAffectedByEffect`](/api/functions/Duel/IsPlayerAffectedByEffect) | `imported_from_dataeditorx` | 715 | Check if the player is affected by the effect of the code type, and return the effect if there is one |
| [`Duel.GetMZoneCount`](/api/functions/Duel/GetMZoneCount) | `imported_from_dataeditorx` | 702 | Return the number of available [zone slots] in the Monster Zone on player's field [after targets leave] |
| [`Card.IsLevel`](/api/functions/Card/IsLevel) | `imported_from_dataeditorx` | 676 | Check if card c is Level level1 [, or level2...] |
| [`Card.GetAttack`](/api/functions/Card/GetAttack) | `imported_from_dataeditorx` | 658 | Return the current attack power of c, the return value is a negative that is "?" |
| [`Duel.GetAttackTarget`](/api/functions/Duel/GetAttackTarget) | `imported_from_dataeditorx` | 658 | Return to the battle was attacked card, if the return nil said that a direct attack |
| [`Duel.SetTargetCard`](/api/functions/Duel/SetTargetCard) | `imported_from_dataeditorx` | 638 | Sets the currently chained objects to targets Note that here the object refers to the generalized object, including objects that do not take the effect that the object... |
| [`Duel.DiscardHand`](/api/functions/Duel/DiscardHand) | `imported_from_dataeditorx` | 625 | Filter function allows the player to select and discard the player to meet the screening conditions f soldiers is not equal to ex min-max Zhang card The seventh argume... |
| [`Group.Merge`](/api/functions/Group/Merge) | `imported_from_dataeditorx` | 622 | Combine all cards in g2 to g1 Note: g2 itself does not change |
| [`Card.IsImmuneToEffect`](/api/functions/Card/IsImmuneToEffect) | `imported_from_dataeditorx` | 604 | Check whether c immune effect e (that is not affected by the impact of e) |
| [`Duel.GetMatchingGroupCount`](/api/functions/Duel/GetMatchingGroupCount) | `imported_from_dataeditorx` | 589 | Filter function to return to the specified location to meet the filter condition f and not equal to the number of ex card |
| [`Auxiliary.AddXyzProcedure`](/api/functions/Auxiliary/AddXyzProcedure) | `imported_from_dataeditorx` | 578 | Add an excess summon for c With the conditions to meet the conditions for the f-level cv-maxct lv monster to be stacked The rest of the parameters are used to stack on... |
| [`Card.GetCode`](/api/functions/Card/GetCode) | `imported_from_dataeditorx` | 569 | Returns the current codename for c (possibly because the effect changes) |
| [`Card.IsRelateToBattle`](/api/functions/Card/IsRelateToBattle) | `imported_from_dataeditorx` | 565 | Check whether c is associated with this battle Note: This effect is usually used for damage calculation before the end of the injury phase, used to check whether the f... |
| [`Card.GetLevel`](/api/functions/Card/GetLevel) | `imported_from_dataeditorx` | 559 | Returns the current level of c |
| [`Auxiliary.NonTuner`](/api/functions/Auxiliary/NonTuner) | `imported_from_dataeditorx` | 503 | Filter non-Tuner monsters satisfying a single filter condition f, returning a function with a bool return type; if only non-Tuner monsters are required, use aux.NonTun... |
| [`Auxiliary.AddSynchroProcedure`](/api/functions/Auxiliary/AddSynchroProcedure) | `imported_from_dataeditorx` | 488 | Add a cohomology call to c F1 to adjust the filter to meet the conditions, f2 to adjust to meet other than the filter conditions (usually aux.NonTuner) Adjust monsters... |
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
| ...and 434 more |  |  |  |

## Raw Chinese In English Fields

No raw Chinese text was detected in English fields during this generation.

## DataEditorX Sync Rule

Sync generated `_functions` and `_function_english` files to DataEditorX only after the reviewed text has been regenerated here. Sacred Book is the source of truth for the next pass.
