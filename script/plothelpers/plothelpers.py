''' Plotting class that is used to generate configurable plots '''

import math
import json
import logging
import ntpath
from os.path import join, isfile
from collections import namedtuple
from cycler import cycler
import matplotlib.pyplot as plt
import pandas as pd

# Helper classes to generate plots

FORMAT = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('__name__')

COLOR_WHEEL = ['b', 'r', 'g', 'y']

class Plot(object):
    ''' Plot object to create a template which is used by the Plotter object
        To be passed as an input to the Plotter object

    '''

    def __init__(self, **kwargs):
        self.plots = []
        self.subplots = []
        for k, v in kwargs.items():
            setattr(self, k, v)

    def add_plot(self, plot_title):
        self.plots.append({"plot_title": plot_title})
        self.plots[-1].update({"subplots": []})

    def add_subplot(self, subplot_dict, plot_number=-1):
        self.plots[plot_number]["subplots"].append(subplot_dict)

    def to_dict(self):
        plot_dict = {"plots": self.plots}
        return plot_dict

    @staticmethod
    def create_subplot_dict(x_index=0, 
                            x_label="Time (seconds)", 
                            x_min=None, 
                            x_max=None,
                            y_min=None, 
                            y_max=None, 
                            y_index=None, 
                            y_label=None, 
                            subtitle=None):

        ''' Template function for subplot parameters

        Args:
            x_index (int):      Index of the x-axis variable
            x_min (float):      Minimum x-axis value
            x_max (float):      Maximum x-axis value
            x_label (string):   x-axis label
            y_index (int):      Index of the y-axis variable(s)
            y_min (float):      Minimum y-axis value
            y_max (float):      Maximum x-axis value
            y_label (string):   y-axis label
            subtitle (string):  Subtitle for axes object

        Returns:
            dict:   Dictionary containing subplot parameters

        '''
        _subplot_dict = {
            "subtitle": subtitle,
            "x_index": x_index,
            "x_label": x_label,
            "x_max": x_max,
            "x_min": x_min,
            "y_index": y_index,
            "y_label": y_label,
            "y_min": y_min,
            "y_max": y_max,
        }

        return _subplot_dict

    # Alternative constructor from json template
    @classmethod        
    def from_json(cls, json_file_path):
        ''' Alternative constructor to build the plot object from a json template'''

        with open(json_file_path) as json_plot_file:
            plot_params = json.load(json_plot_file)
        return cls(**plot_params)

    def __repr__(self):
        return self.__class__.__qualname__

# Plotting functions

class Plotter(object):

    def __init__(self, plot_json_template, plot_config='..\\config\\plt_config_params.json'):
        self.plt_config_params = None
        self._load_default_params(plot_config)
        self.data_files = []
        self.plots = []
        for k, v in plot_json_template.items():
            setattr(self, k, v)

    def _load_default_params(self, plot_config):
        ''' Function to load default plotting parameters
            Configuration can be passed as a json file path or equivalent dict
        '''
        if isfile(plot_config):
            with open(plot_config):
                self.plt_config_params = json.load(plot_config)
        elif isinstance(plot_config, dict):
            self.plt_config_params = plot_config
        plt.rcParams.update(self.plt_config_params)

    def _init_figure(self, num_subplots):
        logger.info("Initialising plot figure.. \t [{}]".format(str(i+1)))
        self.fig = plt.figure()
        if num_subplots == 1:
            _length, _height = self.plt_config_params['figure.figsize']
            self.fig.set_size_inches(_length, _height)
        else:
            _length = self.plt_config_params['figure.figsize'][0] * 2
            _height = math.ceil(num_subplots/2) * self.plt_config_params['figure.figsize'][1]
            self.fig.set_size_inches(_length, _height)
        return self.fig

    def _init_subplot(self, ax, subplot_params, k):
        logger.info("Initialising subplot.. \t [{}]".format(k+1))
        ax.set_xlabel(subplot_params['x_label'])
        ax.set_ylabel(subplot_params['y_label'])

    def _generate_axes(self, num_axes, fig):
        axes = []
        logger.info("Generating axes.. \t \t [{}]".format(num_axes))
        if num_axes == 1:
            axes.append(fig.add_subplot(1, 1, 1)) 
        else:
            for i in range(num_axes):
                axes.append(fig.add_subplot(math.ceil(num_axes/2), 2, i + 1))
        return axes

    def add_data_file(self, file_path, output_path, skiprows=4):
        data_file = namedtuple('data_file', ['file_path', 'output_path', 'skiprows'])
        self.data_files.append(data_file(file_path, output_path, skiprows))

    def _path_leaf(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)

    def plot_all(self):

        _plot_counter = 0

        for data_file in self.data_files:
            file_path, output_path, skiprows = data_file
            _df = pd.read_excel(file_path, skiprows=skiprows, index_col=0)
            _fname = self._path_leaf(file_path).split(".")[0]

            for i, plot in enumerate(self.plots):
                num_subplots = len(plot['subplots'])
                suptitle_size = self.plt_config_params['font.size'] + 10
                fig = self._init_figure(num_subplots)
                fig.suptitle(plot['plot_title'], fontsize=suptitle_size)
                axes = self._generate_axes(fig, num_subplots)
                plt.rc('axes', prop_cycle=(cycler('color', COLOR_WHEEL)))
                plt.tight_layout(pad=4.0, w_pad=4.0, h_pad=4.0)

                for k, subplot in enumerate(plot['subplots']):
                    self._init_subplot(axes[k], subplot, k)
                    x_axis = subplot['x_index']
                    y_axis = subplot['y_index']
                    y_min = None
                    y_max = None
                    
                    if subplot['x_min'] is not "null":
                        x_min = subplot['x_min']
                    else:
                        x_min = _df.index.min()

                    if subplot['x_max'] is not "null":
                        x_max = subplot['x_max']
                    else:
                        x_max = _df.index.max()

                    if subplot['y_min'] is not "null":
                        y_min = subplot['y_min']

                    if subplot['y_max'] is not "null":
                        y_max = subplot['y_max']

                    # if (subplot['x_min'] is not "null") and (subplot['x_max'] is not "null"):
                    x_lims = [x_min, x_max]

                    if y_min is not None and y_max is not None:
                        y_lims = [y_min, y_max]
                        _df.iloc[:, y_axis].plot(ax=axes[k], grid='on', xlim=x_lims, ylim=y_lims)
                    else:
                        _df.iloc[:, y_axis].plot(ax=axes[k], grid='on', xlim=x_lims)
                    # y_lims = [subplot['y_min'], subplot['y_max']]
                    
                    if subplot['subtitle'] is not "null":
                        axes[k].set_title(subplot['subtitle'])

                plot_name = f"Figure {_plot_counter}.png"

                fig.savefig(join(output_path, plot_name))
                logger.info("Plotting: {}".format(str(join(output_path, plot_name))))

                _plot_counter += 1



'''
Comment for later
data_files should be a dictionary with the file_path as key
Subsequent plots to be added with that key
Specify:
output_path
skiprows
subplot template
optional axes

should export plotter config to json
'''