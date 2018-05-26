import pandas as pd
from os.path import relpath, join
from glob import glob
import matplotlib.pyplot as plt

data_folder = relpath("../data")
data_files = glob(data_folder + "/*.xlsx")
output_folder = relpath("../output")

for i, item in enumerate(data_files):
    print(i, ": ", item)
    
df1 = pd.read_excel(data_files[0], skiprows=4, index_col=0)
df2 = pd.read_excel(data_files[1], skiprows=4, index_col=0)

df1.merge(df2, left_on=True, right_on=True)