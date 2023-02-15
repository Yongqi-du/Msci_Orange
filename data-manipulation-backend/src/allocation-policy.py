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
import csv

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
        return f"PropertyID: {self.PropertyID}, Category: {self.Category}, BedroomSize: {self.BedroomSize}, ReleaseDate: {self.ReleaseDate}"

    def getSize(self):
        return self.BedroomSize
    
    def getCategory(self):
        return self.Category

    @classmethod
    def getAllProperties(cls):
        return [properties for properties in cls.instances]
    
    @classmethod
    def getNumProperties(cls):
        return len(cls.instances)

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
    
    @classmethod
    def deleteProperty(cls, PropertyID):
        for property in cls.instances:
            if property.PropertyID == PropertyID:
                cls.instances.remove(property)
                return True
        return False

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
    def getAllApplications(cls):
        return [applications for applications in cls.instances]
    
    @classmethod
    def getNumApplications(cls):
        return len(cls.instances)

    @classmethod
    def checkExistence(cls, instance):
        if instance in cls.instances:
            return True
        else: 
            return False

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
    def getApplicationsBeforeDate(cls, Date):
        datetime_date = datetime.datetime.combine(Date, datetime.datetime.min.time())
        return [application for application in cls.instances if application.StartDate <= datetime_date]

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
            if Category == "Temporary Decants": 
                Category = "Decants"
            elif Category == "Permanent Decants":
                Category = "Decants"
            elif Category == "First time applicants":
                Category = "FirstTimeApplicant"
            elif Category == "home scheme":
                Category = "HomeScheme"
            elif Category == "Homeless":
                Category = "Homeless"
            elif Category == "Social Services Quota (adult)":
                Category = "SocialServicesQuota"
            elif Category == "Social Services Quota (Children)":
                Category = "SocialServicesQuota"
            elif Category == "Spare Room downsizer":
                Category = "Downsizer"
            elif Category == "Under occupier":
                Category = "Downsizer"
            elif Category == "Transfer":
                Category = "Transfer"
            elif Category == "Tenant Finder Service (TFS) Prevention":
                Category = "TenantFinder"
            elif Category == "Panel moves":
                Category = "PanelMoves"
            else: 
                Category = "Other"
            BedroomSize = int(row.get('Bedroom', 1))
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
        
        # Check if the dictionary is empty
        if not waitingList:
            return None
        
        # Find the list in band_applications with the lowest numbered band
        priority_band = min(waitingList.keys())

        # Return the first element of the priority_band list, if it exists
        priority_list = waitingList.get(priority_band, [])
        if priority_list:
            candidate = priority_list[0]
            # cls.instances.remove(candidate)
            return candidate

        # If no priority_list is found, return None
        return None


    @classmethod
    def removeApplicationByID(cls, ApplicationID):
        for application in cls.instances:
            if application.ApplicationID == ApplicationID:
                cls.instances.remove(application)
                return True
        return False

    @classmethod
    def removeApplication(cls, instance):
        if instance in cls.instances:
            cls.instances.remove(instance)


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
        "Decants": 0.8,
        "Other": 0.01
    }

    supply = {
        "1": 58,
        "2": 53,
        "3": 29,
        "4": 2
    }
    totalSupply = sum(supply.values())

    def __init__(self, startDate, endDate, currentDate=None, propertyReleaseType="Randomly"):
        self.startDate = startDate
        self.endDate = endDate
        self.currentDate = currentDate if currentDate is not None else startDate
        self.propertyReleaseType = propertyReleaseType

        self.housing_stock = pd.read_excel("../data/HRA_stock.xlsx", engine="openpyxl")
        self.housing_register = pd.read_excel("../data/RBK_Housing_Register.xlsx", engine="openpyxl")

        Applications.from_dataframe(self.housing_register)

        self.assignHouseToCategory(1, "Decants")
        self.assignHouseToCategory(2, "Decants")
        self.assignHouseToCategory(3, "Decants")
        self.assignHouseToCategory(4, "Decants")
        self.assignHouseToCategory(1, "PanelMoves")
        self.assignHouseToCategory(2, "PanelMoves")
        self.assignHouseToCategory(3, "PanelMoves")
        self.assignHouseToCategory(4, "PanelMoves")
        self.assignHouseToCategory(1, "Homeless")
        self.assignHouseToCategory(2, "Homeless")
        self.assignHouseToCategory(3, "Homeless")
        self.assignHouseToCategory(4, "Homeless")
        self.assignHouseToCategory(1, "SocialServicesQuota")
        self.assignHouseToCategory(2, "SocialServicesQuota")
        self.assignHouseToCategory(3, "SocialServicesQuota")
        self.assignHouseToCategory(4, "SocialServicesQuota")
        self.assignHouseToCategory(1, "Transfer")
        self.assignHouseToCategory(2, "Transfer")
        self.assignHouseToCategory(3, "Transfer")
        self.assignHouseToCategory(4, "Transfer")
        self.assignHouseToCategory(1, "HomeScheme")
        self.assignHouseToCategory(2, "HomeScheme")
        self.assignHouseToCategory(3, "HomeScheme")
        self.assignHouseToCategory(4, "HomeScheme")
        self.assignHouseToCategory(1, "FirstTimeApplicants")
        self.assignHouseToCategory(2, "FirstTimeApplicants")
        self.assignHouseToCategory(3, "FirstTimeApplicants")
        self.assignHouseToCategory(4, "FirstTimeApplicants")
        self.assignHouseToCategory(1, "TenantFinder")
        self.assignHouseToCategory(2, "TenantFinder")
        self.assignHouseToCategory(3, "TenantFinder")
        self.assignHouseToCategory(4, "TenantFinder")
        self.assignHouseToCategory(1, "Downsizer")
        self.assignHouseToCategory(2, "Downsizer")
        self.assignHouseToCategory(3, "Downsizer")
        self.assignHouseToCategory(4, "Downsizer")

        # allProperties = Property.getAllProperties()
        # for property in allProperties:
        #     print(property)

        # numOfProperties = Property.getNumProperties()
        # print(str(numOfProperties) + " properties were allocated to categories for giving out")
        # difTotalSupply = self.totalSupply - numOfProperties
        # print(str(difTotalSupply) + " properties were not used of the total supply")
        
        with open('data.csv', mode='w') as csv_file:
            fieldnames = ['Date', 'Queue', 'New', 'Resolved']
            writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            writer.writeheader()

            while self.currentDate < self.endDate:
                # self.displayCurrentDate()
                queuedApplication = Applications.getApplicationsBeforeDate(self.currentDate)
                newApplication = Applications.getApplicationsByDate(self.currentDate)
                # print(len(queuedApplication))
                resolvedApplication = self.resolveApplication()
                # resolvedApplication = 0

                writer.writerow({'Date': self.currentDate, 'Queue': len(queuedApplication), 'New': len(newApplication), 'Resolved': resolvedApplication})

                self.currentDate += datetime.timedelta(days=1)

            # Check if there are property
            
            # Find the appropriate candidate

            # Remove the candidate and the property from their appropriate instances
        
        # self.resolveApplication()

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
        total = PanelMoves + Homeless + SocialServicesQuota + Transfer + HomeScheme + FirstTimeApplicants + TenantFinder + Downsizer + Decants
        self.policy["Other"] = 1 - total

    def assignHouseToCategory(self, BedroomSize, Category):
        total = self.supply[str(BedroomSize)]
        assignedForCategory = int(total * self.policy[Category])

        Property.generateProperties(BedroomSize, Category, self.currentDate, assignedForCategory)

    def displayCurrentDate(self):
        print("The current date is:", self.currentDate)
    
    def resolveApplication(self):
        availableProperties = Property.getAllProperties()
        resolvedCounter = 0
        for property in availableProperties:
            Category = property.getCategory()
            Size = property.getSize()
            print(property)
            candidate = Applications.findPriority(Category=Category, BedroomSize=Size)
            print(candidate)
            if candidate is None:
                continue
            Property.deleteProperty(property)
            Applications.removeApplication(candidate)
            resolvedCounter += 1
        return resolvedCounter
    

if __name__ == "__main__":
    
    modeller = Modeller(startDate=datetime.date(2022, 1, 1), endDate=datetime.date(2022, 12, 31))



