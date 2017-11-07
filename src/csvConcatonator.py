import glob, os

def Concatonate():
    os.chdir("../CSVs")
    outFile = open('Output.csv','a+')
    listLines = []
    fileList = glob.glob("*.csv")
    if 'Output.csv' in fileList:
        fileList.remove('Output.csv')

    outList = outFile.readlines()
    for file in fileList:
        inFile = open(file,'r')
        for line in inFile:
            if (line in listLines) or (line in outList) or (line == ''):
                continue
            else:
                listLines.append(line)
        inFile.close()
        os.remove(file)
    for x in listLines:
        outFile.write(x)
    outFile.close()
    os.chdir("../src")

