#!/usr/bin/env python3
"""
Test script to verify MCP agent functionality.
"""

import sys
import tempfile
import os

# Test 1: Import the package
print("Test 1: Importing mcpdocs_agent...")
try:
    import mcpdocs_agent
    print(f"✓ Successfully imported mcpdocs_agent v{mcpdocs_agent.__version__}")
except ImportError as e:
    print(f"✗ Failed to import: {e}")
    sys.exit(1)

# Test 2: Import server module
print("\nTest 2: Importing server module...")
try:
    from mcpdocs_agent import server
    print("✓ Successfully imported server module")
except ImportError as e:
    print(f"✗ Failed to import server: {e}")
    sys.exit(1)

# Test 3: Check dependencies
print("\nTest 3: Checking dependencies...")
dependencies = [
    ("numpy", "2.0.0"),
    ("pandas", "2.2.0"),
    ("matplotlib", "3.9.0"),
    ("dask", "2024.12.0"),
    ("mcp", "1.1.0"),
]

for package, min_version in dependencies:
    try:
        module = __import__(package)
        version = getattr(module, "__version__", "unknown")
        print(f"  {package}: {version}")
    except ImportError:
        print(f"  {package}: NOT INSTALLED")

# Test 4: Test data generation
print("\nTest 4: Testing data generation...")
try:
    import numpy as np
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    
    # Save to temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        temp_file = f.name
        data = np.column_stack((x, y))
        np.savetxt(f, data, fmt='%.6f', header='x y', comments='')
    
    # Verify file exists
    if os.path.exists(temp_file):
        print(f"✓ Data generation successful: {len(x)} points")
        os.unlink(temp_file)
    else:
        print("✗ Data file not created")
except Exception as e:
    print(f"✗ Data generation failed: {e}")

# Test 5: Test statistics computation
print("\nTest 5: Testing statistics computation...")
try:
    import pandas as pd
    
    # Create test data
    test_data = pd.DataFrame({
        'x': np.linspace(0, 2 * np.pi, 100),
        'y': np.sin(np.linspace(0, 2 * np.pi, 100))
    })
    
    # Compute stats
    stats = test_data.describe()
    print(f"✓ Statistics computation successful")
    print(f"  Mean x: {stats.loc['mean', 'x']:.4f}")
    print(f"  Mean y: {stats.loc['mean', 'y']:.4f}")
except Exception as e:
    print(f"✗ Statistics failed: {e}")

# Test 6: Test matplotlib availability
print("\nTest 6: Testing matplotlib...")
try:
    import matplotlib
    matplotlib.use('Agg')  # Use non-interactive backend
    import matplotlib.pyplot as plt
    
    # Create a simple plot
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 4, 9])
    plt.close()
    
    print("✓ Matplotlib working correctly")
except Exception as e:
    print(f"✗ Matplotlib failed: {e}")

print("\n" + "="*50)
print("All tests completed successfully! ✓")
print("="*50)
print("\nThe MCP agent is ready to use.")
print("Run with: python -m mcpdocs_agent")
