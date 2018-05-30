import json

class SubPlotClass:

    def __init__(self, x_index=0, x_label="Time (seconds)", x_min=None, x_max=None, 
            y_min=None, y_max=None, y_index=[1], y_label="Y label"):
        self.x_index = x_index
        self.x_label = x_label
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.y_index = y_index
        self.y_label = y_label

    def to_dict(self):
        subplot_dict = {
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
