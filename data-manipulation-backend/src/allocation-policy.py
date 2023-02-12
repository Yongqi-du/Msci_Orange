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
from datetime import datetime, timedelta
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

    def __str__(self):
        return f"PropertyID: {self.ApplicationID}, Category: {self.Category}, BedroomSize: {self.BedroomSize}, ReleaseDate: {self.ReleaseDate}"

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

class Modeller:
    def __init__(self, startDate, endDate, currentDate=None, propertyReleaseType="Randomly"):
        self.startDate = startDate
        self.endDate = endDate
        self.currentDate = currentDate if currentDate is not None else startDate
        self.propertyReleaseType = propertyReleaseType

        self.housing_stock = pd.read_excel("../data/HRA_stock.xlsx", engine="openpyxl")
        self.housing_register = pd.read_excel("../data/RBK_Housing_Register.xlsx", engine="openpyxl")

        Applications.from_dataframe(self.housing_register)

        self.total1Bed = 58
        self.total2Bed = 53
        self.total3Bed = 29
        self.total4Bed = 2

        self.PanelMoves = 0.02
        self.Homeless = 0.04
        self.SocialServicesQuota = 0.04
        self.Transfer = 0.01
        self.HomeScheme = 0.04
        self.FirstTimeApplicants = 0.01
        self.TenantFinder = 0.01
        self.Downsizer = 0.02
        self.Decants = 0.8
    
    def setAllocationPolicy(self, PanelMoves, Homeless, SocialServicesQuota, Transfer, HomeScheme, FirstTimeApplicants, TenantFinder, Downsizer, Decants):
        self.PanelMoves = PanelMoves
        self.Homeless = Homeless
        self.SocialServicesQuota = SocialServicesQuota
        self.Transfer = Transfer
        self.HomeScheme = HomeScheme
        self.FirstTimeApplicants = FirstTimeApplicants
        self.TenantFinder = TenantFinder
        self.Downsizer = Downsizer
        self.Decants = Decants

    def assignHouseToCategory(self):
        BedroomSize = 1
        Property.generateProperties()

    def displayCurrentDate(self):
        print("The current date is:", self.currentDate)

    def increment_date(self):
        self.currentDate += timedelta(days=1)
        if self.currentDate > self.endDate:
            return False
        return True

    '''
    Returns the number of applicants waiting and assigned for the day
    '''
    # def dayAllocation

    '''
    Returns the number of applicants waiting and assigned for the week
    '''
    # def weekAllocation

    '''
    Returns the number of applicants waiting and assigned for the month
    '''
    # def monthAllocation

    '''
    Returns the number of applicants waiting and assigned for the quarter
    '''
    # def quarterAllocation
    


    

if __name__ == "__main__":
    housing_stock, housing_register = loadDataFromExcel()
    
    Applications.from_dataframe(housing_register)
    # applicationsByCategory = Applications.getApplicationsByCategory("Transfer")
    applications = Applications.getApplicationsBySize(4)
    for application in applications:
        print(application)

