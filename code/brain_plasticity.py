import re
import zipfile
import os
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

"""
Process data for the visualization of the brain network with specified areas.
"""
def process_file(input_file, output_file, header):
    """
    Processes a text file, applying specific modifications, and writes the
    result to a new file.

    Parameters:
    - input_file (str): The path to the input text file.
    - output_file (str): The path to the output text file where the processed
    content will be saved.
    - header (str): The header string to be added at the beginning of the file,
    defining column names.
    """
    # Open the input file for reading
    with open(input_file, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Add the header to the beginning of the lines
    lines.insert(0, header + '\n')

    # Process the lines and filter out lines starting with '#'
    processed_lines = []
    for line in lines:
        if not line.startswith('#'):
            # Use regular expression to replace the value in the fifth column
            line = re.sub(r' area_(\d+)', r' \1', line)

            # Append the processed line
            processed_lines.append(line)

    # Open the output file for writing with tab separation
    with open(output_file, 'w') as file:
        # Write the processed lines back to the file
        file.writelines(processed_lines)

def generate_areas_file(directory, step, in_out):
    """
    Loads and merges network and position data from specified files.

    Args:
    directory (str): Directory path where the files are located.
    step (int): Step number to identify specific file.
    in_out (str): Identifier to distinguish input/output network files.

    Returns:
    None: The function saves the merged data to a new file.
    """
    # Load the input files
    file_network = f'{directory}/rank_0_step_{step}_{in_out}_network_edited.txt'
    file_positions = f'{directory}/rank_0_positions_edited.txt'

    # Read the files with a flexible delimiter handling both spaces and tabs
    df_network = pd.read_csv(file_network, delimiter='[ \t]+', engine='python')
    df_positions = pd.read_csv(file_positions, delimiter='[ \t]+', engine='python')

    # Merge the network dataframe with the positions dataframe twice: once for the TargetID and once for the SourceID
    merged = df_network.merge(df_positions, left_on='TargetID', right_on='LocalID')
    merged = merged.merge(df_positions, left_on='SourceID', right_on='LocalID', suffixes=('_Target', '_Source'))

    # Select and rename columns to match the output format
    output_df = merged[['TargetRank', 'TargetID', 'SourceRank', 'SourceID', 'Weight',
                        'Area_Target', 'PosX_Target', 'PosY_Target', 'PosZ_Target',
                        'Area_Source', 'PosX_Source', 'PosY_Source', 'PosZ_Source']].copy()

    output_df.rename(columns={'Area_Target': 'TargetArea', 'PosX_Target': 'TargetPosX',
                              'PosY_Target': 'TargetPosY', 'PosZ_Target': 'TargetPosZ',
                              'Area_Source': 'SourceArea', 'PosX_Source': 'SourcePosX',
                              'PosY_Source': 'SourcePosY', 'PosZ_Source': 'SourcePosZ'}, inplace=True)

    # Save to a new file
    output_file = f'{directory}/rank_0_step_{step}_{in_out}_network_areas1.txt'
    output_df.to_csv(output_file, sep=' ', index=False)

def generate_areas2_file(directory, step, in_out):
    """
    Processes neural network data to calculate average positions and sum of weights.

    Args:
    directory (str): Directory where the input file is located.
    step (int): Simulation step for identifying the specific file.
    in_out (str): Specifies whether the file is input or output type.

    Returns:
    None: The function saves the processed data to a new file.

    The function loads network data, combines target and source positions to calculate
    average positions per area, groups data by target and source areas, calculates sum
    of weights, and assigns average positions. The output is saved to a new file.
    """
    # Load the original file
    input_file = f'{directory}/rank_0_step_{step}_{in_out}_network_areas1.txt'
    df = pd.read_csv(input_file, delimiter='[ \t]+', engine='python')

    # Combine Target and Source positions and calculate unique average positions for each area
    df_combined = pd.concat([
        df[['TargetArea', 'TargetPosX', 'TargetPosY', 'TargetPosZ']].rename(
            columns={'TargetArea': 'Area', 'TargetPosX': 'PosX', 'TargetPosY': 'PosY', 'TargetPosZ': 'PosZ'}),
        df[['SourceArea', 'SourcePosX', 'SourcePosY', 'SourcePosZ']].rename(
            columns={'SourceArea': 'Area', 'SourcePosX': 'PosX', 'SourcePosY': 'PosY', 'SourcePosZ': 'PosZ'})
    ])

    # Calculate average positions for each area
    area_avg_positions = df_combined.groupby('Area').mean().round(5)

    # Group by 'TargetArea' and 'SourceArea', and then calculate the required sum
    grouped = df.groupby(['TargetArea', 'SourceArea'])
    output_df = grouped.agg(SumWeights=('Weight', 'sum')).reset_index()

    # Use the pre-calculated averages for each area for both target and source positions
    for index, row in output_df.iterrows():
        target_area = row['TargetArea']
        source_area = row['SourceArea']
        output_df.at[index, 'AvgTargetPosX'] = area_avg_positions.loc[target_area, 'PosX']
        output_df.at[index, 'AvgTargetPosY'] = area_avg_positions.loc[target_area, 'PosY']
        output_df.at[index, 'AvgTargetPosZ'] = area_avg_positions.loc[target_area, 'PosZ']
        output_df.at[index, 'AvgSourcePosX'] = area_avg_positions.loc[source_area, 'PosX']
        output_df.at[index, 'AvgSourcePosY'] = area_avg_positions.loc[source_area, 'PosY']
        output_df.at[index, 'AvgSourcePosZ'] = area_avg_positions.loc[source_area, 'PosZ']

    # Save to a new file
    output_file = f'{directory}/rank_0_step_{step}_{in_out}_network_areas2.txt'
    output_df.to_csv(output_file, sep=' ', index=False)

def generate_areas3_file(directory, step, in_out):
    """
    Processes network data to create a modified structure with separate entries for source and target areas.

    This function loads data from a specified 'network_areas2.txt' file, iterates through each row to generate
    two new rows for every original row (one for source and one for target positions), and saves this new data structure
    to 'network_areas.txt'. It's used to facilitate further analysis of network connectivity and spatial data in neuroscience.

    Args:
    directory (str): The directory path where the input and output files are located.
    step (int): The step number in the simulation process.
    in_out (str): Indicates whether the file is for input or output in the network analysis.

    Returns:
    None: Saves the processed data to a new file.
    """
    # Load the previously generated file
    input_file = f'{directory}/rank_0_step_{step}_{in_out}_network_areas2.txt'
    df = pd.read_csv(input_file, delimiter='[ \t]+', engine='python')

    # List to store the new rows
    new_rows = []

    # Loop through the rows of the input DataFrame and create two new rows for each
    for index, row in df.iterrows():
        # First new row (Source position values)
        new_rows.append({'TargetArea': row['TargetArea'],
                         'SourceArea': row['SourceArea'],
                         'Area': row['SourceArea'],
                         'AvgPosX': row['AvgSourcePosX'],
                         'AvgPosY': row['AvgSourcePosY'],
                         'AvgPosZ': row['AvgSourcePosZ'],
                         'SumWeights': row['SumWeights']})

        # Second new row (Target position values)
        new_rows.append({'TargetArea': row['TargetArea'],
                         'SourceArea': row['SourceArea'],
                         'Area': row['TargetArea'],
                         'AvgPosX': row['AvgTargetPosX'],
                         'AvgPosY': row['AvgTargetPosY'],
                         'AvgPosZ': row['AvgTargetPosZ'],
                         'SumWeights': row['SumWeights']})

    # Create a DataFrame from the list of new rows
    new_df = pd.DataFrame(new_rows)

    # Save to a new file
    output_file = f'{directory}/rank_0_step_{step}_{in_out}_network_areas.txt'
    new_df.to_csv(output_file, sep=' ', index=False)

def clean_up_files(*file_paths):
    for file_path in file_paths:
        try:
            os.remove(file_path)
        except OSError as e:
            print(f"Error: {file_path} : {e.strerror}")

def get_areas(data_directory, result_directory, in_out):
    # Make sure the output directory exists
    if not os.path.exists(result_directory):
        os.makedirs(result_directory)

    process_file(f'{data_directory}/positions/rank_0_positions.txt', f'{result_directory}/rank_0_positions_edited.txt', 'LocalID PosX PosY PosZ Area Type')

    for step in range(0, 1000001, 10000):
        process_file(f'{data_directory}/network/rank_0_step_{step}_{in_out}_network.txt', f'{result_directory}/rank_0_step_{step}_{in_out}_network_edited.txt', 'TargetRank TargetID SourceRank SourceID Weight')
        generate_areas_file(result_directory, step, in_out)
        generate_areas2_file(result_directory, step, in_out)
        generate_areas3_file(result_directory, step, in_out)
        clean_up_files(f'{result_directory}/rank_0_step_{step}_{in_out}_network_edited.txt',
                      f'{result_directory}/rank_0_step_{step}_{in_out}_network_areas1.txt',
                      f'{result_directory}/rank_0_step_{step}_{in_out}_network_areas2.txt')

# Example usage:

# get_areas('SciVisContest23/viz-no-network', 'no_network_area', 'out')
# get_areas('SciVisContest23/viz-no-network', 'no_network_area', 'in')

# get_areas('SciVisContest23/viz-disable', 'disable_area', 'out')
# get_areas('SciVisContest23/viz-disable', 'disable_area', 'in')

# get_areas('SciVisContest23/viz-stimulus', 'stimulus_area', 'out')
# get_areas('SciVisContest23/viz-stimulus', 'stimulus_area', 'in')

# get_areas('SciVisContest23/viz-calcium', 'calcium_area', 'out')
# get_areas('SciVisContest23/viz-calcium', 'calcium_area', 'in')


"""
Create timeseries for the visualization of the brain network to be compatible
with ParaView.
"""
def create_timeseries(directory, in_out):
    """
    Rename files in the specified directory for proper ordering in ParaView.

    Args:
    directory (str): Path to the directory containing the files.
    file_type (str): Type of the files ('in' or 'out').
    """
    pattern = rf'rank_0_step_(\d+)_{in_out}_network_areas.txt'
    for filename in os.listdir(directory):
        match = re.match(pattern, filename)
        if match:
            # Extract the number part from the filename
            number_part = int(match.group(1))

            # Format the number with leading zeros (7 digits)
            new_number_part = f'{number_part:07d}'

            # Construct the new filename
            new_filename = f'rank_0_step_{new_number_part}_{in_out}_network_areas.txt'

            # Construct full old and new file paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed {old_file} to {new_file}')

# Example usage:

# create_timeseries('/no_network_area', 'in')
# create_timeseries('/no_network_area', 'out')

# create_timeseries('/disable_area', 'in')
# create_timeseries('/disable_area', 'out')

# create_timeseries('/stimulus_area', 'in')
# create_timeseries('/stimulus_area', 'out')

# create_timeseries('/calcium_area', 'in')
# create_timeseries('/calcium_area', 'out')


"""
Group data to monitor grown and connected axons/dendrites per area.
"""
def read_positions_file(positions_file):
    df = pd.read_csv(positions_file, delimiter=' ')
    return dict(zip(df['LocalID'], df['Area']))

def process_neuron_files(data_directory, neuron_to_area):
    area_data = {area: {col: np.zeros(10000) for col in range(1, 11)} for area in range(48)}
    neuron_count_by_area = {area: np.zeros(10000) for area in range(48)}

    for neuron_id in tqdm(range(1, 50001), desc='Processing Neuron Files'):
        neuron_file = os.path.join(data_directory, f"monitors/0_{neuron_id - 1}.csv")
        area = neuron_to_area[neuron_id]
        df_neuron = pd.read_csv(neuron_file, delimiter=';', header=None)

        for i in range(10000):
            step = i
            neuron_count_by_area[area][step] += 1
            for col in range(1, 11):
                column_index = 2 + col
                area_data[area][col][step] += df_neuron.iloc[i, column_index]

    # Calculate averages and sums for each area
    for area in area_data:
        for step in range(10000):
            count = neuron_count_by_area[area][step]
            if count > 0:
                for col in range(1, 11):  # Averages for 10 columns
                    area_data[area][col][step] /= count

    return area_data

def save_area_data(output_directory, area_data):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for area in range(48):
        filename = f"area_{area}.csv"
        filepath = os.path.join(output_directory, filename)
        with open(filepath, 'w') as file:
            file.write('Step,Activity,Dampening,CurrentCalcium,TargetCalcium,SynapticInput,BackgroundInput,GrownAxons,ConnectedAxons,GrownDendrites,ConnectedDendrites\n')
            for step in range(10000):
                values = [area_data[area][col][step] for col in range(1, 11)]
                file.write(f"{step+1},")  # Step numbering from 1
                file.write(','.join(str(v) for v in values))
                file.write('\n')

def data_per_area(data_directory, positions_file, output_directory):
    neuron_to_area = read_positions_file(positions_file)
    area_data = process_neuron_files(data_directory, neuron_to_area)
    save_area_data(output_directory, area_data)

# Example usage:

# data_per_area('SciVisContest23/viz-no-network', 'no_network_area/rank_0_positions_edited.txt', 'no_network_per_area')

# data_per_area('SciVisContest23/viz-stimulus', 'stimulus_area/rank_0_positions_edited.txt', 'stimulus_per_area')

# data_per_area('SciVisContest23/viz-calcium', 'calcium_area/rank_0_positions_edited.txt', 'calcium_per_area')

# data_per_area('SciVisContest23/viz-disable', 'disable_area/rank_0_positions_edited.txt', 'disable_per_area')


"""
Generate figures of the monitored grown and connected axons/dendrites per area.
"""
def growth_connections_calcium_plot_no_network(filename, area):
    steps = []
    target_calcium_levels = []
    calcium_levels = []
    grown_axons = []
    connected_axons = []
    grown_dendrites = []
    connected_dendrites = []
    lines_table = 0

    with open(filename, 'r') as file:
        for line in file:
            split_data = line.split(',')

            if lines_table == 1:
                step = float(split_data[0]) * 100
                calcium_level = float(split_data[3])
                target_calcium_level = float(split_data[4])
                grown_axon = float(split_data[7])
                connected_axon = float(split_data[8])
                grown_dendrite = float(split_data[9])
                connected_dendrite = float(split_data[10])

                steps.append(step)
                calcium_levels.append(calcium_level)
                target_calcium_levels.append(target_calcium_level)
                grown_axons.append(grown_axon)
                connected_axons.append(connected_axon)
                grown_dendrites.append(grown_dendrite)
                connected_dendrites.append(connected_dendrite)

            if split_data[0] == 'Step':
                lines_table = 1

        fig, ax1 = plt.subplots(figsize=(12, 9))

        # Plotting on the primary y-axis
        ax1.plot(steps, grown_axons, 'c', label='Grown Axons')
        ax1.plot(steps, connected_axons, 'b', label='Connected Axons')
        ax1.plot(steps, grown_dendrites, 'salmon', label='Grown Dendrites')
        ax1.plot(steps, connected_dendrites, 'sienna', label='Connected Dendrites')
        ax1.set_xlabel("Step ($x 10^6$)", fontsize=26, fontname='Times New Roman')
        ax1.set_ylabel('Grown and connected axons/dendrites (normalized) [—]', fontsize=24, fontname='Times New Roman')
        ax1.tick_params(axis='y', labelsize=20)
        ax1.tick_params(axis='x', labelsize=20)

        # Plotting on the secondary y-axis
        ax2 = ax1.twinx()
        ax2.plot(steps, calcium_levels, 'r--', label='Calcium Level')
        ax2.plot(steps, target_calcium_levels, 'k--', label='Target Calcium Level')
        ax2.set_ylabel('Calcium level (normalized) [--]', fontsize=24, fontname='Times New Roman')
        ax2.tick_params(axis='y', labelsize=20)

        # Title and Legend
        plt.title(f'Area {area}, no-network', fontdict={'fontname': 'Times New Roman', 'fontsize': 26})
        lines, labels = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc='lower right', fontsize='18')

        # Save the plot to a file
        output_path = 'no_network_figures'
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        plt.savefig(f'{output_path}/no_network_area_{area}.png', format='png', dpi=300)
        # plt.show()

