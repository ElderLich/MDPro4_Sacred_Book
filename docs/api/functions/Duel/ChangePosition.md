# Duel.ChangePosition

## Signature

```lua
Duel.ChangePosition(Card|Group targets, int au, [int ad], [int du], [int dd], [bool noflip], [bool setavailable]) -> int
```

## Description

Changing the representation of targets returns the number of actual operations
The attack on the watch side becomes au, the attack on the inside indicates ad,
The side of the garage that becomes du, inside the garrison said to become dd
If noflip = true, the reverse effect will not be triggered (but the effect of inversion will be triggered)
If setavailable = true then the object will become the back side also launched reversal effect

## Parameters

- `targets` `Card|Group`
- `au` `int`
- `ad` `int` optional - default: au
- `du` `int` optional - default: au
- `dd` `int` optional - default: au
- `noflip` `bool` optional - default: false
- `setavailable` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4880`
