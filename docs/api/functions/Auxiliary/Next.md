# Auxiliary.Next

## Signature

```lua
Auxiliary.Next(Group g) -> void
```

## Description

Iterator for group g; the pointer starts at the first card and moves to the next card with each call, typically used when operating on cards in g
For example:
local g=Group.CreateGroup()
for tc in aux.Next(g) do
end
Equivalent to:
local g=Group.CreateGroup()
local tc=g:GetFirst()
while tc do
  tc=g:GetNext()
end

## Parameters

- `g` `Group`

## Source

- `Utilities/utility.lua:82`
