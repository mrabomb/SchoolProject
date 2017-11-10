import config

inFile = '../ErrorLog/Errors.txt'
file = open(inFile, 'r')

errorList = []
errorCount = 0

print("Relevant Errors:")

for line in file:
    if 'timeout' in line:
        errorCount = errorCount + 1
        if (config.settings['printAll']):
            errorList.append(line)
            print(line)
        elif("tvol" in line) or ("ttimes" in line):
            continue
        else:
            errorList.append(line)
            print(line)
        
print("\n" + str(errorCount))
file.close()



