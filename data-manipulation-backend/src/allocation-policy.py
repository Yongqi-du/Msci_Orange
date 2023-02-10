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
import random

def sort_category_by_band(current_application, current_application_band, current_application_id):
    '''
    Assign application to corresponding list based on AppCategory
    '''
    current_application_category = current_application["AppCategory"]
    if current_application_category == "Armed Forces Personnel" or current_application_category == "Armed Forces Veterans" or current_application_category == "Mobility Schemes (Pan London)" or current_application_category == "Staff rehousing" or current_application_category == "Sheltered":
        if current_application_band == "Band 1":
            Other[0].append(current_application_id)
        elif current_application_band == "Band 2":
            Other[1].append(current_application_id)
        elif current_application_band == "Band 3":
            Other[2].append(current_application_id)
        elif current_application_band == "Band 4":
            Other[3].append(current_application_id)
        elif current_application_band == "Band 5":
            Other[4].append(current_application_id)

    elif current_application_category == "First time applicants":
        if current_application_band == "Band 1":
            FirstTimeApplicant[0].append(current_application_id)
        elif current_application_band == "Band 2":
            FirstTimeApplicant[1].append(current_application_id)
        elif current_application_band == "Band 3":
            FirstTimeApplicant[2].append(current_application_id)
        elif current_application_band == "Band 4":
            FirstTimeApplicant[3].append(current_application_id)
        elif current_application_band == "Band 5":
            FirstTimeApplicant[4].append(current_application_id)

    elif current_application_category == "Grypsy & Travellers" or current_application_category == "Homeless":
        if current_application_band == "Band 1":
            Homeless[0].append(current_application_id)
        elif current_application_band == "Band 2":
            Homeless[1].append(current_application_id)
        elif current_application_band == "Band 3":
            Homeless[2].append(current_application_id)
        elif current_application_band == "Band 4":
            Homeless[3].append(current_application_id)
        elif current_application_band == "Band 5":
            Homeless[4].append(current_application_id)

    elif current_application_category == "home scheme":
        if current_application_band == "Band 1":
            HomeScheme[0].append(current_application_id)
        elif current_application_band == "Band 2":
            HomeScheme[1].append(current_application_id)
        elif current_application_band == "Band 3":
            HomeScheme[2].append(current_application_id)
        elif current_application_band == "Band 4":
            HomeScheme[3].append(current_application_id)
        elif current_application_band == "Band 5":
            HomeScheme[4].append(current_application_id)

    elif current_application_category == "Panel moves":
        if current_application_band == "Band 1":
            Emergency[0].append(current_application_id)
        elif current_application_band == "Band 2":
            Emergency[1].append(current_application_id)
        elif current_application_band == "Band 3":
            Emergency[2].append(current_application_id)
        elif current_application_band == "Band 4":
            Emergency[3].append(current_application_id)
        elif current_application_band == "Band 5":
            Emergency[4].append(current_application_id)

    elif current_application_category == "Permanent Decants" or current_application_category == "Temporary Decants":
        if current_application_band == "Band 1":
            Decants[0].append(current_application_id)
        elif current_application_band == "Band 2":
            Decants[1].append(current_application_id)
        elif current_application_band == "Band 3":
            Decants[2].append(current_application_id)
        elif current_application_band == "Band 4":
            Decants[3].append(current_application_id)
        elif current_application_band == "Band 5":
            Decants[4].append(current_application_id)

    elif current_application_category == "Social Services Quota (adult)" or current_application_category == "Social Services Quota (Children)":
        if current_application_band == "Band 1":
            SocialServicesQuota[0].append(current_application_id)
        elif current_application_band == "Band 2":
            SocialServicesQuota[1].append(current_application_id)
        elif current_application_band == "Band 3":
            SocialServicesQuota[2].append(current_application_id)
        elif current_application_band == "Band 4":
            SocialServicesQuota[3].append(current_application_id)
        elif current_application_band == "Band 5":
            SocialServicesQuota[4].append(current_application_id)

    elif current_application_category == "Spare Room downsizer" or current_application_category == "Under occupier":
        if current_application_band == "Band 1":
            Downsizer[0].append(current_application_id)
        elif current_application_band == "Band 2":
            Downsizer[1].append(current_application_id)
        elif current_application_band == "Band 3":
            Downsizer[2].append(current_application_id)
        elif current_application_band == "Band 4":
            Downsizer[3].append(current_application_id)
        elif current_application_band == "Band 5":
            Downsizer[4].append(current_application_id)

    elif current_application_category == "Tenant Finder Service (TFS) Prevention":
        if current_application_band == "Band 1":
            TenantFinder[0].append(current_application_id)
        elif current_application_band == "Band 2":
            TenantFinder[1].append(current_application_id)
        elif current_application_band == "Band 3":
            TenantFinder[2].append(current_application_id)
        elif current_application_band == "Band 4":
            TenantFinder[3].append(current_application_id)
        elif current_application_band == "Band 5":
            TenantFinder[4].append(current_application_id)

    elif current_application_category == "Transfer":
        if current_application_band == "Band 1":
            Transfer[0].append(current_application_id)
        elif current_application_band == "Band 2":
            Transfer[1].append(current_application_id)
        elif current_application_band == "Band 3":
            Transfer[2].append(current_application_id)
        elif current_application_band == "Band 4":
            Transfer[3].append(current_application_id)
        elif current_application_band == "Band 5":
            Transfer[4].append(current_application_id)

