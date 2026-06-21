# Card.GetTextAttack

## Signature

```lua
Card.GetTextAttack(Card c) -> int
```

## Description

Returns the attack power recorded on card c

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3442`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **105** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetTextAttack`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua) | 59 |
| Meklord Astro Mekanikle | `63468625` | [Scripts/c63468625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63468625.lua) | 57 |
| Spirit Poacher | `85150300` | [Scripts/c85150300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85150300.lua) | 54 |
| Raidraptor - Rising Rebellion Falcon | `71222868` | [Scripts/c71222868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71222868.lua) | 52 |
| Super Armored Robot Armed Black Iron "C" | `77754169` | [Scripts/c77754169.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77754169.lua) | 52 |
| Cynet Backdoor | `43839002` | [Scripts/c43839002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43839002.lua) | 52 |
| Allure Queen LV5 | `23756165` | [Scripts/c23756165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23756165.lua) | 51 |
| Tragic Twin Twined Jewels | `81143465` | [Scripts/c81143465.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81143465.lua) | 51 |
| Meklord Astro Dragon Triskelion | `4837861` | [Scripts/c4837861.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4837861.lua) | 51 |
| Meklord Emperor Granel | `4545683` | [Scripts/c4545683.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4545683.lua) | 50 |
| CXyz Gimmick Puppet Fanatix Machinix | `3685372` | [Scripts/c3685372.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3685372.lua) | 50 |
| Crossmind Archfiend | `52644170` | [Scripts/c52644170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52644170.lua) | 50 |
| Blaze Cannon | `4059313` | [Scripts/c4059313.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4059313.lua) | 49 |
| Maiden of Blue Tears | `99176254` | [Scripts/c99176254.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99176254.lua) | 49 |
| Meklord Emperor Skiel | `31930787` | [Scripts/c31930787.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31930787.lua) | 48 |
| Nightmare-Eyes Restrict | `30138615` | [Scripts/c30138615.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30138615.lua) | 48 |
| Ebon Sun | `96029570` | [Scripts/c96029570.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96029570.lua) | 48 |
| Crystal Clear Wing Synchro Dragon | `59765225` | [Scripts/c59765225.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59765225.lua) | 47 |
| Meklord Emperor Wisel | `68140974` | [Scripts/c68140974.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68140974.lua) | 47 |
| Gizmek Okami, the Dreaded Deluge Dragon | `43218406` | [Scripts/c43218406.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43218406.lua) | 47 |
| Nibiru, the Primal Being | `27204311` | [Scripts/c27204311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27204311.lua) | 47 |
| Loud Cloud the Storm Serpent | `61465001` | [Scripts/c61465001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61465001.lua) | 46 |
| R.B. Last Stand | `43450363` | [Scripts/c43450363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43450363.lua) | 46 |
| The Atmosphere | `14466224` | [Scripts/c14466224.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14466224.lua) | 46 |
| ...and 81 more |  |  |  |

## Script Examples

### Duel Link Dragon, the Duel Dragon (`60025883`)

Source: [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua)

```lua
	local zone=bit.band(c:GetLinkedZone(tp),0x1f)
	local tc=e:GetLabelObject()
	local atk=tc:GetTextAttack()
	local def=tc:GetTextDefense()
	local lv=tc:GetOriginalLevel()
```

### Meklord Astro Mekanikle (`63468625`)

Source: [Scripts/c63468625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63468625.lua)

```lua
	local tc=Duel.GetFirstTarget()
	if tc:IsFaceup() and tc:IsRelateToEffect(e) and tc:IsType(TYPE_MONSTER) then
		local atk=tc:GetTextAttack()
		if atk<0 then atk=0 end
		if not Duel.Equip(tp,tc,c,false) then return end
```

### Spirit Poacher (`85150300`)

Source: [Scripts/c85150300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85150300.lua)

```lua
function s.sfilter(c,e,tp)
	return c:GetOriginalType()&TYPE_MONSTER>0 and c:IsFaceup() and c:IsCanBeSpecialSummoned(e,0,1-tp,false,false,POS_FACEUP,1-tp)
		and Duel.GetLP(1-tp)>=c:GetBaseAttack() and c:GetTextAttack()>=0
end
function s.settg(e,tp,eg,ep,ev,re,r,rp,chk)
```
