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

def sort_category_by_band(current_application, current_application_band, current_application_id):
    '''
    Assign application to corresponding list based on AppCategory
    '''
    current_application_category = current_application["AppCategory"]
    if current_application_category == "Armed Forces Personnel":
        if current_application_band == "Band 1":
            ArmedForcesPersonnel[0].append(current_application_id)
        elif current_application_band == "Band 2":
            ArmedForcesPersonnel[1].append(current_application_id)
        elif current_application_band == "Band 3":
            ArmedForcesPersonnel[2].append(current_application_id)
        elif current_application_band == "Band 4":
            ArmedForcesPersonnel[3].append(current_application_id)
        elif current_application_band == "Band 5":
            ArmedForcesPersonnel[4].append(current_application_id)

    elif current_application_category == "Armed Forces Veterans":
        if current_application_band == "Band 1":
            ArmedForcesVeterans[0].append(current_application_id)
        elif current_application_band == "Band 2":
            ArmedForcesVeterans[1].append(current_application_id)
        elif current_application_band == "Band 3":
            ArmedForcesVeterans[2].append(current_application_id)
        elif current_application_band == "Band 4":
            ArmedForcesVeterans[3].append(current_application_id)
        elif current_application_band == "Band 5":
            ArmedForcesVeterans[4].append(current_application_id)

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

    elif current_application_category == "Grypsy & Travellers":
        if current_application_band == "Band 1":
            GypsyAndTravellers[0].append(current_application_id)
        elif current_application_band == "Band 2":
            GypsyAndTravellers[1].append(current_application_id)
        elif current_application_band == "Band 3":
            GypsyAndTravellers[2].append(current_application_id)
        elif current_application_band == "Band 4":
            GypsyAndTravellers[3].append(current_application_id)
        elif current_application_band == "Band 5":
            GypsyAndTravellers[4].append(current_application_id)

    elif current_application_category == "home scheme":
        if current_application_band == "Band 1":
            homescheme[0].append(current_application_id)
        elif current_application_band == "Band 2":
            homescheme[1].append(current_application_id)
        elif current_application_band == "Band 3":
            homescheme[2].append(current_application_id)
        elif current_application_band == "Band 4":
            homescheme[3].append(current_application_id)
        elif current_application_band == "Band 5":
            homescheme[4].append(current_application_id)
            
    elif current_application_category == "Homeless":
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

    elif current_application_category == "Mobility Schemes (Pan London)":
        if current_application_band == "Band 1":
            MobilitySchemes[0].append(current_application_id)
        elif current_application_band == "Band 2":
            MobilitySchemes[1].append(current_application_id)
        elif current_application_band == "Band 3":
            MobilitySchemes[2].append(current_application_id)
        elif current_application_band == "Band 4":
            MobilitySchemes[3].append(current_application_id)
        elif current_application_band == "Band 5":
            MobilitySchemes[4].append(current_application_id)

    elif current_application_category == "Panel moves":
        if current_application_band == "Band 1":
            MobilitySchemes[0].append(current_application_id)
        elif current_application_band == "Band 2":
            MobilitySchemes[1].append(current_application_id)
        elif current_application_band == "Band 3":
            MobilitySchemes[2].append(current_application_id)
        elif current_application_band == "Band 4":
            MobilitySchemes[3].append(current_application_id)
        elif current_application_band == "Band 5":
            MobilitySchemes[4].append(current_application_id)

    elif current_application_category == "Panel moves":
        if current_application_band == "Band 1":
            PanelMoves[0].append(current_application_id)
        elif current_application_band == "Band 2":
            PanelMoves[1].append(current_application_id)
        elif current_application_band == "Band 3":
            PanelMoves[2].append(current_application_id)
        elif current_application_band == "Band 4":
            PanelMoves[3].append(current_application_id)
        elif current_application_band == "Band 5":
            PanelMoves[4].append(current_application_id)

    elif current_application_category == "Permanent Decants":
        if current_application_band == "Band 1":
            PermanentDecants[0].append(current_application_id)
        elif current_application_band == "Band 2":
            PermanentDecants[1].append(current_application_id)
        elif current_application_band == "Band 3":
            PermanentDecants[2].append(current_application_id)
        elif current_application_band == "Band 4":
            PermanentDecants[3].append(current_application_id)
        elif current_application_band == "Band 5":
            PermanentDecants[4].append(current_application_id)

    elif current_application_category == "Sheltered":
        if current_application_band == "Band 1":
            Sheltered[0].append(current_application_id)
        elif current_application_band == "Band 2":
            Sheltered[1].append(current_application_id)
        elif current_application_band == "Band 3":
            Sheltered[2].append(current_application_id)
        elif current_application_band == "Band 4":
            Sheltered[3].append(current_application_id)
        elif current_application_band == "Band 5":
            Sheltered[4].append(current_application_id)

    elif current_application_category == "Social Services Quota (adult)":
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

    elif current_application_category == "Social Services Quota (Children)":
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

    elif current_application_category == "Spare Room downsizer":
        if current_application_band == "Band 1":
            SpareRoomDownsizer[0].append(current_application_id)
        elif current_application_band == "Band 2":
            SpareRoomDownsizer[1].append(current_application_id)
        elif current_application_band == "Band 3":
            SpareRoomDownsizer[2].append(current_application_id)
        elif current_application_band == "Band 4":
            SpareRoomDownsizer[3].append(current_application_id)
        elif current_application_band == "Band 5":
            SpareRoomDownsizer[4].append(current_application_id)

    elif current_application_category == "Staff rehousing":
        if current_application_band == "Band 1":
            StaffRehousing[0].append(current_application_id)
        elif current_application_band == "Band 2":
            StaffRehousing[1].append(current_application_id)
        elif current_application_band == "Band 3":
            StaffRehousing[2].append(current_application_id)
        elif current_application_band == "Band 4":
            StaffRehousing[3].append(current_application_id)
        elif current_application_band == "Band 5":
            StaffRehousing[4].append(current_application_id)

    elif current_application_category == "Temporary Decants":
        if current_application_band == "Band 1":
            TemporaryDecants[0].append(current_application_id)
        elif current_application_band == "Band 2":
            TemporaryDecants[1].append(current_application_id)
        elif current_application_band == "Band 3":
            TemporaryDecants[2].append(current_application_id)
        elif current_application_band == "Band 4":
            TemporaryDecants[3].append(current_application_id)
        elif current_application_band == "Band 5":
            TemporaryDecants[4].append(current_application_id)

    elif current_application_category == "Tenant Finder Service (TFS) Prevention":
        if current_application_band == "Band 1":
            TenantFinderServicePrevention[0].append(current_application_id)
        elif current_application_band == "Band 2":
            TenantFinderServicePrevention[1].append(current_application_id)
        elif current_application_band == "Band 3":
            TenantFinderServicePrevention[2].append(current_application_id)
        elif current_application_band == "Band 4":
            TenantFinderServicePrevention[3].append(current_application_id)
        elif current_application_band == "Band 5":
            TenantFinderServicePrevention[4].append(current_application_id)

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

    elif current_application_category == "Under occupier":
        if current_application_band == "Band 1":
            UnderOccupier[0].append(current_application_id)
        elif current_application_band == "Band 2":
            UnderOccupier[1].append(current_application_id)
        elif current_application_band == "Band 3":
            UnderOccupier[2].append(current_application_id)
        elif current_application_band == "Band 4":
            UnderOccupier[3].append(current_application_id)
        elif current_application_band == "Band 5":
            UnderOccupier[4].append(current_application_id)

