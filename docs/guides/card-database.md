# Card Database

The `.cdb` file gives a script its visible card data:

- Name and card text.
- Type, Attribute, Race, Level/Rank/Link data.
- ATK and DEF.
- Category flags used by editors and search tools.

The script file gives the card behavior. A useful learning workflow is to keep
the database text beside the script so you can ask: which line implements this
sentence?

The generated [examples](../examples/) do this automatically for a starter set
of cards.

For a first card, follow [Card Data and Script Wiring](../learn/card-data-and-script-wiring)
for the ID, type bits, four packed set codes, and the sixteen prompt strings.

## Standard And Rush Data

Sacred Book imports `cards.cdb` and `rush_cards.cdb` from the game's English
locale. Standard and Rush examples keep their data and scripts separate, so a
card's text is paired with the appropriate implementation. Use
[Rush examples](../examples/rush) or the format selector in
[Script Explorer](../tools/script-explorer) when researching a Rush effect.

## Rush Card Data And Runtime Rules

| Field or setting | Role in the local MDPro4 implementation |
| --- | --- |
| Card ID | `Card.IsRushDuelCard()` recognizes `120000000 <= id < 130000000`. Preserve real imported IDs. |
| `datas.ot` / editor rule or pool | Availability metadata. The imported English Rush database currently uses `4`; do not rewrite it wholesale to `0x100`. |
| Client `CardPool.RushDuel = 0x100` | A client search/filter flag. It is a separate concept from the observed database `ot` value. |
| `datas.type` with `0x8` | Legend marker (`TYPE_LEGEND`). It can accompany Monster, Spell, or Trap types. |
| `datas.type` with `0x8000` | Maximum marker (`TYPE_MAXIMUM`). The Lua procedure still supplies Maximum behavior. |
| Local duel's Rush mode | Selects the Rush runtime and its bootstrap. This is not enabled by a card's type or pool alone. |

The game loads Rush data from `Data/locales/<locale>/rush_cards.cdb` and the
Rush script package from `Data/rush_scripts.zip`. Its host prepares a dedicated
native catalog and a session bootstrap. When testing changed packaged data,
follow the host's restart message if its native archive is still held open.

Rush races include Magical Knight, Hydragon, Omega Psychic, Celestial Warrior,
Galaxy, and Cyborg. Cyborg uses `0x80000000`, so preserving the full 32-bit mask
matters when an editor reads or writes the integer. Labels may be translated;
the numerical bits must agree with the game's data and Rush constants.

The Rush Ritual library also uses a Fusion database bit for Extra Deck
placement, then removes the effective Fusion type through
`RD.AddRitualProcedure(c)`. Read [Rush summon procedures](../learn/rush-summon-procedures)
before editing those type combinations.

## Verify A Database Edit In The Game

1. Save, close, and reopen the card in the editor; check its ID, type, race,
   strings, and set codes survived the round trip.
2. Confirm the game loads the edited database and the matching `c<ID>.lua`.
3. Check the card's name, description, frame, stats, and effect prompts.
4. Test its behavior in the intended duel format, including an illegal
   activation state. A correct editor preview verifies only the data view.

For Rush, continue with the [Rush learning path](../learn/rush-duel).
