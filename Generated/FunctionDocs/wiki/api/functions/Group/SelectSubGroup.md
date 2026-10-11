# Group.SelectSubGroup

## Signature

```lua
Group.SelectSubGroup(Group g, int tp, function f, bool cancelable, [int min], [int max], ... any) -> Group|nil
```

## Description

Lets tp select a subgroup from g with size between min and max that satisfies f. It respects already selected cards and returns nil if no valid selection is completed.
Use Group.CheckSubGroup for the legality check, then SelectSubGroup where the player actually chooses the cards. If the chosen Group is stored for a later callback, call KeepAlive and later DeleteGroup.
Use this for group-level requirements; use Group.FilterSelect for ordinary one-card filters.

## How To Use It

Use this when the player must choose a subset that satisfies a group-level rule, not just individual card filters.

```lua
local sg=g:SelectSubGroup(tp,s.goal,false,2,3)
if sg then
    Duel.SendtoGrave(sg,REASON_EFFECT)
end
```

Use the matching `Group.CheckSubGroup` shape in `chk==0` legality checks so the real prompt only appears after activation is legal.

## Related Functions

- [Group.CheckSubGroup](/api/functions/Group/CheckSubGroup)
- [Group.SelectUnselect](/api/functions/Group/SelectUnselect)
- [Group.Select](/api/functions/Group/Select)

## Parameters

- `g` `Group`
- `tp` `int`
- `f` `function`
- `cancelable` `bool`
- `min` `int` optional
- `max` `int` optional
- `...` `any`

## Returns

- `Group|nil` - The selected subgroup, or nil if no valid selection is completed.

## Source

- `Utilities/utility.lua:1258`
