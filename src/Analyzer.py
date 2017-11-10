from shutil import copyfile
import os

#custom modules
from ColumnSorter import *

#Comment this for testing
copyfile('../CSVs/Output.csv', 'fuseFile.csv')

file = 'fuseFile.csv'
fileToFix = fuseFile(file)
fileToSort = fixTime(fileToFix)
sortedFile = sortFile(fileToSort)


'''
inFile = open(file,'r')

dataList = []
for line in inFile:
    dataList.append(line)

tempList = dataList
rowList = []
for line in tempList:
    row = [x.strip() for x in line.split(',')]
    rowList.append(row)



#sort numerically by second column and then again by first





inFile.close()
#os.remove(inFile)
'''
