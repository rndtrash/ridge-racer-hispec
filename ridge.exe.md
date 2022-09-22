# RIDGE.EXE

## Description

The game executable itself.

## Memory addresses

|Address (hex)|Data type|Description|Values|Notes|
|-------------|---------|-----------|------|-----|
|`80085d68`|short|Race track selection|1 up to 4|-|
|`80085e0c`|short|Music selection|0 - Random, 1 - Ridge Racer, 2 - Grip|Any value above 3 crashes the console immediately!|
|`80085e0e`|short|Game state|See [Game states](#game-states)|Some values are... "normalised"? And the game keeps running as usual.|

### Game states

|# (hex)|Description|
|-------|-----------|
|`00`|Transition to the Gameplay|
|`01`|Gameplay or transition to Demo step 1 (used by Music player step 2)|
|`02`|Transition to Main menu|
|`03`|Main menu, waving flag|
|`04`|Transition to Demo|
|`05`|Demo|
|`06`|Transition to Select screen|
|`07`|Select screen|
|`08`|Transition to Other demo or Replay|
|`09`|Other demo or Replay|
|`0a`|Undefined (the game stops)|
|`0b`|Undefined (blue screen)|
|`0c`|The same waving flag but eventually jumps to `1e`|
|`0d`|Transition to Name entry|
|`0e`|Name entry|
|`0f`|Transition to Game Over|
|`10`|Game Over|
|`11`|Transition to Options|
|`12`|Options|
|`13`|Transition to Button config|
|`14`|Options -> Button config|
|`15`|Transition to Records|
|`16`|Options -> Records|
|`17`|Transition to Adjust Screen|
|`18`|Options -> Adjust Screen|
|`19`|Load demo assets (Demo step 2) (used by Music player step 1)|
|`1a`|Demo step 3 (or Options -> Music player)|
|`1b`|Transition to Game Option|
|`1c`|Options -> Game Option|
|`1d`|??? (jumps to Best scores)|
|`1e`|Best scores|
|`1f`|Transition to Result|
|`20`|Result|
|`21`|Transition to Memory card|
|`22`|Options -> Memory card|
|`23`|Transition to Memory Card -> Load|
|`24`|Options -> Memory card -> Load|
|`25`|Transition to Memory Card -> Save|
|`26`|Options -> Memory card -> Save|
|`32`|Transition to Information|
|`33`|Information|
|`34`|Transition to other executable (NAMCO Catalogue or Original Mode)|
|`35`|Now loading!|
