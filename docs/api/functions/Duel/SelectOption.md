# Duel.SelectOption

## Signature

```lua
Duel.SelectOption(int player, int desc1, ... any) -> int
```

## Description

Shows player a list of description ids and returns the zero-based index of the selected option.
The selected description id is also announced to the client.

## Parameters

- `player` `int`
- `desc1` `int`
- `...` `any`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5024`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **479** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SelectOption) with `Duel.SelectOption`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer](/examples/cards/76794549) | `76794549` | [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76794549.lua) | 2 |
| [Ashtraja Susanoo](/examples/cards/17020474) | `17020474` | [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17020474.lua) | 1 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27693363.lua) | 1 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57261568.lua) | 1 |
| [GMX Associate Noma](/examples/cards/83528184) | `83528184` | [Scripts/c83528184.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83528184.lua) | 1 |
| [Albion the Branded Dragon](/examples/cards/87746184) | `87746184` | [Scripts/c87746184.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87746184.lua) | 1 |
| [Chronograph Sorcerer](/examples/cards/12289247) | `12289247` | [Scripts/c12289247.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12289247.lua) | 2 |
| Trickstar Diffusion | `63181559` | [Scripts/c63181559.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63181559.lua) | 3 |
| Vaylantz Genesis Grand Duke | `76075139` | [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76075139.lua) | 3 |
| Vernusylph and the Changing Season | `37313338` | [Scripts/c37313338.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37313338.lua) | 1 |
| Trirealm Rift Judgment | `65195679` | [Scripts/c65195679.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65195679.lua) | 1 |
| Secrets of Dark Magic | `59514116` | [Scripts/c59514116.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59514116.lua) | 3 |
| Mecha Phantom Beast Auroradon | `44097050` | [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44097050.lua) | 1 |
| Power Tool Braver Dragon | `63265554` | [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63265554.lua) | 1 |
| Deep Sea Minstrel | `71978434` | [Scripts/c71978434.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71978434.lua) | 1 |
| Magikey Duo | `51510279` | [Scripts/c51510279.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51510279.lua) | 1 |
| Koa'ki Meiru Rooklord | `10060427` | [Scripts/c10060427.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10060427.lua) | 4 |
| D/D/D Deviser King Deus Machinex | `46593546` | [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46593546.lua) | 1 |
| Arktos XII - Chronochasm Vaylantz | `50687050` | [Scripts/c50687050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50687050.lua) | 1 |
| Ursarctic Quint Charge | `15758127` | [Scripts/c15758127.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15758127.lua) | 3 |
| GMX - VELOX | `82706696` | [Scripts/c82706696.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82706696.lua) | 1 |
| Erebus the Underworld Monarch | `23064604` | [Scripts/c23064604.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23064604.lua) | 4 |
| Horn of Olifant | `55749927` | [Scripts/c55749927.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55749927.lua) | 3 |
| Hi-Speedroid Cork Shooter | `23361526` | [Scripts/c23361526.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23361526.lua) | 1 |
| ...and 455 more |  |  |  |

## Script Examples

### Astrograph Sorcerer (`76794549`)

Source: [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76794549.lua)

```lua
		local op=0
		if Duel.GetLocationCount(tp,LOCATION_MZONE)>0 and tc:IsCanBeSpecialSummoned(e,0,tp,false,false) then
			op=Duel.SelectOption(tp,aux.Stringid(76794549,1),aux.Stringid(76794549,2))
		else
			op=Duel.SelectOption(tp,aux.Stringid(76794549,1))
```

### Ashtraja Susanoo (`17020474`)

Source: [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17020474.lua)

```lua
		local set=s.setfilter(tc,e,tp)
		if tc:IsAbleToHand()
			and (not set or Duel.SelectOption(tp,1190,1153)==0) then
			Duel.SendtoHand(tc,nil,REASON_EFFECT)
			Duel.ConfirmCards(1-tp,tc)
```

### Ursarctic Polari (`27693363`)

Source: [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27693363.lua)

```lua
	if tc then
		if tc:IsAbleToHand() and (not tc:IsCanBeSpecialSummoned(e,0,tp,false,false) or not check
			or Duel.SelectOption(tp,1190,1152)==0) then
			Duel.SendtoHand(tc,nil,REASON_EFFECT)
		else
```
