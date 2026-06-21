# Group.IsExists

## Signature

```lua
Group.IsExists(Group g, function f, int count, [Card|Group|nil ex], ... any) -> bool
```

## Description

Checks whether at least count cards in g satisfy filter f and are not excluded by ex.
Extra arguments after ex are passed to f after the card argument.

## How To Use It

Use this to check whether a Group contains enough cards with a property.

```lua
if g:IsExists(Card.IsRace,1,nil,RACE_DRAGON) then
    -- at least one Dragon is in g
end
```

The `count` parameter is useful for requirements such as "2 or more monsters with different names" once the filter captures the condition you need.

## Parameters

- `g` `Group`
- `f` `function`
- `count` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:919`
