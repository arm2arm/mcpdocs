#!/usr/bin/env python3
"""
Generate sine wave data points and save to a text file.
"""

import numpy as np

# Generate x values from 0 to 2*pi
x = np.linspace(0, 2 * np.pi, 100)

# Calculate sine values
y = np.sin(x)

# Save data to file
data = np.column_stack((x, y))
np.savetxt('sin_data.txt', data, fmt='%.6f', header='x y', comments='')

print("Sine wave data generated successfully!")
print(f"Generated {len(x)} data points from 0 to 2π")
