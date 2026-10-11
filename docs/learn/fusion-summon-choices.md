# Fusion Summon Choices

**Before this lesson:** read [Fusion Procedures](fusion-procedure) to distinguish
a Fusion Monster's material requirement from the effect that summons it.
**Goal:** explain each prompt, keep alternative material routes separate, and
rebuild the legal choices when the effect resolves.

This lesson uses the pinned `Utilities/procedure.lua` and ordinary `Scripts/`
cards. Rush has a [separate summon library](rush-summon-procedures).

## The Player Makes More Than One Choice

| Stage | Question the script answers | Does the player choose yet? |
| --- | --- | --- |
| Activation check | Is at least one Fusion Monster summonable with a legal set of materials? | No. `chk==0` only checks. |
| Resolution search | Which Fusion Monsters are summonable with the materials available now? | No. Build the current candidates first. |
| Monster selection | Which of those Fusion Monsters will be summoned? | Yes. Choose one monster. |
| Route selection | If both normal materials and Chain Material work for that monster, which route will be used? | Yes, when both routes exist. |
| Material selection | Which legal material set will summon that exact monster through that route? | Yes. Use its Fusion procedure. |
| Execution | Record the materials, move them through the chosen route, and summon. | Follow the committed choices. |

Choosing a Fusion Monster at resolution does not make it a card targeted at
activation. [Polymerization (`24094653`)](/examples/cards/24094653) has a target
callback, but that callback only checks feasibility and announces the summon.
It does not call `Duel.SelectTarget`.

## Begin With A Complete Helper-Based Spell

This is a complete tutorial script for a plain Fusion Spell using the local
helper's normal material locations. Give it its own matching database ID and
Normal Spell entry; the Fusion Monsters in the Extra Deck need their own
material procedures.

```lua
local s,id=GetID()

function s.initial_effect(c)
    aux.AddFusionEffectProcUltimate(c,{})
end
```

[`aux.AddFusionEffectProcUltimate`](/api/functions/Auxiliary/AddFusionEffectProcUltimate)
creates and registers an activation effect. Its target callback
checks whether a summon exists. Its operation gathers materials again, builds
the available Fusion Monster list, and handles the prompts above. The empty
table uses the helper defaults; it does not mean that every Extra Deck monster
or every group of monsters is legal.

Try it with two Fusion Monsters having different material requirements. Make
one requirement impossible, then make both possible. The monster prompt should
offer only the currently feasible choices. This is a useful first test before
adding a custom material filter.

## Read The Two Selection Calls

Here is the normal-route selection core from the Polymerization pattern,
shown as a **resolution fragment**. `e`, `tp`, and `chkf=tp` belong to the
operation; `mg1` is the freshly filtered material pool; `sg1` is the Group of
Fusion Monsters already proven summonable through that pool.

```lua
Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
local selected=sg1:Select(tp,1,1,nil)
local tc=selected:GetFirst()
if not tc then return end

local materials=Duel.SelectFusionMaterial(tp,tc,mg1,nil,chkf)
tc:SetMaterial(materials)
```

[`Group.Select`](/api/functions/Group/Select) chooses the destination monster. `Duel.SelectFusionMaterial`
then invokes **that monster's registered material procedure**. Selecting two
arbitrary cards with `Group.Select(tp,2,2,nil)` would check only a quantity,
not named material slots, substitute rules, or additional group restrictions.

The fourth argument to `SelectFusionMaterial` is a required material Card, or
`nil`. [Surprise Fusion (`35167375`)](/examples/cards/35167375) passes its
changed monster there so that it must be used. The same required card must
appear in the corresponding `CheckFusionMaterial` check.

::: warning This is not a cancellation flag
In this core, the optional sixth argument of
[`Duel.SelectFusionMaterial`](/api/functions/Duel/SelectFusionMaterial) is
`not_material`. It is not a generic “allow Cancel” argument. The normal
Polymerization monster choice uses `Select(tp,1,1,nil)`; do not add an exit
option simply because another selection API accepts a Boolean.
:::

## Chain Material Is An Alternative Route

Polymerization and `FusionEffectUltimateOperation` keep these Groups separate:

| Group | Meaning |
| --- | --- |
| `mg1` | Materials for the normal route. |
| `sg1` | Fusion Monsters legal through `mg1`. |
| `mg2` | Materials supplied by the Chain Material effect. |
| `sg2` | Fusion Monsters legal through `mg2` and that effect's filter. |

