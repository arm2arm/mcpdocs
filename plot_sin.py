#!/usr/bin/env python3
"""
Plot sine wave from data file and save as PNG.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read data from file using pandas
df = pd.read_csv('sin_data.txt', sep=' ')
x = df['x'].values
y = df['y'].values

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')
plt.grid(True, alpha=0.3)
plt.xlabel('x (radians)', fontsize=12)
plt.ylabel('sin(x)', fontsize=12)
plt.title('Sine Wave Plot', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)

# Add horizontal line at y=0
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)

# Set x-axis ticks at multiples of π/2
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           ['0', 'π/2', 'π', '3π/2', '2π'])

# Save the plot
plt.tight_layout()
plt.savefig('sin_plot.png', dpi=150, bbox_inches='tight')

print("Sine wave plot created successfully!")
print("Output saved to: sin_plot.png")
