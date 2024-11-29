import pandas
from modules.file_utils import read_excel_sheet
import os
import pandas as pd
import re

def raw_dataraw_files(files, sheet_name, directory_name):
    """
    Process all files, reading the specified sheet and combining the data.
    """
    raw_data = {}
    print("Storing Files ........ \n")
    for file in files:
        print(f"{file} and sheet name {sheet_name}")
        raw_data[os.path.join(directory_name, file)]=read_excel_sheet(os.path.join(directory_name, file), sheet_name)
    print("Storing completed")
    return raw_data

def header_consistency(index_header):
    ref = ['Postcode', 'Dwelling Types', 'Number of Bedrooms', 'First Quartile Weekly Rent for New Bonds\n$', 'Median Weekly Rent for New Bonds\n$', 'Third Quartile Weekly Rent for New Bonds\n$', 'New Bonds Lodged\nNo.', 'Total Bonds Held\nNo.', 'Quarterly change in Median Weekly Rent',
             'Annual change in Median Weekly Rent', 'Quarterly change in New Bonds Lodged', 'Annual change in New Bonds Lodged']
    unmatch = []
    for file_name, header in index_header.items():
        if header != ref:
            print("The number of columns are not same")
            print(file_name)
            unmatch.append(file_name)
    return unmatch


def header_finder(raw_data):

    discrepancies = []
    reference_column = None
    index_data = {}
    index_header = {}
    print("Finding the header row index for file..... \n")
    for file_path, data in raw_data.items():
        header_row = None
        print(f"file number: {file_path}")
        for index, row in data.iterrows():
            if str(row[0]).startswith("Postcode"):  # Check if the first column starts with "Postcode"
                header_row = index
                index_data[file_path] = header_row
                index_header[file_path] = row.to_list()

        if header_row is None:
            print(f"No header row starting with 'Postcode' found in {file_path}.")
            discrepancies.append((file_path, "No header found"))
            continue
    if len(discrepancies) == 0:
        print("There is no such file without a header")
    unmatched = header_consistency(index_header)
    print("Finding the header row index for file completed ")

    return index_data, unmatched

def extract_date_info(file_name):
    match = re.search(r'(\w+)-(\d{4})', file_name)  # Match month and year
    if match:
        month_name = match.group(1).lower()
        year = match.group(2)
        # Map month names to month numbers
        month_map = {
            "january": 1, "february": 2, "march": 3, "april": 4,
            "may": 5, "june": 6, "july": 7, "august": 8,
            "september": 9, "october": 10, "november": 11, "december": 12
        }
        month = month_map.get(month_name, None)
        return month, year
    return None, None

def data_concat(index_data, unmatched, raw_data):
    """
    Concatenate data from files with consistent headers.
    """
    final_data = pd.DataFrame()  # Initialize an empty DataFrame
    print("Concatenating all the dataframes..... ")
    for file_name, data in raw_data.items():
        if file_name not in unmatched:
            index_num = index_data[file_name]
            # Skip rows before the header row and reset column names
            data_with_header = raw_data[file_name].iloc[index_num:].reset_index(drop=True)
            data_with_header.columns = data_with_header.iloc[0]  # Set first row as column names
            month, year = extract_date_info(file_name)

            if month and year:
                data_with_header["Month"] = month
                data_with_header["Year"] = year

            data_with_header = data_with_header[1:]  # Drop the header row
            final_data = pd.concat([final_data, data_with_header], ignore_index=True)
            month, year = extract_date_info(file_name)
    print("Concatenating Done")

    return final_data


