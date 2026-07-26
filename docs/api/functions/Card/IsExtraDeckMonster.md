# Card.IsExtraDeckMonster

## Signature

```lua
Card.IsExtraDeckMonster(Card c) -> bool
```

## Description

Checks whether c is a card kind treated by the core as an Extra Deck monster.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3501`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **16** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsExtraDeckMonster`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [GMX Associate Noma](/examples/cards/83528184) | `83528184` | [Scripts/c83528184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83528184.lua) | 1 |
| Deep Sea Minstrel | `71978434` | [Scripts/c71978434.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71978434.lua) | 1 |
| Thunder Dragonduo | `55591586` | [Scripts/c55591586.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55591586.lua) | 1 |
| Thunder Dragon Thunderstormech | `12081875` | [Scripts/c12081875.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12081875.lua) | 1 |
| Majestic Star Dragon | `7841112` | [Scripts/c7841112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7841112.lua) | 1 |
| Gold Pride - Nytro Blaster | `58884063` | [Scripts/c58884063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58884063.lua) | 1 |
| Alsei, the Sylvan High Protector | `10406322` | [Scripts/c10406322.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10406322.lua) | 1 |
| Gold Pride - Star Leon | `22390469` | [Scripts/c22390469.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22390469.lua) | 1 |
| Majestic Red Dragon | `67030233` | [Scripts/c67030233.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67030233.lua) | 1 |
| Gold Pride - Eradicator | `45464587` | [Scripts/c45464587.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45464587.lua) | 1 |
| Lightray Diabolos | `30126992` | [Scripts/c30126992.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30126992.lua) | 1 |
| Red Dragon Ninja | `58165765` | [Scripts/c58165765.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58165765.lua) | 1 |
| Trickstar Bouquet | `99890852` | [Scripts/c99890852.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99890852.lua) | 1 |
| Sylvan Blessing | `91650245` | [Scripts/c91650245.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91650245.lua) | 1 |
| Abyss Warrior | `88409165` | [Scripts/c88409165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88409165.lua) | 1 |
| Wattsychic Fighter | `81028112` | [Scripts/c81028112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81028112.lua) | 1 |

## Script Examples

### GMX Associate Noma (`83528184`)

Source: [Scripts/c83528184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83528184.lua)

```lua
	if tg:GetCount()>0 then
		for tc in aux.Next(tg) do
			if tc:IsExtraDeckMonster()
				or Duel.SelectOption(tp,aux.Stringid(id,2),aux.Stringid(id,3))==0 then
				Duel.SendtoDeck(tc,nil,SEQ_DECKTOP,REASON_EFFECT)
```

### Deep Sea Minstrel (`71978434`)

Source: [Scripts/c71978434.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71978434.lua)

```lua
	local tc=Duel.GetFirstTarget()
	if tc:IsRelateToEffect(e) then
		if tc:IsExtraDeckMonster()
			or Duel.SelectOption(tp,aux.Stringid(71978434,2),aux.Stringid(71978434,3))==0 then
			Duel.SendtoDeck(tc,nil,SEQ_DECKTOP,REASON_EFFECT)
```

### Thunder Dragonduo (`55591586`)

Source: [Scripts/c55591586.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55591586.lua)

```lua
	local tc=Duel.GetFirstTarget()
	if tc:IsRelateToEffect(e) then
		if tc:IsExtraDeckMonster()
			or Duel.SelectOption(tp,aux.Stringid(55591586,4),aux.Stringid(55591586,5))==0 then
			Duel.SendtoDeck(tc,nil,SEQ_DECKTOP,REASON_EFFECT)
```
