import json
from glob import glob
from os.path import abspath, basename, join, relpath, splitext

from Plots.Plots import PlotClass, SubPlotClass

plot_folder = abspath("../plot_files/C2WF")
plot_files = glob(plot_folder + "/*.json")
data_folder = abspath("../data/C2WF")
output_folder = abspath("../output/C2WF")
data_files = glob(data_folder + "/*.xlsx")

for i, data_path in enumerate(data_files[0:1]):

    plot = PlotClass(data_path, output_folder, appendix="A")
    subplot_1 = SubPlotClass(y_index=[1,3])
    subplot_2 = SubPlotClass(y_index=[4,5,6])
    subplot_3 = SubPlotClass(y_index=[1,7,8])
    subplot_4 = SubPlotClass(y_index=[1,2,3])
    
    plot.add_plot(basename(data_path).split('.')[0])
    plot.add_subplot(0, subplot_1.to_dict())
    plot.add_subplot(0, subplot_2.to_dict())
    plot.add_subplot(0, subplot_3.to_dict())
    plot.add_subplot(0, subplot_4.to_dict())

    json_file_name = basename(splitext(data_path)[0] + '.json')
    print("Printing json_file_name")
    print(json_file_name)
    print("Printing json output file")
    print(join(plot_folder, json_file_name))
    with open(join(plot_folder, json_file_name), 'w') as js:
        json.dump(plot.to_dict(), js, indent=4)
