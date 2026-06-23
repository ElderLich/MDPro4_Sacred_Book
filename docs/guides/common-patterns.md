# Common Patterns

Many scripts repeat the same shapes.

## Filters

```lua
function s.filter(c)
  return c:IsFaceup() and c:IsSetCard(0x123)
end
```

Filters usually receive a `Card` first and return `true` or `false`.

## Target Then Operation

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
  if chk==0 then return Duel.IsPlayerCanDraw(tp,1) end
  Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,1)
end

function s.operation(e,tp,eg,ep,ev,re,r,rp)
  Duel.Draw(tp,1,REASON_EFFECT)
end
```

The target checks legality and declares what will happen. The operation performs
the effect.

## Flag Effects

Use [Flag effects](/learn/flag-effects) when a script needs temporary memory,
such as whether a player has already used one option this turn or whether a
specific card was marked by an earlier operation.

## Count Limits

Use [count limits](/learn/count-limits) for normal once-per-turn and shared-use
limits. `SetCountLimit(1,id)` spends a use of the effect's shared count code,
while custom activity counters handle restrictions based on Summons, attacks,
or chains that already happened this turn.
