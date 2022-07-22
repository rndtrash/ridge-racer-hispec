# MAP.RIM

## Description

This file contains the map and probably some other things.

## Structure

Please note that even though MIPS I is *bi-endian*, PSX is *little endian*.

|Offset|Size (bytes)|Name|Description|
|------|----|----|-----------|
|`0x0`|`0x800`|`padding`|Padding. Initially it's *mostly* filled with `0xFF`.|
|`0x800`|`4`|`itemCount`|Amount of items|
|`0x804`|`itemCount * 4`|`itemOffsets`|Offsets relative to `0x800`. In function `0x80017540` each item's relative offset to memory is turned into absolute by adding the pointer to the `MAP.RIM` file + `0x800`.|
|`+ items * 4`|`items * 56`|`items`|Items themselves!|


### Item types

#### Shared (unless said otherwise)

|Offset|Size (bytes)|Name|Description|
|------|------------|----|-----------|
|`0x0`|`4`|id|Index of a function from the function table @ `0x8007ED24`. Only first two bytes are actually used.|

Sizes do not include the shared fields.

#### Quad

**ID:** `0x00010000` (`00 00 01 00`)

**Size:** 52 bytes

**Note:** VXY\* registers contain two signed 16-bit values, while VZ\* registers takes a signed 16-bit value sign extended to 32 bits.

|Offset|Size (bytes)|Name|Description|
|------|------------|----|-----------|
|`0x4`|`4`|XY0|Loaded into VXY0 data register of GTE.|
|`0x8`|`4`|Z0|Loaded into VZ0 data register of GTE.|
|`0xC`|`4`|XY1|Loaded into VXY1 data register of GTE.|
|`0x10`|`4`|Z1|Loaded into VZ1 data register of GTE.|
|`0x14`|`4`|XY2|Loaded into VXY2 data register of GTE.|
|`0x18`|`4`|Z2|Loaded into VZ2 data register of GTE.|
|`0x1C`|`4`|XY3|Loaded into VXY0 data register of GTE.|
|`0x20`|`4`|Z3|Loaded into VZ0 data register of GTE.|
|`0x24`|-|-|Unknown.|
|`0x34`|`4`|unknown1|Possibly indicates that there is a next block.|
