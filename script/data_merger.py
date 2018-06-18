import pandas as pd
from functools import reduce
from os.path import relpath, join, abspath, isfile
from glob import glob
import matplotlib.pyplot as plt
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def merge_data(df_left, df_right):
    logger.info('Merging data')
    _df_merged = pd.merge(df_left, df_right, how='outer', left_index=True, right_index=True).interpolate().dropna()
    return _df_merged

def data_file_generator(data_files):
    logger.info('Reading in data')
    for data_file in data_files:
        df = pd.read_excel(data_file, skiprows=4)
        df = df.apply(pd.to_numeric) 
        logger.info(df.columns[0])
        df.set_index(df.columns[0])
        yield df

if __name__ == '__main__':
    _, *data_files = sys.argv
    print("Running main func")
    print(f"Data files: {data_files}")

    # Check if valid files
    logger.info('Checking if valid files')
    for file in data_files:
        
        logger.info(f'Isfile: {isfile(abspath(file))} - {abspath(file)}')
    # pass

    # df_left = pd.read_excel(df_left_path, index_col=0, skiprows=4)
    # df_right = pd.read_excel(df_right_path, index_col=0, skiprows=4)
    df_merged = reduce(merge_data, data_file_generator(data_files))
    logger.info('Writing file: output.csv')
    df_merged.to_csv('output.csv')

else:
    print("Importing this")
    # data_folder = relpath("../data")
    # data_files = glob(data_folder + "/*.xlsx")
    # output_folder = relpath("../output")

    # for i, item in enumerate(data_files):
    #     print(i, ": ", item)
        
    # df1 = pd.to_numeric(pd.read_excel(data_files[0], skiprows=4, index_col=0), errors='coerce'))
    # df2 = pd.to_numeric(pd.read_excel(data_files[1], skiprows=4, index_col=0), errors='coerce'))

    # df3 = pd.merge(df1, df2, how='outer', left_index=True, right_index=True)
