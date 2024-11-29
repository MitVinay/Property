import yaml
from modules.file_utils import list_excel_files
from modules.data_processing import raw_dataraw_files, header_finder, data_concat


def main():

    with open('./config.yaml', 'r') as config_data:
        config=yaml.safe_load(config_data)
        data_directory = config['data_directory']
        output_file = config['output_file']
        sheet_name = config['sheet_name']
    
    # Getting list of file names
    files = list_excel_files(data_directory)

    raw_data = raw_dataraw_files(files = files, sheet_name=sheet_name, directory_name=data_directory)
    index_data, unmatched  = header_finder(raw_data)
    final_data = data_concat(index_data, unmatched, raw_data)

    




if __name__ == '__main__':
    main()


