
# coding: utf-8

import pandas as pd
from os.path import relpath, join
from glob import glob
import matplotlib.pyplot as plt
import matplotlib as mpl
import ast
import math

data_folder = relpath("../data")
data_files = glob(data_folder + "/*.xlsx")
output_folder = relpath("../output")
font_size = 12
fig_height = 6
fig_length = 8

# Set all default styles for plotting in matplotlib
#mpl.rcParams['grid.color'] = 'k'
#mpl.rcParams['grid.linestyle'] = '--'
mpl.rcParams['grid.linewidth'] = 1.2
mpl.rcParams['axes.linewidth'] = 1.2
mpl.rcParams['lines.linewidth'] = 1.2
mpl.rcParams['figure.dpi'] = 80
mpl.rcParams['savefig.dpi'] = 200
mpl.rcParams['font.size'] = font_size
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['figure.titlesize'] = 'medium'
mpl.rcParams['patch.force_edgecolor'] = True
mpl.rcParams['patch.facecolor'] = 'b'
mpl.rcParams['font.sans-serif'] = "Times New Roman"
mpl.rcParams['font.family'] = "sans-serif"
mpl.rcParams['image.cmap'] = 'jet'

def returnYlabel(title):

    if "VOLT" in title:
        return "Voltage (pu)"
    elif "FREQ" in title:
        return "Frequency (pu)"
    elif "_P" in title:
        return "Power (MW)"
    elif "_Q" in title:
        return "Reactive Power (MVar)"
    else:
        print("Unknown variable (Title is " + title + ")")
        return str(input("Enter new ylabel: "))

def GenerateYlabels(df_columns):
    y_labels = []
    for title in df_columns:
        if returnYlabel(title) not in y_labels:
            y_labels.append(returnYlabel(title))
    return y_labels

def checkio(*args):
    result = []
    for value in args:
        if isinstance(value, (list, tuple)):
            result += checkio(*value)
        else:
            result.append(value)
    return tuple(result)

def IndexInput(max_index):
    while True:
        try:
            user_input = int(ast.literal_eval(input("Enter selected index: ")))
        except ValueError:
            print("Unknown input.")
            continue
        if user_input not in range(max_index + 1):
            print("Index out of range.")
            continue
        else:
            break
    return user_input

def IndexInputPlot(max_index):
    while True:
        try:
            raw_input = input("Enter indexes to plot: ")
            if not raw_input:
                print("No input.")
                user_input = None
                break
            user_input = ast.literal_eval(raw_input)
        except ValueError:
            print("Unknown input.")
            continue

        except SyntaxError:
            print("Unknown input.")
            continue

        if isinstance(user_input, (list,tuple)):
            if any([value not in range(max_index + 1 ) for value in checkio(user_input)]):
                print("Index out of range.")
                continue
            else:
                return user_input
        else:
            if user_input not in range(max_index + 1 ):
                print("Index out of range.")
                continue
            else:
                return user_input

    return user_input

def printColumns(df):
    print("Index" + "\t" + "Value")
    for i, name in enumerate(df):
        print(str(i) + "\t" + name)

def GenerateAxes(fig, numAxes):
    axes = []
#    print("Generating axes.. " + str(numAxes))
    if numAxes <= 1:
        axes.append(fig.add_subplot(1, 1, 1))

    else:
        for i in range(numAxes):
            axes.append(fig.add_subplot(math.ceil(numAxes/2), 2, i + 1))
    return axes

def InitialiseFigure(_length=18, _height=12, _font_size=14):
    fig = plt.figure()
    plt.rcParams.update({'font.size': _font_size})
    fig.set_size_inches(_length, _height)
#    fig.tight_layout()
    return fig

def InitialiseAxes(axes):
    for ax in axes:
        ax.grid(linestyle = '--')
    return axes

print(str(len(data_files)) + " files found in " + data_folder)
printColumns(data_files)
data_file_index = IndexInput(len(data_files))

print("Reading data: " + data_files[data_file_index])
df = pd.read_excel(data_files[0], skiprows=4, index_col=0)
printColumns(df.columns)

