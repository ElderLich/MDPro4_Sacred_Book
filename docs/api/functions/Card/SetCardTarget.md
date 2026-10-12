# Card.SetCardTarget

## Signature

```lua
Card.SetCardTarget(Card c1, Card c2) -> void
```

## Description

Registers c2 as a persistent card target of c1.
This stores a card-target relation used by functions such as Card.GetCardTarget and by related-card disable checks; it is separate from Duel.SelectTarget's Chain target list.

## Parameters

- `c1` `Card`
- `c2` `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3591`

## Guided Examples

Learn how to use this function in context:

- [Normal And Continuous Traps](/learn/normal-and-continuous-traps)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **121** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.SetCardTarget) with `Card.SetCardTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Future Fusion Nova](/examples/cards/92058902) | `92058902` | [Scripts/c92058902.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92058902.lua) | 2 |
| Trickstar Light Stage | `35371948` | [Scripts/c35371948.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35371948.lua) | 1 |
| Trickstar Light Arena | `63492244` | [Scripts/c63492244.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63492244.lua) | 1 |
| Future Fusion | `77565204` | [Scripts/c77565204.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77565204.lua) | 1 |
| Red Dragon Archfiend's Chains | `92936364` | [Scripts/c92936364.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92936364.lua) | 1 |
| Cubic Mandala | `8837932` | [Scripts/c8837932.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8837932.lua) | 1 |
| Goblin Freefall Squad | `85123771` | [Scripts/c85123771.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85123771.lua) | 1 |
| Zero Extra Link | `60162470` | [Scripts/c60162470.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60162470.lua) | 1 |
| Gladiator Beast Darius | `25924653` | [Scripts/c25924653.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25924653.lua) | 1 |
| Marincess Sleepy Maiden | `57541158` | [Scripts/c57541158.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57541158.lua) | 1 |
| Phantom Knights' Sword | `61936647` | [Scripts/c61936647.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61936647.lua) | 1 |
| Earthbound Prison | `71089030` | [Scripts/c71089030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71089030.lua) | 1 |
| Ninjitsu Art of Shadow Sealing | `13629812` | [Scripts/c13629812.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13629812.lua) | 1 |
| Ninjitsu Art of Dancing Leaves | `68038375` | [Scripts/c68038375.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c68038375.lua) | 1 |
| Prevention Star | `94303232` | [Scripts/c94303232.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94303232.lua) | 1 |
| Ninjitsu Art of Duplication | `50766506` | [Scripts/c50766506.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50766506.lua) | 1 |
| Portable Battery Pack | `61840587` | [Scripts/c61840587.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61840587.lua) | 1 |
| Performapal Changeraffe | `69228245` | [Scripts/c69228245.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69228245.lua) | 1 |
| Phantom Knights' Fog Blade | `25542642` | [Scripts/c25542642.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25542642.lua) | 1 |
| Battle Royal Mode - Joining | `65433790` | [Scripts/c65433790.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65433790.lua) | 1 |
| Dimension Mirage | `80560728` | [Scripts/c80560728.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80560728.lua) | 1 |
| Number 45: Crumble Logos the Prophet of Demolition | `29208536` | [Scripts/c29208536.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29208536.lua) | 1 |
| World Legacy's Secret | `98935722` | [Scripts/c98935722.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98935722.lua) | 1 |
| Dimension Sphinx | `17787975` | [Scripts/c17787975.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17787975.lua) | 1 |
| ...and 97 more |  |  |  |

## Script Examples

### Future Fusion Nova (`92058902`)

Source: [Scripts/c92058902.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92058902.lua)

```lua
		aux.FCheckAdditional=nil
		tc:CompleteProcedure()
		c:SetCardTarget(tc)
		fid=c:GetFieldID()
		tc:RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,0,1,fid)
```

### Trickstar Light Stage (`35371948`)

Source: [Scripts/c35371948.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35371948.lua)

```lua
	local cid=Duel.GetChainInfo(0,CHAININFO_CHAIN_ID)
	if c:IsRelateToEffect(e) and tc:IsFacedown() and tc:IsRelateToEffect(e) and tc:GetFlagEffectLabel(35371949)==cid then
		c:SetCardTarget(tc)
		e:SetLabelObject(tc)
		c:ResetFlagEffect(35371948)
```

### Trickstar Light Arena (`63492244`)

Source: [Scripts/c63492244.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63492244.lua)

```lua
	local cid=Duel.GetChainInfo(0,CHAININFO_CHAIN_ID)
	if c:IsRelateToEffect(e) and tc:IsFacedown() and tc:IsRelateToEffect(e) and tc:GetFlagEffectLabel(63492245)==cid then
		c:SetCardTarget(tc)
		e:SetLabelObject(tc)
		c:ResetFlagEffect(63492244)
```
