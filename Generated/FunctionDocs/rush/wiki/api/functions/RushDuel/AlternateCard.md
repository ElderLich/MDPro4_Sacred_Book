# RushDuel.AlternateCard

Alias: `RD.AlternateCard`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AlternateCard(int code) -> void
```

## Description

Loads c&lt;code&gt;.lua for an alternate-art card that shares its implementation.

## Parameters

- `code` `int`: Source card passcode.

## Returns

No return values.

## Source

`Rush/Utilities/RDBase.lua:68`

```lua
function RushDuel.AlternateCard(code)
    Duel.LoadScript("c" .. code .. ".lua")
end
```
