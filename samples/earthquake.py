import sys

#call file argument filename
filename=sys.argv[1]


#open file, call it f
f=open(filename, "r")

#read in data
#create lists for data

longitude=[]
latitude=[]

#set up variable to go through lines and let it start with 1 to avoid header
linecount=0
#read data into lists
for line in f:
  if linecount==0:
    header=line
    linecount+=1 
    continue

  linelist=line.split(",")
  longitude+=[float(linelist[0])]
  latitude+=[float(linelist[1])]

#close file
f.close()

#create rounded lists
round_longitude=[]
round_latitude=[]

for i in range(len(longitude)):
  round_longitude+=[int(round(longitude[i]))]
  round_latitude+=[int(round(latitude[i]))]


#create frequency list
frequency=[[0,0,0]]

#add all the events into the frequency list (only caring about integer longitude and latitude) with frequency


for i in range(len(longitude)):
  #check whether frequence has and entry with the same long and lat und increment its frequency by one. alternatively create corresponding list entry
  t=0
  for j in range(len(frequency)):
    if frequency[j][0]==round_longitude[i] and frequency[j][1]==round_latitude[i]:
      frequency[j][2]+=1
      t=1
  if t==0:
    frequency.append([round_longitude[i], round_latitude[i], 1])

#find the most frequent location

top_frequency=0

for i in range(len(frequency)):
  if top_frequency<frequency[i][2]:
    top_frequency=frequency[i][2]

for i in range(len(frequency)):
  if frequency[i][2]==top_frequency:
    print "The most frequent location has longitude " + str(frequency[i][0]) + " and latitude " + str(frequency[i][1]) + ". It has frequency " + str(top_frequency)

del frequency[0]
# Write frequency to file

filestring="Longitude, Latitude, Frequency\n"

#write each line as a string and append
for i in range(len(frequency)):
  filestring+=str(frequency[i][0])+","+str(frequency[i][1])+"," + str(frequency[i][2])+"\n"

fout=open("earthquake_frequency.csv","w")
fout.write(filestring)
fout.close()





    




