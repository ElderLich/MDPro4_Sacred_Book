# RushDuel.ExecuteRitualSummon

Alias: `RD.ExecuteRitualSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ExecuteRitualSummon(Effect e, int tp, int type, table list, int chkf, Card|nil gc, function mat_move, [bool cancelable]) -> Card|nil,Group|nil
```

## Description

Executes a prepared Ritual route list: chooses a summon candidate, optionally chooses among compatible material-source routes, selects materials, moves them, then calls Duel.SpecialSummon and CompleteProcedure.
Returns the chosen Card and selected material Group. The pinned implementation ignores the numeric return from Duel.SpecialSummon; receiving a Card is not proof that the summon succeeded. Treat material Groups as borrowed unless explicitly retained for later use.
With cancelable=true, canceling monster selection returns nil. Canceling material selection goes back to monster selection; it does not immediately leave this helper. Pass a validated route list produced by the matching Get*SummonData helper.

## Parameters

- `e` `Effect`: Source effect.
- `tp` `int`: Selecting and summoning player.
- `type` `int`: RITUAL_* material comparison mode matching the prepared route list.
- `list` `table`: Prepared material-route entries from the matching Get*SummonData helper.
- `chkf` `int`: Check flags from the route builder.
- `gc` `Card|nil`: Required material, if any.
- `mat_move` `function`: Movement callback (player, materials, effect) for the ordinary route; alternative routes use their own operation.
- `cancelable` `bool` (optional): Allow cancellation at the monster-choice step; default false.

## Returns

- `Card|nil`: Chosen summon candidate, or nil on permitted monster-selection cancellation; not a success count.
- `Group|nil`: Selected materials when execution reaches the return statement.

## Source

`Rush/Utilities/RDRitual.lua:262`

```lua
function RushDuel.ExecuteRitualSummon(e, tp, type, list, chkf, gc, mat_move, cancelable)
    local sg = Group.CreateGroup()
    for _, data in ipairs(list) do
        sg:Merge(data[3])
    end
    ::cancel::
    local rc = nil
    Duel.Hint(HINT_SELECTMSG, tp, HINTMSG_SPSUMMON)
    if cancelable then
        rc = sg:SelectUnselect(nil, tp, false, true, 1, 1)
        if not rc then
            return nil
        end
    else
        rc = sg:Select(tp, 1, 1, nil):GetFirst()
    end
    local options = {}
    for _, data in ipairs(list) do
        local ce, sg = data[1], data[3]
        if sg:IsContains(rc) then
            if ce then
                table.insert(options, {true, ce:GetDescription(), data})
            else
                table.insert(options, {true, 1168, data})
            end
        end
    end
    local data = options[1][3]
    if #options > 1 then
        data = RushDuel.SelectOption(tp, table.unpack(options))
    end
    local ce, mg = data[1], data[2]
    if RushDuel.RitualExtraMaterialFilter then
        mg = mg:Filter(RushDuel.RitualExtraMaterialFilter, nil, e, tp, rc, mg)
    end
    RushDuel.CurrentRitualEffect = e
    local mat = RushDuel.SelectRitualMaterial(tp, rc, type, mg, gc)
    RushDuel.CurrentRitualEffect = nil
    if not mat then
        goto cancel
    end
    local cg = mat:Filter(RushDuel.ConfirmCardFilter, nil)
    if #cg > 0 then
        Duel.ConfirmCards(1 - tp, cg)
    end
    rc:SetMaterial(mat)
    if ce then
        local fop = ce:GetOperation()
        fop(ce, e, tp, rc, mat)
    else
        mat_move(tp, mat, e)
    end
    Duel.BreakEffect()
    Duel.SpecialSummon(rc, SUMMON_TYPE_RITUAL, tp, tp, false, false, POS_FACEUP)
    rc:CompleteProcedure()
    return rc, mat
end
```
