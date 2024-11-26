"""
CSV Files and Data Manipulation using manual parsing

For this exercise, you are going to interpret and parse data from the file "StoreVisitorSalesData.csv"
(DATAFILE). This will be done through the usage and modification of classes, used
to store and manipulate data retrieved from the file.

                PART ONE
- Read the data from file "StoreVisitorSalesData.csv"
- using .split(), separate the data in each line into individual data elements.
 You can store this in a list for now
- print out the split data lists to check that everything is correct. If there are
errors in the formatting of the csv file, this may require some additional code to
merge together data

Addtional Materials
watch out for the encoding of the csv file! When reading the file with the
default encoding of `utf-8`, then there will be a mysterious set of characters
appended to the front of the file text: ï»¿

either use parameter `encoding = "utf-8-sig` when reading the file, or manually
remove the first 3 characters from the line text of the first line only.


                PART TWO
CSV files are composed of records - these are the lines in a file. Construct a class
`Record` with the following requirements:
- Stores a list of column names
- Stores a list of data values from the columns
- __init__ takes a list of column names and another list of column data to store
- Has a function GetData which takes in a singular column name and returns the relevant
 data for that column using .index on a list to find the index of a value

- Store data retrieved from the csv file in a list of records
- Fetch and print columnData from each Record to ensure that the data is stored correctly


                PART THREE
We are interested in which locations are getting below 75% visitor:sale rate.
- Using the record list only:
- Utilise the GetData function of Record to get values for "SalesLastWeek" and "VisitorsLastWeek"
- Find the percentage of visitors which make a sale
- Output all StoreLocations and sale:visitor % where the % is under 75


                PART FOUR
The latest sales data has just came in with file "StoreVisitorSalesDataLatest.csv" (LATEST_DATAFILE).
However, Loughborough's latest sales data is missing.

- Open and read the data from "LoughboroughSalesHistory.csv" into a list of records.
- Use the records GetData() function to retrieve the Sales from each week and determine the mean.
- Open and read the data from "StoreVisitorSalesDataLatest.csv" into a list of records
- Update the record for Loughborough with the mean sales value

You may want to create a function for reading files into records!
You could also implement an additional function in class Record to update data
"""