def randomGenerateProperty(num1Bed, total1Bed, num2Bed, total2Bed, num3Bed, total3Bed, num4Bed, total4Bed):
    avail1Bed = False
    avail2Bed = False
    avail3Bed = False
    avail4Bed = False
    if num1Bed < total1Bed:
        avail1Bed = True
    if num2Bed < total2Bed:
        avail2Bed = True
    if num3Bed < total3Bed:
        avail3Bed = True
    if num4Bed < total4Bed:
        avail4Bed = True
    return (avail1Bed, avail2Bed, avail3Bed, avail4Bed)


if __name__ == "__main__":
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
    ArmedForcesPersonnel = [[], [], [], [], []]
    ArmedForcesVeterans = [[], [], [], [], []]
    FirstTimeApplicant = [[], [], [], [], []]
    GypsyAndTravellers=[[], [], [], [], []]
    homescheme = [[], [], [], [], []]
    Homeless = [[], [], [], [], []]
    MobilitySchemes = [[], [], [], [], []]
    PanelMoves = [[], [], [], [], []]
    PermanentDecants = [[], [], [], [], []]
    Sheltered = [[], [], [], [], []]
    SocialServicesQuota = [[], [], [], [], []]
    SpareRoomDownsizer = [[], [], [], [], []]
    StaffRehousing = [[], [], [], [], []]
    TemporaryDecants = [[], [], [], [], []]
    TenantFinderServicePrevention = [[], [], [], [], []]
    Transfer = [[], [], [], [], []]
    UnderOccupier = [[], [], [], [], []]

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

