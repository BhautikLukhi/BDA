import sys
import csv
from collections import Counter

if len(sys.argv)==3:
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	a=[]
	with open(sys.argv[1]) as csvfile:
		csvreader = csv.reader(csvfile, delimiter='\t')
		for row in csvreader:
			a1 = row[0]
			a.append(a1)
	output= len(set(a))
	with open(sys.argv[2],'w') as o:
		o.write('%d' % output)
else:
	print('you need a file path')
	exit(1)	
