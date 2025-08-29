#!/usr/bin/env python3

import argparse
import os
import struct

def getMapRim():
	f = open('rrhispec/MAP.RIM', 'rb')
	f.read(0x800) # TODO: need to figure out what are those for...
	return f

def read_int(map):
	b = map.read(4)
	return int.from_bytes(b, byteorder='little')

def read_file(map, position):
	map.seek(position)
	id = read_int(map)
	match id:
		case 0x00010000:
			print('DEBUG: Quad')
			print(read_quad(map))
		case _:
			padding = 10
			print(f'Unknown ID {id:#0{padding}x}, ignoring')

def read_quad(map):
	return struct.unpack('<hhhxxhhhxxhhhxxhhhxxxxxxxxxxxxxxxxxxL', map.read(52))

def vertex_11bit(v):
	return (v & 0x3FF) * (-1 if (v & 0x400) else 1) # TODO: is it even correct

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('method', choices=['map2obj', 'list', 'allitemtypes'], metavar='method')
	parser.add_argument('method_args', nargs='*')
	args = parser.parse_args()
	with getMapRim() as map:
		match args.method:
			case 'map2obj':
				m2oparser = argparse.ArgumentParser()
				m2oparser.add_argument('output')
				m2oargs = m2oparser.parse_args(args.method_args)

				items_count = read_int(map)

				items = [] # an array of offsets
				for i in range(items_count):
					items.append(read_int(map) + 0x800)

				vertex_n = 1
				vertecies = []
				faces = []
				for item in items:
					map.seek(item)
					id = read_int(map)
					if id != 0x00010000:
						continue
					quad = read_quad(map)
					indexes = []
					for i in range(4):
						v = (vertex_11bit(quad[i * 3 + 0]),
							vertex_11bit(quad[i * 3 + 1]),
							vertex_11bit(quad[i * 3 + 2]))
						idx = 0
						try:
							idx = vertecies.index(v)
						except ValueError:
							vertecies.append(v)
							idx = vertex_n
							vertex_n += 1
						indexes.append(idx)
					faces.append((indexes[0], indexes[1], indexes[2]))
					faces.append((indexes[3], indexes[1], indexes[2]))
				with open(m2oargs.output, 'w') as obj:
					for v in vertecies:
						obj.write(f'v {v[0]} {v[1]} {v[2]}\n')
					for f in faces:
						obj.write(f'f {f[0]} {f[1]} {f[2]}\n')
			case 'list':
				items_count = read_int(map)

				items = [] # an array of offsets
				for i in range(items_count):
					items.append(read_int(map) + 0x800)
				print(items)

				for item in items:
					read_file(map, item)
				print('Items in MAP.RIM:', items_count)
			case 'allitemtypes':
				items_count = read_int(map)

				items = [] # an array of offsets
				for i in range(items_count):
					items.append(read_int(map) + 0x800)
				items.append(os.path.getsize('rrhispec/MAP.RIM'))

				item_types = {}
				non_constant = []
				for i in range(len(items) - 1):
					item = items[i]
					size = items[i + 1] - items[i] - 2
					map.seek(item)
					id = read_int(map)
					if id in non_constant:
						continue
					if id in item_types and item_types[id] != size:
						print(f'WARNING: ID {id:#0{10}x} has different size! ({size} vs {item_types[id]})')
						del item_types[id]
						non_constant.append(id)
						continue
					item_types[id] = size
				print('Item types MAP.RIM:')
				for type in item_types.items():
					print(f'ID: {type[0]:#0{10}x}, length: {type[1]}')
				print('Item types without a constant size:')
				for type in non_constant:
					print(f'ID: {type:#0{10}x}')
			case _:
				print("Unknown method", args.method)
				parser.print_help()
