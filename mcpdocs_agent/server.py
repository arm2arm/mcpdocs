#!/usr/bin/env python3
"""
MCP Server for REANA Scientific Workflows

This MCP server provides tools for scientific data processing, visualization,
and workflow automation using REANA.
"""

import asyncio
import logging
from typing import Any, Sequence

import numpy as np
import pandas as pd
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
)
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GenerateDataParams(BaseModel):
    """Parameters for generating sine wave data."""
    num_points: int = Field(default=100, description="Number of data points to generate")
    start: float = Field(default=0.0, description="Start value in radians")
    end: float = Field(default=6.283185307179586, description="End value in radians (default: 2π)")
    function: str = Field(default="sin", description="Function to generate: sin, cos, tan")


class PlotDataParams(BaseModel):
    """Parameters for plotting data."""
    data_file: str = Field(description="Path to data file to plot")
    output_file: str = Field(default="plot.png", description="Output plot filename")
    title: str = Field(default="Data Plot", description="Plot title")
    xlabel: str = Field(default="x", description="X-axis label")
    ylabel: str = Field(default="y", description="Y-axis label")


class StatisticsParams(BaseModel):
    """Parameters for computing statistics."""
    data_file: str = Field(description="Path to data file")


class S3DataParams(BaseModel):
    """Parameters for S3 data operations."""
    bucket: str = Field(description="S3 bucket name")
    prefix: str = Field(description="S3 key prefix/path")
    endpoint_url: str = Field(default="https://s3.data.aip.de:9000", description="S3 endpoint URL")
    sample_fraction: float = Field(default=0.01, description="Fraction of data to sample (0.0-1.0)")