def growth_connections_calcium_plot_stimulus(filename, area):
    steps = []
    target_calcium_levels = []
    calcium_levels = []
    grown_axons = []
    connected_axons = []
    grown_dendrites = []
    connected_dendrites = []
    lines_table = 0

    with open(filename, 'r') as file:
        for line in file:
            split_data = line.split(',')

            if lines_table == 1:
                step = float(split_data[0]) * 100
                calcium_level = float(split_data[3])
                target_calcium_level = float(split_data[4])
                grown_axon = float(split_data[7])
                connected_axon = float(split_data[8])
                grown_dendrite = float(split_data[9])
                connected_dendrite = float(split_data[10])

                steps.append(step)
                calcium_levels.append(calcium_level)
                target_calcium_levels.append(target_calcium_level)
                grown_axons.append(grown_axon)
                connected_axons.append(connected_axon)
                grown_dendrites.append(grown_dendrite)
                connected_dendrites.append(connected_dendrite)

            if split_data[0] == 'Step':
                lines_table = 1

        fig, ax1 = plt.subplots(figsize=(12, 9))

        # Plotting on the primary y-axis
        ax1.plot(steps, grown_axons, 'c', label='Grown Axons')
        ax1.plot(steps, connected_axons, 'b', label='Connected Axons')
        ax1.plot(steps, grown_dendrites, 'salmon', label='Grown Dendrites')
        ax1.plot(steps, connected_dendrites, 'sienna', label='Connected Dendrites')
        ax1.set_xlabel("Step ($x 10^6$)", fontsize=26, fontname='Times New Roman')
        ax1.set_ylabel('Grown and connected axons/dendrites (normalized) [—]', fontsize=24, fontname='Times New Roman')
        ax1.tick_params(axis='y', labelsize=20)
        ax1.tick_params(axis='x', labelsize=20)

        # Plotting on the secondary y-axis
        ax2 = ax1.twinx()
        ax2.plot(steps, calcium_levels, 'r--', label='Calcium Level')
        ax2.plot(steps, target_calcium_levels, 'k--', label='Target Calcium Level')
        ax2.set_ylabel('Calcium level (normalized) [--]', fontsize=24, fontname='Times New Roman')
        ax2.tick_params(axis='y', labelsize=20)

        # Title and Legend
        plt.title(f'Area {area}, stimulus', fontdict={'fontname': 'Times New Roman', 'fontsize': 26})
        lines, labels = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc='lower right', fontsize='18')

        # Save the plot to a file
        output_path = 'stimulus_figures'
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        plt.savefig(f'{output_path}/stimulus_area_{area}.png', format='png', dpi=300)
        # plt.show()

