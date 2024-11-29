import pandas as pd

def save_sample_data(dataframe, output_path, sample_size=1000):

    print("Saving a sample of the data...")
    
    sample_data = dataframe.head(sample_size)
    
    sample_data.to_csv(output_path, index=False)
    print(f"Sample of {sample_size} records saved to {output_path}")



