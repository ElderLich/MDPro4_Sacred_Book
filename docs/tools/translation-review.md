# Function Translation Review

This queue tracks function pages whose English should be reviewed by hand. It is stricter than the generator backlog: imported English can be technically present but still read like a rough machine translation.

## Summary

- Total functions: **998**
- Functions used by current scripts: **753**
- Functions with raw Chinese text in English fields: **0**
- Functions queued for natural-English review: **646**

## English Status Counts

| Status | Count |
| --- | ---: |
| `imported_from_dataeditorx` | 646 |
| `translated_exact` | 352 |

## Priority Review Queue

Sorted by current script usage count so the most visible function pages are reviewed first.

| Function | Status | Script Uses | Current English Preview |
| --- | --- | ---: | --- |
| [`Card.RegisterEffect`](/api/functions/Card/RegisterEffect) | `imported_from_dataeditorx` | 13259 | Register the effect e to c, return the global id of the effect, and set the Handler of e to c By default, if c is registered with the effect of immune e then the regis... |
| [`Effect.CreateEffect`](/api/functions/Effect/CreateEffect) | `imported_from_dataeditorx` | 13255 | Create a new empty effect And the owner of the effect is c |
| [`Effect.SetType`](/api/functions/Effect/SetType) | `imported_from_dataeditorx` | 13255 | Set the Type property for effect e |
| [`Effect.SetCode`](/api/functions/Effect/SetCode) | `imported_from_dataeditorx` | 12685 | Set the Code property for effect e |
| [`Effect.SetOperation`](/api/functions/Effect/SetOperation) | `imported_from_dataeditorx` | 12642 | Set the Operation property |
| [`Effect.SetTarget`](/api/functions/Effect/SetTarget) | `imported_from_dataeditorx` | 12249 | Set the Target property |
| [`Effect.SetCategory`](/api/functions/Effect/SetCategory) | `imported_from_dataeditorx` | 11335 | Set the Category property |
| [`Effect.SetProperty`](/api/functions/Effect/SetProperty) | `imported_from_dataeditorx` | 10315 | Set the Property property |
| [`Effect.GetHandler`](/api/functions/Effect/GetHandler) | `imported_from_dataeditorx` | 10235 | Returns the card on which the effect takes effect (usually a card that registers the effect with Card.RegisterEffect) |
| [`Duel.Hint`](/api/functions/Duel/Hint) | `imported_from_dataeditorx` | 9864 | Send hint_type to the player player type of message prompts, the contents of the prompt desc |
| [`Auxiliary.Stringid`](/api/functions/Auxiliary/Stringid) | `imported_from_dataeditorx` | 9526 | Used to index the card number code for the card the first id (from 0) effect prompts |
| [`Effect.SetDescription`](/api/functions/Effect/SetDescription) | `imported_from_dataeditorx` | 9024 | Sets the effect description for effect e |
| [`Effect.SetRange`](/api/functions/Effect/SetRange) | `imported_from_dataeditorx` | 9017 | Set the Range property for effect e |
| [`Effect.SetCondition`](/api/functions/Effect/SetCondition) | `imported_from_dataeditorx` | 8970 | Set the Condition property |
| [`Effect.SetCountLimit`](/api/functions/Effect/SetCountLimit) | `imported_from_dataeditorx` | 7849 | Set the number of times a round can be launched count (only trigger type effect is valid), the same code (not equal to 0 or 1) share a number of times The code contain... |
| [`Duel.IsExistingMatchingCard`](/api/functions/Duel/IsExistingMatchingCard) | `imported_from_dataeditorx` | 7440 | Filter the function to check if there are at least count cards that satisfy the filter condition f and not equal to ex The seventh argument starts as an extra parameter |
| [`Card.IsRelateToEffect`](/api/functions/Card/IsRelateToEffect) | `imported_from_dataeditorx` | 6854 | Check whether c is associated with effect e Note: Each launch into the effect of chain, the effect of launching the card, and the effect of the specified object (With... |
| [`Card.IsFaceup`](/api/functions/Card/IsFaceup) | `imported_from_dataeditorx` | 6473 | Check whether c is a surface-side representation |
| [`Effect.SetValue`](/api/functions/Effect/SetValue) | `imported_from_dataeditorx` | 6375 | Set the Value property |
| [`Card.IsLocation`](/api/functions/Card/IsLocation) | `imported_from_dataeditorx` | 5741 | Check if c is the current location Note: When the monster summon, reverse call, call special summon before the success, And location = LOCATION_MZONE, this function re... |
| [`Group.GetCount`](/api/functions/Group/GetCount) | `imported_from_dataeditorx` | 5682 | Returns the number of cards in g |
| [`Card.IsType`](/api/functions/Card/IsType) | `imported_from_dataeditorx` | 5427 | Check if c is of type type |
| [`Card.IsSetCard`](/api/functions/Card/IsSetCard) | `imported_from_dataeditorx` | 5411 | Check whether c is a card with the name setname |
| [`Duel.SelectMatchingCard`](/api/functions/Duel/SelectMatchingCard) | `imported_from_dataeditorx` | 5321 | Filter function, the player sel_player select the specified location to meet the filter condition f and not equal to the ex min-max card The ninth parameter starts as... |
| [`Effect.SetReset`](/api/functions/Effect/SetReset) | `imported_from_dataeditorx` | 5295 | Set the reset parameter |
| [`Duel.GetLocationCount`](/api/functions/Duel/GetLocationCount) | `imported_from_dataeditorx` | 5270 | Returns the number of spaces available in the player's field Location can only be LOCATION_MZONE or LOCATION_SZONE Reason is LOCATION_REASON_TOFIELD or LOCATION_REASON... |
| [`Duel.SelectTarget`](/api/functions/Duel/SelectTarget) | `imported_from_dataeditorx` | 5043 | Filter function, so that player sel_player select the specified location to meet the filter condition f and not equal ex And can be the min-max card of the object that... |
| [`Card.IsControler`](/api/functions/Card/IsControler) | `imported_from_dataeditorx` | 4889 | Check whether the current control of c is a controler |
| [`Duel.IsExistingTarget`](/api/functions/Duel/IsExistingTarget) | `imported_from_dataeditorx` | 4870 | Filter function to check whether there is at least the specified number of positions to meet the filter conditions f and not equal ex And can become a card of an objec... |
| [`Effect.SetCost`](/api/functions/Effect/SetCost) | `imported_from_dataeditorx` | 4714 | Set the Cost property |
| [`Duel.GetFirstTarget`](/api/functions/Duel/GetFirstTarget) | `imported_from_dataeditorx` | 4696 | Returns all linked object cards that are normally only used when an object is used |
| [`Duel.SpecialSummon`](/api/functions/Duel/SpecialSummon) | `imported_from_dataeditorx` | 4581 | Let player player to sumtype way, pos that special targets to target_player target field If nocheck is true, the card's calling condition is disregarded. If nolimit is... |
| [`Card.IsCanBeSpecialSummoned`](/api/functions/Card/IsCanBeSpecialSummoned) | `imported_from_dataeditorx` | 4086 | Check whether c can be sumplayer with the effect of the player e to sumtype form sumpos special summon to target_player field If nocheck is true, the call condition of... |
| [`Group.GetFirst`](/api/functions/Group/GetFirst) | `imported_from_dataeditorx` | 3524 | Returns the first card in g and resets the current pointer to the first card in g Returns nil if card does not exist in g |
| [`Duel.GetMatchingGroup`](/api/functions/Duel/GetMatchingGroup) | `imported_from_dataeditorx` | 3195 | Filter function to return to the specified location to meet the filter condition f and not equal to the ex card The sixth parameter starts as an extra parameter |
| [`Effect.SetTargetRange`](/api/functions/Effect/SetTargetRange) | `imported_from_dataeditorx` | 2987 | Set the Target Range property for effect e S_range refers to our area of ​​influence The o_range value affects the partner area If the EFFECT_FLAG_ABSOLUTE_RANGE flag... |
| [`Card.IsCode`](/api/functions/Card/IsCode) | `imported_from_dataeditorx` | 2963 | Check whether the card number c is code1[, or code2 ...] |
| [`Duel.SendtoHand`](/api/functions/Duel/SendtoHand) | `imported_from_dataeditorx` | 2963 | The reason to target the player sent to the player's hand, the return value is the actual number of operations If player is nil, the card's holder's hand is returned |
| [`Card.IsRace`](/api/functions/Card/IsRace) | `imported_from_dataeditorx` | 2789 | Check if c is race race |
| [`Card.IsAbleToHand`](/api/functions/Card/IsAbleToHand) | `imported_from_dataeditorx` | 2720 | Check whether c can hand Note: This function returns false only if the card or player is affected by the effect of being unable to join the hand (such as Ray King) |
| [`Duel.Destroy`](/api/functions/Duel/Destroy) | `imported_from_dataeditorx` | 2699 | Destroy targets dest by reason reason, the return value is actually destroyed by the number If the reason contains REASON_RULE, the break event will not check whether... |
| [`Card.EnableReviveLimit`](/api/functions/Card/EnableReviveLimit) | `imported_from_dataeditorx` | 2609 | Add a limit to the cs for c |
| [`Duel.ConfirmCards`](/api/functions/Duel/ConfirmCards) | `imported_from_dataeditorx` | 2581 | Identify targets for the player |
| [`Effect.Clone`](/api/functions/Effect/Clone) | `imported_from_dataeditorx` | 2492 | Create a new copy of effect e |
| [`Group.Clone`](/api/functions/Group/Clone) | `imported_from_dataeditorx` | 2491 | Create a new copy of card group g |
| [`Group.IsExists`](/api/functions/Group/IsExists) | `imported_from_dataeditorx` | 2212 | Filter function to check if there is at least count of cards in g that satisfy the filter condition f and not equal to ex Starting from the 5th parameter as an additio... |
| [`Duel.GetChainInfo`](/api/functions/Duel/GetChainInfo) | `imported_from_dataeditorx` | 2166 | Returns the chainc information, if chainc = 0, returns the chain of information currently being processed This function returns the corresponding number of return valu... |
| [`Duel.RegisterEffect`](/api/functions/Duel/RegisterEffect) | `imported_from_dataeditorx` | 2115 | Register the effect e as the player's effect to the global environment |
| [`Duel.BreakEffect`](/api/functions/Duel/BreakEffect) | `imported_from_dataeditorx` | 1927 | Interrupt the current effect, so that after the effect of treatment as not treated simultaneously, this function will cause the wrong time |
| [`Effect.SetHintTiming`](/api/functions/Effect/SetHintTiming) | `imported_from_dataeditorx` | 1837 | Set the prompt point |
| [`Effect.SetLabel`](/api/functions/Effect/SetLabel) | `imported_from_dataeditorx` | 1706 | Sets the Label property |
| [`Effect.GetLabel`](/api/functions/Effect/GetLabel) | `imported_from_dataeditorx` | 1697 | Returns the Label property |
| [`Effect.SetLabelObject`](/api/functions/Effect/SetLabelObject) | `imported_from_dataeditorx` | 1678 | Sets the LabelObject property |
| [`Effect.GetLabelObject`](/api/functions/Effect/GetLabelObject) | `imported_from_dataeditorx` | 1630 | Returns the LabelObject property |
| [`Duel.Remove`](/api/functions/Duel/Remove) | `imported_from_dataeditorx` | 1626 | In the case of reason, except for the pos form, the return value is the actual number being manipulated If the reason contains REASON_TEMPORARY, then the exception is... |
| [`Card.IsAttribute`](/api/functions/Card/IsAttribute) | `imported_from_dataeditorx` | 1441 | Check whether c belongs to attribute attribute |
| [`Group.Select`](/api/functions/Group/Select) | `imported_from_dataeditorx` | 1391 | Let player player from g select the min-max Zhang is not equal to the ex card |
| [`Auxiliary.NecroValleyFilter`](/api/functions/Auxiliary/NecroValleyFilter) | `imported_from_dataeditorx` | 1314 | Return a new filter condition based on filter condition f: cards that satisfy f and are not affected by Necrovalley function Auxiliary.NecroValleyFilter(f) return func... |
| [`Duel.SelectYesNo`](/api/functions/Duel/SelectYesNo) | `imported_from_dataeditorx` | 1293 | Let player player select Yes or No |
| [`Card.IsReason`](/api/functions/Card/IsReason) | `imported_from_dataeditorx` | 1246 | Check if c contains the reason |
| [`Card.GetControler`](/api/functions/Card/GetControler) | `imported_from_dataeditorx` | 1228 | Returns the current controller of c |
| [`Duel.GetTurnPlayer`](/api/functions/Duel/GetTurnPlayer) | `imported_from_dataeditorx` | 1212 | Returns the current round of players |
| [`Card.IsOnField`](/api/functions/Card/IsOnField) | `imported_from_dataeditorx` | 1094 | Check if c is present Note: This function returns false when the monster summons, reverses the call, and when the summon is successful |
| [`Effect.IsActiveType`](/api/functions/Effect/IsActiveType) | `imported_from_dataeditorx` | 1079 | Check if the effect type of e (monster, magic, trap) has a type |
| [`Duel.Release`](/api/functions/Duel/Release) | `imported_from_dataeditorx` | 1067 | The reason for the liberation of targets to return the value of the actual liberation of the number of targets If the reason contains REASON_COST, it will not check wh... |
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
| [`Group.Filter`](/api/functions/Group/Filter) | `imported_from_dataeditorx` | 823 | The filter function filters the card from g that satisfies the filter condition f and is not equal to ex Starting from the 4th parameter as an additional parameter |
| [`Duel.Damage`](/api/functions/Duel/Damage) | `imported_from_dataeditorx` | 817 | To the reason reason to give players the player caused value damage, the actual value of the damage received The return value is 0 if the damage becomes an effect such... |
| [`Group.IsContains`](/api/functions/Group/IsContains) | `imported_from_dataeditorx` | 802 | Check g for card c |
| [`Card.IsLevelBelow`](/api/functions/Card/IsLevelBelow) | `imported_from_dataeditorx` | 795 | Check whether c is below the level level (at least 1) |
| [`Card.IsAbleToRemove`](/api/functions/Card/IsAbleToRemove) | `imported_from_dataeditorx` | 781 | Check whether c can be player except player |
| [`Group.GetNext`](/api/functions/Group/GetNext) | `imported_from_dataeditorx` | 781 | Point the pointer to the next card and return the card, or nil if it does not exist |
| [`Duel.SpecialSummonComplete`](/api/functions/Duel/SpecialSummonComplete) | `imported_from_dataeditorx` | 780 | This function is called after determining that a number of calls to Duel.SpecialSummonStep are completed, for triggering an event |
| [`Duel.SpecialSummonStep`](/api/functions/Duel/SpecialSummonStep) | `imported_from_dataeditorx` | 779 | This function is Duel.SpecialSummon decomposition process, only a special summon a card c This function is used for an effect while simultaneously calling multiple car... |
| [`Card.IsPreviousControler`](/api/functions/Card/IsPreviousControler) | `imported_from_dataeditorx` | 761 | Check if card c's previous controller was player |
| [`Card.IsLevelAbove`](/api/functions/Card/IsLevelAbove) | `imported_from_dataeditorx` | 754 | Check whether c is above level level |
| [`Auxiliary.bfgcost`](/api/functions/Auxiliary/bfgcost) | `imported_from_dataeditorx` | 752 | Simplified method for the filter condition of banishing this card, used in effect registration for cost function aux.bfgcost(e, tp, eg, ep, ev, re, r, rp, chk) if chk=... |
| [`Effect.IsHasType`](/api/functions/Effect/IsHasType) | `imported_from_dataeditorx` | 735 | Check if the effect is of type type |
| [`Duel.HintSelection`](/api/functions/Duel/HintSelection) | `imported_from_dataeditorx` | 731 | Manually displays the animated effect of the selected object for g and records that the card is selected as the object |
| [`Duel.IsPlayerAffectedByEffect`](/api/functions/Duel/IsPlayerAffectedByEffect) | `imported_from_dataeditorx` | 715 | Check if the player is affected by the effect of the code type, and return the effect if there is one |
| [`Duel.GetMZoneCount`](/api/functions/Duel/GetMZoneCount) | `imported_from_dataeditorx` | 702 | Return the number of available [zone slots] in the Monster Zone on player's field [after targets leave] |
| [`Card.IsLevel`](/api/functions/Card/IsLevel) | `imported_from_dataeditorx` | 676 | Check if card c is Level level1 [, or level2...] |
| [`Duel.Equip`](/api/functions/Duel/Equip) | `imported_from_dataeditorx` | 659 | The player as a player c1 equipment card equipment to the c2, the return value that is successful Up = false to retain the card before the representation Is_step = tru... |
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
| [`Duel.ChangePosition`](/api/functions/Duel/ChangePosition) | `imported_from_dataeditorx` | 511 | Changing the representation of targets returns the number of actual operations The attack on the watch side becomes au, the attack on the inside indicates ad, The side... |
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
| [`Duel.MoveToField`](/api/functions/Duel/MoveToField) | `imported_from_dataeditorx` | 254 | Let the player move_player to move the c target_player field, the return value that is successful Dest can only be LOCATION_MZONE or LOCATION_SZONE, pos represents an... |
| [`Card.IsSummonPlayer`](/api/functions/Card/IsSummonPlayer) | `imported_from_dataeditorx` | 253 | Check if the player who Normal Summoned or Special Summoned card c is player |
| [`Effect.GetOperation`](/api/functions/Effect/GetOperation) | `imported_from_dataeditorx` | 253 | Returns the operation attribute |
| [`Effect.GetTarget`](/api/functions/Effect/GetTarget) | `imported_from_dataeditorx` | 253 | Returns the target attribute |
| [`Duel.Overlay`](/api/functions/Duel/Overlay) | `imported_from_dataeditorx` | 251 | The ocard as a stack of cards stacked c |
| [`Card.GetType`](/api/functions/Card/GetType) | `imported_from_dataeditorx` | 246 | Returns the current type of c |
| [`Effect.GetType`](/api/functions/Effect/GetType) | `imported_from_dataeditorx` | 246 | Returns the Type property |
| [`Card.CheckFusionMaterial`](/api/functions/Card/CheckFusionMaterial) | `imported_from_dataeditorx` | 244 | Check if g contains a set of fusion material that c needs [must contain gc] |
| [`Duel.CreateToken`](/api/functions/Duel/CreateToken) | `imported_from_dataeditorx` | 239 | Creates a new Token with the passed in parameter value and returns |
| [`Group.FilterSelect`](/api/functions/Group/FilterSelect) | `imported_from_dataeditorx` | 239 | Filter function, allowing players to choose from the g player min-max sheets meet the screening conditions f and not equal to the ex card Starting with the 7th argumen... |
| [`Effect.GetValue`](/api/functions/Effect/GetValue) | `imported_from_dataeditorx` | 238 | Returns the value attribute |
| [`Auxiliary.tgoval`](/api/functions/Auxiliary/tgoval) | `imported_from_dataeditorx` | 234 | Simplified method for the filter function preventing being targeted by opponent's card effects, used in effect registration for SetValue function aux.tgoval(e, re, rp)... |
| [`Duel.GetTurnCount`](/api/functions/Duel/GetTurnCount) | `imported_from_dataeditorx` | 231 | Returns the current number of turns |
| [`Card.IsFusionSetCard`](/api/functions/Card/IsFusionSetCard) | `imported_from_dataeditorx` | 229 | Check the c as a fusion material can be used as a name setname card |
| ...and 486 more |  |  |  |

## Raw Chinese In English Fields

No raw Chinese text was detected in English fields during this generation.

## DataEditorX Sync Rule

Sync generated `_functions` and `_function_english` files to DataEditorX only after the reviewed text has been regenerated here. Sacred Book is the source of truth for the next pass.
