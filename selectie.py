#!/usr/bin/python
import os
import datetime
import glob
import csv
import shutil

csvfile = os.getcwd() + "/selectie.csv"

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
    fullfilename = os.getcwd()+'/Foto/'+filename
    if not os.path.isfile(fullfilename):
        continue
    shutil.copy2(fullfilename, os.getcwd()+'/Selectie/'+filename)