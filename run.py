#!/usr/bin/python
import sys, random, os, math

def upload_data(data_file, hdfs_dir):
	cmd = 'hadoop fs -mkdir %s' % (hdfs_dir)
	os.system(cmd)
	cmd = 'hadoop fs -put %s %s/datas' % (data_file, hdfs_dir)
	os.system(cmd)

def init_centers(data_file, K):
	fin = open(data_file)
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

def comp_dist(X,Y):
	sum = 0
	for i in xrange(len(X)):
		sum += math.pow((float(X[i])-float(Y[i])), 2)
	return math.sqrt(sum)

def comp_diff(iter):
	diff = 0
	fc = open('centers_'+str(iter+1))
	for line in fc:
		cols = line.strip().split('\t')
		cid = int(cols[0])
		diff += comp_dist(centers[cid], cols[2:])
		centers[cid] = cols[2:]
	fc.close()
	return diff

if __name__ == '__main__':
	if len(sys.argv)!=5:
		print 'RUN: python run.py data_file size K hdfs_dir'
	else:
		data_file = sys.argv[1]
		size = int(sys.argv[2])
		K = int(sys.argv[3])
		hdfs_dir = sys.argv[4]
	
		upload_data(data_file, hdfs_dir)
		init_centers(data_file, K)
		centers = [[0 for col in range(size)] for row in range(K)]
		for iter in xrange(200):
			cmd = "./iter.sh %d %d %d %s" % (iter,size,K,hdfs_dir)
			os.system(cmd)
			if comp_diff(iter)<1e-15:
				break
