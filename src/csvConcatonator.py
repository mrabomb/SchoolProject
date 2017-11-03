import glob, os
os.chdir("../CSVs")

outFile = open('Output.csv','w')
listLines = []
fileList = glob.glob("*.csv")
if 'Output.csv' in fileList:
    fileList.remove('Output.csv')

for file in fileList:
    inFile = open(file,'r')
    for line in inFile:
        if line in listLines:
            continue
        else:
            listLines.append(line)
    inFile.close()
    os.remove(file)
for x in listLines:
    outFile.write(x)
outFile.close()

