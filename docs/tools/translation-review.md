# Function Translation Review

This queue tracks function pages whose English should be reviewed by hand. It is stricter than the generator backlog: imported English can be technically present but still read like a rough machine translation.

## Summary

- Total functions: **998**
- Functions used by current scripts: **753**
- Functions with raw Chinese text in English fields: **0**
- Functions queued for natural-English review: **252**

## English Status Counts

| Status | Count |
| --- | ---: |
| `imported_from_dataeditorx` | 252 |
| `translated_exact` | 746 |

## Priority Review Queue

Sorted by current script usage count so the most visible function pages are reviewed first.

| Function | Status | Script Uses | Current English Preview |
| --- | --- | ---: | --- |
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
| [`Group.SelectWithSumEqual`](/api/functions/Group/SelectWithSumEqual) | `imported_from_dataeditorx` | 19 | Let the player player select a subset of min-max from g so that the sum of the specific functions of the subset is equal to sum, starting at the 7th argument as an ext... |
| [`Auxiliary.bdcon`](/api/functions/Auxiliary/bdcon) | `imported_from_dataeditorx` | 18 | Check if e:GetHandler() is related to the current battle, typically used for the condition of EVENT_BATTLE_DESTROYING function Auxiliary.bdcon(e, tp, eg, ep, ev, re, r... |
| [`Card.GetAttackAnnouncedCount`](/api/functions/Card/GetAttackAnnouncedCount) | `imported_from_dataeditorx` | 18 | Returns the number of times this declaration was asserted Note: Attack is invalid will not count the number of attacks, but will be counted into the number of attacks... |
| [`Card.GetTextDefense`](/api/functions/Card/GetTextDefense) | `imported_from_dataeditorx` | 18 | Return the c 's card record of the garrison |
| [`Card.ResetEffect`](/api/functions/Card/ResetEffect) | `imported_from_dataeditorx` | 18 | To reset the type to reset_type, reset the type reset_code manual reset c impact of the impact The reset_type can only be one of the following types, and the correspon... |
| [`Card.GetCardTargetCount`](/api/functions/Card/GetCardTargetCount) | `imported_from_dataeditorx` | 17 | Returns the number of current persistent objects |
| [`Card.GetFusionAttribute`](/api/functions/Card/GetFusionAttribute) | `imported_from_dataeditorx` | 17 | Return the Attribute of card c when used as Fusion Material \[for a Fusion Summon by player\] |
| [`Card.GetSummonPlayer`](/api/functions/Card/GetSummonPlayer) | `imported_from_dataeditorx` | 17 | Return to Summoner / Special Summoner c Players |
| [`Auxiliary.gbspcon`](/api/functions/Auxiliary/gbspcon) | `imported_from_dataeditorx` | 16 | Simplified method for the filter condition of Gladiator Beast general effects (Special Summoned by the effect of a "Gladiator Beast" monster), used in effect registrat... |
| [`Card.CreateRelation`](/api/functions/Card/CreateRelation) | `imported_from_dataeditorx` | 16 | For c1 established in c2 contact this contact, only because c1 occurred RESET_EVENT the event reset |
| [`Card.GetMutualLinkedGroupCount`](/api/functions/Card/GetMutualLinkedGroupCount) | `imported_from_dataeditorx` | 16 | Return the number of cards in the group mutually linked with card c |
| [`Card.IsExtraDeckMonster`](/api/functions/Card/IsExtraDeckMonster) | `imported_from_dataeditorx` | 16 | Check if c is originally a Fusion, Synchro, Xyz, or Link Monster. This function only checks the type, regardless of the monster's current state |
| [`Duel.AnnounceCoin`](/api/functions/Duel/AnnounceCoin) | `imported_from_dataeditorx` | 16 | Let the player declare the positive and negative sides of the coin |
| [`Auxiliary.synlimit`](/api/functions/Auxiliary/synlimit) | `imported_from_dataeditorx` | 15 | Simplified method for the filter function preventing summoning (broadly) by methods other than Synchro Summon, used in effect registration for SetValue se is the effec... |
| [`Card.GetCardTarget`](/api/functions/Card/GetCardTarget) | `imported_from_dataeditorx` | 15 | Returns all currently persistent objects |
| [`Card.GetLinkRace`](/api/functions/Card/GetLinkRace) | `imported_from_dataeditorx` | 15 | Return the Race of card c when used as Link Material \[for a Link Summon by player\] |
| [`Card.IsLinkBelow`](/api/functions/Card/IsLinkBelow) | `imported_from_dataeditorx` | 14 | Check if card c's Link Marker count is link or lower (at least 1) |
| [`Card.IsLinkState`](/api/functions/Card/IsLinkState) | `imported_from_dataeditorx` | 14 | Check if card c is in a linked state |
| [`Auxiliary.AddXyzProcedureLevelFree`](/api/functions/Auxiliary/AddXyzProcedureLevelFree) | `imported_from_dataeditorx` | 13 | Add an Xyz Summon procedure for c Use minc \[to maxc\] monsters satisfying condition f, and within the group satisfying condition gf, for overlay; f is a required condit... |
| [`Auxiliary.IsCanBeQuickEffect`](/api/functions/Auxiliary/IsCanBeQuickEffect) | `imported_from_dataeditorx` | 13 | Check if the effect of c becomes a Quick Effect. |
| [`Card.GetColumnZone`](/api/functions/Card/GetColumnZone) | `imported_from_dataeditorx` | 13 | Return the zones \[from player's perspective\] within the location range that are in the same column as card c \[including left columns and right columns\], location value... |
| [`Card.GetFusionCode`](/api/functions/Card/GetFusionCode) | `imported_from_dataeditorx` | 13 | Return c as the fusion material when the card number (including the original c card number) |
| [`Card.IsOriginalSetCard`](/api/functions/Card/IsOriginalSetCard) | `imported_from_dataeditorx` | 13 | Check if card c is originally a card with setname in its name |
| [`Card.SetFlagEffectLabel`](/api/functions/Card/SetFlagEffectLabel) | `imported_from_dataeditorx` | 13 | Returns whether or not c has an identifier of type code, and sets its Label property to label |
| [`Group.CheckWithSumGreater`](/api/functions/Group/CheckWithSumGreater) | `imported_from_dataeditorx` | 13 | The sum of the subsets is determined by a function f, which is a function that returns an interger value Check that there is a subset in g that satisfies that the sum... |
| [`Auxiliary.AddRitualProcEqual2`](/api/functions/Auxiliary/AddRitualProcEqual2) | `imported_from_dataeditorx` | 12 | Add a Ritual Summon effect for c filter is the condition the Ritual Monster must satisfy; the sum of the Ritual Levels of the materials must equal the Ritual Monster's... |
| [`Auxiliary.bdgcon`](/api/functions/Auxiliary/bdgcon) | `imported_from_dataeditorx` | 12 | Check if e:GetHandler() is related to the current battle, typically used for EVENT_BATTLE_DESTROYING and when an opponent's monster is destroyed by battle and sent to... |
| [`Card.GetLinkedGroupCount`](/api/functions/Card/GetLinkedGroupCount) | `imported_from_dataeditorx` | 12 | Return the number of monster cards in the zones linked to card c |
| [`Card.GetPosition`](/api/functions/Card/GetPosition) | `imported_from_dataeditorx` | 12 | Returns the current representation of c |
| [`Card.GetRealFieldID`](/api/functions/Card/GetRealFieldID) | `imported_from_dataeditorx` | 12 | Returns the actual timestamp for the c transition to the current position Opening the card from the inside does not change this value |
| [`Card.IsCanBeSynchroMaterial`](/api/functions/Card/IsCanBeSynchroMaterial) | `imported_from_dataeditorx` | 12 | Check whether c can become a homophonic homophonic monster sc material |
| [`Duel.GetCounter`](/api/functions/Duel/GetCounter) | `imported_from_dataeditorx` | 12 | Returns the number of counterstype types that exist on the farm S represents the position of the player's own removable pointer, o represents the position of the oppon... |
| [`Duel.GetUsableMZoneCount`](/api/functions/Duel/GetUsableMZoneCount) | `imported_from_dataeditorx` | 12 | Return the number of available Monster Zones on player's field \[for use_player\] NOTE: The original description includes a question mark (?), indicating potential uncer... |
| [`Effect.GetCategory`](/api/functions/Effect/GetCategory) | `imported_from_dataeditorx` | 12 | Returns the Category property |
| [`Auxiliary.AddFusionProcCodeRep`](/api/functions/Auxiliary/AddFusionProcCodeRep) | `imported_from_dataeditorx` | 11 | For the c designated cc the same monster for the fusion material, code for the card number |
| [`Auxiliary.EnableArcanaCoin`](/api/functions/Auxiliary/EnableArcanaCoin) | `imported_from_dataeditorx` | 11 | add "Toss a coin and get the following effects" effect to Arcana Force monsters |
| [`Auxiliary.MZoneSequence`](/api/functions/Auxiliary/MZoneSequence) | `imported_from_dataeditorx` | 11 | Return the Monster Zone sequence number; from left to right, zones are 0-4; for Extra Monster Zones, return left as 1 or right as 3 |
| [`Auxiliary.AddBanishRedirect`](/api/functions/Auxiliary/AddBanishRedirect) | `imported_from_dataeditorx` | 10 | If this face-up card would leave the field, banish it instead. |
| [`Auxiliary.AddEquipSpellEffect`](/api/functions/Auxiliary/AddEquipSpellEffect) | `imported_from_dataeditorx` | 10 | Add EFFECT_TYPE_ACTIVATE effect to Equip Spell Cards |
| [`Auxiliary.AddFusionProcCodeFunRep`](/api/functions/Auxiliary/AddFusionProcCodeFunRep) | `imported_from_dataeditorx` | 10 | Add a Fusion Summon procedure for c Use 1 monster with code and minc-maxc monsters satisfying filter condition f as Fusion Materials Equivalent to aux.AddFusionProcMix... |
| [`Auxiliary.AddFusionProcFunFunRep`](/api/functions/Auxiliary/AddFusionProcFunFunRep) | `imported_from_dataeditorx` | 10 | Add a Fusion Summon procedure for c Use 1 monster satisfying filter condition f1 and minc-maxc monsters satisfying filter condition f2 as Fusion Materials Equivalent t... |
| [`Card.GetBattledGroupCount`](/api/functions/Card/GetBattledGroupCount) | `imported_from_dataeditorx` | 10 | Returns the number of cards battled for this turn |
| [`Card.GetLinkAttribute`](/api/functions/Card/GetLinkAttribute) | `imported_from_dataeditorx` | 10 | Return the Attribute of card c when used as Link Material \[for a Link Summon by player\] |
| [`Card.IsNotTuner`](/api/functions/Card/IsNotTuner) | `imported_from_dataeditorx` | 10 | Check whether c can be used as a non-adjustment |
| [`Duel.GetOverlayCount`](/api/functions/Duel/GetOverlayCount) | `imported_from_dataeditorx` | 10 | Returns the number of all stacked cards in the specified location |
| [`Duel.Readjust`](/api/functions/Duel/Readjust) | `imported_from_dataeditorx` | 10 | Refresh the card information on the field Unspecified or unclear principle Do not use this function to avoid an infinite loop |
| [`Auxiliary.IsMaterialListSetCard`](/api/functions/Auxiliary/IsMaterialListSetCard) | `imported_from_dataeditorx` | 9 | Check if card c lists setcode as a material in its material_setcode |
| [`Auxiliary.qlifilter`](/api/functions/Auxiliary/qlifilter) | `imported_from_dataeditorx` | 9 | Simplified method for the filter function for Qli Monster general immunity (unaffected by effects of monsters with lower original Level/Rank than this card's Level), u... |
| [`Card.GetOriginalRank`](/api/functions/Card/GetOriginalRank) | `imported_from_dataeditorx` | 9 | Returns the class of the card in c |
| [`Card.GetRightScale`](/api/functions/Card/GetRightScale) | `imported_from_dataeditorx` | 9 | Returns the right-hand pendulum scale of c |
| [`Card.GetSynchroLevel`](/api/functions/Card/GetSynchroLevel) | `imported_from_dataeditorx` | 9 | Return to the co-ordination of c with the call monster sc with the level This function returns the same value as Card.GetLevel(c) except for certain cards such as modems. |
| [`Card.IsCanHaveCounter`](/api/functions/Card/IsCanHaveCounter) | `imported_from_dataeditorx` | 9 | Check if countertype counters can be placed on c |
| [`Card.IsDualState`](/api/functions/Card/IsDualState) | `imported_from_dataeditorx` | 9 | Check whether c is in the re-call state |
| [`Card.IsRelateToCard`](/api/functions/Card/IsRelateToCard) | `imported_from_dataeditorx` | 9 | Check whether c1 and c2 are linked |
| [`Auxiliary.AddFusionProcMix`](/api/functions/Auxiliary/AddFusionProcMix) | `imported_from_dataeditorx` | 8 | Add a Fusion Summon procedure for c Use 1 of each card in the additional parameters as Fusion Materials; additional parameters can be function or card code (int code),... |
| [`Auxiliary.CheckUnionEquip`](/api/functions/Auxiliary/CheckUnionEquip) | `imported_from_dataeditorx` | 8 | Check if Union Monster uc can be equipped to monster tc as a Union Equip |
| [`Auxiliary.linklimit`](/api/functions/Auxiliary/linklimit) | `imported_from_dataeditorx` | 8 | Simplified method for the filter function preventing summoning (broadly) by methods other than Link Summon, used in effect registration for SetValue se is the effect u... |
| [`bit.bxor`](/api/functions/bit/bxor) | `imported_from_dataeditorx` | 8 | A and b bit XOR |
| [`bit.rshift`](/api/functions/bit/rshift) | `imported_from_dataeditorx` | 8 | A Move to the right b |
| [`Card.CheckUnionTarget`](/api/functions/Card/CheckUnionTarget) | `imported_from_dataeditorx` | 8 | Check if ec is a valid Union Equip target for c. Checks for EFFECT_UNION_LIMIT and new/old Union effects. |
| [`Card.EnableDualState`](/api/functions/Card/EnableDualState) | `imported_from_dataeditorx` | 8 | Set c to re-call state |
| [`Card.GetColumnGroupCount`](/api/functions/Card/GetColumnGroupCount) | `imported_from_dataeditorx` | 8 | Usage is the same as above, but returns the number of cards |
| [`Card.GetHandSynchro`](/api/functions/Card/GetHandSynchro) | `imported_from_dataeditorx` | 8 | If card c is affected by the hand Synchro effect EFFECT_HAND_SYNCHRO, return Effect e, function target, int min, int max; otherwise return nil |
| [`Card.GetTributeRequirement`](/api/functions/Card/GetTributeRequirement) | `imported_from_dataeditorx` | 8 | Returns the minimum and maximum number of sacrifices required to normally call c |
| [`Card.SetHint`](/api/functions/Card/SetHint) | `imported_from_dataeditorx` | 8 | Set the card prompt for type c to c Type can only be the following value, the corresponding value type is CHINT_TURN Turns CHINT_CARD card id CHINT_RACE race CHINT_ATT... |
| [`Duel.CheckChainUniqueness`](/api/functions/Duel/CheckChainUniqueness) | `imported_from_dataeditorx` | 8 | Check the existence of the current chain of the same name card launch, true that no card with the same name |
| [`Duel.SelectField`](/api/functions/Duel/SelectField) | `imported_from_dataeditorx` | 8 | Have player select zones; flag1 is the low bit, flag2 is the high bit, together forming the selectable zones; count is the number of zones to choose Return the selecte... |
| [`Group.Remove`](/api/functions/Group/Remove) | `imported_from_dataeditorx` | 8 | Remove all cards from g that satisfy the filter condition f and not equal to ex, the fourth parameter starts with the extra argument |
| [`Auxiliary.AddFusionProcShaddoll`](/api/functions/Auxiliary/AddFusionProcShaddoll) | `imported_from_dataeditorx` | 7 | Exclusive to Shaddoll Fusion Monsters; attribute is the required Attribute |
| [`Auxiliary.evospcon`](/api/functions/Auxiliary/evospcon) | `imported_from_dataeditorx` | 7 | Simplified method for the filter condition of Evolsaur general effects (Special Summoned by the effect of an "Evolsaur" monster), used in effect registration for SetCo... |
| [`Card.GetDestination`](/api/functions/Card/GetDestination) | `imported_from_dataeditorx` | 7 | Returns the destination of the c position change This function is valid only when processing position transitions instead of effects |
| [`Card.GetPreviousAttackOnField`](/api/functions/Card/GetPreviousAttackOnField) | `imported_from_dataeditorx` | 7 | Returns the attack power before the c position changes |
| [`Card.GetRitualLevel`](/api/functions/Card/GetRitualLevel) | `imported_from_dataeditorx` | 7 | Returns the ritual liberation level for rc ritual monsters This function returns the same value as Card.GetLevel(c) except for certain cards such as ritual objects |
| [`Duel.SwapSequence`](/api/functions/Duel/SwapSequence) | `imported_from_dataeditorx` | 7 | Swap the positions of c1 and c2 |
| [`Auxiliary.AddFusionProcFunFun`](/api/functions/Auxiliary/AddFusionProcFunFun) | `imported_from_dataeditorx` | 6 | Add a Fusion Summon procedure for c Use 1 monster satisfying filter condition f1 and cc monsters satisfying filter condition f2 as Fusion Materials Equivalent to aux.A... |
| [`Auxiliary.nzdef`](/api/functions/Auxiliary/nzdef) | `imported_from_dataeditorx` | 6 | Simplified method for the filter function for face-up monsters with non-zero DEF function aux.nzdef(c) return c:IsFaceup() and c:GetDefense()&gt;0 end |
| [`bit.lshift`](/api/functions/bit/lshift) | `imported_from_dataeditorx` | 6 | A Move to the left b |
| [`Duel.GetLinkedGroup`](/api/functions/Duel/GetLinkedGroup) | `imported_from_dataeditorx` | 6 | Return the group of linked cards in s_range and o_range zones from player's perspective \[as long as the last two parameters are not 0, they become LOCATION_MZONE\] NOTE... |
| [`Auxiliary.SelectSameCount`](/api/functions/Auxiliary/SelectSameCount) | `imported_from_dataeditorx` | 5 | Select the same number of cards from each group. |
| [`Auxiliary.TuneMagicianCheckX`](/api/functions/Auxiliary/TuneMagicianCheckX) | `imported_from_dataeditorx` | 5 | Exclusive to Tuning Magician (73941492) |
| [`Card.CheckFusionSubstitute`](/api/functions/Card/CheckFusionSubstitute) | `imported_from_dataeditorx` | 5 | Check whether the c can replace the material description card name of the fusion monster fc |
| [`Card.GetPreviousLocation`](/api/functions/Card/GetPreviousLocation) | `imported_from_dataeditorx` | 5 | Returns the position before the c position changes |
| [`Duel.GetFlagEffectLabel`](/api/functions/Duel/GetFlagEffectLabel) | `imported_from_dataeditorx` | 5 | Return the Label of the flag effect of type code for player; return nil if no such effect exists |
| [`Duel.GetOverlayGroup`](/api/functions/Duel/GetOverlayGroup) | `imported_from_dataeditorx` | 5 | Returns all stacked cards at a specified location |
| [`Duel.IsPlayerCanRelease`](/api/functions/Duel/IsPlayerCanRelease) | `imported_from_dataeditorx` | 5 | Check whether the player can liberate the player c |
| [`Duel.SetFlagEffectLabel`](/api/functions/Duel/SetFlagEffectLabel) | `imported_from_dataeditorx` | 5 | Return whether player has a flag effect of type code and set its Label property to label |
| [`Duel.SetFusionMaterial`](/api/functions/Duel/SetFusionMaterial) | `imported_from_dataeditorx` | 5 | Set g to be the fusion material you want to use |
| [`Auxiliary.AddFusionProcFunRep2`](/api/functions/Auxiliary/AddFusionProcFunRep2) | `imported_from_dataeditorx` | 4 | Add a Fusion Summon procedure for c Use minc-maxc monsters satisfying the same condition f as Fusion Materials Equivalent to aux.AddFusionProcMixRep(c, false, insf, f,... |
| [`Auxiliary.DragonXyzSpSummonType`](/api/functions/Auxiliary/DragonXyzSpSummonType) | `imported_from_dataeditorx` | 4 | The `nolimit` parameter for Special Summon effects of Dragon, Xyz monsters where Soul Drain Dragon is available (Soul Drain Dragon, Level 8/LIGHT/Dragon/4000/0) |
| [`Auxiliary.GetColumn`](/api/functions/Auxiliary/GetColumn) | `imported_from_dataeditorx` | 4 | Return the column sequence number of card c from player's perspective, excluding the Field Zone; from left to right, columns are 0-4 |
| [`Auxiliary.GetValueType`](/api/functions/Auxiliary/GetValueType) | `imported_from_dataeditorx` | 4 | Return the Lua type of value |
| [`Auxiliary.IsSelfEquip`](/api/functions/Auxiliary/IsSelfEquip) | `imported_from_dataeditorx` | 4 | Check if c has a equip card equipped by the effect of itself. |
| [`Card.GetAttackableTarget`](/api/functions/Card/GetAttackableTarget) | `imported_from_dataeditorx` | 4 | Returns the attackable card set and whether it can attack directly |
| [`Card.GetAttackedCount`](/api/functions/Card/GetAttackedCount) | `imported_from_dataeditorx` | 4 | Returns the number of times this round has been attacked Note: If this value is different from the return value of the previous function, then this card has been a dir... |
| [`Card.GetLeaveFieldDest`](/api/functions/Card/GetLeaveFieldDest) | `imported_from_dataeditorx` | 4 | Returns the destination of an effect (such as the universe) that was changed as a result of departure from c |
| [`Card.GetPreviousLevelOnField`](/api/functions/Card/GetPreviousLevelOnField) | `imported_from_dataeditorx` | 4 | Returns the rank before the c position change |
| [`Card.IsXyzLevel`](/api/functions/Card/IsXyzLevel) | `imported_from_dataeditorx` | 4 | Check c for excess monster xyzc with the level of whether the excess is lv |
| [`Duel.DisableSelfDestroyCheck`](/api/functions/Duel/DisableSelfDestroyCheck) | `imported_from_dataeditorx` | 4 | Disable card self-destruction checks; no parameter or enabled=true disables the check, enabled=false enables the check |
| [`Effect.GetCondition`](/api/functions/Effect/GetCondition) | `imported_from_dataeditorx` | 4 | Returns the condition property |
| [`Auxiliary.AddRitualProcEqualCode`](/api/functions/Auxiliary/AddRitualProcEqualCode) | `imported_from_dataeditorx` | 3 | Add a Ritual Summon effect for c code is the card code of the Ritual Monster; the sum of the Ritual Levels of the materials must equal the original Level of the Ritual... |
| [`Auxiliary.ArcanaCondition`](/api/functions/Auxiliary/ArcanaCondition) | `imported_from_dataeditorx` | 3 | condition of Arcana Force monster effect from coin toss |
| [`Auxiliary.dogcon`](/api/functions/Auxiliary/dogcon) | `imported_from_dataeditorx` | 3 | Check if e:GetHandler() was destroyed by the opponent and sent to the Graveyard from your field, used for SetCondition function Auxiliary.dogcon(e, tp, eg, ep, ev, re,... |
| [`Auxiliary.DrytronSpSummonType`](/api/functions/Auxiliary/DrytronSpSummonType) | `imported_from_dataeditorx` | 3 | The `nolimit` parameter for Special Summon effects of Drytron cards |
| [`Auxiliary.indsval`](/api/functions/Auxiliary/indsval) | `imported_from_dataeditorx` | 3 | Simplified method for the filter function preventing destruction by your own card effects, used in effect registration for SetValue function aux.indsval(e, re, rp) ret... |
| [`Auxiliary.PhantasmsSpSummonType`](/api/functions/Auxiliary/PhantasmsSpSummonType) | `imported_from_dataeditorx` | 3 | The `nolimit` parameter for Special Summon effects of Phantasms cards |
| [`Auxiliary.TriamidSpSummonType`](/api/functions/Auxiliary/TriamidSpSummonType) | `imported_from_dataeditorx` | 3 | The `nolimit` parameter for Special Summon effects of Triamid cards |
| [`Card.CancelCardTarget`](/api/functions/Card/CancelCardTarget) | `imported_from_dataeditorx` | 3 | Cancel c2 as a perpetual object of c1 |
| [`Card.GetMutualLinkedGroup`](/api/functions/Card/GetMutualLinkedGroup) | `imported_from_dataeditorx` | 3 | Return the group of cards mutually linked with card c |
| [`Card.IsCanBeLinkMaterial`](/api/functions/Card/IsCanBeLinkMaterial) | `imported_from_dataeditorx` | 3 | Check if c can be used as Link Material \[for Link Monster sc\]; if sc is not specified, must pass nil |
| [`Card.IsLinkMarker`](/api/functions/Card/IsLinkMarker) | `imported_from_dataeditorx` | 3 | Check if card c has a Link Marker in direction dir dir values are: LINK_MARKER_BOTTOM_LEFT =0x001 -- ↙ LINK_MARKER_BOTTOM      =0x002 -- ↓ LINK_MARKER_BOTTOM_RIGHT=0x0... |
| [`Card.ReleaseEffectRelation`](/api/functions/Card/ReleaseEffectRelation) | `imported_from_dataeditorx` | 3 | Manually release the link between c and effect e |
| [`Card.ReverseInDeck`](/api/functions/Card/ReverseInDeck) | `imported_from_dataeditorx` | 3 | The setting c is indicated in the front of the deck |
| [`Duel.ChangeBattleDamage`](/api/functions/Duel/ChangeBattleDamage) | `imported_from_dataeditorx` | 3 | The player player in this battle by the harm into value, check for false is the original combat damage to 0 also change the damage |
| [`Duel.GetCoinResult`](/api/functions/Duel/GetCoinResult) | `imported_from_dataeditorx` | 3 | Returns the result of the current coin |
| [`Duel.GetDrawCount`](/api/functions/Duel/GetDrawCount) | `imported_from_dataeditorx` | 3 | Returns the player's number of rules drawn per turn |
| [`Effect.IsActivatable`](/api/functions/Effect/IsActivatable) | `imported_from_dataeditorx` | 3 | Check whether the effect can be launched by the player |
| [`Auxiliary.AddFusionProcCode4`](/api/functions/Auxiliary/AddFusionProcCode4) | `imported_from_dataeditorx` | 2 | For the c designated card number for the code1, code2, code3, code4 monster for the fusion material |
| [`Auxiliary.EnableReviveLimitPendulumSummonable`](/api/functions/Auxiliary/EnableReviveLimitPendulumSummonable) | `imported_from_dataeditorx` | 2 | If monster c is Pendulum Summoned from location, it can bypass revival restrictions NOTE: The original description includes a question mark (?), indicating potential u... |
| [`Auxiliary.FilterEqualFunction`](/api/functions/Auxiliary/FilterEqualFunction) | `imported_from_dataeditorx` | 2 | Filter cards satisfying a single filter condition f with value value, returning a function with a bool return type; additional parameters start from the third paramete... |
| [`Auxiliary.penlimit`](/api/functions/Auxiliary/penlimit) | `imported_from_dataeditorx` | 2 | Simplified method for the filter function preventing summoning (broadly) by methods other than Pendulum Summon, used in effect registration for SetValue se is the effe... |
| [`Auxiliary.TargetEqualFunction`](/api/functions/Auxiliary/TargetEqualFunction) | `imported_from_dataeditorx` | 2 | Used in effect registration, returns a function with a bool return type; additional parameters start from the third parameter function Auxiliary.TargetEqualFunction(f,... |
| [`Auxiliary.tgsval`](/api/functions/Auxiliary/tgsval) | `imported_from_dataeditorx` | 2 | Simplified method for the filter function preventing being targeted by your own card effects, used in effect registration for SetValue function aux.tgsval(e, re, rp) r... |
| [`Card.AssumeProperty`](/api/functions/Card/AssumeProperty) | `imported_from_dataeditorx` | 2 | Use the value of assume_type c as assume_value (genome fighter) Assume_type is the following type ASSUME_CODE card number The ASSUME_TYPE type ASSUME_LEVEL class ASSUM... |
| [`Card.GetAttributeInGrave`](/api/functions/Card/GetAttributeInGrave) | `imported_from_dataeditorx` | 2 | Return the Attribute card c is treated as having in the Graveyard |
| [`Card.GetPreviousDefenseOnField`](/api/functions/Card/GetPreviousDefenseOnField) | `imported_from_dataeditorx` | 2 | Returns the defensive power before the c position changes |
| [`Card.GetSummonLocation`](/api/functions/Card/GetSummonLocation) | `imported_from_dataeditorx` | 2 | Returns the call position of c |
| [`Card.ReplaceEffect`](/api/functions/Card/ReplaceEffect) | `imported_from_dataeditorx` | 2 | Replace the effect of c with the effect of the card whose card number is code, and add additional reset conditions The return value is the code id representing the rep... |
| [`Duel.GetDiceResult`](/api/functions/Duel/GetDiceResult) | `imported_from_dataeditorx` | 2 | Returns the result of the current dice |
| [`Duel.IsPlayerCanSSet`](/api/functions/Duel/IsPlayerCanSSet) | `imported_from_dataeditorx` | 2 | Check if player can Set \[scard\] |
| [`Duel.SetDiceResult`](/api/functions/Duel/SetDiceResult) | `imported_from_dataeditorx` | 2 | Forcibly modify the result of casting dice to res This function is used in the persistent EVENT_TOSS_DICE event |
| [`Auxiliary.AddFusionProcCode2FunRep`](/api/functions/Auxiliary/AddFusionProcCode2FunRep) | `imported_from_dataeditorx` | 1 | Add a Fusion Summon procedure for c Use 1 monster each with codes code1 and code2, and minc-maxc monsters satisfying filter condition f as Fusion Materials Equivalent... |
| [`Auxiliary.AddFusionProcMixRep`](/api/functions/Auxiliary/AddFusionProcMixRep) | `imported_from_dataeditorx` | 1 | Add a Fusion Summon procedure for c Use minc-maxc monsters satisfying f1 and 1 of each monster in the additional parameters as Fusion Materials Additional parameters c... |
| [`Auxiliary.AddRitualProcEqual`](/api/functions/Auxiliary/AddRitualProcEqual) | `imported_from_dataeditorx` | 1 | Add a ritual summon effect to c Filter for the ritual monster to meet the conditions, the material level must be equal to the ritual monster level |
| [`Auxiliary.AddRitualProcEqual2Code2`](/api/functions/Auxiliary/AddRitualProcEqual2Code2) | `imported_from_dataeditorx` | 1 | Add a Ritual Summon effect for c code1, code2 are the card codes of the Ritual Monsters; the sum of the Levels of the materials must equal the Ritual Monster's Level E... |
| [`Auxiliary.BecomeOriginalCode`](/api/functions/Auxiliary/BecomeOriginalCode) | `imported_from_dataeditorx` | 1 | The name of `c` becomes the original name of `tc` |
| [`Auxiliary.GetAdjacentGroup`](/api/functions/Auxiliary/GetAdjacentGroup) | `imported_from_dataeditorx` | 1 | Get the card group adjacent to (i,j) |
| [`Auxiliary.GetFieldIndex`](/api/functions/Auxiliary/GetFieldIndex) | `imported_from_dataeditorx` | 1 | Get the global row and column index of c |
| [`Auxiliary.xyzlimit`](/api/functions/Auxiliary/xyzlimit) | `imported_from_dataeditorx` | 1 | Simplified method for the filter function preventing summoning (broadly) by methods other than Xyz Summon, used in effect registration for SetValue se is the effect us... |
| [`Card.ClearEffectRelation`](/api/functions/Card/ClearEffectRelation) | `imported_from_dataeditorx` | 1 | Clear all the effects of c contact |
| [`Card.GetBattledGroup`](/api/functions/Card/GetBattledGroup) | `imported_from_dataeditorx` | 1 | Returns the deck of the card that fought this turn Fighting has occurred in the calculation of the damage occurred, for the sword and other animals, animal judgments |
| ...and 92 more |  |  |  |

## Raw Chinese In English Fields

No raw Chinese text was detected in English fields during this generation.

## DataEditorX Sync Rule

Sync generated `_functions` and `_function_english` files to DataEditorX only after the reviewed text has been regenerated here. Sacred Book is the source of truth for the next pass.
