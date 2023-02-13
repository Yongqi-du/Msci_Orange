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

    @classmethod
    def assignProperty(cls, BedroomSize, Category):
        # Find a property instance with the same BedroomSize and Category
        for property in cls.instances:
            if property.BedroomSize == BedroomSize and property.Category == Category:
                # Remove the property instance from instances and return it
                cls.instances.remove(property)
                return property

        # If no matching property instance is found, return None
        return None

class Applications:
    instances = []
    
    def __init__(self, ID, Band, Category, BedroomSize, StartDate):
        self.ApplicationID = ID
        self.Band = Band
        self.Category = Category
        self.BedroomSize = BedroomSize
        self.StartDate = StartDate
        self.WaitTime = 0
        Applications.instances.append(self)

    def __str__(self):
        return f"  ApplicationID: {self.ApplicationID}, Band: {self.Band}, Category: {self.Category}, BedroomSize: {self.BedroomSize}, StartDate: {self.StartDate}"
    
    @classmethod
    def getApplicationsByBand(cls, Band):
        return [applications for applications in cls.instances if applications.Band == Band]
    
    @classmethod
    def getApplicationsBySize(cls, BedroomSize):
        return [applications for applications in cls.instances if applications.BedroomSize == BedroomSize]

    @classmethod
    def getApplicationsByCategory(cls, Category):
        return [applications for applications in cls.instances if applications.Category == Category]

    @classmethod
    def getApplicationsByDate(cls, Date):
        datetime_date = datetime.datetime.combine(Date, datetime.datetime.min.time())
        return [application for application in cls.instances if application.StartDate == datetime_date]


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
    
    @classmethod
    def getApplicationsBySizeAndCategory(cls, BedroomSize, Category):
        # Find all application instances of the requested BedroomSize and Category
        applications = [application for application in cls.instances if application.BedroomSize == BedroomSize and application.Category == Category]

        # Split the applications into lists based on their Band
        band_applications = {}
        for application in applications:
            if application.Band not in band_applications:
                band_applications[application.Band] = []
            band_applications[application.Band].append(application)
        
        # Sort each band list by their StartDate
        for band, application_list in band_applications.items():
            application_list.sort(key=lambda x: x.StartDate)

        # Return the dictionary of band applications
        return band_applications

    @classmethod
    def findPriority(cls, BedroomSize, Category):
        waitingList = Applications.getApplicationsBySizeAndCategory(BedroomSize, Category)
        # Find the list in band_applications with the lowest numbered band
        priority_band = min(waitingList.keys())

        # Return the first element of the priority_band list, if it exists
        priority_list = waitingList.get(priority_band, [])
        if priority_list:
            candidate = priority_list[0]
            cls.instances.remove(candidate)
            return candidate

        # If no priority_list is found, return None
        return None

class Modeller:
    policy = {
        "PanelMoves": 0.02,
        "Homeless": 0.04,
        "SocialServicesQuota": 0.04,
        "Transfer": 0.01,
        "HomeScheme": 0.04,
        "FirstTimeApplicants": 0.01,
        "TenantFinder": 0.01,
        "Downsizer": 0.02,
        "Decants": 0.8
    }

    supply = {
        "1": 58,
        "2": 53,
        "3": 29,
        "4": 2
    }

    def __init__(self, startDate, endDate, currentDate=None, propertyReleaseType="Randomly"):
        self.startDate = startDate
        self.endDate = endDate
        self.currentDate = currentDate if currentDate is not None else startDate
        self.propertyReleaseType = propertyReleaseType

        self.housing_stock = pd.read_excel("../data/HRA_stock.xlsx", engine="openpyxl")
        self.housing_register = pd.read_excel("../data/RBK_Housing_Register.xlsx", engine="openpyxl")

        Applications.from_dataframe(self.housing_register)

        self.assignHouseToCategory(1, "Decants")

        while self.currentDate < self.endDate:
            self.displayCurrentDate()
            # print(self.currentDate)
            todayApplication = Applications.getApplicationsByDate(self.currentDate)
            for application in todayApplication:
                print(application)
            self.currentDate += datetime.timedelta(days=1)
        
        print("Terminating Model")
        exit()

    
    def setAllocationPolicy(self, PanelMoves, Homeless, SocialServicesQuota, Transfer, HomeScheme, FirstTimeApplicants, TenantFinder, Downsizer, Decants):
        # Update the policy dictionary with the new values
        self.policy["PanelMoves"] = PanelMoves
        self.policy["Homeless"] = Homeless
        self.policy["SocialServicesQuota"] = SocialServicesQuota
        self.policy["Transfer"] = Transfer
        self.policy["HomeScheme"] = HomeScheme
        self.policy["FirstTimeApplicants"] = FirstTimeApplicants
        self.policy["TenantFinder"] = TenantFinder
        self.policy["Downsizer"] = Downsizer
        self.policy["Decants"] = Decants

    def assignHouseToCategory(self, BedroomSize, Category):
        total = self.supply[str(BedroomSize)]
        assignedForCategory = int(total * self.policy[Category])

        Property.generateProperties(BedroomSize, Category, self.currentDate, assignedForCategory)
        

    def displayCurrentDate(self):
        print("The current date is:", self.currentDate)

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
    
    modeller = Modeller(startDate=datetime.date(2022, 1, 1), endDate=datetime.date(2022, 12, 31))



