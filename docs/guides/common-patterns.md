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
