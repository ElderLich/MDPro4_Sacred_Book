# Auxiliary.NecroValleyFilter

## Signature

```lua
Auxiliary.NecroValleyFilter(function f) -> void
```

## Description

Returns a wrapper filter that requires f(target, ...) and also rejects cards currently protected by Necrovalley while the Chain is disablable.

## Parameters

- `f` `function`

## Source

- `Utilities/utility.lua:920`