def growth_connections_calcium_plot_disable(filename, area):
    steps = []
    target_calcium_levels = []
    calcium_levels = []
    grown_axons = []
    connected_axons = []
    grown_dendrites = []
    connected_dendrites = []
    lines_table = 0

    with open(filename, 'r') as file:
        for line in file:
            split_data = line.split(',')

            if lines_table == 1:
                step = float(split_data[0]) * 100
                calcium_level = float(split_data[3])
                target_calcium_level = float(split_data[4])
                grown_axon = float(split_data[7])
                connected_axon = float(split_data[8])
                grown_dendrite = float(split_data[9])
                connected_dendrite = float(split_data[10])

                steps.append(step)
                calcium_levels.append(calcium_level)
                target_calcium_levels.append(target_calcium_level)
                grown_axons.append(grown_axon)
                connected_axons.append(connected_axon)
                grown_dendrites.append(grown_dendrite)
                connected_dendrites.append(connected_dendrite)

            if split_data[0] == 'Step':
                lines_table = 1

        fig, ax1 = plt.subplots(figsize=(12, 9))

        # Plotting on the primary y-axis
        ax1.plot(steps, grown_axons, 'c', label='Grown Axons')
        ax1.plot(steps, connected_axons, 'b', label='Connected Axons')
        ax1.plot(steps, grown_dendrites, 'salmon', label='Grown Dendrites')
        ax1.plot(steps, connected_dendrites, 'sienna', label='Connected Dendrites')
        ax1.set_xlabel("Step ($x 10^6$)", fontsize=26, fontname='Times New Roman')
        ax1.set_ylabel('Grown and connected axons/dendrites (normalized) [—]', fontsize=24, fontname='Times New Roman')
        ax1.tick_params(axis='y', labelsize=20)
        ax1.tick_params(axis='x', labelsize=20)

        # Plotting on the secondary y-axis
        ax2 = ax1.twinx()
        ax2.plot(steps, calcium_levels, 'r--', label='Calcium Level')
        ax2.plot(steps, target_calcium_levels, 'k--', label='Target Calcium Level')
        ax2.set_ylabel('Calcium level (normalized) [--]', fontsize=24, fontname='Times New Roman')
        ax2.tick_params(axis='y', labelsize=20)

        # Title and Legend
        plt.title(f'Area {area}, Disable', fontdict={'fontname': 'Times New Roman', 'fontsize': 26})
        lines, labels = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc='center right', fontsize='18')

        # Save the plot to a file
        output_path = 'disable_figures'
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        plt.savefig(f'{output_path}/disable_area_{area}.png', format='png', dpi=300)
        # plt.show()

