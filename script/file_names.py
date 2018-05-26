from os.path import relpath, join, basename
from glob import glob

data_folder = relpath("C:/Users/Kevin.Tu/WSP O365/Roberts, Vivienne - Information/LSF Submission/Submission/Attachments")
data_files = glob(data_folder + "/*")
#output_folder = relpath("../output")

for i, item in enumerate(data_files):
    print(basename(item))
    
#df1 = pd.read_excel(data_files[0], skiprows=4, index_col=0)
#df2 = pd.read_excel(data_files[1], skiprows=4, index_col=0)
#
#df1.merge(df2, left_on=True, right_on=True)
