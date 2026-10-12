# Auxiliary.bdcon

## Signature

```lua
Auxiliary.bdcon(Effect e, int tp, Group eg, int ep, int ev, Effect re, int r, int rp) -> bool
```

## Description

Battle-destroying condition helper that returns true while the handler is still related to battle.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `int`
- `re` `Effect`
- `r` `int`
- `rp` `int`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:767`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **18** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.bdcon) with `Auxiliary.bdcon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Altergeist Memorygant | `23790299` | [Scripts/c23790299.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23790299.lua) | 1 |
| Commander Souza, Swordmaster | `72867001` | [Scripts/c72867001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72867001.lua) | 1 |
| Blade Garoodia the Cubic Beast | `78509901` | [Scripts/c78509901.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78509901.lua) | 1 |
| Dark Garnex the Cubic Beast | `41114306` | [Scripts/c41114306.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41114306.lua) | 1 |
| Crimson Nova the Dark Cubic Lord | `30270176` | [Scripts/c30270176.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30270176.lua) | 1 |
| Favorite HERO Shining Flare Wingman | `87758525` | [Scripts/c87758525.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87758525.lua) | 1 |
| Hot Red Dragon Archfiend King Calamity | `62242678` | [Scripts/c62242678.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62242678.lua) | 1 |
| D/D/D Wise King Solomon | `32232538` | [Scripts/c32232538.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c32232538.lua) | 1 |
| Elemental HERO Shining Neos Wingman | `56733747` | [Scripts/c56733747.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56733747.lua) | 1 |
| Geomathmech Magma | `15248594` | [Scripts/c15248594.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15248594.lua) | 1 |
| Ancient Gear Golem - Ultimate Pound | `95735217` | [Scripts/c95735217.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95735217.lua) | 1 |
| Guivre | `18905769` | [Scripts/c18905769.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18905769.lua) | 1 |
| CXyz Skypalace Babylon | `49202331` | [Scripts/c49202331.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49202331.lua) | 1 |
| Beast-Eyes Pendulum Dragon | `72378329` | [Scripts/c72378329.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72378329.lua) | 1 |
| Crimson Nova Trinity the Dark Cubic Lord | `72664875` | [Scripts/c72664875.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72664875.lua) | 1 |
| Horus the Black Flame Dragon LV6 | `11224103` | [Scripts/c11224103.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11224103.lua) | 1 |
| Brain Golem | `17313545` | [Scripts/c17313545.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17313545.lua) | 1 |
| Alien Hunter | `62315111` | [Scripts/c62315111.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62315111.lua) | 1 |

## Script Examples

### Altergeist Memorygant (`23790299`)

Source: [Scripts/c23790299.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23790299.lua)

```lua
	e2:SetCode(EVENT_BATTLE_DESTROYING)
	e2:SetCountLimit(1,23790300)
	e2:SetCondition(aux.bdcon)
	e2:SetTarget(c23790299.destg)
	e2:SetOperation(c23790299.desop)
```

### Commander Souza, Swordmaster (`72867001`)

Source: [Scripts/c72867001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72867001.lua)

```lua
	e2:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
	e2:SetCode(EVENT_BATTLE_DESTROYING)
	e2:SetCondition(aux.bdcon)
	e2:SetTarget(s.drtg)
	e2:SetOperation(s.drop)
```

### Blade Garoodia the Cubic Beast (`78509901`)

Source: [Scripts/c78509901.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78509901.lua)

```lua
	e4:SetCode(EVENT_BATTLE_DESTROYING)
	e4:SetProperty(EFFECT_FLAG_CARD_TARGET)
	e4:SetCondition(aux.bdcon)
	e4:SetTarget(c78509901.sptg2)
	e4:SetOperation(c78509901.spop2)
```
