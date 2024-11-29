import pandas as pd
import numpy as np

def clean_rental_data(df):

    # Replacing invalid entries like 's' and '-'
    df.replace({'-': np.nan, 's': np.nan}, inplace=True)
    
    print("Invalid entries like - and s, has been removed with NUll")

    # Convert percentage columns with actual percentages.
    percentage_columns = [
        "Quarterly change in Median Weekly Rent",
        "Annual change in Median Weekly Rent",
        "Quarterly change in New Bonds Lodged",
        "Annual change in New Bonds Lodged"
    ]

    for col in percentage_columns:
        df[col] = df[col].apply(lambda x: x*100 if pd.notnull(x) else x)
    
    print("Succesffully converted percentage columns with actual percentages")

    # Ensure all numeric columns are correct types
    df['Postcode'] = df['Postcode'].astype(int)
    df['Year'] = df['Year'].astype(int)
    df['Month'] = df['Month'].astype(int)

    print("Data type of Postcode, Year and Month ")

    return df