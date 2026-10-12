# RushDuel.IsCanAttachPierce

Alias: `RD.IsCanAttachPierce`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachPierce(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 贯通
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:243`

```lua
function RushDuel.IsCanAttachPierce(card)
    return RushDuel.IsCanAttack(card) and not RushDuel.IsHasAttachEffect(card, EFFECT_PIERCE)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **22** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanAttachPierce) with `RushDuel.IsCanAttachPierce`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Transam Scride | `120109036` | [Rush/Scripts/c120109036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109036.lua) | 1 |
| Super Princess of the Flock - Max Mutton \[L\] | `120293007` | [Rush/Scripts/c120293007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293007.lua) | 1 |
| Divinebreath the Orchestral Music Fiend | `120247018` | [Rush/Scripts/c120247018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247018.lua) | 1 |
| Transam Lika | `120109024` | [Rush/Scripts/c120109024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109024.lua) | 1 |
| Dark Matter Freya | `120261027` | [Rush/Scripts/c120261027.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261027.lua) | 1 |
| Roadstar Gladimagia | `120272042` | [Rush/Scripts/c120272042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272042.lua) | 1 |
| Alchemicalize Orb | `120272037` | [Rush/Scripts/c120272037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272037.lua) | 1 |
| Ultimate Flag Beast Cannon Rhino | `120109008` | [Rush/Scripts/c120109008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109008.lua) | 1 |
| Tribemirror Dragon | `120261051` | [Rush/Scripts/c120261051.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261051.lua) | 1 |
| Swift Gaia the Dragon Champion | `120257047` | [Rush/Scripts/c120257047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257047.lua) | 1 |
| Clawmeleon | `120205018` | [Rush/Scripts/c120205018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120205018.lua) | 1 |
| Kheiron the Star Knight | `120170038` | [Rush/Scripts/c120170038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170038.lua) | 1 |
| Meteor Charge | `120208043` | [Rush/Scripts/c120208043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120208043.lua) | 1 |
| Powerful Pierce!! | `120140012` | [Rush/Scripts/c120140012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120140012.lua) | 1 |
| Art Angel Diamond Needle | `120228013` | [Rush/Scripts/c120228013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228013.lua) | 1 |
| Dark-Eyes Breakstar Cat | `120235017` | [Rush/Scripts/c120235017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235017.lua) | 1 |
| Prime Tractiger | `120257005` | [Rush/Scripts/c120257005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257005.lua) | 1 |
| Piercing Samurai | `120199016` | [Rush/Scripts/c120199016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199016.lua) | 1 |
| Thunder Gazelle | `120222040` | [Rush/Scripts/c120222040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120222040.lua) | 1 |
| Vietor the Prevailing Wind | `120183036` | [Rush/Scripts/c120183036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120183036.lua) | 1 |
| Innocent Lancer | `120130035` | [Rush/Scripts/c120130035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120130035.lua) | 1 |
| Pierce! | `120120037` | [Rush/Scripts/c120120037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120120037.lua) | 1 |

## Script Examples

### Transam Scride (`120109036`)

Source: [Rush/Scripts/c120109036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109036.lua)

```lua
end
function cm.filter(c)
	return c:IsFaceup() and RD.IsCanAttachPierce(c)
end
function cm.posfilter(c,e,tp)
```

### Super Princess of the Flock - Max Mutton [L] (`120293007`)

Source: [Rush/Scripts/c120293007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293007.lua)

```lua
cm.indval=RD.ValueEffectIndesType(TYPE_MONSTER+TYPE_SPELL+TYPE_TRAP,TYPE_MONSTER+TYPE_SPELL+TYPE_TRAP)
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsAbleToEnterBP() and RD.IsCanAttachPierce(e:GetHandler())
end
cm.cost=RD.CostSendHandToGrave(Card.IsAbleToGraveAsCost,2,2)
```

### Divinebreath the Orchestral Music Fiend (`120247018`)

Source: [Rush/Scripts/c120247018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247018.lua)

```lua
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return RD.IsCanAttachEffectIndes(c,tp,cm.indval) or RD.IsCanAttachPierce(c)
end
cm.cost=RD.CostSendHandToGrave(Card.IsAbleToGraveAsCost,1,3,function(g)
```
