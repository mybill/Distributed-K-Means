#!/usr/bin/python
import random

if __name__ == '__main__':
	K = 3
	
	fin = open('datas')
	lines = fin.readlines()
	fin.close()

	centers = random.sample(lines, K)
	fout = open('centers-0','w')
	cid = 0
	for line in centers:
		cols = line.strip().split('\t')
		fout.write( '%d\t\t%f\t%f\n' % (cid, float(cols[0]), float(cols[1])) )
		cid += 1
	fout.close()
