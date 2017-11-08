
file = 'testfile.csv'
inFile = open(file,'r')

dataList = []
for line in inFile:
    dataList.append(line)

tempList = dataList
for line in tempList:
    [x.strip() for x in line.split(',')]
    


inFile.close()
