import json
from glob import glob
from os.path import abspath, basename, join, relpath, splitext
import logging
import ntpath
# import itertools
from plothelpers.plothelpers import PlotClass, SubPlotClass

logging.basicConfig(level=logging.INFO)

running_plot_number = 0

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

plot_folder = abspath("../plot_files/C2WF")
plot_files = glob(plot_folder + "/*.json")
data_folder = abspath('U:\\Projects\\PS101926_2208519A\\05_WrkPapers\\WP\\GPS Report Technical Record\\Results_7June18')
output_folder = abspath("../output/C2WF")
data_files = glob(data_folder + "/*.xlsx")

volt_var_files = glob(data_folder + '\\voltvar\\*.xlsx')

for i, data_path in enumerate(volt_var_files):

    running_plot_number += 1

    fname = path_leaf(data_path).split(".")[0]

    plot = PlotClass(data_path, join(output_folder, 'Volt Var'), appendix="A")
    subplot_1 = SubPlotClass(y_index=[1], y_label="Active Power (pu)", subtitle="Active Power in PU", x_min=0, x_max=45.0, y_min=0.9, y_max=1.0)
    subplot_2 = SubPlotClass(y_index=[2], y_label="Reactive Power (pu)", subtitle="Reactive Power in PU)", x_min=0, x_max=45.0)
    subplot_3 = SubPlotClass(y_index=[6], y_label="Voltage (pu)", subtitle="POC Voltage in PU (pu) (rated MVA)", x_min=0, x_max=45.0)
    subplot_4 = SubPlotClass(y_index=[40], y_label="Voltage (pu)", subtitle="Remote bus Ref Voltage in PU", x_min=0, x_max=45.0)
    subplot_5 = SubPlotClass(y_index=[42], y_label="MVAr", subtitle="Branch MVAr for Qdroop", x_min=0, x_max=45.0)
    subplot_6 = SubPlotClass(y_index=[9], y_label="Voltage (pu)", subtitle="Terminal Voltage in PU", x_min=0, x_max=45.0)

    # plot.add_plot(f"Figure {running_plot_number}: C2WF {fname}", f"Figure {running_plot_number}")
    plot.add_plot(f"{fname}", f"Figure {running_plot_number}")
    plot.add_subplot(0, subplot_1.to_dict())
    plot.add_subplot(0, subplot_2.to_dict())
    plot.add_subplot(0, subplot_3.to_dict())
    plot.add_subplot(0, subplot_4.to_dict())   
    plot.add_subplot(0, subplot_5.to_dict())
    plot.add_subplot(0, subplot_6.to_dict())

    json_file_name = basename(splitext(data_path)[0] + '.json')
    logging.info("Creating json file: {}".format(join(plot_folder, json_file_name)))

    with open(join(plot_folder, json_file_name), 'w') as js:
        json.dump(plot.to_dict(), js, indent=4)

winter_high_fault_ride_through_files = glob(data_folder + "\\FaultRideThrough\\Winter High\\Normal\\*.xlsx")

for i, data_path in enumerate(winter_high_fault_ride_through_files):

    running_plot_number += 1

    fname = path_leaf(data_path).split(".")[0]
    logging.info(join(output_folder, 'Volt Var'))
    plot = PlotClass(data_path, join(output_folder, 'Fault Ride Through/Winter High'), appendix="A")
    subplot_1 = SubPlotClass(y_index=[1], y_label="Active Power (MW)", subtitle="Active Power in MW", x_min=8.0, x_max=20.0, y_min=0.0, y_max = 1.1)
    subplot_2 = SubPlotClass(y_index=[2], y_label="Reactive Power (MVAr)", subtitle="Reactive Power in MVAr", x_min=8.0, x_max=20.0)
    subplot_3 = SubPlotClass(y_index=[5], y_label="Current (pu)", subtitle="Terminal Current in PU (rated MVA base)", x_min=8.0, x_max=20.0)
    subplot_4 = SubPlotClass(y_index=[6,7], y_label="Voltage (pu)", subtitle="Voltage in PU", x_min=8.0, x_max=20.0)


    # plot.add_plot(f"Figure {running_plot_number}: C2WF {fname}", f"Figure {running_plot_number}")
    plot.add_plot(f"{fname}", f"Figure {running_plot_number}")
    plot.add_subplot(0, subplot_1.to_dict())
    plot.add_subplot(0, subplot_2.to_dict())
    plot.add_subplot(0, subplot_3.to_dict())
    plot.add_subplot(0, subplot_4.to_dict())   


    json_file_name = basename(splitext(data_path)[0] + '.json')
    logging.info("Creating json file: {}".format(join(plot_folder, json_file_name)))

    with open(join(plot_folder, json_file_name), 'w') as js:
        json.dump(plot.to_dict(), js, indent=4)

