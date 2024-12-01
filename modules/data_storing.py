import pandas as pd

def save_sample_data(dataframe, output_path):

    dataframe.columns = [
    'Postcode',
    'Dwelling_Types',
    'Number_of_Bedrooms',
    'First_Quartile_Weekly_Rent_for_New_Bonds_',
    'Median_Weekly_Rent_for_New_Bonds_',
    'Third_Quartile_Weekly_Rent_for_New_Bonds_',
    'New_Bonds_Lodged_No_',
    'Total_Bonds_Held_No_',
    'Quarterly_change_in_Median_Weekly_Rent',
    'Annual_change_in_Median_Weekly_Rent',
    'Quarterly_change_in_New_Bonds_Lodged',
    'Annual_change_in_New_Bonds_Lodged',
    'Month',
    'Year'
]

    print("Saving  of the data...")

    dataframe.to_csv(output_path, index=False)
    print(f" Data Frame saved to {output_path}")



