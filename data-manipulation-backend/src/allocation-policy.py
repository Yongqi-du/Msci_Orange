'''
Allocation Policy

Applications
ApplicationID | Band | Category | Bedroom | BandStartDate | Wait Time


Property
PropertyID | Bedroom | Category | ReleaseDate
ReleaseDate
    1. Do we assume properties open up after certain times
        Apparently council get access to homes every year (58 1 bed flats, 53 2 bed flats, etc)
    2. Can we get some tracking information on property availability

Order applications by BandStartDate
Initialize current_date to track allocation process
while loop to (while current_date < latest date in data)
    add applications who have the same BandStartDate as current_date to pool
    sort applications by Category
    Category is split by Band
    Band is ordered by BandStartDate
    bands are connected in order (1 to 5)
    if current_date == Property.ReleaseDate
        check category of property
        find highest priority in fitting applications
    increment application's waiting time
    increment current_date
'''

import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    housing_stock = pd.read_excel("..\\data\\HRA_stock.xlsx", engine="openpyxl")
    housing_register = pd.read_excel("..\\data\\RBK_Housing_Register.xlsx", engine="openpyxl")
    print(housing_stock)
    # print(housing_register)
    housing_register_banded = housing_register.value_counts("Band").sort_index()
    print(housing_register_banded)

