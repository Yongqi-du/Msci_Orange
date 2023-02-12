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

class Property:
    id_counter = 0
    instances = []

    def __init__(self, BedroomSize, Category, ReleaseDate):
        self.PropertyID = Property.id_counter
        Property.id_counter += 1
        self.BedroomSize = BedroomSize
        self.Category = Category
        self.ReleaseDate = ReleaseDate
        Property.instances.append(self)

    @classmethod
    def getPropertiesByRoomSize(cls, BedroomSize):
        return [property for property in cls.instances if property.BedroomSize == BedroomSize]

    @classmethod
    def getPropertiesByCategory(cls, Category):
        return [property for property in cls.instances if property.Category == Category]

    @classmethod
    def getPropertiesByDate(cls, Date):
        return [property for property in cls.instances if property.ReleaseDate == Date]
    
    @classmethod
    def generateProperties(cls, BedroomSize, Category, ReleaseDate, number):
        for i in range(number):
            cls(BedroomSize, Category, ReleaseDate)

class Applications:
    instances = []
    categories = {}
    
    def __init__(self, ID, Band, Category, BedroomSize, StartDate):
        self.ApplicationID = ID
        self.Band = Band
        self.Category = Category
        self.BedroomSize = BedroomSize
        self.StartDate = StartDate
        self.WaitTime = 0
        Applications.instances.append(self)
        
        if Category not in Applications.categories:
            Applications.categories[Category] = {}
        if Band not in Applications.categories[Category]:
            Applications.categories[Category][Band] = []
        Applications.categories[Category][Band].append(self)
        Applications.categories[Category][Band].sort(key=lambda x: x.StartDate)

    def __str__(self):
        return f"ApplicationID: {self.ApplicationID}, Band: {self.Band}, Category: {self.Category}, BedroomSize: {self.BedroomSize}, StartDate: {self.StartDate}"
    
    @classmethod
    def getApplicationsByBand(cls, Band):
        return [applications for applications in cls.instances if applications.Band == Band]
    
    @classmethod
    def getApplicationsBySize(cls, BedroomSize):
        return [applications for applications in cls.instances if applications.BedroomSize == BedroomSize]

    @classmethod
    def getApplicationsByCategory(cls, Category):
        return cls.categories.get(Category, [])

    @classmethod
    def from_dataframe(cls, df):
        for index, row in df.iterrows():
            if index is None or row is None:
                break
            if any(pd.isna(row)):
                continue
            ID = row.get('ApplicationId', None)
            Band = row.get('Band', 5)
            Category = row.get('AppCategory', "Other")
            BedroomSize = row.get('Bedroom', "1")
            StartDate = row['BandStartDate']
            cls(ID, Band, Category, BedroomSize, StartDate)


def loadDataFromExcel():
    # Load Data
    housing_stock = pd.read_excel("../data/HRA_stock.xlsx", engine="openpyxl")
    housing_register = pd.read_excel("../data/RBK_Housing_Register.xlsx", engine="openpyxl")

    return housing_stock, housing_register

if __name__ == "__main__":
    housing_stock, housing_register = loadDataFromExcel()
    
    Applications.from_dataframe(housing_register)
    # applicationsByCategory = Applications.getApplicationsByCategory("Transfer")
    applications = Applications.getApplicationsBySize(4)
    for application in applications:
        print(application)


