# Card.ResetEffect

## Signature

```lua
Card.ResetEffect(Card c, int reset_code, int reset_type) -> void
```

## Description

To reset the type to reset_type, reset the type reset_code manual reset c impact of the impact
The reset_type can only be one of the following types, and the corresponding reset type is
RESET_EVENT An event reset_code is set for the event
RESET_PHASE End of phase Reset the reset_code to phase
RESET_CODE reset the effect of the specified code reset_code for the type of effect code, can only be reset EFFECT_TYPE_SINGLE sustainable type effect
RESET_COPY resets the effect of the copy. Reset_code is copy_id
RESET_CARD The effect of resetting the card reset_code is the card number of the effect owner

## Parameters

- `c` `Card`
- `reset_code` `int`
- `reset_type` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3550`
