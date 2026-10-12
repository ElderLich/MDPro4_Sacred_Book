# Duel.GetLinkedGroup

## Signature

```lua
Duel.GetLinkedGroup(int player, int s, int o) -> Group|nil
```

## Description

Returns a Group of cards in player-relative locations s and o that are linked.
Use the Card.GetLinkedGroup method when checking one Link Monster; use this Duel helper for field-wide location-mask checks.

## Parameters

- `player` `int` - Perspective player.
- `s` `int` - Location mask on player's side.
- `o` `int` - Location mask on the opponent's side from player's perspective.

## Returns

- `Group|nil` - Linked cards, or nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4940`

## Guided Examples

Learn how to use this function in context:

- [Link Procedure Guide](/learn/link-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetLinkedGroup) with `Duel.GetLinkedGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Borrelcode Dragon | `67288539` | [Scripts/c67288539.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67288539.lua) | 2 |
| Pitknight Filly | `25919316` | [Scripts/c25919316.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25919316.lua) | 2 |
| Crusadia Draco | `54525057` | [Scripts/c54525057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54525057.lua) | 2 |
| Crusadia Reclusia | `55241609` | [Scripts/c55241609.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55241609.lua) | 2 |
| Voltester | `18585765` | [Scripts/c18585765.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18585765.lua) | 2 |
| Crusadia Krawler | `55838342` | [Scripts/c55838342.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55838342.lua) | 2 |

## Script Examples

### Borrelcode Dragon (`67288539`)

Source: [Scripts/c67288539.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67288539.lua)

```lua
function c67288539.immcon(e)
	local tp=e:GetHandlerPlayer()
	local lg1=Duel.GetLinkedGroup(tp,1,1)
	local lg2=Duel.GetLinkedGroup(1-tp,1,1)
	lg1:Merge(lg2)
```

### Pitknight Filly (`25919316`)

Source: [Scripts/c25919316.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25919316.lua)

```lua
end
function s.atkcon(e,tp,eg,ep,ev,re,r,rp)
	local lg1=Duel.GetLinkedGroup(tp,1,1)
	local lg2=Duel.GetLinkedGroup(1-tp,1,1)
	lg1:Merge(lg2)
```

### Crusadia Draco (`54525057`)

Source: [Scripts/c54525057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54525057.lua)

```lua
end
function c54525057.thcon(e,tp,eg,ep,ev,re,r,rp)
	local lg1=Duel.GetLinkedGroup(tp,1,1)
	local lg2=Duel.GetLinkedGroup(1-tp,1,1)
	lg1:Merge(lg2)
```
