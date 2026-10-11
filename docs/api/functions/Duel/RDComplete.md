# Duel.RDComplete

## Signature

```lua
Duel.RDComplete() -> void
```

## Description

Completes reserved step damage/recover processing after Duel.Damage or Duel.Recover is called with is_step=true.
Call this once after all stepped LP changes in the batch have been queued.

## How To Use It

Use this after one or more stepped `Duel.Damage` or `Duel.Recover` calls.

```lua
Duel.Damage(tp,500,REASON_EFFECT,true)
Duel.Damage(1-tp,500,REASON_EFFECT,true)
Duel.RDComplete()
```

Without this call, the reserved damage/recovery batch is not completed. Use ordinary sequential calls, often separated by `Duel.BreakEffect()`, when the card text wants one action and then another.

## Related Functions

- [Duel.Damage](/api/functions/Duel/Damage)
- [Duel.Recover](/api/functions/Duel/Recover)

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4903`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **43** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.RDComplete) with `Duel.RDComplete`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Crimson Nova the Dark Cubic Lord | `30270176` | [Scripts/c30270176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30270176.lua) | 1 |
| Aiza the Dragoness of Deranged Devotion | `63378869` | [Scripts/c63378869.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63378869.lua) | 1 |
| Superheavy Samurai Soulbang Cannon | `3064425` | [Scripts/c3064425.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3064425.lua) | 1 |
| Meklord Astro Dragon Asterisk | `38522377` | [Scripts/c38522377.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38522377.lua) | 1 |
| Earthbound Resonance | `95207988` | [Scripts/c95207988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95207988.lua) | 1 |
| Neos Wiseman | `5126490` | [Scripts/c5126490.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5126490.lua) | 1 |
| Yubel - The Loving Defender Forever | `47172959` | [Scripts/c47172959.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47172959.lua) | 1 |
| Pyrorex the Elemental Lord | `35842855` | [Scripts/c35842855.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35842855.lua) | 1 |
| TA.I. Strike | `86449372` | [Scripts/c86449372.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86449372.lua) | 1 |
| Exploderokket Dragon | `31353051` | [Scripts/c31353051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31353051.lua) | 1 |
| Seventh Barian's | `39513225` | [Scripts/c39513225.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39513225.lua) | 1 |
| Hyper Psychic Blaster/Assault Mode | `37169670` | [Scripts/c37169670.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37169670.lua) | 1 |
| Fusion Fright Waltz | `34449261` | [Scripts/c34449261.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34449261.lua) | 1 |
| Pair Bear Scare!! | `21501961` | [Scripts/c21501961.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21501961.lua) | 1 |
| Destiny HERO - Dynatag | `37780349` | [Scripts/c37780349.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37780349.lua) | 1 |
| Performage Flame Eater | `4807253` | [Scripts/c4807253.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4807253.lua) | 1 |
| Capacitor Stalker | `29716911` | [Scripts/c29716911.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29716911.lua) | 1 |
| The Big Saturn | `34004470` | [Scripts/c34004470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34004470.lua) | 1 |
| Sorcerer of Sebek | `39767432` | [Scripts/c39767432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39767432.lua) | 1 |
| Saber Reflection | `35037880` | [Scripts/c35037880.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35037880.lua) | 1 |
| Red-Eyes Burn | `71782404` | [Scripts/c71782404.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71782404.lua) | 1 |
| Chthonian Blast | `18271561` | [Scripts/c18271561.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18271561.lua) | 1 |
| Photon Alexandra Queen | `75797046` | [Scripts/c75797046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75797046.lua) | 1 |
| Koa'ki Ring | `46089249` | [Scripts/c46089249.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46089249.lua) | 1 |
| ...and 19 more |  |  |  |

## Script Examples

### Crimson Nova the Dark Cubic Lord (`30270176`)

Source: [Scripts/c30270176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30270176.lua)

```lua
	Duel.Damage(tp,3000,REASON_EFFECT,true)
	Duel.Damage(1-tp,3000,REASON_EFFECT,true)
	Duel.RDComplete()
end
```

### Aiza the Dragoness of Deranged Devotion (`63378869`)

Source: [Scripts/c63378869.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63378869.lua)

```lua
		Duel.Damage(1-tp,bc:GetTextAttack(),REASON_EFFECT,true)
		Duel.Damage(tp,bc:GetTextAttack(),REASON_EFFECT,true)
		Duel.RDComplete()
	end
	local fid=e:GetHandler():GetFieldID()
```

### Superheavy Samurai Soulbang Cannon (`3064425`)

Source: [Scripts/c3064425.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3064425.lua)

```lua
		Duel.Damage(tp,1000,REASON_EFFECT,true)
		Duel.Damage(1-tp,1000,REASON_EFFECT,true)
		Duel.RDComplete()
	end
end
```
