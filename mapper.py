#!/usr/bin/python
import sys
import numpy as np
from scipy.linalg import norm

def read_centers():
	fc = open('centers-'+sys.argv[1])
	cid = 0
	for line in fc:
		cols = line.strip().split('\t')
		for j in xrange(size):
			centers[cid][j] = float(cols[j+2])
		cid += 1
	fc.close()

def run():
	dist = np.zeros(K)
	count = np.zeros(K)
	instance_sum = np.zeros((K,size))
	
	for line in sys.stdin:
		cols = line.strip().split('\t')
		instance = np.array(cols[:],float)
		for i in xrange(K):
			dist[i] = norm(instance-centers[i])
		cid = dist.argmin()
		count[cid] += 1
		instance_sum[cid] += instance
		
	for cid in xrange(K):
		print '%d\t%d' % (cid, count[cid]),
		for i in xrange(size):
			print '\t%f' % (instance_sum[cid][i]),
		print ''

if __name__ == '__main__':
	K = 3
	size = 2
	centers = np.zeros((K,size))
	read_centers()
	run()
