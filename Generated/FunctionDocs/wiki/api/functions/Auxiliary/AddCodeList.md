# Auxiliary.AddCodeList

## Signature

```lua
Auxiliary.AddCodeList(Card c, ... any) -> void
```

## Description

Registers one or more card codes as codes listed by c, so later checks such as Auxiliary.IsCodeListed can find them. Skipped while c is copying an effect.

## Parameters

- `c` `Card`
- `...` `any`

## Source

- `Utilities/utility.lua:533`
