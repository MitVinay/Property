import pandas as pd

def save_sample_data(dataframe, output_path):

    print("Saving a sample of the data...")

    dataframe.to_csv(output_path, index=False)
    print(f" Data Frame saved to {output_path}")



