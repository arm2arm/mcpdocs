# Dask Interactive Notebook

This directory contains an interactive Jupyter notebook demonstrating data visualization with Dask and hvplot from S3 data.

## Overview

The `dask_interactive.ipynb` notebook demonstrates:

1. **S3 Data Access**: Reading large parquet datasets from S3 using Dask
2. **Interactive Visualization**: Creating interactive plots with hvplot
3. **Dynamic Filtering**: Using Panel widgets for real-time data exploration
4. **Scalable Analysis**: Working with large datasets efficiently

## Features

- **Interactive Scatter Plots**: Explore relationships between galactic coordinates
- **Hexbin Plots**: Visualize density distributions efficiently
- **Histograms**: Analyze data distributions interactively
- **Widget-based Filtering**: Dynamically filter data using range sliders
- **Dashboard Integration**: Combine multiple visualizations into a cohesive dashboard

## Data Source

The notebook uses the same S3 data source as the existing `dask_s3_plot` example:
- **Dataset**: shboost_08july2024_pub.parq
- **S3 Endpoint**: https://s3.data.aip.de:9000
- **Access**: Anonymous (public)
- **Format**: Parquet

## Requirements

To run this notebook, you'll need:

- Python 3.7+
- Jupyter Notebook or JupyterLab
- Required packages:
  - dask
  - hvplot
  - panel
  - pandas
  - numpy
  - s3fs
  - bokeh

## Installation

```bash
pip install dask hvplot panel pandas numpy s3fs bokeh
```

## Usage

1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Open `dask_interactive.ipynb`

3. Run the cells sequentially to:
   - Load data from S3
   - Explore basic statistics
   - Create interactive visualizations
   - Use widgets to filter and explore data

## Key Advantages

- **Efficient Memory Usage**: Dask's lazy evaluation prevents loading the entire dataset into memory
- **Interactive Exploration**: hvplot and Panel provide rich, responsive visualizations
- **Scalability**: The same code works with both sampled data and the full dataset
- **Reproducibility**: All data access and processing is clearly documented

## Related Examples

- [`../dask_s3_read/`](../dask_s3_read/): Basic S3 data reading and statistics
- [`../dask_s3_plot/`](../dask_s3_plot/): Static hexbin plot generation

## Tips

- Start with the sampled data (5% of the dataset) for faster interactive exploration
- Use the widgets to dynamically filter data and see real-time updates
- The full dataset can be processed by removing the sampling step
- All plots are interactive - hover over points to see detailed information