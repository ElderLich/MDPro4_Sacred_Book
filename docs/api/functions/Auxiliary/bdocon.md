# Auxiliary.bdocon

## Signature

```lua
Auxiliary.bdocon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Check if e:GetHandler() is related to the current battle, typically used for EVENT_BATTLE_DESTROYING and when battling an opponent's monster, as a condition
function Auxiliary.bdocon(e, tp, eg, ep, ev, re, r, rp)
  local c=e:GetHandler()
  return c:IsRelateToBattle() and c:IsStatus(STATUS_OPPO_BATTLE)
end

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `any`
- `re` `Effect`
- `r` `any`
- `rp` `int`

## Source

- `Utilities/utility.lua:769`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **70** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.bdocon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Nirvana High Paladin | `80896940` | [Scripts/c80896940.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80896940.lua) | 55 |
| Thunder Dragonduo | `55591586` | [Scripts/c55591586.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55591586.lua) | 55 |
| Junk Warrior Extreme | `16327715` | [Scripts/c16327715.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16327715.lua) | 52 |
| Supreme King Z-ARC | `13331639` | [Scripts/c13331639.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13331639.lua) | 50 |
| Destiny HERO - Dominance | `69394324` | [Scripts/c69394324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69394324.lua) | 50 |
| Despian Proskenion | `18666161` | [Scripts/c18666161.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18666161.lua) | 45 |
| Flower Cardian Zebra Grass with Moon | `43413875` | [Scripts/c43413875.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43413875.lua) | 45 |
| Black Luster Soldier - Envoy of the Beginning | `72989439` | [Scripts/c72989439.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72989439.lua) | 45 |
| Dark Templar @Ignister | `97383507` | [Scripts/c97383507.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97383507.lua) | 44 |
| Phantasm Spiral Assault | `97795930` | [Scripts/c97795930.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97795930.lua) | 43 |
| Gizmek Kaku, the Supreme Shining Sky Stag | `63633694` | [Scripts/c63633694.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63633694.lua) | 43 |
| Abyss Actor - Evil Heel | `52240819` | [Scripts/c52240819.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52240819.lua) | 42 |
| Deskbot 004 | `22227683` | [Scripts/c22227683.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22227683.lua) | 42 |
| Malefic Truth Dragon | `37115575` | [Scripts/c37115575.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37115575.lua) | 42 |
| Dangerous Frightfur Nightmary | `58468105` | [Scripts/c58468105.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58468105.lua) | 42 |
| Noh-P.U.N.K. Foxy Tune | `55920742` | [Scripts/c55920742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55920742.lua) | 42 |
| Black Luster Soldier - Soldier of Chaos | `49202162` | [Scripts/c49202162.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49202162.lua) | 42 |
| Fossil Machine Skull Buggy | `10040267` | [Scripts/c10040267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10040267.lua) | 40 |
| Fossil Machine Skull Wagon | `83656563` | [Scripts/c83656563.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83656563.lua) | 39 |
| Delta Tri | `12079734` | [Scripts/c12079734.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12079734.lua) | 39 |
| Full Armored Utopic Ray Lancer | `1269512` | [Scripts/c1269512.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1269512.lua) | 38 |
| Gaia the Magical Knight of Dragons | `15989522` | [Scripts/c15989522.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15989522.lua) | 38 |
| Fire Fighting Daruma Doll | `64514892` | [Scripts/c64514892.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64514892.lua) | 38 |
| Black Luster Soldier - Soldier of Light and Darkness | `70405001` | [Scripts/c70405001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70405001.lua) | 37 |
| ...and 46 more |  |  |  |

## Script Examples

### Nirvana High Paladin (`80896940`)

Source: [Scripts/c80896940.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80896940.lua)

```lua
	e6:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e6:SetCode(EVENT_BATTLE_DESTROYING)
	e6:SetCondition(aux.bdocon)
	e6:SetOperation(c80896940.lpop)
	c:RegisterEffect(e6)
```

### Thunder Dragonduo (`55591586`)

Source: [Scripts/c55591586.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55591586.lua)

```lua
	e3:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e3:SetCode(EVENT_BATTLE_DESTROYING)
	e3:SetCondition(aux.bdocon)
	e3:SetCost(c55591586.cost)
	e3:SetTarget(c55591586.target)
```

### Junk Warrior Extreme (`16327715`)

Source: [Scripts/c16327715.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16327715.lua)

```lua
	e2:SetCode(EVENT_BATTLE_DESTROYING)
	e2:SetCountLimit(1,id+o)
	e2:SetCondition(aux.bdocon)
	e2:SetCost(aux.bfgcost)
	e2:SetTarget(s.sptg2)
```