# Initialize MCP server
app = Server("mcpdocs-agent")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List all available tools."""
    return [
        Tool(
            name="generate_sine_data",
            description="Generate sine/cosine/tangent wave data points and save to a file",
            inputSchema=GenerateDataParams.model_json_schema(),
        ),
        Tool(
            name="plot_data",
            description="Create a visualization plot from data file and return as PNG",
            inputSchema=PlotDataParams.model_json_schema(),
        ),
        Tool(
            name="compute_statistics",
            description="Compute statistical summary (mean, std, min, max, etc.) from data file",
            inputSchema=StatisticsParams.model_json_schema(),
        ),
        Tool(
            name="analyze_s3_data",
            description="Read and analyze parquet data from S3 storage using Dask",
            inputSchema=S3DataParams.model_json_schema(),
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
    """Handle tool calls."""
    
    if name == "generate_sine_data":
        params = GenerateDataParams(**arguments)
        
        # Generate data based on function type
        x = np.linspace(params.start, params.end, params.num_points)
        
        if params.function == "sin":
            y = np.sin(x)
        elif params.function == "cos":
            y = np.cos(x)
        elif params.function == "tan":
            y = np.tan(x)
        else:
            return [TextContent(
                type="text",
                text=f"Error: Unknown function '{params.function}'. Use 'sin', 'cos', or 'tan'."
            )]
        
        # Save data to file
        output_file = f"{params.function}_data.txt"
        data = np.column_stack((x, y))
        np.savetxt(output_file, data, fmt='%.6f', header='x y', comments='')
        
        result = f"Generated {params.num_points} {params.function} data points from {params.start:.2f} to {params.end:.2f} radians.\n"
        result += f"Saved to: {output_file}\n"
        result += f"Data range: x=[{x.min():.4f}, {x.max():.4f}], y=[{y.min():.4f}, {y.max():.4f}]"
        
        return [TextContent(type="text", text=result)]
    
    elif name == "plot_data":
        params = PlotDataParams(**arguments)
        
        try:
            import matplotlib
            matplotlib.use('Agg')  # Use non-interactive backend
            import matplotlib.pyplot as plt
            
            # Read data from file
            df = pd.read_csv(params.data_file, sep=r'\s+')
            
            if len(df.columns) < 2:
                return [TextContent(
                    type="text",
                    text=f"Error: Data file must have at least 2 columns. Found: {len(df.columns)}"
                )]
            
            x = df.iloc[:, 0].values
            y = df.iloc[:, 1].values
            
            # Create plot
            plt.figure(figsize=(10, 6))
            plt.plot(x, y, 'b-', linewidth=2)
            plt.grid(True, alpha=0.3)
            plt.xlabel(params.xlabel, fontsize=12)
            plt.ylabel(params.ylabel, fontsize=12)
            plt.title(params.title, fontsize=14, fontweight='bold')
            plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
            
            # Set π-based ticks if data range suggests radians
            if x.max() > 5 and x.max() < 8:
                plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
                          ['0', 'π/2', 'π', '3π/2', '2π'])
            
            plt.tight_layout()
            plt.savefig(params.output_file, dpi=150, bbox_inches='tight')
            plt.close()
            
            # Read the image and encode as base64
            import base64
            with open(params.output_file, 'rb') as f:
                image_data = base64.b64encode(f.read()).decode('utf-8')
            
            result = f"Plot created successfully!\n"
            result += f"Data points: {len(x)}\n"
            result += f"X range: [{x.min():.4f}, {x.max():.4f}]\n"
            result += f"Y range: [{y.min():.4f}, {y.max():.4f}]\n"
            result += f"Saved to: {params.output_file}"
            
            return [
                TextContent(type="text", text=result),
                ImageContent(
                    type="image",
                    data=image_data,
                    mimeType="image/png"
                )
            ]
            
        except Exception as e:
            return [TextContent(type="text", text=f"Error creating plot: {str(e)}")]
    
    elif name == "compute_statistics":
        params = StatisticsParams(**arguments)
        
        try:
            # Read data from file
            df = pd.read_csv(params.data_file, sep=r'\s+')
            
            # Compute statistics
            stats = df.describe()
            
            result = f"Statistical Summary for {params.data_file}\n"
            result += "=" * 60 + "\n\n"
            result += f"Total rows: {len(df)}\n"
            result += f"Total columns: {len(df.columns)}\n\n"
            result += "Descriptive Statistics:\n"
            result += "-" * 60 + "\n"
            result += stats.to_string()
            
            # Add correlation if multiple columns
            if len(df.columns) > 1:
                result += "\n\n" + "Correlation Matrix:\n" + "-" * 60 + "\n"
                result += df.corr().to_string()
            
            return [TextContent(type="text", text=result)]
            
        except Exception as e:
            return [TextContent(type="text", text=f"Error computing statistics: {str(e)}")]
    
    elif name == "analyze_s3_data":
        params = S3DataParams(**arguments)
        
        try:
            import dask.dataframe as dd
            
            # Construct S3 path
            s3_path = f"s3://{params.bucket}/{params.prefix}/*.parquet"
            
            logger.info(f"Reading data from {s3_path}")
            
            # Read parquet data from S3
            df = dd.read_parquet(
                s3_path,
                storage_options={
                    'use_ssl': True,
                    'anon': True,
                    'client_kwargs': dict(endpoint_url=params.endpoint_url)
                }
            )
            
            # Sample and compute
            logger.info(f"Sampling {params.sample_fraction*100}% of data...")
            df_sample = df.sample(frac=params.sample_fraction).persist()
            df_compute = df_sample.compute()
            
            # Compute statistics
            stats = df_compute.describe()
            
            result = f"S3 Data Analysis Results\n"
            result += "=" * 60 + "\n\n"
            result += f"S3 Path: {s3_path}\n"
            result += f"Endpoint: {params.endpoint_url}\n"
            result += f"Sample fraction: {params.sample_fraction*100}%\n\n"
            result += f"Sample size: {len(df_compute)} rows\n"
            result += f"Columns: {len(df_compute.columns)}\n"
            result += f"Column names: {', '.join(df_compute.columns[:10])}"
            if len(df_compute.columns) > 10:
                result += f"... ({len(df_compute.columns) - 10} more)"
            result += "\n\n"
            result += "Descriptive Statistics:\n"
            result += "-" * 60 + "\n"
            result += stats.to_string()
            
            # Memory usage
            memory_gb = df_compute.memory_usage(deep=True).sum() / 1e9
            result += f"\n\nMemory usage: {memory_gb:.2f} GB"
            
            return [TextContent(type="text", text=result)]
            
        except Exception as e:
            logger.error(f"Error analyzing S3 data: {str(e)}")
            return [TextContent(type="text", text=f"Error analyzing S3 data: {str(e)}")]
    
    else:
        return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def main():
    """Run the MCP server."""
    logger.info("Starting MCP server for REANA scientific workflows...")
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
