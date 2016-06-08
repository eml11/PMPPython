import sys
import csv
import numpy
# get filename passed to file
# sys.argv is the list of python
# arguments. Note sys.argv[0] is
# the name of the python program
# i.e. meteor.py
#filename = sys.argv[1]
#filename = '../data/meteor.csv'
# open file for reading
f=open(sys.argv[1],'rb')
#with open('filename','r') as csvfile:
csvreader = csv.reader(f)
altitude=[]
rownum=0;
for row in csvreader:
 if rownum==0:
  header=row
  rownum+=1
  continue
# linelist=row.split(",")
 #print row[1]
 altitude+=[float(row[1])] #need to convert to float!

f.close()
print('\n'.join(map(str,altitude)))
print 'The mean of Altitude =', sum(altitude) / float(len(altitude))
   # This skips the first row of the CSV file.
    # csvreader.next() also works in Python 2.
#    next(csvreader)
#     for row in csvreader:
