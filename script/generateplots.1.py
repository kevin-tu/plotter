import json
from glob import glob
from os.path import abspath, basename, join, relpath, splitext
import logging
import ntpath
# import itertools
from plothelpers_V0.plothelpers import PlotClass, SubPlotClass

logging.basicConfig(level=logging.INFO)

running_plot_number = 0

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

plot_folder = abspath("../plot_files/NESF")
plot_files = glob(plot_folder + "/*.json")
data_folder = abspath('..\\data\\NESF\\Merged_results_20180608')
output_folder = abspath("../output/NESF")
data_files = glob(data_folder + "/*.csv")


for i, data_path in enumerate(data_files):

    running_plot_number += 1

    fname = path_leaf(data_path).split(".")[0]

    plot = PlotClass(data_path, output_folder, appendix="A")
    subplot_1 = SubPlotClass(y_index=[5, 23], pscad_index = None, y_label="Active Power (MW)", subtitle="Active power at the inverter terminal", x_min=8, x_max=25.0)
    subplot_2 = SubPlotClass(y_index=[8, 21, 9], pscad_index = [8], y_label="Active Power (MW)", subtitle="Active power at the POC", x_min=8, x_max=25.0)
    subplot_3 = SubPlotClass(y_index=[10, 24], pscad_index = None, y_label="Reactive Power (MVAr)", subtitle="Reactive power at the inverter terminal", x_min=8, x_max=25.0)
    subplot_4 = SubPlotClass(y_index=[13, 22], pscad_index = [13], y_label="Reactive power (MVAr)", subtitle="Reactive power at the POC", x_min=8, x_max=25.0)
    subplot_5 = SubPlotClass(y_index=[0, 25], pscad_index = None, y_label="Voltage (pu)", subtitle="Voltage at the inverter terminal", x_min=8, x_max=25.0)
    subplot_6 = SubPlotClass(y_index=[3, 20, 4], pscad_index = [3], y_label="Voltage (pu)", subtitle="Voltage at the POC", x_min=8, x_max=25.0)
    subplot_7 = SubPlotClass(y_index=[1, 18], pscad_index = None, y_label="Voltage (pu)", subtitle="33kV Voltage", x_min=8, x_max=25.0)
    subplot_8 = SubPlotClass(y_index=[2, 19], pscad_index = None, y_label="Voltage (pu)", subtitle="132kV Voltage", x_min=8, x_max=25.0)
    subplot_9 = SubPlotClass(y_index=[15, 14], pscad_index = None, y_label="PU on MVA base", subtitle="Inverter Id", x_min=8, x_max=25.0)
    subplot_10 = SubPlotClass(y_index=[17, 16], pscad_index = None, y_label="PU on MVA base", subtitle="Inverter Iq", x_min=8, x_max=25.0)

    # plot.add_plot(f"Figure {running_plot_number}: C2WF {fname}", f"Figure {running_plot_number}")
    plot.add_plot(f"Figure {running_plot_number}-1: {fname}", f"Figure {running_plot_number}-1")
    plot.add_plot(f"Figure {running_plot_number}-2: {fname}", f"Figure {running_plot_number}-2")
    plot.add_subplot(0, subplot_1.to_dict())
    plot.add_subplot(0, subplot_2.to_dict())
    plot.add_subplot(0, subplot_3.to_dict())
    plot.add_subplot(0, subplot_4.to_dict())   
    plot.add_subplot(0, subplot_5.to_dict())
    plot.add_subplot(0, subplot_6.to_dict())
    plot.add_subplot(1, subplot_7.to_dict())
    plot.add_subplot(1, subplot_8.to_dict())
    plot.add_subplot(1, subplot_9.to_dict())
    plot.add_subplot(1, subplot_10.to_dict())

    json_file_name = basename(splitext(data_path)[0] + '.json')
    logging.info("Creating json file: {}".format(join(plot_folder, json_file_name)))

    with open(join(plot_folder, json_file_name), 'w') as js:
        json.dump(plot.to_dict(), js, indent=4)

