import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Load data from Excel
file_path = "C:/Users/erica/OneDrive/Documents/0 Classes/Winter 2025/ME 50a/Project 1/excel/2-2-4-a.xlsx"
df = pd.read_excel(file_path)

# Ensure data is sorted by nodes for better plotting
df.sort_values(by='Nodes', inplace=True)

# Plot configuration
plt.figure(figsize=(8, 6))

# Get the number of unique node counts to generate unique grayscale colors
unique_node_counts = df['Nodes'].nunique()
grayscale_colors = cm.Greys_r(np.linspace(0.1, 0.7, unique_node_counts))  # Darker shades of gray

# Group data by 'Nodes' and plot each group with a unique darker shade of gray
for i, (node_count, group) in enumerate(df.groupby('Nodes')):
    plt.scatter(group['Displacement'], group['Stress'], label=f'Nodes: {node_count}', color=grayscale_colors[i], s=40)

# AIAA-style customization
plt.xlabel('Displacement in y (m)', fontsize=14, color='black')
plt.ylabel('Equivalent Stress (Pa)', fontsize=14, color='black')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_facecolor('white')
plt.gca().spines['bottom'].set_color('black')
plt.gca().spines['left'].set_color('black')
plt.tick_params(axis='both', colors='black')

# Adjust legend to show each node count only once
handles, labels = plt.gca().get_legend_handles_labels()
unique_labels = dict(zip(labels, handles))  # Remove duplicate labels
plt.legend(unique_labels.values(), unique_labels.keys(), fontsize=12)

plt.tight_layout()

# Save the plot as a PNG file
output_path = 'stress_vs_displacement_darker_shades_of_gray.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
plt.show()

print(f"Plot saved as {output_path}")
