import os
import shutil

for fname in os.listdir():
	if "script" in fname: continue
	name = fname.split('.')[0]
	os.mkdir(name)
	for i in range(20):
		shutil.copyfile(fname, os.path.join(name,f"{name}_{i}.jpg"))