"""
                        PART ONE
"""
import pandas as pd
DATAFILE = "../ImportFiles/StoreVisitorSalesData.csv"

# Read the specified columns using usecols and list of column names
# a list of column indexes is also valid, which would be [0, 2, 3]
weekVisitorsSales = pd.read_csv(DATAFILE, usecols=["StoreLocation", "SalesLastWeek", "VisitorsLastWeek"])

# Each Locations Sales-to-Visit ratio
SaleVisitPercents = []
for index, locationSales in enumerate(weekVisitorsSales["SalesLastWeek"]):
    # decimal fraction of sales per visit
    ratio = locationSales / weekVisitorsSales["VisitorsLastWeek"][index]

    # turn decimal into %
    percentage = ratio * 100
    SaleVisitPercents.append(percentage)

for index, location in enumerate(weekVisitorsSales["StoreLocation"]):
    if SaleVisitPercents[index] >= 75:
        continue

    print(location + ": For each Visit, " + str(SaleVisitPercents[index]) + "% result in a sale.")

print("mean:" + str(weekVisitorsSales["SalesLastWeek"].mean()))

"""
                        PART TWO
"""

# switch to different file now
LATEST_DATAFILE = "../ImportFiles/StoreVisitorSalesDataLatest.csv"
LOUGHBOROUGH_SALES = "../ImportFiles/LoughboroughSalesHistory.csv"

# Read the specified columns using usecols and list of column names
# a list of column indexes is also valid, which would be [0, 2, 3]
weekVisitorsSales = pd.read_csv(LATEST_DATAFILE, usecols=["StoreLocation", "SalesLastWeek", "VisitorsLastWeek"])


for index, locationSales in enumerate(weekVisitorsSales["SalesLastWeek"]):
    # decimal fraction of sales per visit
    print(locationSales)