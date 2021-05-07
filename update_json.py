#!/usr/bin/env python3

import sys
import os
import json

def load_json(fn='./de.json', t='NONE'):
	try:
		f = open(fn,'r', encoding='utf-8')
		js = json.loads(f.read())
		f.close()
		return js
	except:
		print("Error reading {t} from {path}, exiting.".format(t=t, path=fn))
		sys.exit(1)

if not len(sys.argv) == 4:
	print('Usage: ./'+sys.argv[0]+' [changes_file] [input_file] [output_file]')
	sys.exit(1)

update_json = load_json(sys.argv[1], 'changes_file')
original_json = load_json(sys.argv[2], 'file_to_update')

for k in update_json.keys():
	if k in original_json:
		original_json[k] = update_json[k]

try:
	f = open(sys.argv[3],'w',encoding='utf-8')
	f.write(json.dumps(original_json, ensure_ascii=False, indent=4, sort_keys=False)+'\n')
	f.close()
except:
	print('Writing to {f} failed! Exiting.'.format(f=sys.argv[3]))


