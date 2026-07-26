# Card.IsPreviousSetCard

## Signature

```lua
Card.IsPreviousSetCard(Card c, int setcode1, [int setcode2], [... int]) -> bool
```

## Description

Checks whether c's previous card-code or added previous set-code data matches any supplied setcode value.
Nil setcode arguments are skipped. This uses the previous state recorded before the last relevant field or position update, not c's current Set membership.

## Parameters

- `c` `Card`
- `setcode1` `int`
- `setcode2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3398`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **76** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsPreviousSetCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [D/D/D/D Super-Dimensional Sovereign Emperor Zero Paradox](/examples/cards/97417863) | `97417863` | [Scripts/c97417863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97417863.lua) | 1 |
| Fossil Fusion | `59419719` | [Scripts/c59419719.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59419719.lua) | 1 |
| Ursarctic Quint Charge | `15758127` | [Scripts/c15758127.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15758127.lua) | 1 |
| Gem-Knight Master Diamond Dispersion | `25342956` | [Scripts/c25342956.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25342956.lua) | 1 |
| Gunkan Sushipyard Seaside Supper Spot | `62200831` | [Scripts/c62200831.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62200831.lua) | 1 |
| Unification of the Cubic Lords | `34325937` | [Scripts/c34325937.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34325937.lua) | 1 |
| Salamangreat Zebroid X | `44161893` | [Scripts/c44161893.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44161893.lua) | 1 |
| Ultimate Crystal Magic | `36328300` | [Scripts/c36328300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36328300.lua) | 2 |
| PSY-Frame Accelerator | `51053997` | [Scripts/c51053997.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51053997.lua) | 1 |
| Evil HERO Inferno Wing - Backfire | `59893882` | [Scripts/c59893882.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59893882.lua) | 1 |
| Nerva the Power Patron of Creation | `53589300` | [Scripts/c53589300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53589300.lua) | 1 |
| Battle Shogun of the Six Samurai | `74752631` | [Scripts/c74752631.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74752631.lua) | 1 |
| Fandora, the Flying Fighting Furtress | `26162470` | [Scripts/c26162470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26162470.lua) | 1 |
| Mementotlan Akihiron | `54207171` | [Scripts/c54207171.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54207171.lua) | 1 |
| Xtra HERO Wonder Driver | `1948619` | [Scripts/c1948619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1948619.lua) | 1 |
| Draco Awakening | `66092596` | [Scripts/c66092596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66092596.lua) | 1 |
| Sunvine Thrasher | `91557476` | [Scripts/c91557476.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91557476.lua) | 1 |
| D/D/D Zero Doom Queen Machinex | `20715411` | [Scripts/c20715411.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20715411.lua) | 1 |
| Parametalfoes Azortless | `37491810` | [Scripts/c37491810.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37491810.lua) | 1 |
| Icejade Manifestation | `72776252` | [Scripts/c72776252.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72776252.lua) | 1 |
| Alviss of the Nordic Alfar | `27024795` | [Scripts/c27024795.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27024795.lua) | 1 |
| Centur-Ion Primera Primus | `8841431` | [Scripts/c8841431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8841431.lua) | 1 |
| Mythical Institution | `94599451` | [Scripts/c94599451.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94599451.lua) | 1 |
| Kuribah | `44632120` | [Scripts/c44632120.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44632120.lua) | 1 |
| ...and 52 more |  |  |  |

## Script Examples

### D/D/D/D Super-Dimensional Sovereign Emperor Zero Paradox (`97417863`)

Source: [Scripts/c97417863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97417863.lua)

```lua
function c97417863.lefilter(c,tp,re)
	return re and re:IsActiveType(TYPE_SPELL) and c:IsReason(REASON_EFFECT)
		and c:IsPreviousControler(tp) and c:IsPreviousPosition(POS_FACEUP) and c:IsPreviousSetCard(0x10af)
end
function c97417863.atkcon(e,tp,eg,ep,ev,re,r,rp)
```

### Fossil Fusion (`59419719`)

Source: [Scripts/c59419719.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59419719.lua)

```lua
end
function c59419719.cfilter(c,tp)
	return c:IsPreviousSetCard(0x149) and c:GetPreviousTypeOnField()&TYPE_FUSION~=0
		and c:IsReason(REASON_BATTLE+REASON_EFFECT) and c:IsPreviousControler(tp) and c:IsPreviousLocation(LOCATION_MZONE)
end
```

### Ursarctic Quint Charge (`15758127`)

Source: [Scripts/c15758127.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15758127.lua)

```lua
end
function c15758127.cfilter(c,tp)
	return c:IsPreviousSetCard(0x163) and c:IsPreviousPosition(POS_FACEUP) and c:GetPreviousTypeOnField()&TYPE_SYNCHRO~=0 and c:GetPreviousControler()==tp
end
function c15758127.tdcon(e,tp,eg,ep,ev,re,r,rp)
```
