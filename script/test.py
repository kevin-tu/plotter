from glob import glob
from os.path import abspath, join
import pandas as pd
import matplotlib.pyplot as plt
import logging
import math
from cycler import cycler
from itertools import chain

def _init_figure(num_subplots):
    # logger.info("Initialising plot figure.. \\t [{}]".format(str(i+1)))
    logger.info("Initialising plot figure..")
    fig = plt.figure()
    if num_subplots == 1:
        _length, _height = PLT_DEFAULT_PARAMS['figure.figsize']
        fig.set_size_inches(_length, _height)
    else:
        _length = PLT_DEFAULT_PARAMS['figure.figsize'][0] * 2
        _height = math.ceil(num_subplots/2) * PLT_DEFAULT_PARAMS['figure.figsize'][1]
        fig.set_size_inches(_length, _height)
    return fig

def _init_subplot(ax, subplot_params, k):
    logger.info("Initialising subplot.. \\t [{}]".format(k+1))
    ax.set_xlabel(subplot_params['x_label'])
    ax.set_ylabel(subplot_params['y_label'])

def _generate_axes(*, num_axes, fig):
    axes = []
    logger.info("Generating axes.. \\t \\t [{}]".format(num_axes))
    if num_axes == 1:
        axes.append(fig.add_subplot(1, 1, 1)) 
    else:
        for i in range(num_axes):
            axes.append(fig.add_subplot(math.ceil(num_axes/2), 2, i + 1))
    return axes

def benchmark_plot(*, _merged_df, pscad_index, psse_index, subtitle, ax):
    logger.info('Running benchmark plot function')
    # pscad_data = _df_pscad.iloc[:, pscad_index]
    # psse_data = _df_psse.iloc[:, psse_index]
    # print(pscad_data.head())
    
    plot_index = pscad_index + psse_index

    plot_df = _merged_df.iloc[:, plot_index]
    # upper_limit_plot_df = plot_df.iloc[:, pscad_index] * 1.1
    # lower_limit_plot_df = plot_df.iloc[:, pscad_index] * 0.9
    # upper_limit_plot_df.columns = [upper_limit_plot_df.columns[0] + ' + 10%']
    # lower_limit_plot_df.columns = [lower_limit_plot_df.columns[0] + ' - 10%']
    # lower_limit_plot_df = plot_df * 0.9
    plt.rc('axes', prop_cycle=(cycler('color', COLOR_WHEEL)))
    plot_df.plot(ax=ax, grid='on', xlim=[0,25])
    # upper_limit_plot_df.plot(ax=ax, grid='on')
    # lower_limit_plot_df.plot(ax=ax, grid='on')
    # psse_data.plot(ax=ax, color='r')
    # pscad_x_index = _df_pscad.iloc[:0].values
    # psse_x_index = _df_psse.iloc[:0].values
    # ax.plot(pscad_x_index, pscad_data, 'b')
    # ax.plot(pscad_x_index, pscad_data*1.1, 'r')
    # ax.plot(pscad_x_index, pscad_data*0.9, 'g')
    # ax.plot(psse_x_index, psse_data, 'y')
    ax.set_title(subtitle)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

COLOR_WHEEL = ['b', 'r', 'g', 'y']

PLT_DEFAULT_PARAMS = {
    "figure.figsize": [6.0, 3.9],
    "grid.linewidth": 1.2,
    "grid.linestyle": "--",
    "axes.linewidth": 1.2,
    "lines.linewidth": 1.2,
    "figure.dpi": 80,
    "savefig.dpi": 200,
    "font.size": 12,
    "legend.fontsize": 12,
    "figure.titlesize": 12,
    "patch.force_edgecolor": "True",
    "patch.facecolor": "b",
    "font.sans-serif": "Times New Roman",
    "font.family": "sans-serif"
}

FONT_SIZE = PLT_DEFAULT_PARAMS['font.size']

logger.info("Loading default plotting parameters")
plt.rcParams.update(PLT_DEFAULT_PARAMS)

# Reading in file directories
logger.info("Reading in file directories")
# PSCAD_DIRECTORY = abspath('C:\\Users\\mrkev\\Documents\\GitHub\\plotter\\data\\NESF\\PSCAD_Results_20180608')
# PSSE_DIRECTORY = abspath('C:\\Users\\mrkev\\Documents\\GitHub\\plotter\\data\\NESF\\PSEE_Results_20180608')
# PSCAD_FILES = glob(PSCAD_DIRECTORY + '\\*.xlsx')
# PSSE_FILES = glob(PSSE_DIRECTORY + '\\*.xlsx')

MERGED_DIRECTORY = abspath('C:\\Users\\mrkev\\Documents\\GitHub\\plotter\\data\\NESF\\Merged_Results_20180608')
MERGED_FILES = glob(MERGED_DIRECTORY + '\\*.csv')

# logger.info(f'Reading PSCAD: {PSCAD_DIRECTORY}')
# logger.info(f'Number of files: {len(PSCAD_FILES)}')
# for file_path in PSCAD_FILES:
#     logger.info(file_path)

# logger.info(f'Reading PSSE: {PSSE_DIRECTORY}')
# logger.info(f'Number of files: {len(PSSE_FILES)}')
# for file_path in PSSE_FILES:
#     logger.info(file_path)

logger.info(f'Reading MERGED FILES: {MERGED_DIRECTORY}')
logger.info(f'Number of files: {len(MERGED_FILES)}')
for file_path in MERGED_FILES:
    logger.info(file_path)

# for i in range(len(PSCAD_FILES)):
# num_subplots = len(PSCAD_FILES)
num_subplots = 1
fig = _init_figure(num_subplots)
axes = _generate_axes(num_axes=num_subplots, fig=fig)
output_folder = abspath('C:\\Users\\mrkev\\Documents\\GitHub\\plotter\\data\\NESF\\output')
plot_name = 'testplot.png'

plt.rc('axes', prop_cycle=(cycler('color', COLOR_WHEEL)))

for i in range(1):
    logger.info('Reading in MERGED files')
    # _df_pscad = pd.read_excel(PSCAD_FILES[i], skiprows=2, index_col=0)
    # df_pscad = pd.read_excel(PSCAD_FILES[i], skiprows=1, index_col=0).convert_objects(convert_numeric=True)
    # df_psse = pd.read_excel(PSSE_FILES[i], skiprows=3, index_col=0).convert_objects(convert_numeric=True)
    df_merged = pd.read_csv(MERGED_FILES[0], index_col=0)
    # logger.info('Merging plots')
    # df_merged = pd.read_csv
    # print(df_pscad.head())
    # print(df_psse.head())

    benchmark_plot(_merged_df=df_merged, pscad_index=[6], psse_index=[23], subtitle="Test title", ax = axes[0])
    
    logger.info('Saving fig')
    fig.savefig(join(output_folder, plot_name))
    logger.info("Plotting: {}".format(str(join(output_folder, plot_name))))

    for subplot_number, ax in enumerate(axes):
        pass

    # from collections import namedtuple
    # plot_params = namedtuple('plot_params', ['title', 'pscad_index', 'pscad_upper_index', 'pscad_lower_index', 'psse_index'])

    # plot_01 = plot_params('Active power at the inverter terminal',)
