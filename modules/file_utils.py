import os
import pandas as pd

def list_excel_files(directory):
    """
    List all Excel files in the given directory.
    """
    list_names = []
    for each in os.listdir(directory):
        if each.endswith('xlsx'):
            list_names.append(each)
    print("List of file names stored successfully")
    return list_names

def read_excel_sheet(file_path, sheet_name):
    """
    Read a specific sheet from an Excel file.
    """
    try:
        sheet_to_df_map = pd.read_excel(file_path, sheet_name=sheet_name)
        return sheet_to_df_map
    except Exception as e:
        print(f"Error Reading file {file_path} with error {e}")
        return None


    