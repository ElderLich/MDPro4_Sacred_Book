# Group.GetNext

## Signature

```lua
Group.GetNext(Group g) -> Card|nil
```

## Description

Advances g's internal iterator and returns the next card, or nil when there are no more cards.

## How To Use It

`GetNext` belongs to the `GetFirst` iteration pattern. It advances the same internal pointer and returns nil after the final card.

```lua
for tc in aux.Next(g) do
    -- aux.Next wraps GetFirst/GetNext
end
```

When you only need the number of cards, use `#g` or `g:GetCount()` instead of iterating.

## Parameters

- `g` `Group`

## Returns

- `Card|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:908`
