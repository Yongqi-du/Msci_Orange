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


def loadDataFromExcel():
    # Load Data
    housing_stock = pd.read_excel("../data/HRA_stock.xlsx", engine="openpyxl")
    housing_register = pd.read_excel("../data/RBK_Housing_Register.xlsx", engine="openpyxl")

    return housing_stock, housing_register

def setPropertyAmount():
    total1Bed = 58
    total2Bed = 53
    total3Bed = 29
    total4Bed = 2

    Decants = 0.8
    SocialServicesQuota = 0.04


if __name__ == "__main__":
    housing_stock, housing_register = loadDataFromExcel()
    
    Applications.from_dataframe(housing_register)
    # applicationsByCategory = Applications.getApplicationsByCategory("Transfer")
    applications = Applications.getApplicationsBySize(4)
    for application in applications:
        print(application)

