# Auxiliary.IsCodeListed

## Signature

```lua
Auxiliary.IsCodeListed(Card c, int code) -> bool|nil
```

## Description

Checks whether code is registered in c's card_code_list by Auxiliary.AddCodeList or a related helper.
The Lua helper returns true for a listed code and nil otherwise, so it is normally used as a truthy check.

## Parameters

- `c` `Card`
- `code` `int`

## Returns

- `bool|nil` - true if code is listed by c; nil otherwise.

## Source

- `Utilities/utility.lua:547`
