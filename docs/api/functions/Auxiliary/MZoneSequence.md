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

- `Utilities/utility.lua:721`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **13** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.MZoneSequence) with `Auxiliary.MZoneSequence`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Distrust Paranoia | `81965543` | [Scripts/c81965543.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81965543.lua) | 2 |
| S-Force Signify | `19951423` | [Scripts/c19951423.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19951423.lua) | 1 |
| Angelechy Enlisted | `81797573` | [Scripts/c81797573.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81797573.lua) | 3 |
| World Legacy's Secret | `98935722` | [Scripts/c98935722.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98935722.lua) | 2 |
| Vaylantz World - Konig Wissen | `75952542` | [Scripts/c75952542.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75952542.lua) | 1 |
| Scareclaw Reichheart | `82361809` | [Scripts/c82361809.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82361809.lua) | 1 |
| World Legacy Whispers | `62530723` | [Scripts/c62530723.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62530723.lua) | 1 |
| Disablaster the Negation Fortress | `58707981` | [Scripts/c58707981.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58707981.lua) | 2 |
| World Legacy Key | `2930675` | [Scripts/c2930675.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2930675.lua) | 1 |
| Scareclaw Astra | `83488497` | [Scripts/c83488497.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83488497.lua) | 1 |
| Scareclaw Acro | `46877100` | [Scripts/c46877100.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46877100.lua) | 1 |
| Scareclaw Belone | `19882096` | [Scripts/c19882096.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19882096.lua) | 1 |
| Broken Line | `88086137` | [Scripts/c88086137.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88086137.lua) | 1 |

## Script Examples

### Distrust Paranoia (`81965543`)

Source: [Scripts/c81965543.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81965543.lua)

```lua
end
function s.efilter(e,te)
	local seq1=aux.MZoneSequence(e:GetHandler():GetSequence())
	local seq=Duel.GetChainInfo(0,CHAININFO_TRIGGERING_SEQUENCE)
	if (te:GetActivateLocation()&LOCATION_ONFIELD)==0 then return false end
```

### S-Force Signify (`19951423`)

Source: [Scripts/c19951423.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19951423.lua)

```lua
end
function s.cfilter(c,seq2)
	local seq1=aux.MZoneSequence(c:GetSequence())
	return c:IsFaceup() and c:IsSetCard(0x156) and seq1==4-seq2
end
```

### Angelechy Enlisted (`81797573`)

Source: [Scripts/c81797573.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81797573.lua)

```lua
end
function s.rmfilter(c,ec,tp)
	local seq1=aux.MZoneSequence(c:GetSequence())
	local seq2=aux.MZoneSequence(ec:GetSequence())
	local seq3=4-seq2
```
