# Card Data And Script Wiring

A card script is only half of a custom card. The database entry gives the card
its ID, name, text, type, stats, set codes, and script prompt strings. The Lua
file gives that card behavior. If those two halves drift apart, the script can
be correct and the card will still feel broken in the client.

Use this page after [Write Your First Custom Card](first-custom-card). It is a
small checklist for making one card exist cleanly in `cards.cdb` and matching it
to `Scripts/c<ID>.lua`.

For Rush cards, also check [Rush database and runtime wiring](../guides/card-database#rush-card-data-and-runtime-rules).
The card's pool label, special type bits, and the duel's Rush mode have separate
roles.

## The Two Local Tables

Local `cards.cdb` stores ordinary card data in two SQLite tables:

| Table | Fields Sacred Book cares about first |
| --- | --- |
| `datas` | `id`, `ot`, `alias`, `setcode`, `type`, `atk`, `def`, `level`, `race`, `attribute`, `category` |
| `texts` | `id`, `name`, `desc`, `str1` through `str16` |

DataEditorX uses the same model. Its local `Card` class has 16 script string
slots, four packed set-code slots, and fields for alias, type, stats, race,
attribute, and category. For normal `.cdb` files, `setcode` is saved as an
integer. For Link Monsters, DataEditorX stores Link markers in the database
`def` field instead of ordinary DEF.

## ID, File Name, And `GetID`

The database ID and script file name must match:

| Piece | Example |
| --- | --- |
| Database `datas.id` and `texts.id` | `12345678` |
| Script file | `Scripts/c12345678.lua` |
| Script header | `local s,id=GetID()` |
| Prompt strings | `aux.Stringid(id,0)`, `aux.Stringid(id,1)`, ... |

`GetID()` lets the same numeric ID feed your effect table and prompt lookups.
If the file name and database ID do not match, the card can load without running
the script you thought you wrote.

## Main Text Versus Script Strings

The large card text field belongs in `texts.desc`. The small script prompt
strings belong in `texts.str1` through `texts.str16`.

Local `Auxiliary.Stringid` is simple:

```lua
function Auxiliary.Stringid(code,id)
    return code*16+id
end
```

That means `aux.Stringid(id,0)` reads the first script string for this card,
`aux.Stringid(id,1)` reads the second, and so on. Local scripts use those values
for descriptions, yes/no prompts, option prompts, and client hints:

```lua
e1:SetDescription(aux.Stringid(id,0))
Duel.SelectYesNo(tp,aux.Stringid(id,1))
Duel.Hint(HINT_SELECTMSG,tp,aux.Stringid(id,2))
```

Keep `desc` for the card's effect text. Keep `str1` to `str16` short and
action-oriented, such as "Draw 1 card" or "Set this card".

## Type And Stats Must Match The Script Shape

The card type in `datas.type` is not decoration. It decides whether the card is
a Monster, Spell, or Trap, and which subtype bits apply.

| Script shape | Data shape |
| --- | --- |
| Normal Spell activation with `EFFECT_TYPE_ACTIVATE` and `EVENT_FREE_CHAIN` | `TYPE_SPELL` |
| Quick-Play Spell | `TYPE_SPELL + TYPE_QUICKPLAY` |
| Continuous Spell with face-up effects | `TYPE_SPELL + TYPE_CONTINUOUS` |
| Normal Trap | `TYPE_TRAP` |
| Continuous Trap with field effects | `TYPE_TRAP + TYPE_CONTINUOUS` |
| Counter Trap | `TYPE_TRAP + TYPE_COUNTER` |
| Effect Monster | `TYPE_MONSTER + TYPE_EFFECT` |
| Link Monster | `TYPE_MONSTER + TYPE_LINK + TYPE_EFFECT`, with Link markers in `def` |

If a script reads `e:GetHandler():IsType(TYPE_QUICKPLAY)` or searches for
`TYPE_TRAP`, the database type bits decide the answer. If a guide tells you to
make a Quick-Play version of a script, that change happens in card data as well
as in any timing code.

## Categories Are Search And UI Metadata

`datas.category` is not the same as `Effect.SetCategory`. The database category
flags are broad card-info labels used by editor/search tooling. The script's
`SetCategory` and `Duel.SetOperationInfo` describe a specific effect and Chain
Link.

For a first card, make them agree in spirit:

| Card behavior | Useful database category labels | Script categories |
| --- | --- | --- |
| Draw cards. | Draw | `CATEGORY_DRAW` |
| Destroy a target. | Destroy | `CATEGORY_DESTROY` |
| Change battle position. | Position | `CATEGORY_POSITION` |
| Special Summon. | Special Summon | `CATEGORY_SPECIAL_SUMMON` |
| Banish cards. | Banish | `CATEGORY_REMOVE` |

Do not use database category flags to prove activation legality. The script
still needs `chk==0`, target filters, and operation info.

## Set Codes And Archetype Filters

DataEditorX exposes four set-code boxes. Locally, those are packed as four
16-bit set codes in the `datas.setcode` integer. Its card model writes each
entered hex value into the next 16-bit slot.

Scripts should still call `Card.IsSetCard`, not unpack `datas.setcode` by hand:

```lua
function s.filter(c)
    return c:IsFaceup() and c:IsSetCard(0x1ce)
end
```

The local core checks the card's current code, second code, database set code,
and added set-code effects. That is why `IsSetCard` is safer than comparing a
raw integer field.

Use [Archetypes and Set Codes](archetypes-and-setcodes) when the card belongs
to a family or subfamily. For a standalone first custom card, leave set codes at
`0`.

## Alias Is Name Identity, Not A Shortcut

The `alias` field is for cards that are treated as another card name or variant.
Most custom cards should leave it as `0`.

Alias and original-code behavior affect identity checks:

| Need | Use |
| --- | --- |
| Current treated-as code or exact named card checks | [`Card.IsCode`](/api/functions/Card/IsCode) |
| Printed/original identity rules | [`Card.IsOriginalCodeRule`](/api/functions/Card/IsOriginalCodeRule) |
| Reading original identity values | [`Card.GetOriginalCodeRule`](/api/functions/Card/GetOriginalCodeRule) |

Do not fill alias just to connect a card to an archetype. Use set codes for
families and listed-card helpers for text such as "lists this card".

## First Custom Card Data Checklist

For the Normal Spell in [Write Your First Custom Card](first-custom-card), the
database side should look like this:

| Field | Value shape |
| --- | --- |
| `id` | The same number used in `Scripts/c<ID>.lua`. |
| `alias` | `0` unless the card really is treated as another card name. |
| `type` | Spell, with no Quick-Play/Continuous/Equip/Field subtype. |
| `atk`, `def`, `level`, `race`, `attribute` | `0` or blank-style defaults for a Spell. |
| `category` | Position and Draw-style labels. |
| `desc` | The full card text. |
| `str1` | A short prompt such as "Change a monster to face-down Defense Position". |
| `setcode` | `0` unless the card belongs to a real local family. |

Then check the Lua side:

1. The file name is `c<ID>.lua`.
2. The file starts with `local s,id=GetID()`.
3. Any `aux.Stringid(id,n)` calls have matching string slots.
4. Data type matches the script pattern.
5. Database category labels match the effect's visible action.
6. Set code and alias are deliberate, not guessed.

Useful API pages:

- [`Auxiliary.Stringid`](/api/functions/Auxiliary/Stringid)
- [`Effect.SetDescription`](/api/functions/Effect/SetDescription)
- [`Card.IsCode`](/api/functions/Card/IsCode)
- [`Card.IsSetCard`](/api/functions/Card/IsSetCard)
- [`Card.IsOriginalCodeRule`](/api/functions/Card/IsOriginalCodeRule)
- [`Card.GetOriginalCodeRule`](/api/functions/Card/GetOriginalCodeRule)