def sort_category_by_band(current_application, current_application_band, current_application_id):
    '''
    Assign application to corresponding list based on AppCategory
    '''
    current_application_category = current_application["AppCategory"]
    try:
        current_application_size = int(current_application["Bedroom"]) - 1
    except ValueError:
        current_application_size = 0


    if current_application_category == "Armed Forces Personnel" or current_application_category == "Armed Forces Veterans" or current_application_category == "Mobility Schemes (Pan London)" or current_application_category == "Staff rehousing" or current_application_category == "Sheltered":
        if current_application_band == "Band 1":
            Other[current_application_size][0].append(current_application_id)
        elif current_application_band == "Band 2":
            Other[current_application_size][1].append(current_application_id)
        elif current_application_band == "Band 3":
            Other[current_application_size][2].append(current_application_id)
        elif current_application_band == "Band 4":
            Other[current_application_size][3].append(current_application_id)
        elif current_application_band == "Band 5":
            Other[current_application_size][4].append(current_application_id)

    elif current_application_category == "First time applicants":
        if current_application_band == "Band 1":
            FirstTimeApplicant[current_application_size][0].append(current_application_id)
        elif current_application_band == "Band 2":
            FirstTimeApplicant[current_application_size][1].append(current_application_id)
        elif current_application_band == "Band 3":
            FirstTimeApplicant[current_application_size][2].append(current_application_id)
        elif current_application_band == "Band 4":
            FirstTimeApplicant[current_application_size][3].append(current_application_id)
        elif current_application_band == "Band 5":
            FirstTimeApplicant[current_application_size][4].append(current_application_id)

    elif current_application_category == "Grypsy & Travellers" or current_application_category == "Homeless":
        if current_application_band == "Band 1":
            Homeless[current_application_size][0].append(current_application_id)
        elif current_application_band == "Band 2":
            Homeless[current_application_size][1].append(current_application_id)
        elif current_application_band == "Band 3":
            Homeless[current_application_size][2].append(current_application_id)
        elif current_application_band == "Band 4":
            Homeless[current_application_size][3].append(current_application_id)
        elif current_application_band == "Band 5":
            Homeless[current_application_size][4].append(current_application_id)

    elif current_application_category == "home scheme":
        if current_application_band == "Band 1":
            HomeScheme[current_application_size][0].append(current_application_id)
        elif current_application_band == "Band 2":
            HomeScheme[current_application_size][1].append(current_application_id)
        elif current_application_band == "Band 3":
            HomeScheme[current_application_size][2].append(current_application_id)
        elif current_application_band == "Band 4":
            HomeScheme[current_application_size][3].append(current_application_id)
        elif current_application_band == "Band 5":
            HomeScheme[current_application_size][4].append(current_application_id)

    elif current_application_category == "Panel moves":
        if current_application_band == "Band 1":
            Emergency[current_application_size][0].append(current_application_id)
        elif current_application_band == "Band 2":
            Emergency[current_application_size][1].append(current_application_id)
        elif current_application_band == "Band 3":
            Emergency[current_application_size][2].append(current_application_id)
        elif current_application_band == "Band 4":
            Emergency[current_application_size][3].append(current_application_id)
        elif current_application_band == "Band 5":
            Emergency[current_application_size][4].append(current_application_id)

    elif current_application_category == "Permanent Decants" or current_application_category == "Temporary Decants":
        if current_application_band == "Band 1":
            Decants[current_application_size][0].append(current_application_id)
        elif current_application_band == "Band 2":
            Decants[current_application_size][1].append(current_application_id)
        elif current_application_band == "Band 3":
            Decants[current_application_size][2].append(current_application_id)
        elif current_application_band == "Band 4":
            Decants[current_application_size][3].append(current_application_id)
        elif current_application_band == "Band 5":
            Decants[current_application_size][4].append(current_application_id)

    elif current_application_category == "Social Services Quota (adult)" or current_application_category == "Social Services Quota (Children)":
        if current_application_band == "Band 1":
            SocialServicesQuota[current_application_size][0].append(current_application_id)
        elif current_application_band == "Band 2":
            SocialServicesQuota[current_application_size][1].append(current_application_id)
        elif current_application_band == "Band 3":
            SocialServicesQuota[current_application_size][2].append(current_application_id)
        elif current_application_band == "Band 4":
            SocialServicesQuota[current_application_size][3].append(current_application_id)
        elif current_application_band == "Band 5":
            SocialServicesQuota[current_application_size][4].append(current_application_id)

    elif current_application_category == "Spare Room downsizer" or current_application_category == "Under occupier":
        if current_application_band == "Band 1":
            Downsizer[current_application_size][0].append(current_application_id)
        elif current_application_band == "Band 2":
            Downsizer[current_application_size][1].append(current_application_id)
        elif current_application_band == "Band 3":
            Downsizer[current_application_size][2].append(current_application_id)
        elif current_application_band == "Band 4":
            Downsizer[current_application_size][3].append(current_application_id)
        elif current_application_band == "Band 5":
            Downsizer[current_application_size][4].append(current_application_id)

    elif current_application_category == "Tenant Finder Service (TFS) Prevention":
        if current_application_band == "Band 1":
            TenantFinder[current_application_size][0].append(current_application_id)
        elif current_application_band == "Band 2":
            TenantFinder[current_application_size][1].append(current_application_id)
        elif current_application_band == "Band 3":
            TenantFinder[current_application_size][2].append(current_application_id)
        elif current_application_band == "Band 4":
            TenantFinder[current_application_size][3].append(current_application_id)
        elif current_application_band == "Band 5":
            TenantFinder[current_application_size][4].append(current_application_id)

    elif current_application_category == "Transfer":
        if current_application_band == "Band 1":
            Transfer[current_application_size][0].append(current_application_id)
        elif current_application_band == "Band 2":
            Transfer[current_application_size][1].append(current_application_id)
        elif current_application_band == "Band 3":
            Transfer[current_application_size][2].append(current_application_id)
        elif current_application_band == "Band 4":
            Transfer[current_application_size][3].append(current_application_id)
        elif current_application_band == "Band 5":
            Transfer[current_application_size][4].append(current_application_id)

def initialiseProperties(size: int, totalAvail: int, allocationPolicy):
    properties = []
    for category, percentage in allocationPolicy.items():
        allocation = int(totalAvail * percentage)
        for i in range(allocation):
            properties.append([size, category])
    return properties

