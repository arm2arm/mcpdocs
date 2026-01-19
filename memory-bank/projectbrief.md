# Project Brief

## Overview
A collection of REANA serial workflow examples demonstrating various patterns for reproducible scientific computing.

## Core Requirements
- Generate sine wave data points (100 points from 0 to 2π)
- Create a plot with proper labels, grid, and π-based x-axis ticks
- Use REANA's serial workflow engine
- Store outputs as files (sin_data.txt, sin_plot.png)
- Ensure reproducibility through containerization

## Technical Stack
- **Workflow Engine**: REANA serial
- **Container**: gitlab-p4n.aip.de:5005/compute4punch/container-stacks/astro-ml:latest
- **Client**: reanahub/reana-client:0.9.4
- **Data Processing**: pandas
- **Visualization**: matplotlib

## Success Criteria
- Workflow runs successfully on REANA server
- Output files (sin_plot.png) generated correctly
- Workflow is reproducible and documented
- Code follows project conventions

## Project Scope
- **sin_plot/**: Simple two-step serial workflow (generate → plot)
- **dask_s3_read/**: Read from S3, compute statistics
- **dask_s3_plot/**: Read from S3, create hexbin plots
- Educational examples for REANA workflows
- Foundation for more complex scientific workflows
