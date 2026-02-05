# MCP Agent for REANA Scientific Workflows

## Overview

The **mcpdocs-agent** is an MCP (Model Context Protocol) server that provides agentic capabilities for scientific computing workflows. It offers AI assistants and automation tools to interact with REANA workflows, process scientific data, and create visualizations.

## Features

- **Data Generation**: Generate mathematical function data (sine, cosine, tangent)
- **Data Visualization**: Create publication-quality plots from data files
- **Statistical Analysis**: Compute comprehensive statistics on datasets
- **Cloud Data Access**: Read and analyze parquet data from S3 storage using Dask
- **Workflow Integration**: Designed to work seamlessly with REANA workflows

## Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Install from source

```bash
# Clone the repository
git clone https://github.com/arm2arm/mcpdocs.git
cd mcpdocs

# Install the package
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

## Usage

### Running the MCP Server

```bash
# Run the MCP server
python -m mcpdocs_agent
```

The server will start and listen for MCP protocol messages on stdin/stdout.

### MCP Configuration

Add the following to your MCP client configuration (e.g., Claude Desktop, Cline):

```json
{
  "mcpServers": {
    "mcpdocs-agent": {
      "command": "python",
      "args": ["-m", "mcpdocs_agent"],
      "description": "MCP server for REANA scientific workflow automation and data analysis"
    }
  }
}
```

## Available Tools

### 1. generate_sine_data

Generate sine, cosine, or tangent wave data points and save to a file.

**Parameters:**
- `num_points` (int): Number of data points to generate (default: 100)
- `start` (float): Start value in radians (default: 0.0)
- `end` (float): End value in radians (default: 2π)
- `function` (str): Function to generate: "sin", "cos", or "tan" (default: "sin")

**Example:**
```
Generate 200 sine wave points from 0 to 4π
```

### 2. plot_data

Create a visualization plot from a data file and return as PNG.

**Parameters:**
- `data_file` (str): Path to data file to plot (required)
- `output_file` (str): Output plot filename (default: "plot.png")
- `title` (str): Plot title (default: "Data Plot")
- `xlabel` (str): X-axis label (default: "x")
- `ylabel` (str): Y-axis label (default: "y")

**Example:**
```
Plot the data from sin_data.txt with title "Sine Wave"
```

### 3. compute_statistics

Compute statistical summary (mean, std, min, max, etc.) from a data file.

**Parameters:**
- `data_file` (str): Path to data file (required)

**Example:**
```
Compute statistics for sin_data.txt
```

### 4. analyze_s3_data

Read and analyze parquet data from S3 storage using Dask for distributed processing.

**Parameters:**
- `bucket` (str): S3 bucket name (required)
- `prefix` (str): S3 key prefix/path (required)
- `endpoint_url` (str): S3 endpoint URL (default: "https://s3.data.aip.de:9000")
- `sample_fraction` (float): Fraction of data to sample, 0.0-1.0 (default: 0.01)

**Example:**
```
Analyze data from S3 bucket shboost2024 with prefix shboost_08july2024_pub.parq
```

## Example Workflows

### Basic Sine Wave Analysis

1. Generate sine wave data:
   ```
   Generate 100 sine wave points from 0 to 2π
   ```

2. Compute statistics:
   ```
   Compute statistics for sin_data.txt
   ```

3. Create visualization:
   ```
   Plot sin_data.txt with title "Sine Wave Analysis"
   ```

### S3 Cloud Data Analysis

1. Analyze astronomy data from S3:
   ```
   Analyze parquet data from S3 bucket shboost2024 prefix shboost_08july2024_pub.parq with 1% sample
   ```

2. The tool will:
   - Connect to the S3 endpoint
   - Sample 1% of the data for analysis
   - Compute statistics on all numeric columns
   - Report memory usage and data characteristics

## Integration with REANA

The MCP agent complements the existing REANA workflows by providing:

1. **Interactive Data Exploration**: Quickly analyze data before running full workflows
2. **Rapid Prototyping**: Test data generation and visualization parameters
3. **Statistical Validation**: Verify output quality without downloading files
4. **Cloud Data Preview**: Sample and inspect S3 data before processing

### Example Integration

```yaml
# Traditional REANA workflow
workflow:
  type: serial
  specification:
    steps:
      - name: generate
        commands:
          - python generate_data.py
      - name: analyze
        commands:
          - python plot_sin.py
```

With the MCP agent, you can:
1. Prototype the workflow interactively
2. Validate parameters and outputs
3. Then deploy to REANA for reproducible execution

## Library Versions

The MCP agent uses recent, stable versions of scientific Python libraries:

- **mcp**: ≥1.1.0 - Model Context Protocol SDK
- **pydantic**: ≥2.10.0 - Data validation
- **numpy**: ≥2.0.0 - Numerical computing
- **pandas**: ≥2.2.0 - Data manipulation
- **matplotlib**: ≥3.9.0 - Visualization
- **dask**: ≥2024.12.0 - Distributed computing
- **s3fs**: ≥2024.12.0 - S3 filesystem interface
- **pyarrow**: ≥18.1.0 - Parquet file support

## Development

### Running Tests

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

### Code Quality

```bash
# Format code
black mcpdocs_agent/

# Lint code
ruff check mcpdocs_agent/
```

## Architecture

The MCP agent follows a modular architecture:

```
mcpdocs_agent/
├── __init__.py       # Package initialization
├── __main__.py       # CLI entry point
└── server.py         # MCP server implementation
```

### Tool Design

Each tool follows these principles:
1. **Type Safety**: Uses Pydantic models for parameter validation
2. **Error Handling**: Comprehensive error messages and graceful failures
3. **Logging**: Structured logging for debugging
4. **Async Support**: Fully asynchronous for concurrent operations

## Troubleshooting

### Common Issues

**Issue**: ModuleNotFoundError when running the server

**Solution**: Ensure the package is installed:
```bash
pip install -e .
```

**Issue**: S3 connection errors

**Solution**: Check:
- Endpoint URL is correct
- Network connectivity to S3 endpoint
- Bucket and prefix exist
- Use `anon=True` for public buckets

**Issue**: Memory errors with large datasets

**Solution**: Reduce `sample_fraction` parameter when analyzing S3 data

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure code passes formatting and linting
5. Submit a pull request

## License

See the main repository LICENSE file for licensing information.

## Support

- **Issues**: [GitHub Issues](https://github.com/arm2arm/mcpdocs/issues)
- **Documentation**: [Project README](../README.md)
- **Examples**: See the `sin_plot/`, `dask_s3_read/`, and `dask_s3_plot/` directories

## Related Resources

- [MCP Specification](https://modelcontextprotocol.io/)
- [REANA Documentation](https://docs.reana.io/)
- [Dask Documentation](https://docs.dask.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
