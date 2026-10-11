# Card.SetUniqueOnField

## Signature

```lua
Card.SetUniqueOnField(Card c, int s, int o, function|int unique_code, [int unique_location]) -> void
```

## Description

Sets a uniqueness rule for c so only one card with unique_code can exist on the checked field, Monster Zone, or Spell & Trap Zone range.

## Parameters

- `c` `Card`
- `s` `int`
- `o` `int`
- `unique_code` `function|int`
- `unique_location` `int` optional - default: LOCATIOIN_ONFIELD

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3712`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **164** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.SetUniqueOnField) with `Card.SetUniqueOnField`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| D/D/D Deviser King Deus Machinex | `46593546` | [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46593546.lua) | 1 |
| Worldsea Dragon Zealantis | `45112597` | [Scripts/c45112597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45112597.lua) | 1 |
| Don Thousand's Throne | `93238626` | [Scripts/c93238626.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93238626.lua) | 1 |
| Mirrorjade the Iceblade Dragon | `44146295` | [Scripts/c44146295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44146295.lua) | 1 |
| Laevatein, Generaider Boss of Shadows | `74615388` | [Scripts/c74615388.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74615388.lua) | 1 |
| Ryu-Ge Realm - Sea Spires | `28669235` | [Scripts/c28669235.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28669235.lua) | 1 |
| Ryu-Ge Realm - Wyrm Winds | `55154344` | [Scripts/c55154344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55154344.lua) | 1 |
| Cosmic Tree Irmistil | `74139959` | [Scripts/c74139959.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74139959.lua) | 1 |
| Necroquip Princess | `93860227` | [Scripts/c93860227.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93860227.lua) | 1 |
| Bujintei Tsukuyomi | `73289035` | [Scripts/c73289035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73289035.lua) | 1 |
| Tsuchigumo, the Poisonous Mayakashi | `77092311` | [Scripts/c77092311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77092311.lua) | 1 |
| Tengu, the Winged Mayakashi | `4103668` | [Scripts/c4103668.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4103668.lua) | 1 |
| Jizukiru, the Star Destroying Kaiju | `63941210` | [Scripts/c63941210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63941210.lua) | 1 |
| Loptr, Shadow of the Generaider Bosses | `94183877` | [Scripts/c94183877.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94183877.lua) | 1 |
| Oboro-Guruma, the Wheeled Mayakashi | `30607616` | [Scripts/c30607616.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30607616.lua) | 1 |
| Malefic Truth Dragon | `37115575` | [Scripts/c37115575.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37115575.lua) | 1 |
| Gashadokuro, the Skeletal Mayakashi | `39475024` | [Scripts/c39475024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39475024.lua) | 1 |
| Kumongous, the Sticky String Kaiju | `29726552` | [Scripts/c29726552.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29726552.lua) | 1 |
| Yoko, the Graceful Mayakashi | `3486020` | [Scripts/c3486020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3486020.lua) | 1 |
| Ryu-Ge Realm - Dino Domains | `82661630` | [Scripts/c82661630.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82661630.lua) | 1 |
| Gadarla, the Mystery Dust Kaiju | `36956512` | [Scripts/c36956512.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36956512.lua) | 1 |
| Yuki-Onna, the Icicle Mayakashi | `36114945` | [Scripts/c36114945.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36114945.lua) | 1 |
| Jormungandr, Generaider Boss of Eternity | `2665273` | [Scripts/c2665273.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2665273.lua) | 1 |
| Super Anti-Kaiju War Machine Mecha-Dogoran | `84769941` | [Scripts/c84769941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84769941.lua) | 1 |
| ...and 140 more |  |  |  |

## Script Examples

### D/D/D Deviser King Deus Machinex (`46593546`)

Source: [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46593546.lua)

```lua
	--pendulum summon
	aux.EnablePendulumAttribute(c,false)
	c:SetUniqueOnField(1,0,46593546,LOCATION_MZONE)
	--special summon
	local e1=Effect.CreateEffect(c)
```

### Worldsea Dragon Zealantis (`45112597`)

Source: [Scripts/c45112597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45112597.lua)

```lua
--世海龍ジーランティス
function c45112597.initial_effect(c)
	c:SetUniqueOnField(1,0,45112597)
	--link summon
	aux.AddLinkProcedure(c,aux.FilterBoolFunction(Card.IsLinkType,TYPE_EFFECT),1)
```

### Don Thousand's Throne (`93238626`)

Source: [Scripts/c93238626.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93238626.lua)

```lua
--ドン・サウザンドの玉座
function c93238626.initial_effect(c)
	c:SetUniqueOnField(1,0,93238626)
	--activate
	local e1=Effect.CreateEffect(c)
```
