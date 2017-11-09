
file = 'testfile.csv'
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