winter_high_autoreclose_fault_ride_through_files = glob(data_folder + "\\FaultRideThrough\\Winter High\\Autoreclose\\*.xlsx")

for i, data_path in enumerate(winter_high_autoreclose_fault_ride_through_files):

    running_plot_number += 1

    fname = path_leaf(data_path).split(".")[0]
    logging.info(join(output_folder, 'Volt Var'))
    plot = PlotClass(data_path, join(output_folder, 'Fault Ride Through/Winter High'), appendix="A")
    subplot_1 = SubPlotClass(y_index=[1], y_label="Active Power (MW)", subtitle="Active Power in MW", x_min=8.0, x_max=30.0, y_min=0.0, y_max = 1.1)
    subplot_2 = SubPlotClass(y_index=[2], y_label="Reactive Power (MVAr)", subtitle="Reactive Power in MVAr", x_min=8.0, x_max=30.0)
    subplot_3 = SubPlotClass(y_index=[5], y_label="Current (pu)", subtitle="Terminal Current in PU (rated MVA base)", x_min=8.0, x_max=30.0)
    subplot_4 = SubPlotClass(y_index=[6,7], y_label="Voltage (pu)", subtitle="Voltage in PU", x_min=8.0, x_max=30.0)


    # plot.add_plot(f"Figure {running_plot_number}: C2WF {fname}", f"Figure {running_plot_number}")
    plot.add_plot(f"{fname}", f"Figure {running_plot_number}")
    plot.add_subplot(0, subplot_1.to_dict())
    plot.add_subplot(0, subplot_2.to_dict())
    plot.add_subplot(0, subplot_3.to_dict())
    plot.add_subplot(0, subplot_4.to_dict())   


    json_file_name = basename(splitext(data_path)[0] + '.json')
    logging.info("Creating json file: {}".format(join(plot_folder, json_file_name)))

    with open(join(plot_folder, json_file_name), 'w') as js:
        json.dump(plot.to_dict(), js, indent=4)


winter_low_fault_ride_through_files = glob(data_folder + "\\FaultRideThrough\\Winter Low\\Normal\\*.xlsx")

for i, data_path in enumerate(winter_low_fault_ride_through_files):

    running_plot_number += 1

    fname = path_leaf(data_path).split(".")[0]
    logging.info(join(output_folder, 'Volt Var'))
    plot = PlotClass(data_path, join(output_folder, 'Fault Ride Through/Winter Low'), appendix="A")
    subplot_1 = SubPlotClass(y_index=[1], y_label="Active Power (MW)", subtitle="Active Power in MW", x_min=8.0, x_max=20.0, y_min=0.0, y_max = 1.1)
    subplot_2 = SubPlotClass(y_index=[2], y_label="Reactive Power (MVAr)", subtitle="Reactive Power in MVAr", x_min=8.0, x_max=20.0)
    subplot_3 = SubPlotClass(y_index=[5], y_label="Current (pu)", subtitle="Terminal Current in PU (rated MVA base)", x_min=8.0, x_max=20.0)
    subplot_4 = SubPlotClass(y_index=[6,7], y_label="Voltage (pu)", subtitle="Voltage in PU", x_min=8.0, x_max=20.0)


    # plot.add_plot(f"Figure {running_plot_number}: C2WF {fname}", f"Figure {running_plot_number}")
    plot.add_plot(f"{fname}", f"Figure {running_plot_number}")
    plot.add_subplot(0, subplot_1.to_dict())
    plot.add_subplot(0, subplot_2.to_dict())
    plot.add_subplot(0, subplot_3.to_dict())
    plot.add_subplot(0, subplot_4.to_dict())   


    json_file_name = basename(splitext(data_path)[0] + '.json')
    logging.info("Creating json file: {}".format(join(plot_folder, json_file_name)))

    with open(join(plot_folder, json_file_name), 'w') as js:
        json.dump(plot.to_dict(), js, indent=4)

winter_low_autoreclose_fault_ride_through_files = glob(data_folder + "\\FaultRideThrough\\Winter Low\\Autoreclose\\*.xlsx")

