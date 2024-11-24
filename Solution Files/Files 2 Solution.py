import pandas as pd

# pd.set_option("display.max_columns", 200)

storeProduce = pd.read_csv("../ImportFiles/StoreVisitorSalesData.csv",
                           usecols=["SalesLastWeek", "VisitorsLastWeek"])
print(storeProduce.mean())
