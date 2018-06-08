import json
from os.path import abspath, join
import matplotlib.pyplot as plt
import matplotlib as mpl
import logging
import pandas as pd
import math
import os
import sys
from plothelpers.plothelpers import InitialiseFigure, InitialiseSubPlot, GenerateAxes
import time
from glob import glob
from cycler import cycler


# Plotting functions

# def InitialiseFigure(num_subplots, i):
#     logging.info("Initialising plot figure.. \t [{}]".format(str(i+1)))
#     fig = plt.figure()
#     if num_subplots == 1:
#         _length = plt_style_params['figure.figsize'][0]
#         _height = plt_style_params['figure.figsize'][1]
#         fig.set_size_inches(_length, _height)
#     else:
#         _length = plt_style_params['figure.figsize'][0] * 2
#         _height = math.ceil(num_subplots/2) * plt_style_params['figure.figsize'][1]
#         fig.set_size_inches(_length, _height)
#     return fig

# def InitialiseSubPlot(ax, subplot_params, k):
#     logging.info("Initialising subplot.. \t [{}]".format(k+1))
#     ax.set_xlabel(subplot_params['x_label'])
#     ax.set_ylabel(subplot_params['y_label'])

# def GenerateAxes(fig, numAxes):
#     axes = []
#     logging.info("rating axes.. \t \t [{}]".format(numAxes))
#     if numAxes == 1:
#         axes.append(fig.add_subplot(1, 1, 1)) 
#     else:
#         for i in range(numAxes):
#             axes.append(fig.add_subplot(math.ceil(numAxes/2), 2, i + 1))
#     return axes

# Basic setup

COLOR_WHEEL = ['b', 'r', 'g', 'y']

logging.basicConfig(level=logging.INFO)

plot_cfg_path = abspath("../config/plot_styles.json")
plot_folder = abspath("../plot_files/C2WF")
plot_files = glob(plot_folder + "/*.json")
plot_file_path = abspath("../plot_files/C2WF/1a_WH_330_C2WF_Bannabay_3P_C2WF.json")
# output_folder = abspath("../output/C2WF")

with open(plot_cfg_path) as plt_style_config:
    plt_style_params = json.load(plt_style_config)

logging.info("Updating default plotting parameters..")
mpl.rcParams.update(plt_style_params)


for plot_number, plot_file_path in enumerate(plot_files):
# Read in data

    with open(plot_file_path) as plot_file:
        plot_params = json.load(plot_file)

    file_path = abspath(plot_params['file_path'])

    logging.info("Reading in file: \t {}".format(file_path))
    df = pd.read_excel(file_path, skiprows=4, index_col=0)
    start_time = time.time()

    logging.info("Number of plots: \t \t [{}]".format(len(plot_params['plots'])))
    for i, plot in enumerate(plot_params['plots']):
        # logging.info("Number of subplots: \t {}".format(len(plot['subplots'])))
        # logging.info("Plot number: \t\t {}".format(i))
        # plot_name = "Figure {}-{}.png".format(str(plot_params['appendix']).upper(), plot_number + 1)
        plot_name = "{}.png".format(plot['file_name'])
        suptitle_size = plt_style_params['font.size'] + 10
        num_subplots = len(plot['subplots'])
        fig = InitialiseFigure(num_subplots, i, plt_style_params)
        fig.suptitle(plot['plot_title'], fontsize=suptitle_size, y=0.993)
        plt.rc('axes', prop_cycle=(cycler('color', COLOR_WHEEL)))
        axes = GenerateAxes(fig, num_subplots)
        plt.tight_layout(pad=4.0, w_pad=4.0, h_pad=4.0)
        output_folder = plot_params['output_folder']

        for k, subplot in enumerate(plot['subplots']):
            InitialiseSubPlot(axes[k], subplot, k)
            x_axis = subplot['x_index']
            y_axis = subplot['y_index']
            y_min = None
            y_max = None
            
            if subplot['x_min'] is not "null":
                x_min = subplot['x_min']
            else:
                x_min = df.index.min()

            if subplot['x_max'] is not "null":
                x_max = subplot['x_max']
            else:
                x_max = df.index.max()

            if subplot['y_min'] is not "null":
                y_min = subplot['y_min']

            if subplot['y_max'] is not "null":
                y_max = subplot['y_max']

            # if (subplot['x_min'] is not "null") and (subplot['x_max'] is not "null"):
            x_lims = [x_min, x_max]

            if y_min is not None and y_max is not None:
                y_lims = [y_min, y_max]
                logging.info(y_lims)
                df.iloc[:, y_axis].plot(ax=axes[k], grid='on', xlim=x_lims, ylim=y_lims)
            else:
                df.iloc[:, y_axis].plot(ax=axes[k], grid='on', xlim=x_lims)
            # y_lims = [subplot['y_min'], subplot['y_max']]
            
            if subplot['subtitle'] is not "null":
                axes[k].set_title(subplot['subtitle'])

        fig.savefig(join(output_folder, plot_name))
        logging.info("Plotting: {}".format(str(join(output_folder, plot_name))))

    end_time = time.time()

    logging.info("Plotting completed in {} seconds".format(round(end_time - start_time, 2)))