for i, data_path in enumerate(winter_low_autoreclose_fault_ride_through_files):

    running_plot_number += 1

    fname = path_leaf(data_path).split(".")[0]
    logging.info(join(output_folder, 'Volt Var'))
    plot = PlotClass(data_path, join(output_folder, 'Fault Ride Through/Winter Low'), appendix="A")
    subplot_1 = SubPlotClass(y_index=[1], y_label="Active Power (MW)", subtitle="Active Power in MW", x_min=8.0, x_max=30.0, y_min=0.0, y_max = 1.1)
    subplot_2 = SubPlotClass(y_index=[2], y_label="Reactive Power (MVAr)", subtitle="Reactive Power in MVAr", x_min=8.0, x_max=30.0)
    subplot_3 = SubPlotClass(y_index=[5], y_label="Current (pu)", subtitle="Terminal Current in PU (rated MVA base)", x_min=8.0, x_max=30.0)
    subplot_4 = SubPlotClass(y_index=[6,7], y_label="Voltage (pu)", subtitle="Voltage in PU", x_min=8.0, x_max=30.0)


    # plot.add_plot(f"Figure {running_plot_number}: C2WF {fname}", f"Figure {running_plot_number}")
    plot.add_plot(f"{fname}", f"Figure {running_plot_number}")
    plot.add_subplot(0, subplot_1.to_dict())
    plot.add_subplot(0, subplot_2.to_dict())
    plot.add_subplot(0, subplot_3.to_dict())
    plot.add_subplot(0, subplot_4.to_dict())   


    json_file_name = basename(splitext(data_path)[0] + '.json')
    logging.info("Creating json file: {}".format(join(plot_folder, json_file_name)))

    with open(join(plot_folder, json_file_name), 'w') as js:
        json.dump(plot.to_dict(), js, indent=4)


voltage_disturbance_files = glob(data_folder + '\\Voltage Disturbance\\*.xlsx')

for i, data_path in enumerate(voltage_disturbance_files):

    running_plot_number += 1

    fname = path_leaf(data_path).split(".")[0]
    # logging.info(data_path)
    plot = PlotClass(data_path, join(output_folder, 'CUO'), appendix="A")
    subplot_1 = SubPlotClass(y_index=[3], y_label="Active Power (pu)", subtitle="Active Power in PU", x_min=0, x_max=5.0, y_min=0.0, y_max=1.2)
    subplot_2 = SubPlotClass(y_index=[5], y_label="Reactive Power (pu)", subtitle="Reactive Power in PU)", x_min=0, x_max=5.0)
    subplot_3 = SubPlotClass(y_index=[13], y_label="Voltage (pu)", subtitle="POC Voltage in PU", x_min=0, x_max=5.0)


    # plot.add_plot(f"Figure {running_plot_number}: C2WF {fname}", f"Figure {running_plot_number}")
    plot.add_plot(f"{fname}", f"Figure {running_plot_number}")
    plot.add_subplot(0, subplot_1.to_dict())
    plot.add_subplot(0, subplot_2.to_dict())
    plot.add_subplot(0, subplot_3.to_dict())

    json_file_name = basename(splitext(data_path)[0] + '.json')
    logging.info("Creating json file: {}".format(join(plot_folder, json_file_name)))

    with open(join(plot_folder, json_file_name), 'w') as js:
        json.dump(plot.to_dict(), js, indent=4)

frequency_response_files = glob(data_folder + '\\Frequency Response\\*.xlsx')

for i, data_path in enumerate(frequency_response_files):

    running_plot_number += 1

    fname = path_leaf(data_path).split(".")[0]

    plot = PlotClass(data_path, join(output_folder, 'Frequency Response'), appendix="A")
    subplot_1 = SubPlotClass(y_index=[1], y_label="Active Power (pu)", subtitle="Active Power in PU", x_min=0, x_max=25.0)
    subplot_2 = SubPlotClass(y_index=[75], y_label="Frequency deviation (pu)", subtitle="Frequency deviation in PU", x_min=0, x_max=25.0)

    # plot.add_plot(f"Figure {running_plot_number}: C2WF {fname}", f"Figure {running_plot_number}")
    # plot.add_plot("Figure {}: {}".format(i+1, basename(data_path).split('.')[0]))
    plot.add_plot(f"{fname}", f"Figure {running_plot_number}")
    plot.add_subplot(0, subplot_1.to_dict())
    plot.add_subplot(0, subplot_2.to_dict())

    json_file_name = basename(splitext(data_path)[0] + '.json')
    logging.info("Creating json file: {}".format(join(plot_folder, json_file_name)))

    with open(join(plot_folder, json_file_name), 'w') as js:
        json.dump(plot.to_dict(), js, indent=4)