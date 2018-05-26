import json
from os.path import abspath, join
import matplotlib.pyplot as plt
import matplotlib as mpl
import logging
import pandas as pd
import math
import os
import sys
import inspect
import time

# Plotting functions

def InitialiseFigure(num_subplots, i):
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
    logging.info("rating axes.. \t \t [{}]".format(numAxes))
    if numAxes == 1:
        axes.append(fig.add_subplot(1, 1, 1)) 
    else:
        for i in range(numAxes):
            axes.append(fig.add_subplot(math.ceil(numAxes/2), 2, i + 1))
    return axes

# Basic setup

logging.basicConfig(level=logging.INFO)
print(os.path.dirname(os.path.abspath(inspect.stack()[0][1])))

plot_cfg_path = abspath("../config/plot_styles.json")
plot_file_path = abspath("../plot_files/plot.json")
output_folder = abspath("../output")

with open(plot_cfg_path) as plt_style_config:
    plt_style_params = json.load(plt_style_config)

with open(plot_file_path) as plot_file:
    plot_params = json.load(plot_file)

file_path = abspath(plot_params['file_path'])

logging.info("Updating default plotting parameters..")
mpl.rcParams.update(plt_style_params)

# Read in data

logging.info("Reading in file: \t {}".format(file_path))

df = pd.read_excel(file_path, skiprows=4, index_col=0)

start_time = time.time()

logging.info("Number of plots: \t \t [{}]".format(len(plot_params['plots'])))
for i, plot in enumerate(plot_params['plots']):
    # logging.info("Number of subplots: \t {}".format(len(plot['subplots'])))
    # logging.info("Plot number: \t\t {}".format(i))
    plot_name = "Figure {}-{}.png".format(str(plot_params['appendix']).upper(),str(i+1))
    suptitle_size = plt_style_params['font.size']
    num_subplots = len(plot['subplots'])
    fig = InitialiseFigure(num_subplots, i)
    fig.suptitle(plot['plot_title'], fontsize=suptitle_size)
    axes = GenerateAxes(fig, num_subplots)
    plt.tight_layout(pad=4.0, w_pad=4.0, h_pad=4.0)

    for k, subplot in enumerate(plot['subplots']):
        InitialiseSubPlot(axes[k], subplot, k)
        x_axis = subplot['x_index']
        y_axis = subplot['y_index']
#        x_lims = [subplot['x_min'], subplot['x_max']]
#        y_lims = [subplot['y_min'], subplot['y_max']]
        df.iloc[:, y_axis].plot(ax=axes[k], grid='on')

    fig.savefig(join(output_folder, plot_name))
    logging.info("Plotting: {}".format(str(join(output_folder, plot_name))))

end_time = time.time()

logging.info("Plotting completed in {} seconds".format(round(end_time - start_time, 2)))