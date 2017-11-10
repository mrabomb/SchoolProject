import operator, csv, sys, os
from pathlib import Path

def fuseFile(file):
    temp = 'temp.csv'
    output = 'Sorted.csv'

    isFile = Path(file)
    if not isFile.is_file():
        sys.exit()

    #combine col 0 and 1 so we have the date as one string
    with open(file, 'r') as csvfile, open(temp, 'w') as tempFile:
        csvreader = csv.reader(csvfile)
        writer = csv.writer(tempFile)
        for row in csvreader:
            if len(row)== 4:
                outRow = [row[0] + ':' + row[1], row[2], row[3]]
                writer.writerow(outRow)
        csvfile.close()
        tempFile.close()

    #replace the original with the temp
    os.remove(file)
    os.rename(temp, file)

    #clear all our csvs we don't need (this kills the temp)
    doesItStillExist = Path(temp)
    if doesItStillExist.is_file():
        os.remove(temp)

    #return the path to the file that is fused
    return file

'''
def fixTime(inFile):
    #before we sort, the first row needs to be parsed and edited
    #to make sure that the date is correct
    #(combining computer date and server time is bad)
    return(outFile)
'''

def sortFile(file)
    #data is the file with combined col 0 and 1 and properly sorted
    inFile = open(file, 'r')
    data = csv.reader(inFile)

    #sort data
    tempStorage = []
    for row in data:
        if row:
            tempStorage.append(row)

    #makes a key to sort with and then sorts
    def getKey(item):
        return item[0]
    tempStorage.sort(key=getKey)

    #output sorted data as 'Sorted.csv'
    with open(output, 'w') as outFile:
        outCsv = csv.writer(outFile)
        for item in tempStorage:
            outCsv.writerow(item)

    #clear all our csvs we don't need (this kills the original)
    inFile.close()
    isOriginalFileStillThere = Path(file)
    if isOriginalFileStillThere.is_file():
        os.remove(file)
        
    #return path to the sorted file
    return output
