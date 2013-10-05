#!/usr/bin/python
import sys, random, os, math

def upload_data(data_file, hdfs_dir):
	cmd = 'hadoop fs -mkdir %s' % (hdfs_dir)
	os.system(cmd)
	cmd = 'hadoop fs -put %s %s/datas' % (data_file, hdfs_dir)
	os.system(cmd)

def init_centers(data_file, K):
	dict = {}
	fin = open(data_file)
	for line in fin:
		dict[line] = 1
	fin.close()

	cs = random.sample(dict, K)
	fout = open('centers_0','w')
	cid = 0
	for t in cs:
		fout.write( '%d\t\t%s' % (cid, t) )
		cid += 1
	fout.close()
	return len(cs[0].strip().split('\t'))

def comp_dist(X,Y):
	sum = 0
	for i in xrange(len(X)):
		sum += math.pow((X[i]-Y[i]), 2)
	return math.sqrt(sum)

def comp_diff(iter):
	diff = 0
	fc = open('centers_'+str(iter+1))
	for line in fc:
		cols = line.strip().split('\t')
		cid = int(cols[0])
		cc = map(float, cols[2:])
		diff += math.pow(comp_dist(centers[cid],cc), 2)
		centers[cid] = cc
	fc.close()
	return diff

if __name__ == '__main__':
	if len(sys.argv)!=4:
		print 'RUN: python run.py data_file K hdfs_dir'
	else:
		data_file = sys.argv[1]
		K = int(sys.argv[2])
		hdfs_dir = sys.argv[3]
	
		upload_data(data_file, hdfs_dir)
		size = init_centers(data_file, K)
		centers = [[0 for col in range(size)] for row in range(K)]
		for iter in xrange(200):
			print 'iteration %d ...' % (iter)
			cmd = "./iter.sh %d %s" % (iter, hdfs_dir)
			os.system(cmd)
			if comp_diff(iter)<1e-8:
				break
