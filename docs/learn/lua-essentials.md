# Lua Essentials For Card Scripts

**Start here if Lua is new to you.** By the end, you should be able to read a
filter, pass a callback, and recognize three bugs that also occur in real cards.
Then continue to [Script Structure](script-structure).

## Read One Filter

```lua
local s,id=GetID()

function s.filter(c)
    return c:IsFaceup() and c:IsRace(RACE_DRAGON) and c:GetLevel()<=4
end
```

`local` limits a variable's scope. `s` is this card's script table; `id` is its
numeric card ID. `function s.filter(c)` stores a function in that table. The
engine supplies a candidate Card as `c`, and `return` gives the answer back.
The filter above accepts face-up Dragons of Level 4 or lower.

`and` requires both sides to pass; `or` accepts either side. Lua stops checking
as soon as the answer is known. This makes a guard such as
`tc and tc:IsFaceup()` safe when `tc` might be missing.

## Pass A Function Or Call It

```lua
e1:SetTarget(s.target)       -- Save the function for the engine to call later.
local atk=c:GetAttack()      -- Call now and save the returned number.
```

`s.target` is a function value. `s.target()` calls that function immediately.
Writing `e1:SetTarget(s.target())` usually runs a callback before its parameters
exist, then tries to register its result.

A colon passes the object as the first argument:

```lua
c:IsRace(RACE_DRAGON)
Card.IsRace(c,RACE_DRAGON)    -- Same argument shape.
```

This also explains a common filter call:

```lua
local g=Duel.GetMatchingGroup(Card.IsRace,tp,LOCATION_MZONE,0,nil,RACE_DRAGON)
```

The engine calls `Card.IsRace(candidate,RACE_DRAGON)` for each candidate. The
`nil` is the excluded-card argument; it keeps the later argument in its correct
position. See [Filters and Groups](filters-and-groups) for the full pattern.

## Zero Is True In Lua

Only `false` and `nil` are false. The number `0`, an empty string, and an empty
Group are all true in an `if` condition.

```lua
-- A movement function returns a count. Compare that count explicitly.
if Duel.SendtoGrave(tc,REASON_EFFECT)>0 and tc:IsLocation(LOCATION_GRAVE) then
    -- Continue only when the action succeeded and this card reached the GY.
end
```

An empty Group and a missing Group are different:

```lua
if g and g:GetCount()>0 then
    -- There is a Group, and it contains at least one card.
end
```

`SelectSubGroup` can return `nil`. Guard it before using `#g`, `g:GetCount()`, or
any other Group method. A previously successful legality check does not make
that guard unnecessary.

## Compare Values Explicitly

| Expression | Meaning |
| --- | --- |
| `x=1` | Assign 1 to `x`. |
| `x==1` | Test whether `x` equals 1. |
| `x~=1` | Test whether `x` differs from 1. |
| `not c:IsFaceup()` | Invert a Boolean result. |
| `c:GetAttack()~=0` | Test whether ATK is nonzero. |

`not c:GetAttack()==0` means `(not c:GetAttack())==0`. It does **not** mean
“ATK is not zero.” Use `~=` or `not (c:GetAttack()==0)`.

## Masks Represent Several Choices

Constants such as locations and types are bit flags. A mask combines them:

```lua
local locations=LOCATION_HAND|LOCATION_GRAVE
local hasMonsterBit=(c:GetType()&TYPE_MONSTER)~=0
```

Existing scripts often use `+` for distinct flags. Do not add the same bit
twice: `TYPE_MONSTER+TYPE_MONSTER` changes the number. A bitwise `|` preserves
the bit when it is already present.

Also distinguish **any** from **all**:

```lua
c:IsType(TYPE_MONSTER|TYPE_NORMAL)       -- At least one of these bits.
c:IsAllTypes(TYPE_MONSTER|TYPE_NORMAL)   -- Both bits must be present.
```

For wording about a “Normal Monster **card**,” the updated core has a separate
[card-type API](engine-updates#card-type-and-current-type).

## Store Temporary Values Locally

Use `local c=e:GetHandler()` inside a callback for its current Card. A plain
assignment such as `c=e:GetHandler()` writes a global and can interfere with
other scripts. Script-table fields such as `s.listed_names` are shared metadata
for that script, not private memory for each copy on the field.

For state that belongs to an effect or card, learn [Flag Effects](flag-effects),
[Count Limits](count-limits), and [Reset Flags](reset-flags-and-duration).

## Check Your Understanding

Before continuing, predict these answers:

1. Does `if 0 then` enter its branch?
2. Which registers a callback: `s.target` or `s.target()`?
3. Can you call `g:GetFirst()` before checking a possibly missing `g`?
4. Does `IsType(TYPE_MONSTER|TYPE_NORMAL)` require both bits?

::: details Reveal answers
1. Yes. Zero is true in Lua.
2. `s.target` passes the function itself.
3. No. Guard a possible `nil` first; `GetFirst()` can itself return `nil`.
4. No. Use `IsAllTypes` to require both current-type bits.
:::

These are practical checks: the imported upstream fixes for `c2606417.lua`,
`c43419178.lua`, and subgroup selections address exactly these classes of bug.
Continue with [Script Structure](script-structure), then the
[Beginner Script Ladder](beginner-script-ladder).
