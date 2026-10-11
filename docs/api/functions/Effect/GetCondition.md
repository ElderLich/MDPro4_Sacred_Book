# Effect.GetCondition

## Signature

```lua
Effect.GetCondition(Effect e) -> function|nil
```

## Description

Returns e's condition callback, or nil when no condition is set.

## Parameters

- `e` `Effect`

## Returns

- `function|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:641`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Effect.GetCondition) with `Effect.GetCondition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Union Activation | `38527680` | [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua) | 2 |
| Quick Summon | `10086952` | [Scripts/c10086952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10086952.lua) | 2 |
| Dinomorphia Rexterm | `92798873` | [Scripts/c92798873.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92798873.lua) | 1 |
| Bait Doll | `7165085` | [Scripts/c7165085.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7165085.lua) | 1 |
| Hope for Escape | `80036543` | [Scripts/c80036543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80036543.lua) | 1 |

## Script Examples

### Union Activation (`38527680`)

Source: [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua)

```lua
	if c:IsHasEffect(EFFECT_LIMIT_SUMMON_PROC,c:GetControler()) then
		local tte=c:IsHasEffect(EFFECT_LIMIT_SUMMON_PROC,c:GetControler())
		local ec=tte:GetCondition()
		if not ec(e,c,0) then return false end
	end
```

### Quick Summon (`10086952`)

Source: [Scripts/c10086952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10086952.lua)

```lua
	if c:IsHasEffect(EFFECT_LIMIT_SUMMON_PROC,c:GetControler()) then
		local tte=c:IsHasEffect(EFFECT_LIMIT_SUMMON_PROC,c:GetControler())
		local ec=tte:GetCondition()
		if not ec(e,c,0) then
			if e1 then e1:Reset() end
```

### Dinomorphia Rexterm (`92798873`)

Source: [Scripts/c92798873.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92798873.lua)

```lua
		local ce={Duel.IsPlayerAffectedByEffect(tp,EFFECT_LPCOST_CHANGE)}
		for _,te in ipairs(ce) do
			local con=te:GetCondition()
			local val=te:GetValue()
			if (not con or con(te)) then
```
