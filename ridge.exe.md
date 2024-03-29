# RIDGE.EXE

## Description

The game executable itself.

## Memory addresses

|Address (hex)|Data type|Description|Values|Notes|
|-------------|---------|-----------|------|-----|
|`8007b5cc`|pointers[54]|Array of states (see [Game states](#game-states))|Valid function pointers||
|`8007be08`|char*[10]|Names of music tracks|RANDOM PLAY, RIDGE RACER etc||
|`80085d68`|short|Race track selection|1 up to 4||
|`80085d84`|ushort|Timer|Time in frames until the game is over|Timer in seconds = Timer / Framerate (50Hz for PAL, 60Hz for NTSC)|
|`80085dd4`|uint|Music Timer|Time until the next music track. Used for drawing the current music name|The track name is displayed for 600 frames(?)|
|`80085e0c`|short|Music selection|0 - Random, 1 - Ridge Racer, 2 - Grip|Any value above 3 crashes the console immediately!|
|`80085e0e`|short|Game state|See [Game states](#game-states)|Checked each frame, used as index for `8007b5cc`|
|`80085e49`|short|Total racers|1 or more|The position of player is not drawn if only one racer is present|
|`80085ec8`|short|Throttle|`[0; 256]`|Can be increased with X and decreased with Square, also decays with time|
|`80085ef4`|short|Unknown (behaves like throttle)|0 on start, `[15; 249]`|TODO:|
|`80085f00`|ushort|RPM|`[500; 10000]`||
|`80086200`|short|Transmission|0 - Automatic, 1 - Manual|Can be changed while racing|
|`80086202`|short|Current Gear|1 to 6||
|`8008621c`|short|Speed|Any. Speed in KM/H = Speed * 160 / 2336|Negative speed works too!|
|`80086248`|short|Place|1 or 2 since there is only one opponent in this version||

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
|`27`|??? (jumps to `28`)|
|`28` - `2a`|??? (jumps to Options)|
|`2b`|??? (jumps to `2c`)|
|`2c` - `2f`|??? (jumps to Options)|
|`30`|Transition to Credits|
|`31`|Credits|
|`32`|Transition to Information|
|`33`|Information|
|`34`|Transition to other executable (NAMCO Catalogue or Original Mode)|
|`35`|Now loading! (the last safe game state)|
|`36`|??? (jumps to `08`)|
|`37` and onwards|Crashes the system because the index is out of bounds|
