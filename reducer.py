#!/usr/bin/python
import sys
import numpy as np

def output(cid, count, sum):
	if cid!='':
		print '%s\t%d' % (cid, count),
		for i in sum:
			print '\t%f' % (i/count),
		print ''

def run():
	last_cid = ''
	count = 0
	sum = np.zeros(size)
	for line in sys.stdin:
		cols = line.strip().split('\t')
		cid = cols[0]
		if cid==last_cid:
			count += int(cols[1])
			sum += np.array(cols[2:], float)
		else:
			output(last_cid, count, sum)
			last_cid = cid
			count = int(cols[1])
			sum = np.array(cols[2:], float)
	output(last_cid, count, sum)

if __name__ == '__main__':
	size = 2
	run()
