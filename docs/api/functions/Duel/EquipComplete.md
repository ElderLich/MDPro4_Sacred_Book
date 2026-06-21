# Duel.EquipComplete

## Signature

```lua
Duel.EquipComplete() -> void
```

## Description

In the call Duel.Equip, if is_step parameter is true, you need to call this function when the trigger point

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4905`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **19** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.EquipComplete`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Shining Draw](/examples/cards/35906693) | `35906693` | [Scripts/c35906693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35906693.lua) | 63 |
| Power Tool Braver Dragon | `63265554` | [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63265554.lua) | 58 |
| Dragunity Arma Gram | `53184342` | [Scripts/c53184342.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53184342.lua) | 54 |
| Sea Lancer | `22842214` | [Scripts/c22842214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22842214.lua) | 53 |
| Super Armored Robot Armed Black Iron "C" | `77754169` | [Scripts/c77754169.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77754169.lua) | 52 |
| Sacred Noble Knight of King Artorigus | `10613952` | [Scripts/c10613952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10613952.lua) | 48 |
| Therion Irregular | `75290703` | [Scripts/c75290703.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75290703.lua) | 48 |
| Metalhold the Moving Blockade | `42237854` | [Scripts/c42237854.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42237854.lua) | 46 |
| Jupiter the Power Patron of Destruction | `68231287` | [Scripts/c68231287.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68231287.lua) | 46 |
| Arsenal Audit | `49652661` | [Scripts/c49652661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49652661.lua) | 46 |
| Gold Pride - Pin Baller | `28497830` | [Scripts/c28497830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28497830.lua) | 45 |
| Artorigus, King of the Noble Knights | `21223277` | [Scripts/c21223277.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21223277.lua) | 45 |
| Boot-Up Corporal - Command Dynamo | `938717` | [Scripts/c938717.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c938717.lua) | 43 |
| Marincess Battle Ocean | `91027843` | [Scripts/c91027843.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91027843.lua) | 42 |
| Dragunity Knight - Barcha | `25682811` | [Scripts/c25682811.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25682811.lua) | 41 |
| Phantasm Spiral Battle | `34302287` | [Scripts/c34302287.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34302287.lua) | 39 |
| Sword Hunter | `51345461` | [Scripts/c51345461.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51345461.lua) | 31 |
| Gilford the Legend | `69933858` | [Scripts/c69933858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69933858.lua) | 25 |
| Collected Power | `7565547` | [Scripts/c7565547.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7565547.lua) | 25 |

## Script Examples

### Shining Draw (`35906693`)

Source: [Scripts/c35906693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35906693.lua)

```lua
		ec=sg:GetNext()
	end
	Duel.EquipComplete()
end
function c35906693.eqlimit(e,c)
```

### Power Tool Braver Dragon (`63265554`)

Source: [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63265554.lua)

```lua
		tc=sg:GetNext()
	end
	Duel.EquipComplete()
end
function c63265554.pncon(e,tp,eg,ep,ev,re,r,rp)
```

### Dragunity Arma Gram (`53184342`)

Source: [Scripts/c53184342.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53184342.lua)

```lua
			tc=sg:GetNext()
		end
		Duel.EquipComplete()
	end
end
```
