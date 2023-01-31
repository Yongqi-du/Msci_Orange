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
import datetime

if __name__ == "__main__":
    # Load data
    housing_stock = pd.read_excel("../data/HRA_stock.xlsx", engine="openpyxl")
    housing_register = pd.read_excel("../data/RBK_Housing_Register.xlsx", engine="openpyxl")

    # Sort data by BandStartDate
    housing_register_ordered_by_band_date = housing_register.sort_values(by="BandStartDate")

    # Initialize model (date of housing property)
    current_date = datetime.datetime(2014, 1, 1, 0, 0, 0)

    # Model end date
    last_row = housing_register_ordered_by_band_date.tail(1)
    final_date = last_row['BandStartDate'].dt.to_pydatetime()

    # Initialize lists of categories to use for sorting priority
    Homeless = []
    FirstTimeApplicant = []




    while current_date < final_date:
        index = 0
        row = housing_register_ordered_by_band_date.iloc[index]
        print(row)
        index += 1
        current_date = current_date + datetime.timedelta(days=1)
        print(current_date)