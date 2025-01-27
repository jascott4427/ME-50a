import os
import pandas as pd
import matplotlib.pyplot as plt

# Specify the path to the folder containing your xlsx files
input_folder = 'ME 50a\\Project 1\\excel'
output_folder = 'ME 50a\\Project 1\\graphs'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each xlsx file in the folder
for file_name in os.listdir(input_folder):
    if file_name.endswith('.xlsx'):
        file_path = os.path.join(input_folder, file_name)

        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path)

        # Skip the first 3 columns and use the 4th column as x-axis
        x = df.iloc[:, 3]

        # Create a new folder for each file's plots
        file_output_folder = os.path.join(output_folder, file_name.split('.')[0])
        if not os.path.exists(file_output_folder):
            os.makedirs(file_output_folder)

        # Create a figure for plotting multiple y-axes
        fig, ax1 = plt.subplots(figsize=(10, 6))

        # Plot the first column (y-axis) against x
        ax1.plot(x, df.iloc[:, 4], label=df.columns[4], color='black')
        ax1.set_xlabel(df.columns[3])  # Label for x-axis
        ax1.set_ylabel(df.columns[4])  # Label for y-axis
        ax1.tick_params(axis='y', labelcolor='black')

        # Create a second y-axis for the other columns
        ax2 = ax1.twinx()

        # Loop through the additional columns and plot on the second y-axis
        for col in df.columns[5:]:
            ax2.plot(x, df[col], label=col, color='black', linestyle='--')

        # Set the second y-axis label to match the columns plotted
        ax2.set_ylabel(', '.join(df.columns[5:]), color='black')

        # Combine the legends
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')

        # Generate the combined plot file name
        combined_file_name = f"combined_{file_name[:10]}.png"

        # Save the combined plot as a PNG image
        plot_path = os.path.join(file_output_folder, combined_file_name)
        plt.tight_layout()  # Adjust layout to prevent clipping of labels
        plt.savefig(plot_path, format='png')
        plt.close()

        print(f'Combined plot for {file_name} saved as {combined_file_name} in {file_output_folder}')