They merge **`sg1` and `sg2`**, so a monster appears in the choice list when
either route can summon it. They do not merge `mg1` and `mg2` into a material
pool that can mix the two permissions.

After the player picks `tc`, the route follows this table:

| `tc` is legal through | What happens |
| --- | --- |
| Normal route only | Select from `mg1` and use the normal material movement. |
| Chain Material only | Select from `mg2` and call the Chain Material operation. |
| Both | Ask `Duel.SelectYesNo(tp,ce:GetDescription())` whether to use Chain Material. |

Here `ce` is the Effect returned by [`Duel.GetChainMaterial(tp)`](/api/functions/Duel/GetChainMaterial). Its operation
owns its material handling and summon behavior. Moving `mg2` materials yourself
and then calling that operation can perform the action twice or bypass its
restrictions.

## Optional Summoning Has Its Own Decision Point

Surprise Fusion first changes a targeted monster's Race/Attribute, then offers
its optional Fusion Summon if a legal route exists. The bounded choice pattern
is:

```lua
-- After the earlier action and a fresh legal-Fusion check:
if canFusion and Duel.SelectYesNo(tp,aux.Stringid(id,2)) then
    -- Rebuild the available Fusion Monsters, then choose monster and materials.
end
```

`canFusion` represents the result of that check, not just “there is a Fusion
Monster in the Extra Deck.” The full source also verifies that the earlier
change happened and that the required monster is still usable. The player
declines the **optional summon** at this point; that differs from backing out
of a material selection to revise an earlier choice.

Do not copy the yes/no prompt into mandatory Polymerization behavior. A prompt
should implement an actual choice in the card text.

## Additional Locations Also Need Movement Rules

For a tutorial variant whose text explicitly allows GY materials, the helper
configuration can be:

```lua
local s,id=GetID()

function s.initial_effect(c)
    aux.AddFusionEffectProcUltimate(c,{
        mat_location=LOCATION_HAND+LOCATION_MZONE+LOCATION_GRAVE
    })
end
```

In this snapshot, the helper defaults GY material to an `IsAbleToRemove` filter
and banishment through `aux.FMaterialRemove`. The ordinary material operation
is sending to the GY. Therefore, adding `LOCATION_GRAVE` does **not** mean
“send the GY cards to the GY again.” Confirm those defaults against your text
before using this variant.

For different movement, change both the relevant filter and operation.
[Mementotlan Fusion (`66518509`)](/examples/cards/66518509) is a real manual
example: conditional GY access, `IsAbleToDeck` on those materials, then
separate movement for selected GY cards and ordinary materials. Its destruction
flag also gates GY access, and the material set must contain a Memento monster.
Do not copy just the Group merge and omit those restrictions.

## Recheck Before Committing The Choice

At resolution, reconstruct the material pool and destination candidates.
An opponent's earlier Chain Link can remove a material, change control, alter
immunity, or change summon restrictions. A Group remembered at activation is
not a fresh legality check.

For custom group restrictions, the main guide's `aux.FCheckAdditional` pattern
must cover both feasibility checks and the final material selection. Clear the
temporary hook afterward, including before returning from a new failure branch.

Keep `Duel.BreakEffect()` only where the source-backed timing sequence needs it.
It separates effect timing; it is not an animation delay or an opportunity to
rewrite choices already committed by the resolving effect.

## Practice And Review

| Test state | What to inspect |
| --- | --- |
| Two legal Fusion Monsters | Both offered; picking one changes which material sets are legal. |
| One apparently suitable monster with no legal material set | It is excluded from the monster prompt. |
| A required material leaves before resolution | The required-material route fails instead of substituting an unrelated card. |
| Only Chain Material works | Its materials and operation are used without requiring a normal route. |
| Both routes work | The route choice appears; materials never mix across the two routes. |
| GY access is conditional | Removing that condition removes GY materials from both checking and selection. |
| Optional summon declined | The optional branch is skipped; earlier actions remain resolved. |

Continue with [Ritual Summon Choices](ritual-summon-choices) to see a different
kind of cancellation: returning from material selection to monster selection.

## Source Trail

- `Utilities/procedure.lua`: `AddFusionEffectProcUltimate`,
  `FusionEffectUltimateTarget`, `FusionEffectUltimateOperation`.
- `Scripts/c24094653.lua`: normal route versus Chain Material.
- `Scripts/c35167375.lua`: optional summon and required material.
- `Scripts/c66518509.lua`: conditional GY materials and different movement.
- Companion `ygopro-core/libduel.cpp`: `duel_select_fusion_material` argument handling.
