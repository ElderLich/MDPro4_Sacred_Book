# Duel.SetLP

## Signature

```lua
Duel.SetLP(int player, int lp) -> void
```

## Description

Sets player's LP to lp, clamping negative lp values to 0, and sends the LP update message.

## Parameters

- `player` `int`
- `lp` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4847`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **84** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SetLP) with `Duel.SetLP`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Gishki Nekromirror | `36982581` | [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua) | 1 |
| GMX - VELOX | `82706696` | [Scripts/c82706696.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82706696.lua) | 1 |
| Nirvana High Paladin | `80896940` | [Scripts/c80896940.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80896940.lua) | 1 |
| Spirit Poacher | `85150300` | [Scripts/c85150300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85150300.lua) | 1 |
| Mamonaka the Vaylantz United | `40680521` | [Scripts/c40680521.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40680521.lua) | 1 |
| Heavy Polymerization | `58570206` | [Scripts/c58570206.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58570206.lua) | 2 |
| Machina Ruinforce | `46033517` | [Scripts/c46033517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46033517.lua) | 1 |
| Vesper Girsu | `97345699` | [Scripts/c97345699.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97345699.lua) | 1 |
| Number 6: Chronomaly Atlandis | `9161357` | [Scripts/c9161357.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9161357.lua) | 1 |
| GMX Applied Experiment #55 | `18795635` | [Scripts/c18795635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18795635.lua) | 1 |
| Super All In! | `16780318` | [Scripts/c16780318.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16780318.lua) | 1 |
| Super Koi Koi | `66171432` | [Scripts/c66171432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66171432.lua) | 1 |
| Steel-Stringed Sacrifice | `7166709` | [Scripts/c7166709.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7166709.lua) | 1 |
| Cubic Karma | `9659580` | [Scripts/c9659580.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9659580.lua) | 1 |
| Impcantation Chalislime | `65877963` | [Scripts/c65877963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65877963.lua) | 1 |
| Wattkingdom | `41790641` | [Scripts/c41790641.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41790641.lua) | 1 |
| Evil Eyes Unleashed | `8775395` | [Scripts/c8775395.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8775395.lua) | 1 |
| Victorica, Angel of Bravery | `79928401` | [Scripts/c79928401.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79928401.lua) | 1 |
| Evil Eye of Selene | `44133040` | [Scripts/c44133040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44133040.lua) | 1 |
| Number C104: Umbral Horror Masquerade Victory | `42396591` | [Scripts/c42396591.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42396591.lua) | 1 |
| Kozmotown | `67237709` | [Scripts/c67237709.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67237709.lua) | 1 |
| Number C6: Chronomaly Chaos Atlandis | `6387204` | [Scripts/c6387204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6387204.lua) | 1 |
| Performapal Popperup | `11481610` | [Scripts/c11481610.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11481610.lua) | 1 |
| Message in a Bottle | `97433739` | [Scripts/c97433739.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97433739.lua) | 1 |
| ...and 60 more |  |  |  |

## Script Examples

### Gishki Nekromirror (`36982581`)

Source: [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua)

```lua
		Duel.BreakEffect()
		if Duel.SpecialSummon(tc,SUMMON_TYPE_RITUAL,tp,tp,false,true,POS_FACEUP)>0 then
			Duel.SetLP(tp,Duel.GetLP(tp)-tc:GetBaseAttack())
			tc:CompleteProcedure()
		end
```

### GMX - VELOX (`82706696`)

Source: [Scripts/c82706696.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82706696.lua)

```lua
		end
		Duel.DisableShuffleCheck()
		Duel.SetLP(tp,Duel.GetLP(tp)-(dct-seq)*400)
		local spchk=Duel.GetLocationCount(tp,LOCATION_MZONE)>0 and hc:IsCanBeSpecialSummoned(e,0,tp,false,false)
		if hc:IsAbleToHand() and (not spchk or Duel.SelectOption(tp,1190,1152)==0) then
```

### Nirvana High Paladin (`80896940`)

Source: [Scripts/c80896940.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80896940.lua)

```lua
end
function c80896940.lpop(e,tp,eg,ep,ev,re,r,rp)
	Duel.SetLP(1-tp,math.ceil(Duel.GetLP(1-tp)/2))
end
function c80896940.pencon(e,tp,eg,ep,ev,re,r,rp)
```
