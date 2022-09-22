#!/usr/bin/env python3

import os
import struct

def read_int(map):
	b = map.read(4)
	return int.from_bytes(b, byteorder='little')

def read_file(map, position):
	map.seek(position)
	id = read_int(map)
	match id:
		case 0x00010000:
			print('Quad')
			print(read_quad(map))
		case _:
			padding = 10
			print(f'Unknown ID {id:#0{padding}x}, ignoring')

def read_quad(map):
	return struct.unpack('<hhlhhlhhlxxxxxxxxxxxxxxxxxxxxxxxxL', map.read(52))

with open('rrhispec/MAP.RIM', 'rb') as map:
	map.read(0x800) # TODO: need to figure out what are those for...
	items_count = read_int(map)
	print('Items in MAP.RIM:', items_count)

	items = [] # an array of offsets
	for i in range(items_count):
		items.append(read_int(map) + 0x800)
	print(items)

	for item in items:
		read_file(map, item)
