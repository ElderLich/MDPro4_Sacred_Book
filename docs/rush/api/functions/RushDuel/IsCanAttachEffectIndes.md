# RushDuel.IsCanAttachEffectIndes

Alias: `RD.IsCanAttachEffectIndes`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachEffectIndes(any card, any player, any value) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 效果破坏抗性
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:316`

```lua
function RushDuel.IsCanAttachEffectIndes(card, player, value)
    local effects = RushDuel.GetAttachEffects(card, EFFECT_INDESTRUCTABLE_EFFECT)
    return RushDuel.CheckValueEffectIndesType(player, effects, value)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **30** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanAttachEffectIndes) with `RushDuel.IsCanAttachEffectIndes`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lufer the Symbol of the Devils](/examples/rush-cards/120309059) | `120309059` | [Rush/Scripts/c120309059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309059.lua) | 1 |
| [Rising Protect](/examples/rush-cards/120304055) | `120304055` | [Rush/Scripts/c120304055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304055.lua) | 1 |
| [Sunset Rebirth](/examples/rush-cards/120257066) | `120257066` | [Rush/Scripts/c120257066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257066.lua) | 1 |
| Fusionic Defense | `120257064` | [Rush/Scripts/c120257064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257064.lua) | 1 |
| Sevens Road Protection | `120217021` | [Rush/Scripts/c120217021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217021.lua) | 1 |
| Voidvelg Kyrie | `120244006` | [Rush/Scripts/c120244006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244006.lua) | 1 |
| Divinebreath the Orchestral Music Fiend | `120247018` | [Rush/Scripts/c120247018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247018.lua) | 1 |
| Ultra Evolution Miracle | `120274051` | [Rush/Scripts/c120274051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274051.lua) | 1 |
| Wish of OuTerverSe the World-Shattering Emperor \[L\] | `120293058` | [Rush/Scripts/c120293058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293058.lua) | 1 |
| Dice Key Retra | `120272008` | [Rush/Scripts/c120272008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272008.lua) | 1 |
| Destined Doom of the Defiant Souls | `120298016` | [Rush/Scripts/c120298016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298016.lua) | 1 |
| Straynge Magician | `120109032` | [Rush/Scripts/c120109032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109032.lua) | 1 |
| Ever-Grace Princess Mai | `120287014` | [Rush/Scripts/c120287014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287014.lua) | 1 |
| Destroyer of Dragon Sorcerers | `120231049` | [Rush/Scripts/c120231049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231049.lua) | 1 |
| Cyber Gryphon | `120231025` | [Rush/Scripts/c120231025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231025.lua) | 1 |
| Dynamail Dino Dynamix \[R\] | `120274033` | [Rush/Scripts/c120274033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274033.lua) | 1 |
| Meteor Black Drake | `120253047` | [Rush/Scripts/c120253047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253047.lua) | 1 |
| Tribemirror Dragon | `120261051` | [Rush/Scripts/c120261051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261051.lua) | 1 |
| Valkyrion the Magna Wings | `120260024` | [Rush/Scripts/c120260024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260024.lua) | 1 |
| Galactica Oblivion Ark | `120277008` | [Rush/Scripts/c120277008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277008.lua) | 1 |
| Jinzo - Amplified | `120257029` | [Rush/Scripts/c120257029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257029.lua) | 1 |
| Ancient Barrier | `120155040` | [Rush/Scripts/c120155040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155040.lua) | 1 |
| Sevens Chariot | `120244043` | [Rush/Scripts/c120244043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244043.lua) | 1 |
| Neo Plandish | `120228035` | [Rush/Scripts/c120228035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228035.lua) | 1 |
| ...and 6 more |  |  |  |

## Script Examples

### Lufer the Symbol of the Devils (`120309059`)

Source: [Rush/Scripts/c120309059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309059.lua)

```lua
function cm.filter(c)
	return c:IsFaceup() and c:IsAttackBelow(2500)
		and (RD.IsCanAttachEffectIndes(c,tp,cm.indval)
		or RD.IsCanAttachCannotToHandEffect(c,1)
		or RD.IsCanAttachCannotToDeckEffect(c,1))
```

### Rising Protect (`120304055`)

Source: [Rush/Scripts/c120304055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304055.lua)

```lua
end
function cm.exfilter(c,tp)
	return c:IsFaceup() and RD.IsCanAttachEffectIndes(c,tp,cm.indval)
end
function cm.check(g)
```

### Sunset Rebirth (`120257066`)

Source: [Rush/Scripts/c120257066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257066.lua)

```lua
end
function cm.exfilter(c,tp)
	return RD.IsCanAttachEffectIndes(c,tp,cm.indval)
end
function cm.condition1(e,tp,eg,ep,ev,re,r,rp)
```
