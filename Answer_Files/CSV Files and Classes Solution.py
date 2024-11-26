"""
                        PART ONE
"""
DATAFILE_PATH = "../ImportFiles/StoreVisitorSalesData.csv"


# open file object
# This encoding is used due to the file's encoding not being the
# default of utf-8. Sorry!
# see https://stackoverflow.com/a/34399309 for more info
with open(DATAFILE_PATH, "r", encoding="utf-8-sig") as dataFile:
    # list of lines, which are in turn a list of data
    data = [[]]

    for line in dataFile.readlines():
        # remove newline characters and extra whitespace for proper data
        # formatting
        cleanedLine = line.strip()

        # split each element in line into list and add to data array
        lineData = cleanedLine.split(',')
        data.append(lineData)
        print(lineData)


"""
                        PART TWO
"""


class Record:
    columnNames = []  # list of string names
    columnData = []  # list of string data

    # dont forget the constructor!
    def __init__(self, columnNames, columnData):
        self.columnNames = columnNames
        self.columnData = columnData

    def GetData(self, columnName):
        index = self.columnNames.index(columnName)
        data = self.columnData[index]
        return data


recordList = []

with open(DATAFILE_PATH, "r", encoding="utf-8-sig") as dataFile:
    cleanedLine = dataFile.readline().strip()
    columnNames = cleanedLine.split(',')

    # retrieve column data
    for line in dataFile.readlines():
        cleanedLine = line.strip()
        columnData = cleanedLine.split(',')

        dataRecord = Record(columnNames, columnData)
        recordList.append(dataRecord)

        data = dataRecord.GetData("StoreLocation")


"""
                        PART THREE
"""

for record in recordList:
    sales = record.GetData("SalesLastWeek")
    visitors = record.GetData("VisitorsLastWeek")

    salesPerVisitors = int(sales) / int(visitors)
    pcent = salesPerVisitors * 100

    # optionally, you can use the round function to round the % to
    # 2 (or more/less) decimal places
    pcent = round(pcent, 2)

    if pcent >= 75:
        continue

    # under 75% sale rate, print
    print(record.GetData("StoreLocation") + ": " + str(pcent) + "%")

"""
                        PART FOUR
"""

DATAFILE_LATEST_PATH = "../ImportFiles/StoreVisitorSalesDataLatest.csv"
LOUGHBOROUGH_SALES_PATH = "../ImportFiles/LoughboroughSalesHistory.csv"



# optional function to read file into records
def CreateRecordsFrom(csvFilePath):
    # open file to read
    dataFile = open(csvFilePath, 'r', encoding="utf-8-sig")
    dataRecords = []

    cleanedLine = dataFile.readline().strip()
    columnNames = cleanedLine.split(',')

    # retrieve column data
    for line in dataFile.readlines():
        cleanedLine = line.strip()
        columnData = cleanedLine.split(',')

        dataRecord = Record(columnNames, columnData)
        dataRecords.append(dataRecord)

    # ensure file object is closed
    dataFile.close()

    # return list of records from file
    return dataRecords

loughboroughSalesRecords = CreateRecordsFrom(LOUGHBOROUGH_SALES_PATH)
loughboroughMeanSales = 0

# get mean sales
for record in loughboroughSalesRecords:
    # sum up sales
    loughboroughMeanSales += int(record.GetData("Sales"))

# turn into mean
loughboroughMeanSales /= len(loughboroughSalesRecords)
loughboroughMeanSales = round(loughboroughMeanSales, 2)

latestSales = CreateRecordsFrom(DATAFILE_LATEST_PATH)

for index, sales in enumerate(latestSales):
    if sales.GetData("StoreLocation") == "Loughborough":
        salesIndex = sales.columnNames.index("SalesLastWeek")
        latestSales[index].columnData[salesIndex] = loughboroughMeanSales

for sales in latestSales:
    print(sales.columnData)


"""
                        PART FOUR - OPTIONAL CLASS IMPROVEMENT
"""


class Record:
    columnNames = []
    columnData = []

    def __init__(self, columnNames, columnData):
        self.columnNames = columnNames
        self.columnData = columnData

    def GetData(self, columnName):
        index = self.columnNames.index(columnName)
        data = self.columnData[index]
        return data

    # new function to set data value of specific column
    def SetData(self, columnName, value):
        index = self.columnNames.index(columnName)
        self.columnData[index] = value