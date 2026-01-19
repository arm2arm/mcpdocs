# Tech Context

## Technologies Used

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
- **Python 3.x**
  - generate_data.py: NumPy for data generation
  - plot_sin.py: Pandas + Matplotlib for plotting

### Data Formats
- **Input**: None (generated programmatically)
- **Intermediate**: CSV-like text with headers (sin_data.txt)
- **Output**: PNG image (sin_plot.png)

## Development Setup

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

1. **File Paths**: Must use relative paths (no absolute paths)
2. **Working Directory**: Always `/workdir` in containers
3. **Container Access**: Registry must be accessible from REANA cluster
4. **Token Required**: REANA_ACCESS_TOKEN must be valid
5. **Outputs Listed**: Files must be in `outputs.files` to download

## Dependencies
- Docker (for running reana-client)
- Valid REANA credentials

## Tool Usage Patterns

- **reana-client validate**: Always run before `run` to catch errors
- **reana-client status**: Check workflow state (pending, running, finished, failed)
- **reana-client logs**: Debug failed workflows
- **reana-client download**: Get output files after completion