def growth_connections_calcium_plot_calcium(filename, area):
    steps = []
    target_calcium_levels = []
    calcium_levels = []
    grown_axons = []
    connected_axons = []
    grown_dendrites = []
    connected_dendrites = []
    lines_table = 0

    with open(filename, 'r') as file:
        for line in file:
            split_data = line.split(',')

            if lines_table == 1:
                step = float(split_data[0]) * 100
                calcium_level = float(split_data[3])
                target_calcium_level = float(split_data[4])
                grown_axon = float(split_data[7])
                connected_axon = float(split_data[8])
                grown_dendrite = float(split_data[9])
                connected_dendrite = float(split_data[10])

                steps.append(step)
                calcium_levels.append(calcium_level)
                target_calcium_levels.append(target_calcium_level)
                grown_axons.append(grown_axon)
                connected_axons.append(connected_axon)
                grown_dendrites.append(grown_dendrite)
                connected_dendrites.append(connected_dendrite)

            if split_data[0] == 'Step':
                lines_table = 1

        fig, ax1 = plt.subplots(figsize=(12, 9))

        # Plotting on the primary y-axis
        ax1.plot(steps, grown_axons, 'c', label='Grown Axons')
        ax1.plot(steps, connected_axons, 'b', label='Connected Axons')
        ax1.plot(steps, grown_dendrites, 'salmon', label='Grown Dendrites')
        ax1.plot(steps, connected_dendrites, 'sienna', label='Connected Dendrites')
        ax1.set_xlabel("Step ($x 10^6$)", fontsize=26, fontname='Times New Roman')
        ax1.set_ylabel('Grown and connected axons/dendrites (normalized) [—]', fontsize=24, fontname='Times New Roman')
        ax1.tick_params(axis='y', labelsize=20)
        ax1.tick_params(axis='x', labelsize=20)

        # Plotting on the secondary y-axis
        ax2 = ax1.twinx()
        ax2.plot(steps, calcium_levels, 'r--', label='Calcium Level')
        ax2.plot(steps, target_calcium_levels, 'k--', label='Target Calcium Level')
        ax2.set_ylabel('Calcium level (normalized) [--]', fontsize=24, fontname='Times New Roman')
        ax2.tick_params(axis='y', labelsize=20)

        # Title and Legend
        plt.title(f'Area {area}, Calcium', fontdict={'fontname': 'Times New Roman', 'fontsize': 26})
        lines, labels = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc='lower left', fontsize='18')

        # Save the plot to a file
        output_path = 'calcium_figures'
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        plt.savefig(f'{output_path}/calcium_area_{area}.png', format='png', dpi=300)
        # plt.show()

# Example usage:

for i in range(48):
    growth_connections_calcium_plot_no_network(f'no_network_per_area/area_{i}.csv', f'{i}')

for i in range(48):
    growth_connections_calcium_plot_stimulus(f'stimulus_per_area/area_{i}.csv', f'{i}')

for i in range(48):
    growth_connections_calcium_plot_disable(f'disable_per_area/area_{i}.csv', f'{i}')

for i in range(48):
    growth_connections_calcium_plot_calcium(f'calcium_per_area/area_{i}.csv', f'{i}')
