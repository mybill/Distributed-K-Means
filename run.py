#!/usr/bin/python
import sys, random, os

def init_centers():
	fin = open('datas')
	lines = fin.readlines()
	fin.close()

	centers = random.sample(range(len(lines)), K)
	fout = open('centers_0','w')
	cid = 0
	for t in centers:
		cols = lines[t].strip().split('\t')
		fout.write( '%d\t\t%f\t%f\n' % (cid, float(cols[0]), float(cols[1])) )
		cid += 1
	fout.close()

def read_centers(filename):
	diff = 0
	fc = open(filename)
	for line in fc:
		cols = line.strip().split('\t')
		cid = int(cols[0])
		diff += abs(count[cid] - int(cols[1]))##
		count[cid] = int(cols[1])
		#for j in xrange(size):	
			#centers[cid][j] = float(cols[j+2])
	fc.close()
	return diff
	
if __name__ == '__main__':
	K = 3
	size =2
	init_centers()
	centers = [[0 for col in range(size)] for row in range(K)]
	count = [0]*K
	for i in xrange(100):
		cmd = "./iter.sh %d" % (i)
		os.system(cmd)
		if read_centers('centers_'+str(i+1))==0:
			break
