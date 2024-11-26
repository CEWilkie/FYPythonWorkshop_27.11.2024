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

    # turn decimal into % and optionally round to 2 decimal places
    percentage = ratio * 100
    percentage = round(percentage, 2)
    SaleVisitPercents.append(percentage)

for index, location in enumerate(weekVisitorsSales["StoreLocation"]):
    if SaleVisitPercents[index] >= 75:
        continue

    print(location + ": For each Visit, " + str(SaleVisitPercents[index]) + "% result in a sale.")

print("mean:" + str(weekVisitorsSales["SalesLastWeek"].mean()))


"""
                        PART TWO
"""

# using files
LATEST_DATAFILE = "../ImportFiles/StoreVisitorSalesDataLatest.csv"
LOUGHBOROUGH_SALES = "../ImportFiles/LoughboroughSalesHistory.csv"

# Read the specified columns using usecols and list of column names
# a list of column indexes is also valid, which would be [0, 2, 3]
weekVisitorsSales = pd.read_csv(LATEST_DATAFILE, usecols=["StoreLocation", "SalesLastWeek", "VisitorsLastWeek"])

# read the sales data from loughboroughSalesHistory.csv
pastSalesData = pd.read_csv(LOUGHBOROUGH_SALES, usecols=["Sales"])

# fetch the mean of the data and optionally round to 2 decimal places
# mean returns a "series", so use .get("Sales") to retrieve the actual numeric mean
loughboroughMeanSales = pastSalesData.mean().get("Sales")
print(loughboroughMeanSales)

latestSalesPercents = []
for index, location in enumerate(weekVisitorsSales["StoreLocation"]):
    # find the row of Loughborough to update its sales value
    if location == "Loughborough":
        # use .fillna to fill all nan values with the provided value
        weekVisitorsSales = weekVisitorsSales.fillna(loughboroughMeanSales)

    # retrieve sales and visitors data
    sales = weekVisitorsSales["SalesLastWeek"][index]
    visitors = weekVisitorsSales["VisitorsLastWeek"][index]

    # determine percentages
    percentage = sales / visitors
    percentage *= 100
    percentage = round(percentage, 2)

    latestSalesPercents.append(percentage)
    print(percentage)

# compare change from latest to previous
for index, latestPercent in enumerate(latestSalesPercents):
    prevPercent = SaleVisitPercents[index]
    location = weekVisitorsSales["StoreLocation"][index]

    # calc change and round to 2 dp
    change = latestPercent - prevPercent
    change = round(change, 2)

    # output
    print(location + ": change of " + str(change) + "%")
