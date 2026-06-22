# Duel.SpecialSummonComplete

## Signature

```lua
Duel.SpecialSummonComplete() -> int
```

## Description

Completes a batch of successful Duel.SpecialSummonStep calls, raises the Summon events, and returns the number of completed Summons.

## How To Use It

Use this after a batch of successful `Duel.SpecialSummonStep` calls.

```lua
if Duel.SpecialSummonStep(tc,0,tp,tp,false,false,POS_FACEUP) then
    Duel.SpecialSummonComplete()
end
```

Without the complete call, the step Summons do not finish their event handling correctly.

## Related Functions

- [Duel.SpecialSummonStep](/api/functions/Duel/SpecialSummonStep)
- [Duel.SpecialSummon](/api/functions/Duel/SpecialSummon)

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4875`
