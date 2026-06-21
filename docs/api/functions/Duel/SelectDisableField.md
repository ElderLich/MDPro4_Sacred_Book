# Duel.SelectDisableField

## Signature

```lua
Duel.SelectDisableField(int player, int count, int s, int o, int filter) -> int
```

## Description

Let the player player select the specified position to meet the marker condition filter count of the available space, and return to select the location of the marker
Commonly used to select areas can not use or move the monster grid
0: 16) + (l \[i\] == LOCATION_MZONE? 0: 8)) ## flag|= 1 &lt;&lt; (seq \[i\] + (p \[i\] == player?

## Parameters

- `player` `int`
- `count` `int`
- `s` `int`
- `o` `int`
- `filter` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5028`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **50** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.SelectDisableField`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Vaylantz Genesis Grand Duke | `76075139` | [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76075139.lua) | 60 |
| Arktos XII - Chronochasm Vaylantz | `50687050` | [Scripts/c50687050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50687050.lua) | 56 |
| Mamonaka the Vaylantz United | `40680521` | [Scripts/c40680521.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40680521.lua) | 53 |
| S-Force Justify | `35334193` | [Scripts/c35334193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35334193.lua) | 51 |
| Sprind the Irondash Dragon | `1906812` | [Scripts/c1906812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1906812.lua) | 48 |
| Parallel Panzer | `93394164` | [Scripts/c93394164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93394164.lua) | 46 |
| R.B. VALCan Booster | `6821579` | [Scripts/c6821579.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6821579.lua) | 45 |
| Dark Infant @Ignister | `74567889` | [Scripts/c74567889.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74567889.lua) | 45 |
| Seismic Shockwave | `79569173` | [Scripts/c79569173.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79569173.lua) | 42 |
| S-Force Sorted World | `11642993` | [Scripts/c11642993.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11642993.lua) | 40 |
| Kashtira Shangri-Ira | `73542331` | [Scripts/c73542331.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73542331.lua) | 39 |
| Elfnotes: Aristeia of Trust | `50590801` | [Scripts/c50590801.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50590801.lua) | 39 |
| Crusadia Spatha | `39528955` | [Scripts/c39528955.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39528955.lua) | 39 |
| Codebreaker Virus Swordsman | `84121193` | [Scripts/c84121193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84121193.lua) | 38 |
| S-Force Mystify | `4611341` | [Scripts/c4611341.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4611341.lua) | 38 |
| Boompoline!! | `14839621` | [Scripts/c14839621.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14839621.lua) | 38 |
| S-Force Specimen | `82977464` | [Scripts/c82977464.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82977464.lua) | 37 |
| Spring | `60600821` | [Scripts/c60600821.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60600821.lua) | 36 |
| Procession of the Tea Jar | `12612470` | [Scripts/c12612470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12612470.lua) | 36 |
| Aeropixthree | `83094004` | [Scripts/c83094004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83094004.lua) | 36 |
| World Legacy Guardragon | `87571563` | [Scripts/c87571563.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87571563.lua) | 36 |
| Goldilocks the Battle Landscaper | `24521754` | [Scripts/c24521754.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24521754.lua) | 35 |
| Appliancer Electrilyrical World | `3875465` | [Scripts/c3875465.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3875465.lua) | 35 |
| Gouki The Solid Ogre | `22510667` | [Scripts/c22510667.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22510667.lua) | 35 |
| ...and 26 more |  |  |  |

## Script Examples

### Vaylantz Genesis Grand Duke (`76075139`)

Source: [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76075139.lua)

```lua
			if flag==0 then return end
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOZONE)
			local s=Duel.SelectDisableField(tp,1,LOCATION_MZONE,0,~flag)
			local nseq=math.log(s,2)
			Duel.MoveSequence(sc,nseq)
```

### Arktos XII - Chronochasm Vaylantz (`50687050`)

Source: [Scripts/c50687050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50687050.lua)

```lua
			if flag==0 then return end
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOZONE)
			local s=Duel.SelectDisableField(tp,1,LOCATION_MZONE,0,~flag)
			local nseq=math.log(s,2)
			Duel.HintSelection(sg)
```

### Mamonaka the Vaylantz United (`40680521`)

Source: [Scripts/c40680521.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40680521.lua)

```lua
			if flag==0 then return end
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOZONE)
			local s=Duel.SelectDisableField(tp,1,LOCATION_MZONE,0,~flag)
			local nseq=math.log(s,2)
			Duel.MoveSequence(sc,nseq)
```