def allocateProperty(size, category):
    if category == "Decants":
        validCandidates = Decants[size-1]
    elif category == "Homeless":
        validCandidates = Homeless[size-1]
    elif category == "Transfer":
        validCandidates = Transfer[size-1]
    elif category == "Emergency":
        validCandidates = Emergency[size-1]
    elif category == "Downsizer":
        validCandidates = Downsizer[size-1]
    elif category == "FirstTimeApplicant":
        validCandidates = FirstTimeApplicant[size-1]
    elif category == "HomeScheme":
        validCandidates = HomeScheme[size-1]
    elif category == "SocialServicesQuota":
        validCandidates = SocialServicesQuota[size-1]
    elif category == "TenantFinder":
        validCandidates = TenantFinder[size-1]
    elif category == "Other":
        validCandidates = Other[size-1]
    else:
        return None
    for candidates in validCandidates:
        if candidates:
            property_allocated = candidates.pop(0)
            return property_allocated
    return None



# if __name__ == "__main__":
#     # Define Allocation Policy
#     # [Decants, Homeless, Transfer, Emergency, Downsizer, FirstTimeApplicant, HomeScheme, SocialService, TenantFinder, Other]
#     AllocationPolicy = {"Decant": 0.8, "Homeless": 0.04, "Transfer": 0.01, "Emergency": 0.02, "Downsizer": 0.02, "FirstTimeApplicant": 0.01, "HomeScheme": 0.04, "SocialServiceQuota": 0.04, "TenantFinder": 0.01, "Other": 0.01}

#     # Load data
#     housing_stock = pd.read_excel("../data/HRA_stock.xlsx", engine="openpyxl")
#     housing_register = pd.read_excel("../data/RBK_Housing_Register.xlsx", engine="openpyxl")

#     # Sort data by BandStartDate
#     housing_register_ordered_by_band_date = housing_register.sort_values(by="BandStartDate")

#     # Initialize model (date of housing property)
#     current_date = datetime.datetime(2022, 7, 31, 0, 0, 0)

#     # Model end date
#     last_row = housing_register_ordered_by_band_date.tail(1)
#     # final_date = last_row['BandStartDate'].dt.to_pydatetime()
#     final_date = datetime.datetime(2022, 10, 1, 0, 0, 0)

#     # Initialize lists of categories to use for sorting priority
#     Decants  = [[[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []]]
#     Homeless  = [[[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []]]
#     Transfer  = [[[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []]]
#     Emergency = [[[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []]]
#     Downsizer = [[[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []]]
#     FirstTimeApplicant = [[[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []]]
#     HomeScheme = [[[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []]]
#     SocialServicesQuota = [[[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []]]
#     TenantFinder = [[[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []]]
#     Other = [[[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []]]

#     # Keep track of each property types released
#     num1Bed = 0
#     total1Bed = 58
#     num2Bed = 0
#     total2Bed = 53
#     num3Bed = 0
#     total3Bed = 40
#     num4Bed = 0
#     total4Bed = 20

#     # Initialise lists of properties
#     list1Bed = initialiseProperties(1, total1Bed, AllocationPolicy)
#     list2Bed = initialiseProperties(2, total2Bed, AllocationPolicy)
#     list3Bed = initialiseProperties(4, total4Bed, AllocationPolicy)
#     list4Bed = initialiseProperties(4, total4Bed, AllocationPolicy)

#     '''
#     Run model until date is past final_date
#     Final_date can be:
#         1. latest date in data
#         2. target date to run modelling
#     '''
#     index = 0
#     maxIndex = len(housing_register_ordered_by_band_date)-1
#     # print(maxIndex)
#     while current_date < final_date:
#         '''
#         Increment index until row's BandStartDate is larger than current date
#         '''
#         current_application = housing_register_ordered_by_band_date.iloc[index]
#         current_application_date = current_application["BandStartDate"]
#         # print(current_application_date)

#         while current_application_date < current_date:
#             if index < maxIndex:
#                 index += 1
#                 # print(index)
#                 current_application = housing_register_ordered_by_band_date.iloc[index]
#                 current_application_date = current_application["BandStartDate"]
#                 current_application_id = current_application["ApplicationId"]
#                 current_application_band = current_application['Band']
                
#                 sort_category_by_band(current_application, current_application_band, current_application_id)

#             else: 
#                 break
        
#         '''
#         Randomly release properties each day
#         1. Keep track of expected number of property per year
#         2. If that number has not been reached, generate a random number 
#         '''
#         # avail1Bed, avail2Bed, avail3Bed, avail4Bed = randomGenerateProperty(num1Bed, total1Bed, num2Bed, total2Bed, num3Bed, total3Bed, num4Bed, total4Bed)

        
#         # print(current_application_date)
#         # print(index)
        
#         current_date = current_date + datetime.timedelta(days=1)
#         # print(current_date)