if input("Enter 'y' to plot all channels: ") == 'y':
    print("Generating plots..")

    for i, plot in enumerate(df.columns):
        # Initialise figure
        fig = InitialiseFigure(_height = fig_height, _length = fig_length, _font_size = font_size)

        axes = InitialiseAxes(GenerateAxes(fig, 1))
        axes[0].set_ylabel(returnYlabel(df.columns[i]))
        df.iloc[:,i].plot(ax=axes[0], legend=True, grid=True)
        plot_name = "Plot_" + str(i + 1)
        print("Plotting.. " + join(output_folder, plot_name) + ".png")
        fig.savefig(join(output_folder, plot_name))
        fig.clear()
    print("Finished plotting.")

else:
    print("Enter the indexes of the channels to plot as integers or tuples, separated by commas \n")
    print("For single channel plot")
    print("\t" + "Enter a single index.. e.g. 0 \n")
    print("For mutiple channel plot")
    print("\t" + "Enter index separated by commas.. e.g. 0, 1 \n")
    print("For single channel plot")
    print("\t" + "Enter tuples of indexes.. e.g. (0,1), 3, 5, (2,3,4) \n")
    print("Use square brackets [] around the index to plot the channel on its own subplot.. e.g. [0], [1], [3] \n")
    print("Press enter to finish inputs")
    
    plottingList = []
    while True:
        raw_input = IndexInputPlot(len(df.columns))
    
        if raw_input is None:
            break
        plottingList.append(raw_input)
        
    #    if isinstance(raw_input, int):
    #        print(df.columns[raw_input])
    #    elif any(isinstance(x, (list, tuple)) for x in raw_input):
    #        for plot in raw_input:
    #            print(plot)
    #            print("Plot:\t", print(df.columns[plot]))
    #    else:
    #        myString = str()
    #        for plot in raw_input:
    #            myString = ", ".join(df.columns[plot])
    #            print(myString)
    #    try:
    #        print("Plot_", len(plottingList), ": ", str(df.columns[list(plottingList[-1])]))
    #    except TypeError:
    #        print("Plot_", len(plottingList), ": ", str(df.columns[plottingList[-1]]))
    
    print("Plot number: \t" + "Index")
    for i, plot in enumerate(plottingList):
        print("Plot " + str(i + 1) + ": \t" + str(plot))
    
    #plottingList = [(1,2), 3, 4, [(2,3),(4,5)], [(2,3),(4,5),(4,5)], [(2,3),(4,5),(4,5),(2,3)]]
    
    
    
    
    
    print("Generating plots..")
    for plot_number, plot in enumerate(plottingList):
        plot_name = "Plot_" + str(plot_number + 1)
        try:
            if any(isinstance(x, (list, tuple)) for x in plot):
                numPlots = len(plot)
            else:
                numPlots = 1
        except TypeError:
            numPlots = 1
    
    #     Initialise figure
        if numPlots == 1:
            fig = InitialiseFigure(_height = fig_height, _length = fig_length, _font_size = font_size)
        else:
            fig = InitialiseFigure(_height = math.ceil(numPlots/2) * fig_height, _length = 2 * fig_length, _font_size = font_size)
    
        # Initialise axes
        axes = InitialiseAxes(GenerateAxes(fig, numPlots))
    
        # Check if single integer index to plot
        if isinstance(plot, int):
            plotting_df = df.iloc[: , plot]
            plotting_df.plot(ax=axes[0], grid='on', legend=True)
            try:
                axes[0].set_ylabel(returnYlabel(plotting_df.name))
            except AttributeError:
                axes[0].set_ylabel(GenerateYlabels(plotting_df.columns))
    
        # Scenario (multiple channel subplots)
        elif any(isinstance(x, (list, tuple)) for x in plot):
            for i, subplot in enumerate(plot):
    
                try:
                    plotting_df = df.iloc[:, list(subplot)]
                except TypeError:
                    plotting_df = df.iloc[:, subplot]
    
                plotting_df.plot(ax=axes[i], legend=True, grid='on')
                try:
                    axes[i].set_ylabel(returnYlabel(plotting_df.name))
                except AttributeError:
                    axes[i].set_ylabel(GenerateYlabels(plotting_df.columns))
    
        # Scenario (multiple channel plot)
        else:
            plotting_df = df.iloc[: , list(plot)]
            plotting_df.plot(ax=axes[0], grid='on', legend=True)
            try:
                axes[0].set_ylabel(returnYlabel(plotting_df.name))
            except AttributeError:
                axes[0].set_ylabel(GenerateYlabels(plotting_df.columns))
    
    
        print("Plotting.. " + join(output_folder, plot_name) + ".png")
        fig.savefig(join(output_folder, plot_name))
        fig.clear()
    
    print("Finshed plotting.")