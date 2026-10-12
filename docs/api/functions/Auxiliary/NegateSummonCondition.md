# Auxiliary.NegateSummonCondition

## Signature

```lua
Auxiliary.NegateSummonCondition() -> bool
```

## Description

Returns true when no Chain is ready, for effects that negate a Summon.

## Returns

- `bool` - true when no Chain is ready.

## Source

- `Utilities/utility.lua:1836`

## Guided Examples

Learn how to use this function in context:

- [Common Script Errors And Debugging](/learn/common-script-errors-and-debugging)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **26** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.NegateSummonCondition) with `Auxiliary.NegateSummonCondition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dark World Punishment | `3167439` | [Scripts/c3167439.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3167439.lua) | 1 |
| Paradox Fusion | `57355219` | [Scripts/c57355219.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57355219.lua) | 1 |
| Bending Destiny | `94662235` | [Scripts/c94662235.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94662235.lua) | 1 |
| Gravity Collapse | `7811875` | [Scripts/c7811875.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7811875.lua) | 1 |
| Solemn Scolding | `92512625` | [Scripts/c92512625.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92512625.lua) | 1 |
| Floowandereeze and the Scary Sea | `77610503` | [Scripts/c77610503.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77610503.lua) | 1 |
| Solemn Warning | `84749824` | [Scripts/c84749824.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84749824.lua) | 1 |
| Mind Over Matter | `59718521` | [Scripts/c59718521.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59718521.lua) | 1 |
| Majespecter Tempest | `2572890` | [Scripts/c2572890.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2572890.lua) | 1 |
| Pollinosis | `91078716` | [Scripts/c91078716.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c91078716.lua) | 1 |
| Wattcancel | `56993276` | [Scripts/c56993276.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56993276.lua) | 1 |
| The Selection | `30888983` | [Scripts/c30888983.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30888983.lua) | 1 |
| Champion's Vigilance | `82382815` | [Scripts/c82382815.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82382815.lua) | 1 |
| Royal Oppression | `93016201` | [Scripts/c93016201.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93016201.lua) | 1 |
| Chaos Trap Hole | `11593137` | [Scripts/c11593137.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11593137.lua) | 1 |
| Drytron Meteor Shower | `84965420` | [Scripts/c84965420.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84965420.lua) | 1 |
| Solemn Judgment | `41420027` | [Scripts/c41420027.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41420027.lua) | 1 |
| Dream Mirror Oneiromancy | `61459246` | [Scripts/c61459246.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61459246.lua) | 1 |
| Solemn Strike | `40605147` | [Scripts/c40605147.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40605147.lua) | 1 |
| Vanquishing Light | `32233746` | [Scripts/c32233746.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c32233746.lua) | 1 |
| Horn of Heaven | `98069388` | [Scripts/c98069388.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98069388.lua) | 1 |
| Grand Horn of Heaven | `1637760` | [Scripts/c1637760.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1637760.lua) | 1 |
| Saber Hole | `44901281` | [Scripts/c44901281.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44901281.lua) | 1 |
| Pendulum Hole | `68477598` | [Scripts/c68477598.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c68477598.lua) | 1 |
| ...and 2 more |  |  |  |

## Script Examples

### Dark World Punishment (`3167439`)

Source: [Scripts/c3167439.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3167439.lua)

```lua
	e1:SetCode(EVENT_SUMMON)
	e1:SetCountLimit(1,id)
	e1:SetCondition(aux.NegateSummonCondition)
	e1:SetTarget(s.destg)
	e1:SetOperation(s.desop)
```

### Paradox Fusion (`57355219`)

Source: [Scripts/c57355219.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57355219.lua)

```lua
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_SPSUMMON)
	e1:SetCondition(aux.NegateSummonCondition)
	e1:SetCost(c57355219.cost)
	e1:SetTarget(c57355219.target1)
```

### Bending Destiny (`94662235`)

Source: [Scripts/c94662235.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94662235.lua)

```lua
end
function c94662235.condition1(e,tp,eg,ep,ev,re,r,rp)
	return aux.NegateSummonCondition() and c94662235.check(tp)
end
function c94662235.target1(e,tp,eg,ep,ev,re,r,rp,chk)
```
