# Duel.IsPlayerCanRemove

## Signature

```lua
Duel.IsPlayerCanRemove(int player, [Card c], [int reason]) -> bool
```

## Description

With only player, checks whether player is not forbidden from banishing.
With c, checks whether player can banish c for reason; reason defaults to REASON_EFFECT.

## Parameters

- `player` `int`
- `c` `Card` optional
- `reason` `int` optional - default: REASON_EFFECT

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5055`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **32** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.IsPlayerCanRemove) with `Duel.IsPlayerCanRemove`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Clock Lizard | `51476410` | [Scripts/c51476410.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51476410.lua) | 2 |
| Witchcrafter Pittore | `95245544` | [Scripts/c95245544.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95245544.lua) | 1 |
| Silk Bomb Moth | `18300894` | [Scripts/c18300894.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18300894.lua) | 1 |
| Super Koi Koi | `66171432` | [Scripts/c66171432.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66171432.lua) | 2 |
| Gandora-G the Dragon of Destruction | `2333466` | [Scripts/c2333466.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2333466.lua) | 2 |
| Solemn Accusation | `78114463` | [Scripts/c78114463.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78114463.lua) | 2 |
| Kashtira Big Bang | `33925864` | [Scripts/c33925864.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33925864.lua) | 4 |
| Ragnaraika the Evil Seed | `99153051` | [Scripts/c99153051.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c99153051.lua) | 1 |
| Kewl Tune Cue | `16387555` | [Scripts/c16387555.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16387555.lua) | 1 |
| Sacred Scrolls of the Gizmek Legend | `24793135` | [Scripts/c24793135.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24793135.lua) | 2 |
| Axon Kicker Oracle | `33171768` | [Scripts/c33171768.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33171768.lua) | 1 |
| Infernoid Flood | `34446231` | [Scripts/c34446231.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34446231.lua) | 1 |
| Underworld Circle | `73443672` | [Scripts/c73443672.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73443672.lua) | 1 |
| Votis | `75311421` | [Scripts/c75311421.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75311421.lua) | 1 |
| Sacrifice Level-Up | `94185340` | [Scripts/c94185340.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94185340.lua) | 1 |
| Number 95: Galaxy-Eyes Dark Matter Dragon | `58820923` | [Scripts/c58820923.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58820923.lua) | 2 |
| Kashtira Ogre | `94392192` | [Scripts/c94392192.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94392192.lua) | 1 |
| UFOLight | `9275482` | [Scripts/c9275482.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9275482.lua) | 1 |
| Mitsurugi Tempest | `49604192` | [Scripts/c49604192.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49604192.lua) | 2 |
| Psiics, Moonlight of the Ghoti | `26523337` | [Scripts/c26523337.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26523337.lua) | 1 |
| Primite Scream | `27556460` | [Scripts/c27556460.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27556460.lua) | 1 |
| Sauravis, the Ancient and Ascended | `4810828` | [Scripts/c4810828.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4810828.lua) | 1 |
| Ghost Reaper &amp; Winter Cherries | `62015408` | [Scripts/c62015408.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62015408.lua) | 1 |
| Let's Go Together | `38625110` | [Scripts/c38625110.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38625110.lua) | 1 |
| ...and 8 more |  |  |  |

## Script Examples

### Clock Lizard (`51476410`)

Source: [Scripts/c51476410.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51476410.lua)

```lua
function c51476410.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local chkf=PLAYER_NONE
	if chk==0 then return Duel.IsPlayerCanRemove(tp)
		and Duel.IsExistingMatchingCard(c51476410.spfilter3,tp,LOCATION_GRAVE,0,1,nil,e,tp,chkf,e:GetHandler()) end
	Duel.SetOperationInfo(0,CATEGORY_TOEXTRA,nil,1,tp,LOCATION_GRAVE)
```

### Witchcrafter Pittore (`95245544`)

Source: [Scripts/c95245544.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95245544.lua)

```lua
end
function c95245544.drtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanRemove(tp) and Duel.IsPlayerCanDraw(tp,1) end
	Duel.SetTargetPlayer(tp)
	Duel.SetTargetParam(1)
```

### Silk Bomb Moth (`18300894`)

Source: [Scripts/c18300894.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18300894.lua)

```lua
function s.dktg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetFieldGroupCount(tp,0,LOCATION_DECK)>0
		and (Duel.GetLocationCount(tp,LOCATION_SZONE,1-tp,r)>0 or Duel.IsPlayerCanRemove(tp))
	end
	Duel.SetTargetPlayer(tp)
```
