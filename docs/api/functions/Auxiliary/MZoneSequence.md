# Auxiliary.MZoneSequence

## Signature

```lua
Auxiliary.MZoneSequence(int seq) -> int
```

## Description

Returns the local column index for Monster Zone sequence seq from that controller's viewpoint.

## Parameters

- `seq` `int`

## Returns

- `int`

## Source

- `Utilities/utility.lua:718`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **11** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.MZoneSequence`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| S-Force Signus | `19951423` | [Scripts/c19951423.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19951423.lua) | 1 |
| World Legacy's Secret | `98935722` | [Scripts/c98935722.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98935722.lua) | 2 |
| Vaylantz World - Konig Wissen | `75952542` | [Scripts/c75952542.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75952542.lua) | 1 |
| Scareclaw Reichheart | `82361809` | [Scripts/c82361809.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82361809.lua) | 1 |
| World Legacy Whispers | `62530723` | [Scripts/c62530723.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62530723.lua) | 1 |
| Disablaster the Negation Fortress | `58707981` | [Scripts/c58707981.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58707981.lua) | 2 |
| World Legacy Key | `2930675` | [Scripts/c2930675.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2930675.lua) | 1 |
| Scareclaw Astra | `83488497` | [Scripts/c83488497.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83488497.lua) | 1 |
| Scareclaw Acro | `46877100` | [Scripts/c46877100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46877100.lua) | 1 |
| Scareclaw Belone | `19882096` | [Scripts/c19882096.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19882096.lua) | 1 |
| Broken Line | `88086137` | [Scripts/c88086137.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88086137.lua) | 1 |

## Script Examples

### S-Force Signus (`19951423`)

Source: [Scripts/c19951423.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19951423.lua)

```lua
end
function s.cfilter(c,seq2)
	local seq1=aux.MZoneSequence(c:GetSequence())
	return c:IsFaceup() and c:IsSetCard(0x156) and seq1==4-seq2
end
```

### World Legacy's Secret (`98935722`)

Source: [Scripts/c98935722.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98935722.lua)

```lua
end
function c98935722.cfilter(c,seq2)
	local seq1=aux.MZoneSequence(c:GetSequence())
	return c:IsFaceup() and c:IsSetCard(0x10c) and seq1==4-seq2
end
```

### Vaylantz World - Konig Wissen (`75952542`)

Source: [Scripts/c75952542.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75952542.lua)

```lua
end
function c75952542.cfilter(c,seq)
	return aux.MZoneSequence(c:GetSequence())==4-seq
end
function c75952542.sttg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