# def randomGenerateProperty(num1Bed, total1Bed, num2Bed, total2Bed, num3Bed, total3Bed, num4Bed, total4Bed):
#     avail1Bed = False
#     avail2Bed = False
#     avail3Bed = False
#     avail4Bed = False
#     if num1Bed < total1Bed:
#         randomNum = random.random()
#         if randomNum >= 0.5:
#             avail1Bed = True
#     if num2Bed < total2Bed:
#         randomNum = random.random()
#         if randomNum >= 0.5:
#             avail2Bed = True
#     if num3Bed < total3Bed:
#         randomNum = random.random()
#         if randomNum >= 0.5:
#             avail3Bed = True
#     if num4Bed < total4Bed:
#         randomNum = random.random()
#         if randomNum >= 0.5:
#             avail4Bed = True
#     return (avail1Bed, avail2Bed, avail3Bed, avail4Bed)

# def randomCategoryAssigner():
#     randomNum = random.random()
#     if randomNum <= 0.8:
#         category = "Decants"
#     elif randomNum <= 0.84:
#         category = "Homeless"
#     elif randomNum <= 0.85:
#         category = "Transfer"
#     elif randomNum <= 0.87:
#         category = "Emergency"
#     elif randomNum <= 0.89:
#         category = "Downsizer"
#     elif randomNum <= 0.90:
#         category = "First Time Applicant"
#     elif randomNum <= 0.94:
#         category = "Home Scheme"
#     elif randomNum <= 0.98:
#         category = "Social Service Quota"
#     elif randomNum <= 0.99:
#         category = "Tenant Finder"
#     else:
#         category = "Other"
#     return category

def initialiseProperties(size:int, totalAvail:int, allocationPolicy):
    properties = [[]]

if __name__ == "__main__":
    # Define Allocation Policy
    # [Decants, Homeless, Transfer, Emergency, Downsizer, FirstTimeApplicant, HomeScheme, SocialService, TenantFinder, Other]
    AllocationPolicy = {"Decant": 0.8, "Homeless": 0.04, "Transfer": 0.01, "Emergency": 0.02, "Downsizer": 0.02, "FirstTimeApplicant": 0.01, "HomeScheme": 0.04, "SocialServiceQuota": 0.04, "TenantFinder": 0.01, "Other": 0.01}

    # Load data
    housing_stock = pd.read_excel("../data/HRA_stock.xlsx", engine="openpyxl")
    housing_register = pd.read_excel("../data/RBK_Housing_Register.xlsx", engine="openpyxl")

    # Sort data by BandStartDate
    housing_register_ordered_by_band_date = housing_register.sort_values(by="BandStartDate")

    # Initialize model (date of housing property)
    current_date = datetime.datetime(2022, 7, 31, 0, 0, 0)

    # Model end date
    last_row = housing_register_ordered_by_band_date.tail(1)
    # final_date = last_row['BandStartDate'].dt.to_pydatetime()
    final_date = datetime.datetime(2022, 10, 1, 0, 0, 0)

    # Initialize lists of categories to use for sorting priority
    Decants  = [[], [], [], [], []]
    Homeless  = [[], [], [], [], []]
    Transfer  = [[], [], [], [], []]
    Emergency = [[], [], [], [], []]
    Downsizer = [[], [], [], [], []]
    FirstTimeApplicant = [[], [], [], [], []]
    HomeScheme = [[], [], [], [], []]
    SocialServicesQuota = [[], [], [], [], []]
    TenantFinder = [[], [], [], [], []]
    Other = [[], [], [], [], []]

    # Keep track of each property types released
    num1Bed = 0
    total1Bed = 58
    num2Bed = 0
    total2Bed = 53
    num3Bed = 0
    total3Bed = 40
    num4Bed = 0
    total4Bed = 20

    '''
    Run model until date is past final_date
    Final_date can be:
        1. latest date in data
        2. target date to run modelling
    '''
    index = 0
    maxIndex = len(housing_register_ordered_by_band_date)-1
    # print(maxIndex)
    while current_date < final_date:
        '''
        Increment index until row's BandStartDate is larger than current date
        '''
        current_application = housing_register_ordered_by_band_date.iloc[index]
        current_application_date = current_application["BandStartDate"]
        # print(current_application_date)

        while current_application_date < current_date:
            if index < maxIndex:
                index += 1
                # print(index)
                current_application = housing_register_ordered_by_band_date.iloc[index]
                current_application_date = current_application["BandStartDate"]
                current_application_id = current_application["ApplicationId"]
                current_application_band = current_application['Band']
                
                sort_category_by_band(current_application, current_application_band, current_application_id)

            else: 
                break
        
        '''
        Randomly release properties each day
        1. Keep track of expected number of property per year
        2. If that number has not been reached, generate a random number 
        '''
        avail1Bed, avail2Bed, avail3Bed, avail4Bed = randomGenerateProperty(num1Bed, total1Bed, num2Bed, total2Bed, num3Bed, total3Bed, num4Bed, total4Bed)

        
        # print(current_application_date)
        # print(index)
        
        current_date = current_date + datetime.timedelta(days=1)
        # print(current_date)

    print(UnderOccupier)

