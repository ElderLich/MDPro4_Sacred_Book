# Auxiliary.AND

## Signature

```lua
Auxiliary.AND(... any) -> void
```

## Description

Returns a composed predicate that calls each function with the same arguments and stops at the first falsy result.

## Parameters

- `...` `any`

## Source

- `Utilities/utility.lua:97`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **79** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AND`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Hecahands Tartaros](/examples/cards/57809669) | `57809669` | [Scripts/c57809669.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57809669.lua) | 1 |
| D/D Extra Surveyor | `74387963` | [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74387963.lua) | 2 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5148778.lua) | 1 |
| Roar of the Blue-Eyed Dragons | `17725109` | [Scripts/c17725109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17725109.lua) | 1 |
| Defense of the Temple | `96687733` | [Scripts/c96687733.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96687733.lua) | 1 |
| Sinful Spoils of the White Forest | `3496543` | [Scripts/c3496543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3496543.lua) | 1 |
| Dreaming Nemleria | `70155677` | [Scripts/c70155677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70155677.lua) | 1 |
| Elfnotes: Rhapsodia of Madness | `24092792` | [Scripts/c24092792.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24092792.lua) | 1 |
| Azamina Determination | `42201897` | [Scripts/c42201897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42201897.lua) | 2 |
| Phara, the Goddess of the Beginning | `82344137` | [Scripts/c82344137.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82344137.lua) | 1 |
| Possessed Resonance - Wynn | `60516416` | [Scripts/c60516416.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60516416.lua) | 1 |
| Dream Tower of Princess Nemleria | `18458255` | [Scripts/c18458255.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18458255.lua) | 1 |
| Sweet Dreams, Nemleria | `44843954` | [Scripts/c44843954.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44843954.lua) | 1 |
| Amazement Abomination Arlekino | `31600845` | [Scripts/c31600845.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31600845.lua) | 1 |
| Eidos the Underworld Monarch | `31596518` | [Scripts/c31596518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31596518.lua) | 1 |
| Wind Unicorn Parallel, the Dracoslayer | `39016067` | [Scripts/c39016067.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39016067.lua) | 2 |
| Jurrac Stego | `20568404` | [Scripts/c20568404.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20568404.lua) | 2 |
| Artmage Academic Arcane Arts Acropolis | `74733322` | [Scripts/c74733322.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74733322.lua) | 1 |
| Dragunity Lord - Georgius | `70522875` | [Scripts/c70522875.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70522875.lua) | 1 |
| ASHLAN U1000 | `44376395` | [Scripts/c44376395.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44376395.lua) | 2 |
| Twilight Rose Black Knight | `92595825` | [Scripts/c92595825.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92595825.lua) | 1 |
| Cursed Copycat Noble Arms | `23249029` | [Scripts/c23249029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23249029.lua) | 1 |
| R.B. Last Stand | `43450363` | [Scripts/c43450363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43450363.lua) | 1 |
| Arcana Force V - The Hierophant | `3376703` | [Scripts/c3376703.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3376703.lua) | 1 |
| ...and 55 more |  |  |  |

## Script Examples

### Hecahands Tartaros (`57809669`)

Source: [Scripts/c57809669.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57809669.lua)

```lua
		and (not e:IsCostChecked()
		or Duel.GetFlagEffect(tp,id)==0
			and Duel.IsExistingMatchingCard(aux.AND(Card.IsFaceup,Card.IsSetCard),tp,LOCATION_MZONE,0,1,nil,0x1d3))
	local chkf=tp
	local mg1=Duel.GetFusionMaterial(tp):Filter(s.filter1,nil,e)
```

### D/D Extra Surveyor (`74387963`)

Source: [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74387963.lua)

```lua
end
function s.rmtg(e,tp,eg,ep,ev,re,r,rp,chk)
	local ct=Duel.GetMatchingGroupCount(aux.AND(Card.IsFaceup,Card.IsType),tp,0,LOCATION_EXTRA,nil,TYPE_PENDULUM)
	local tg=Duel.GetDecktopGroup(1-tp,ct)
	if chk==0 then return ct>0
```

### Starving Venom Wing Dragon (`5148778`)

Source: [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5148778.lua)

```lua
end
function s.discon(e,tp,eg,ep,ev,re,r,rp)
	return eg:IsExists(aux.AND(Card.IsSummonPlayer,Card.IsFaceup),1,nil,1-tp)
end
function s.distg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
