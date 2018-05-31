import json
from glob import glob
from os.path import abspath, basename, join, relpath, splitext
import logging

logging.basicConfig(level=logging.INFO)

class SubPlotClass:

    def __init__(self, x_index=0, x_label="Time (seconds)", x_min=None, x_max=None, 
            y_min=None, y_max=None, y_index=[1], y_label="Y labe", subtitle=None):
        self.x_index = x_index
        self.x_label = x_label
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.y_index = y_index
        self.y_label = y_label
        self.subtitle = subtitle

    def to_dict(self):
        subplot_dict = {
            "subtitle": self.subtitle,
            "x_index": self.x_index,
            "x_label": self.x_label,
            "x_max": self.x_max,
            "x_min": self.x_min,
            "y_index": self.y_index,
            "y_label": self.y_label,
            "y_min": self.y_min,
            "y_max": self.y_max,
        }

        return subplot_dict

class PlotClass:
    def __init__(self, data_file_path, output_folder, appendix):
        self.data_file_path = data_file_path
        self.output_folder =output_folder
        self.plots = []
        self.subplots = []
        self.appendix = appendix

    def get_num_plots(self):
        return len(self.plots)

    def get_num_subplots(self, plotNumber):
        return len(self.plots[plotNumber])
    
    def add_plot(self, plot_title):
        self.plots.append( {
            "plot_title": plot_title
            }
        )
        self.plots[-1]["subplots"] = []
    
    def add_subplot(self, plotNumber, subplot):
        self.plots[plotNumber]["subplots"].append(subplot)

    def to_dict(self):
        plot_dict = {
            "file_path": self.data_file_path,
            "output_folder": self.output_folder,
            "appendix": self.appendix,
            "plots": self.plots
            }

        return plot_dict

plot_folder = abspath("../plot_files/C2WF")
plot_files = glob(plot_folder + "/*.json")
data_folder = abspath("../data/C2WF")
output_folder = abspath("../output/C2WF")
data_files = glob(data_folder + "/*.xlsx")

for i, data_path in enumerate(data_files):

    plot = PlotClass(data_path, output_folder, appendix="A")
    subplot_1 = SubPlotClass(y_index=[1], y_label="Active Power (MW)", subtitle="Active Power (MW)", x_min=8.0)
    subplot_2 = SubPlotClass(y_index=[2], y_label="Reactive Power (MVAr)", subtitle="Reactive Power (MVAr)", x_min=8.0)
    subplot_3 = SubPlotClass(y_index=[5], y_label="Current (pu)", subtitle="Terminal current (pu) (rated MVA)", x_min=8.0)
    subplot_4 = SubPlotClass(y_index=[6,7], y_label="Voltage (pu)", subtitle="Voltage (pu) at POC", x_min=8.0)
    
    plot.add_plot("Figure {}: {}".format(i+1, basename(data_path).split('.')[0]))
    plot.add_subplot(0, subplot_1.to_dict())
    plot.add_subplot(0, subplot_2.to_dict())
    plot.add_subplot(0, subplot_3.to_dict())
    plot.add_subplot(0, subplot_4.to_dict())

    json_file_name = basename(splitext(data_path)[0] + '.json')
    logging.info("Creating json file: {}".format(join(plot_folder, json_file_name)))

    with open(join(plot_folder, json_file_name), 'w') as js:
        json.dump(plot.to_dict(), js, indent=4)
