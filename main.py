import yaml
from modules.file_utils import list_excel_files
from modules.data_processing import raw_dataraw_files
from modules.data_processing import header_finder, data_concat
from modules.data_storing import save_sample_data
from modules.data_cleaning import clean_rental_data


def main():
    with open('./config.yaml', 'r') as config_data:
        config = yaml.safe_load(config_data)
        data_directory = config['data_directory']
        sheet_name = config['sheet_name']

    # Getting list of file names
    files = list_excel_files(data_directory)

    raw_data = raw_dataraw_files(
        files=files,
        sheet_name=sheet_name,
        directory_name=data_directory
    )
    index_data, unmatched = header_finder(raw_data)
    final_data = data_concat(index_data, unmatched, raw_data)
    final_data = clean_rental_data(final_data)

    # Example usage after concatenating data
    # final_data is the DataFrame created in the data_concat function
    output_path = "./outputs/cleaned_data.csv"

    # Assuming `final_data` is already created
    save_sample_data(final_data, output_path)


if __name__ == '__main__':
    main()
