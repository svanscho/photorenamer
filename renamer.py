#!/usr/bin/python
import os
import datetime
import glob
import os
import datetime
import glob
import csv
import shutil

cwd = os.getcwd() 
target = os.getcwd() + "/All"
os.chdir(target)
files = glob.glob(os.path.join(target, '*'))
allfiles = []
for filename in files:
    t = os.path.getmtime(filename)
    allfiles.append({'name':filename,'time':t})
sortedallfiles = sorted(allfiles,cmp=lambda x,y: cmp(x['time'], y['time']))

mappingtable={}

for f in sortedallfiles:
    filename = f['name']
    if not os.path.isfile(filename):
        continue
    t = os.path.getmtime(filename)
    v= datetime.datetime.fromtimestamp(t)
    x = 'OUTBACK'
    loop = 1
    iterator = 1
    temp_name = x + "_" + str(iterator).zfill(4) + '.JPG'

    while filename != temp_name:
        if not os.path.exists(temp_name):
            os.rename(filename, temp_name)
            mappingtable[filename]=temp_name
            filename = temp_name
        else:
            iterator+=1
            temp_name = x + '_' + str(iterator).zfill(4) + '.JPG'

print mappingtable
f = open('mappingtable.txt', 'w')
f.write(str(mappingtable))
f.close()

csvfile = cwd + "/selectie.csv"
selectie=[]
strengeselectie=[]

with open(csvfile, 'rU') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in csvreader:
        if(row[0]!=''):
            selectie.append(int(row[0]))
        if(row[1]):
            strengeselectie.append(int(row[1]))

for f in selectie:
    x = 'DSC'
    filename = x + "_" + str(f).zfill(4) + '.JPG'   
    fullfilename = cwd +'/All/'+mappingtable[target+'/'+filename]
    if not os.path.isfile(fullfilename):
        continue
    shutil.copy2(fullfilename, cwd+'/Selection/'+mappingtable[target+'/'+filename])

for f in strengeselectie:
    x = 'DSC'
    filename = x + "_" + str(f).zfill(4) + '.JPG'   
    fullfilename = cwd+'/All/'+mappingtable[target+'/'+filename]
    if not os.path.isfile(fullfilename):
        continue
    shutil.copy2(fullfilename, cwd+'/StrictSelection/'+mappingtable[target+'/'+filename])


