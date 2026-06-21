# Group.GetFirst

## Signature

```lua
Group.GetFirst(Group g) -> Card|nil
```

## Description

Returns the first card in g and resets g's internal iterator to that card. Returns nil when g is empty.

## How To Use It

Use `GetFirst`/`GetNext` to iterate through a Group when helper iterators are not available.

```lua
local tc=g:GetFirst()
while tc do
    -- work with tc
    tc=g:GetNext()
end
```

`GetFirst` resets the Group's internal pointer. Starting a second iteration on the same Group resets that pointer again.

## Parameters

- `g` `Group`

## Returns

- `Card|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:909`
