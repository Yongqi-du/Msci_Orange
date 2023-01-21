import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    housing_stock = pd.read_excel("..\\data\\HRA_stock.xlsx", engine="openpyxl")
    housing_register = pd.read_excel("..\\data\\RBK_Housing_Register.xlsx", engine="openpyxl")
    print(housing_stock)
    # print(housing_register)
    housing_register_banded = housing_register.value_counts("Band").sort_index()
    print(housing_register_banded)

    for index, row in enumerate(housing_register_banded):
        plt.title("Number of applications per Housing Band")
        plt.xlabel("Housing Band")
        plt.ylabel("Number of Applications")
        plt.bar(index + 1, row)
    plt.show()

