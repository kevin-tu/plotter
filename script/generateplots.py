from glob import glob
from os.path import relpath, abspath, join
import json

plot_folder = relpath("../plot_files")
plot_files = glob(plot_folder + "/*.json")
data_folder = relpath("../data")
output_folder = relpath("../output")

data_files = glob(data_folder + "/*.xlsx")
data = data_files[0]

plot_json = {
    "file_path": str(abspath(data)),
    "output_folder": str(abspath(data))
}

print("Hello")
print(json.dumps(plot_json, indent=4))
