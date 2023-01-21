import pandas as pd

if __name__ == "__main__":
    housing_stock = pd.read_excel("..\\data\\HRA_stock.xlsx", engine="openpyxl")
    housing_register = pd.read_excel("..\\data\\RBK_Housing_Register.xlsx", engine="openpyxl")
    print(housing_stock)
    print(housing_register)
