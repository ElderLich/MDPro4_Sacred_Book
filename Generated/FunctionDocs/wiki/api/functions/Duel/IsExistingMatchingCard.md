# Duel.IsExistingMatchingCard

## Signature

```lua
Duel.IsExistingMatchingCard([function|nil f], int player, int s, int o, int count, [Card|Group|nil ex], ... any) -> bool
```

## Description

Checks whether the specified locations contain at least count cards that satisfy filter f and are not excluded by ex.
s is player's own location mask and o is the opponent's location mask from that player's viewpoint. Extra arguments after ex are passed to f.

## How To Use It

Use this for activation checks that only need to know whether matching cards exist.

The filter receives each candidate card first, followed by any extra arguments after `ex`:

```lua
function s.filter(c,e,tp)
    return c:IsFaceup() and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

if chk==0 then
    return Duel.IsExistingMatchingCard(s.filter,tp,LOCATION_GRAVE,0,1,nil,e,tp)
end
```

Use `Duel.IsExistingTarget` instead when the card must become an official target of the activating effect.

## Parameters

- `f` `function|nil` optional
- `player` `int`
- `s` `int`
- `o` `int`
- `count` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4972`
