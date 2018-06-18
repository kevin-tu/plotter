import logging
import matplotlib.pyplot as plt
import math
# Helper classes to generate plots

class SubPlotClass:

    def __init__(self, x_index=0, x_label="Time (seconds)", x_min=None, x_max=None, 
            y_min=None, y_max=None, y_index=[1], y_label="Y labe", subtitle=None, pscad_index=None):
        self.x_index = x_index
        self.x_label = x_label
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.y_index = y_index
        self.y_label = y_label
        self.subtitle = subtitle
        self.pscad_index = pscad_index

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
            "pscad_index": self.pscad_index
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
    
    def add_plot(self, plot_title, file_name):
        self.plots.append( {
            "plot_title": plot_title,
            "file_name": file_name
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

# Plotting functions

def InitialiseFigure(num_subplots, i, plt_style_params):
    logging.info("Initialising plot figure.. \t [{}]".format(str(i+1)))
    fig = plt.figure()
    if num_subplots == 1:
        _length = plt_style_params['figure.figsize'][0]
        _height = plt_style_params['figure.figsize'][1]
        fig.set_size_inches(_length, _height)
    else:
        _length = plt_style_params['figure.figsize'][0] * 2
        _height = math.ceil(num_subplots/2) * plt_style_params['figure.figsize'][1]
        fig.set_size_inches(_length, _height)
    return fig

def InitialiseSubPlot(ax, subplot_params, k):
    logging.info("Initialising subplot.. \t [{}]".format(k+1))
    ax.set_xlabel(subplot_params['x_label'])
    ax.set_ylabel(subplot_params['y_label'])

def GenerateAxes(fig, numAxes):
    axes = []
    logging.info("Generating axes.. \t \t [{}]".format(numAxes))
    if numAxes == 1:
        axes.append(fig.add_subplot(1, 1, 1)) 
    else:
        for i in range(numAxes):
            axes.append(fig.add_subplot(math.ceil(numAxes/2), 2, i + 1))
    return axes
