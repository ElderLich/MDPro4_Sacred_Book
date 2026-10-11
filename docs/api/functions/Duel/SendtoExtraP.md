# Duel.SendtoExtraP

## Signature

```lua
Duel.SendtoExtraP(Card|Group targets, int player, int reason) -> int
```

## Description

Sends cards to player-side Extra Deck face-up for reason and returns the number of cards moved.

## Parameters

- `targets` `Card|Group`
- `player` `int`
- `reason` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4863`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **25** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SendtoExtraP) with `Duel.SendtoExtraP`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Kewl Tune Crackle](/examples/cards/39576656) | `39576656` | [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39576656.lua) | 1 |
| Dreaming Nemleria | `70155677` | [Scripts/c70155677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70155677.lua) | 1 |
| Performage Ball Balancer | `92530005` | [Scripts/c92530005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92530005.lua) | 1 |
| Pendulum Witch | `43502497` | [Scripts/c43502497.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43502497.lua) | 1 |
| Shade the Obscure | `77157846` | [Scripts/c77157846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77157846.lua) | 1 |
| Antihuman Intelligence ME-PSY-YA | `58844135` | [Scripts/c58844135.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58844135.lua) | 1 |
| Sweet Dreams, Nemleria | `44843954` | [Scripts/c44843954.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44843954.lua) | 1 |
| Zefraath | `29432356` | [Scripts/c29432356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29432356.lua) | 1 |
| Performapal Odd-Eyes Butler | `56677752` | [Scripts/c56677752.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56677752.lua) | 1 |
| GranSolfachord Musecia | `37972500` | [Scripts/c37972500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37972500.lua) | 1 |
| Dreaming Reality of Nemleria, Realized | `16893370` | [Scripts/c16893370.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16893370.lua) | 1 |
| GranSolfachord Coolia | `84521924` | [Scripts/c84521924.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84521924.lua) | 1 |
| Heavymetalfoes Electrumite | `24094258` | [Scripts/c24094258.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24094258.lua) | 1 |
| Performapal Odd-Eyes Seer | `4836680` | [Scripts/c4836680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4836680.lua) | 1 |
| Majespecter Orthrus - Nue | `66384688` | [Scripts/c66384688.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66384688.lua) | 1 |
| Daidaratant the Ooze Giant | `39943352` | [Scripts/c39943352.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39943352.lua) | 1 |
| Pendulumucho | `18210764` | [Scripts/c18210764.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18210764.lua) | 1 |
| Vaalmonica Invitare | `38491852` | [Scripts/c38491852.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38491852.lua) | 1 |
| Ryu-Ge Rising | `29882827` | [Scripts/c29882827.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29882827.lua) | 1 |
| Solfachord Elegance | `27870337` | [Scripts/c27870337.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27870337.lua) | 2 |
| FaSolfachord Fancia | `54100561` | [Scripts/c54100561.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54100561.lua) | 1 |
| Draco Face-Off | `14733538` | [Scripts/c14733538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14733538.lua) | 1 |
| Archfiend Strategy | `90764871` | [Scripts/c90764871.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90764871.lua) | 1 |
| Abyss Actors Back Stage | `59057953` | [Scripts/c59057953.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59057953.lua) | 1 |
| ...and 1 more |  |  |  |

## Script Examples

### Kewl Tune Crackle (`39576656`)

Source: [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39576656.lua)

```lua
	local dg=g:Filter(aux.NOT(s.retexfilter),nil)
	if #pg>0 then
		Duel.SendtoExtraP(pg,nil,REASON_EFFECT)
	end
	if #dg>0 then
```

### Dreaming Nemleria (`70155677`)

Source: [Scripts/c70155677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70155677.lua)

```lua
	local tc=g:Select(tp,1,1,nil):GetFirst()
	if Duel.MoveToField(tc,tp,tp,LOCATION_SZONE,POS_FACEUP,true) and c:IsRelateToEffect(e) then
		Duel.SendtoExtraP(c,nil,REASON_EFFECT)
	end
end
```

### Performage Ball Balancer (`92530005`)

Source: [Scripts/c92530005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92530005.lua)

```lua
		local g=Duel.SelectMatchingCard(tp,s.schfilter,tp,LOCATION_DECK,0,1,1,nil)
		if g:GetCount()>0 then
			Duel.SendtoExtraP(g,nil,REASON_EFFECT)
		end
	elseif sel==2 then
```
