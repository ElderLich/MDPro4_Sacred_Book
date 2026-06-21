# Auxiliary.RegisterMergedDelayedEvent

## Signature

```lua
Auxiliary.RegisterMergedDelayedEvent(Card c, int code, int event, [Group|nil g]) -> void
```

## Description

Registers global listeners that merge multiple occurrences of event into one EVENT_CUSTOM+code event. The merged event is raised immediately outside a Chain, or at Chain End while in a Chain.

## Parameters

- `c` `Card`
- `code` `int`
- `event` `int`
- `g` `Group|nil` optional - Optional storage group; a kept-alive group is created when omitted.

## Source

- `Utilities/utility.lua:1647`
