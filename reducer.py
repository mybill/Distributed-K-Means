#!/usr/bin/python
import sys

def output(cid, count, sum):
	if cid!='':
		print '%s\t%d' % (cid, count),
		for i in sum:
			print '\t%f' % (i/count),
		print ''

def run():
	last_cid = ''
	count = 0
	sum = [0]*size
	for line in sys.stdin:
		cols = line.strip().split('\t')
		cid = cols[0]
		if cid==last_cid:
			count += int(cols[1])
			for i in xrange(size):
				sum[i] += float(cols[i+2])
		else:
			output(last_cid, count, sum)
			last_cid = cid
			count = int(cols[1])
			for i in xrange(size):
				sum[i] = float(cols[i+2])
	output(last_cid, count, sum)

if __name__ == '__main__':
	size = 2
	run()
