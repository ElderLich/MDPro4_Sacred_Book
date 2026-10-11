# Auxiliary.SequenceToGlobal

## Signature

```lua
Auxiliary.SequenceToGlobal(int p, int loc, int seq) -> int
```

## Description

Converts a player's local Monster Zone or Spell & Trap Zone sequence into a global zone bit. Invalid players, locations, or sequences return 0.
Monster Zone bits are shifted by 16*p+seq; Spell & Trap Zone bits are shifted by 16*p+seq+8.

## Parameters

- `p` `int` - Player whose local field sequence is converted.
- `loc` `int` - LOCATION_MZONE or LOCATION_SZONE.
- `seq` `int` - Sequence inside loc. Monster Zone sequences up to 6 are accepted; Spell & Trap Zone sequences up to 4 are accepted.

## Returns

- `int` - The global zone bit, or 0 for invalid input.

## Source

- `Utilities/utility.lua:1490`

## Guided Examples

Learn how to use this function in context:

- [Field Zones And Sequences](/learn/field-zones-and-sequences)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.SequenceToGlobal) with `Auxiliary.SequenceToGlobal`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ninjitsu Art of Shadow Sealing | `13629812` | [Scripts/c13629812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13629812.lua) | 1 |
| Ghostrick Socuteboss | `32224143` | [Scripts/c32224143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32224143.lua) | 1 |
| Rage of Kairyu-Shin | `82685480` | [Scripts/c82685480.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82685480.lua) | 1 |
| Dimensionhole | `22959079` | [Scripts/c22959079.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22959079.lua) | 1 |
| Magical Musket - Crooked Crown | `47810543` | [Scripts/c47810543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47810543.lua) | 1 |
| Prometeor, the Burning Star | `75713017` | [Scripts/c75713017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75713017.lua) | 1 |

## Script Examples

### Ninjitsu Art of Shadow Sealing (`13629812`)

Source: [Scripts/c13629812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13629812.lua)

```lua
	local c=e:GetHandler()
	local tc=Duel.GetFirstTarget()
	local val=aux.SequenceToGlobal(tc:GetControler(),LOCATION_MZONE,tc:GetSequence())
	if tc:IsRelateToEffect(e) and Duel.Remove(tc,0,REASON_EFFECT+REASON_TEMPORARY)~=0 and tc:IsLocation(LOCATION_REMOVED) then
		c:SetCardTarget(tc)
```

### Ghostrick Socuteboss (`32224143`)

Source: [Scripts/c32224143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32224143.lua)

```lua
function c32224143.operation(e,tp,eg,ep,ev,re,r,rp)
	local tc=Duel.GetFirstTarget()
	local val=aux.SequenceToGlobal(tc:GetControler(),LOCATION_MZONE,tc:GetSequence())
	if tc:IsRelateToEffect(e) and tc:IsFaceup() and Duel.Destroy(tc,REASON_EFFECT)~=0 then
		local e1=Effect.CreateEffect(e:GetHandler())
```

### Rage of Kairyu-Shin (`82685480`)

Source: [Scripts/c82685480.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82685480.lua)

```lua
	local tc=og:GetFirst()
	while tc do
		val=val|aux.SequenceToGlobal(tc:GetPreviousControler(),LOCATION_MZONE,tc:GetPreviousSequence())
		tc=og:GetNext()
	end
```
