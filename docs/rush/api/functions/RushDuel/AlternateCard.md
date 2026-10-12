# RushDuel.AlternateCard

Alias: `RD.AlternateCard`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AlternateCard(int code) -> void
```

## Description

Loads c&lt;code&gt;.lua for an alternate-art card that shares its implementation.

## Parameters

- `code` `int`: Source card passcode.

## Returns

No return values.

## Source

`Rush/Utilities/RDBase.lua:68`

```lua
function RushDuel.AlternateCard(code)
    Duel.LoadScript("c" .. code .. ".lua")
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **252** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AlternateCard) with `RushDuel.AlternateCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Prophecy Phrase the Colors of the Wind | `120218004` | [Rush/Scripts/c120218004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120218004.lua) | 1 |
| Divinebreath the Orchestral Music Fiend | `120287057` | [Rush/Scripts/c120287057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287057.lua) | 1 |
| Transam Assault Linac | `120218012` | [Rush/Scripts/c120218012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120218012.lua) | 1 |
| Celeb Rose Influencers | `120287041` | [Rush/Scripts/c120287041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287041.lua) | 1 |
| Sevens Road Mage | `120197003` | [Rush/Scripts/c120197003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120197003.lua) | 1 |
| Axtion Melody the Music Princess | `120287059` | [Rush/Scripts/c120287059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287059.lua) | 1 |
| Eternal Galactica Oblivion | `120218014` | [Rush/Scripts/c120218014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120218014.lua) | 1 |
| Invitation to a Delirious Dream | `120288005` | [Rush/Scripts/c120288005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120288005.lua) | 1 |
| Hungreed Burger | `120302304` | [Rush/Scripts/c120302304.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120302304.lua) | 1 |
| Celeb Rose Incognito Magician | `120287039` | [Rush/Scripts/c120287039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287039.lua) | 1 |
| Sunset Rebirth | `120283011` | [Rush/Scripts/c120283011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120283011.lua) | 1 |
| Prime Claw Girl | `120282003` | [Rush/Scripts/c120282003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120282003.lua) | 1 |
| Sevens Road Charmy Witch | `120289003` | [Rush/Scripts/c120289003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120289003.lua) | 1 |
| Battletested Curse of Dragon | `120287094` | [Rush/Scripts/c120287094.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287094.lua) | 1 |
| Wish of the Skysavior | `120301008` | [Rush/Scripts/c120301008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301008.lua) | 1 |
| Tubardiche the Music Princess | `120287065` | [Rush/Scripts/c120287065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287065.lua) | 1 |
| Battletested Gaia The Fierce Knight | `120287093` | [Rush/Scripts/c120287093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287093.lua) | 1 |
| Galactica Oblivion Ark | `120218013` | [Rush/Scripts/c120218013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120218013.lua) | 1 |
| Celeb Rose Warlock | `120287046` | [Rush/Scripts/c120287046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287046.lua) | 1 |
| Etraynze the Shadow Flower Restricter | `120288002` | [Rush/Scripts/c120288002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120288002.lua) | 1 |
| Legendary Priest | `120293003` | [Rush/Scripts/c120293003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293003.lua) | 1 |
| Etraynze the Shadow Flower Ninja | `120286011` | [Rush/Scripts/c120286011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120286011.lua) | 1 |
| Elemental HERO Shining Flare Wingman | `120281001` | [Rush/Scripts/c120281001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120281001.lua) | 1 |
| CAN:D LIVE | `120218001` | [Rush/Scripts/c120218001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120218001.lua) | 1 |
| ...and 228 more |  |  |  |

## Script Examples

### Prophecy Phrase the Colors of the Wind (`120218004`)

Source: [Rush/Scripts/c120218004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120218004.lua)

```lua
RD.AlternateCard(120228024)
```

### Divinebreath the Orchestral Music Fiend (`120287057`)

Source: [Rush/Scripts/c120287057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287057.lua)

```lua
RD.AlternateCard(120247018)
```

### Transam Assault Linac (`120218012`)

Source: [Rush/Scripts/c120218012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120218012.lua)

```lua
RD.AlternateCard(120272035)
```
