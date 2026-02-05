# Tech Context

## Technologies Used

### MCP Agent (NEW!)
- **MCP Protocol**: v1.26.0 - Model Context Protocol for AI integration
- **Python**: 3.10+ (tested on 3.10, 3.11, 3.12)
- **Core Libraries** (latest stable versions):
  - **mcp**: ≥1.1.0 (installed: 1.26.0) - MCP SDK
  - **pydantic**: ≥2.10.0 (installed: 2.12.5) - Data validation
  - **numpy**: ≥2.0.0 (installed: 2.4.2) - Numerical computing
  - **pandas**: ≥2.2.0 (installed: 3.0.0) - Data manipulation
  - **matplotlib**: ≥3.9.0 (installed: 3.10.8) - Visualization
  - **dask**: ≥2024.12.0 (installed: 2026.1.2) - Distributed computing
  - **s3fs**: ≥2024.12.0 (installed: 2026.1.0) - S3 filesystem
  - **pyarrow**: ≥18.1.0 (installed: 23.0.0) - Parquet support

- **Tools Provided**:
  1. `generate_sine_data`: Generate mathematical functions (sin/cos/tan)
  2. `plot_data`: Create publication-quality plots
  3. `compute_statistics`: Statistical analysis
  4. `analyze_s3_data`: S3 parquet data processing

### Workflow Engine
- **REANA**: Reproducible Analysis platform
  - Serial workflow type
  - Version: 0.6.0 (specified in reana.yaml)
  - Server: https://reana-p4n.aip.de

### Container Images
1. **reanahub/reana-client:0.9.4**
   - Used for running reana-client commands locally
   - Execute-only image (no interactive shell)
   - Commands: validate, run, status, logs, download

2. **gitlab-p4n.aip.de:5005/compute4punch/container-stacks/astro-ml:latest**
   - Runtime container for workflow steps
   - Pre-installed libraries:
     - astropy==7.1.0, astroquery==0.4.10
     - bokeh==3.3.0, dask, datashader
     - holoviews==1.20.2, hvplot==0.11.3
     - matplotlib==3.8.0, numpy, pandas
     - scikit-learn==1.7.0, scipy==1.11.3
     - tensorflow==2.15.0, xgboost==3.0.2
     - And 50+ more scientific packages

### Programming Languages
- **Python 3.10+**
  - generate_data.py: NumPy for data generation
  - plot_sin.py: Pandas + Matplotlib for plotting
  - mcpdocs_agent: Async MCP server with latest libraries

### Data Formats
- **Input**: None (generated programmatically)
- **Intermediate**: CSV-like text with headers (sin_data.txt)
- **Output**: PNG images (plots), text files (statistics)
- **Cloud Data**: Parquet files from S3

## Development Setup

### MCP Agent Setup
```bash
# Install the MCP agent
pip install -e .

# Run the MCP server
python -m mcpdocs_agent

# Run tests
python test_agent.py

# Run examples
python example_usage.py
```

### MCP Client Configuration
Add to your AI assistant config (e.g., Claude Desktop, Cline):
```json
{
  "mcpServers": {
    "mcpdocs-agent": {
      "command": "python",
      "args": ["-m", "mcpdocs_agent"]
    }
  }
}
```

### Local Development (Windows)
```cmd
# Validate workflow
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -it -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 validate -f reana.yaml

# Run workflow
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -it -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 run -n test -f reana.yaml

# Check status
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 status -w test

# Download outputs
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 download -w test
```

## Technical Constraints

### MCP Agent
1. **Async Operations**: All tool calls are async
2. **Type Safety**: Pydantic models enforce parameter validation
3. **File I/O**: Tools operate on local filesystem
4. **S3 Access**: Requires network connectivity to S3 endpoints
5. **Memory**: S3 sampling controls memory usage

### REANA Workflows
1. **File Paths**: Must use relative paths (no absolute paths)
2. **Working Directory**: Always `/workdir` in containers
3. **Container Access**: Registry must be accessible from REANA cluster
4. **Token Required**: REANA_ACCESS_TOKEN must be valid
5. **Outputs Listed**: Files must be in `outputs.files` to download

## Dependencies

### For MCP Agent
- Python 3.10 or higher
- pip package manager
- Recent versions of scientific libraries

### For REANA Workflows
- Docker (for running reana-client)
- Valid REANA credentials

## Tool Usage Patterns

### MCP Agent
- **generate_sine_data**: Create test data for analysis
- **plot_data**: Visualize any 2-column data file
- **compute_statistics**: Get comprehensive stats on datasets
- **analyze_s3_data**: Sample and analyze cloud parquet data

### REANA Client
- **reana-client validate**: Always run before `run` to catch errors
- **reana-client status**: Check workflow state (pending, running, finished, failed)
- **reana-client logs**: Debug failed workflows
- **reana-client download**: Get output files after completion

## CI/CD

### GitHub Actions
- Automated testing on Python 3.10, 3.11, 3.12
- Validates installation and example execution
- Workflow: `.github/workflows/test-agent.yml`
