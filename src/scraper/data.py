import csv

def findInCsv(term, target="../docs/linklist.csv"):
    reader = csv.reader(open(target), delimiter=';')
    csvList = []
    
    for row in reader:
        csvListRow = []
        
        for col in row:
            csvListRow.append(col)

        csvList.append(csvListRow)
    
    if type(term) is str:
        for row in csvList:
            if term in row:
                return True
    else:
        if term in csvList:
            return True
            
    return False

def writeRowToCsv(row=[], target="../docs/linklist.csv"):
    targetFile = open(target, 'a', newline='')
    writer = csv.writer(targetFile, delimiter=';')
    writer.writerow(row)
    targetFile.close
