# Auxiliary.UseExtraReleaseCount

## Signature

```lua
Auxiliary.UseExtraReleaseCount(Group g, int tp) -> void
```

## Description

Consumes count limits for opponent's cards in g that were released through EFFECT_EXTRA_RELEASE_NONSUM, such as Lair of Darkness-style release effects not selected by Duel.SelectReleaseGroup.

## Parameters

- `g` `Group`
- `tp` `int`

## Source

- `Utilities/utility.lua:1508`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **53** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.UseExtraReleaseCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27693363.lua) | 65 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62714453.lua) | 62 |
| Frightfur Meister | `77522571` | [Scripts/c77522571.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77522571.lua) | 59 |
| Mecha Phantom Beast Auroradon | `44097050` | [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44097050.lua) | 58 |
| Ursarctic Grand Chariot | `80086070` | [Scripts/c80086070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80086070.lua) | 57 |
| Kuribeh | `34419588` | [Scripts/c34419588.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34419588.lua) | 57 |
| Theia, the Primal Being | `85687952` | [Scripts/c85687952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85687952.lua) | 56 |
| Token Support | `53545926` | [Scripts/c53545926.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53545926.lua) | 51 |
| Dawn Angel Kambi | `12500059` | [Scripts/c12500059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12500059.lua) | 51 |
| Hrimnir the Divine Follower | `49904658` | [Scripts/c49904658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49904658.lua) | 51 |
| Supreme King Dragon Odd-Eyes | `96733134` | [Scripts/c96733134.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96733134.lua) | 50 |
| Blaze Cannon | `4059313` | [Scripts/c4059313.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4059313.lua) | 49 |
| Shooting Star Dragon T.G. EX | `63180841` | [Scripts/c63180841.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63180841.lua) | 49 |
| Vampire Voivode | `4918855` | [Scripts/c4918855.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4918855.lua) | 49 |
| Winds Over the Ice Barrier | `17197110` | [Scripts/c17197110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17197110.lua) | 49 |
| Rasterliger | `88000953` | [Scripts/c88000953.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88000953.lua) | 49 |
| Duke Shade, the Sinister Shadow Lord | `12766474` | [Scripts/c12766474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12766474.lua) | 48 |
| Master of Chaos | `85059922` | [Scripts/c85059922.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85059922.lua) | 48 |
| Generaider Boss Bite | `720147` | [Scripts/c720147.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c720147.lua) | 47 |
| Aron, the Ogdoadic King | `34172284` | [Scripts/c34172284.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34172284.lua) | 45 |
| Kuribah | `44632120` | [Scripts/c44632120.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44632120.lua) | 45 |
| Amunessia, the Ogdoadic Queen | `61160289` | [Scripts/c61160289.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61160289.lua) | 44 |
| Citadel Whale | `46290741` | [Scripts/c46290741.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46290741.lua) | 44 |
| Trias Hierarchia | `26866984` | [Scripts/c26866984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26866984.lua) | 44 |
| ...and 29 more |  |  |  |

## Script Examples

### Ursarctic Polari (`27693363`)

Source: [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27693363.lua)

```lua
		Duel.Remove(tc,POS_FACEUP,REASON_EFFECT+REASON_REPLACE)
	else
		aux.UseExtraReleaseCount(rg,tp)
		Duel.Release(tc,REASON_COST)
	end
```

### Ursarctic Polar Star (`62714453`)

Source: [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62714453.lua)

```lua
	else
		rg:AddCard(c)
		aux.UseExtraReleaseCount(rg,tp)
		Duel.Release(rg,REASON_COST)
	end
```

### Frightfur Meister (`77522571`)

Source: [Scripts/c77522571.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77522571.lua)

```lua
	local lv=g:GetSum(Card.GetLevel)
	e:SetLabel(lv)
	aux.UseExtraReleaseCount(g,tp)
	Duel.Release(g,REASON_COST)
end
```
