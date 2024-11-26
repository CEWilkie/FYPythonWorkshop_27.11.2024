"""
CSV Files and Data Manipulation using Pandas

For this exercise, you are going to utilise the pandas library to interpret and parse data from
the file "StoreVisitorSalesData.csv" (DATAFILE)

For a particularly thorough adventure into pandas, I would suggest visiting a tutorial such as
https://www.w3schools.com/python/pandas/default.asp

A good idea with this is to really play around. There is a lot of elements to cover, but hopefully
the particularly important and useful elements will all be covered here.

                PART ONE
A store chain is interested in which locations are getting below 75% visitor:sale rate.

- Utilise the `usecols` parameter to read the contents of DATAFILE, but only the columns
"StoreLocation", "SalesLastWeek" and "VisitorsLastWeek"
- determine the percentage of Sales to Visitors for each store location. Store these in a list.
- Output all locations where the % is below 75%

                PART TWO
The latest sales data has just came in with file "StoreVisitorSalesDataLatest.csv" (LATEST_DATAFILE)

- Utilise the `usecols` parameter to read the contents of DATAFILE, but only the columns
"StoreLocation", "SalesLastWeek" and "VisitorsLastWeek" as before
- Loughborough's SalesLastWeek data is missing for the last week. Replace the
missing data with the mean of its sales from the previous 7 weeks in file
"LoughboroughSalesHistory.csv"
- determine the percentage of Sales to Visitors for each store location. Store these in a list.
- determine the change in percentage from last weeks data to the latest data
"""

import pandas as pd

# Heres the file paths you'll want. Visual Studio users may wish to remove the prefix of ../
DATAFILE = "../ImportFiles/StoreVisitorSalesData.csv"
LATEST_DATAFILE = "../ImportFiles/StoreVisitorSalesDataLatest.csv"
LOUGHBOROUGH_SALES = "../ImportFiles/LoughboroughSalesHistory.csv"

