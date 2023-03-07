import csv
import datetime

import pandas as pd
from applications import Applications
from property import Property


def resolveApplication():
    availableProperties = Property.getAllProperties()
    resolvedCounter = 0
    for prop in availableProperties:
        Category = prop.getCategory()
        Size = prop.getSize()
        print(prop)
        candidate = Applications.findPriority(Category=Category, BedroomSize=Size)
        print(candidate)
        if candidate is None:
            continue
        Property.deleteProperty(prop)
        Applications.removeApplication(candidate)
        resolvedCounter += 1
    return resolvedCounter


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
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            while self.currentDate < self.endDate:
                # self.displayCurrentDate()
                queuedApplication = Applications.getApplicationsBeforeDate(self.currentDate)
                newApplication = Applications.getApplicationsByDate(self.currentDate)
                # print(len(queuedApplication))
                resolvedApplication = resolveApplication()
                # resolvedApplication = 0

                writer.writerow({'Date': self.currentDate, 'Queue': len(queuedApplication), 'New': len(newApplication),
                                 'Resolved': resolvedApplication})

                self.currentDate += datetime.timedelta(days=1)

            # Check if there are property

            # Find the appropriate candidate

            # Remove the candidate and the property from their appropriate instances

        # self.resolveApplication()

        print("Terminating Model")
        exit()

    def setAllocationPolicy(self, PanelMoves, Homeless, SocialServicesQuota, Transfer, HomeScheme, FirstTimeApplicants,
                            TenantFinder, Downsizer, Decants):
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
        total = PanelMoves + Homeless + SocialServicesQuota + Transfer + HomeScheme + FirstTimeApplicants + \
            TenantFinder + Downsizer + Decants
        self.policy["Other"] = 1 - total

    def assignHouseToCategory(self, BedroomSize, Category):
        total = self.supply[str(BedroomSize)]
        assignedForCategory = int(total * self.policy[Category])

        Property.generateProperties(BedroomSize, Category, self.currentDate, assignedForCategory)

    def displayCurrentDate(self):
        print("The current date is:", self.currentDate)


if __name__ == "__main__":
    modeller = Modeller(startDate=datetime.date(2022, 1, 1), endDate=datetime.date(2022, 12, 31))
