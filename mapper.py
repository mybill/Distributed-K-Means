#!/usr/bin/python
import sys, math

def read_centers(iter):
	fc = open('centers_'+iter)
	for line in fc:
		cols = line.strip().split('\t')
		cid = int(cols[0])
		centers[cid] = cols[2:]
	fc.close()

def comp_dist(X,Y):
	sum = 0
	for i in xrange(len(X)):
		sum += math.pow((float(X[i])-float(Y[i])), 2)
	return math.sqrt(sum)

def argmin(X):
	cid = 0
	min = X[0]
	for i,x in enumerate(X):
		if x<min:
			cid = i
			min = x
	return cid

def run():
	dist = [0]*K
	count = [0]*K
	instance_sum = [[0 for col in range(size)] for row in range(K)]
	
	for line in sys.stdin:
		cols = line.strip().split('\t')
		instance = cols[:]
		for i in xrange(K):
			dist[i] = comp_dist(instance, centers[i])
		cid = argmin(dist)
		count[cid] += 1
		for i in xrange(size):
			instance_sum[cid][i] += float(instance[i])
		
	for cid in xrange(K):
		print '%d\t%d' % (cid, count[cid]),
		for i in xrange(size):
			print '\t%f' % (instance_sum[cid][i]),
		print ''

if __name__ == '__main__':
	iter = sys.argv[1]
	size = int(sys.argv[2])
	K = int(sys.argv[3])
	centers = [[0 for col in range(size)] for row in range(K)]
	read_centers(iter)
	run()
