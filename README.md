# REANA Workflow Examples

A collection of REANA serial workflow examples demonstrating various patterns for reproducible scientific computing.

## Project Structure

```
mcpdocs/
├── sin_plot/           # Simple sine wave generation and plotting
├── dask_s3_read/       # Read parquet from S3 and compute statistics
├── dask_s3_plot/       # Read from S3 and create hexbin scatter plots
├── memory-bank/        # AI context/memory documentation
└── .gitignore
```

## Examples

### 1. sin_plot
Simple REANA serial workflow that generates sine wave data and creates a plot.

**Run:**
```cmd
cd sin_plot
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -it -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 run -n test -f reana.yaml
```

**Output:** `sin_plot.png`, `sin_data.txt`

### 2. dask_s3_read
Read parquet data from S3 using Dask and compute statistics.

**Run:**
```cmd
cd dask_s3_read
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -it -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 run -n dask-s3-read -f reana.yaml
```

**Output:** `stats.txt`

### 3. dask_s3_plot
Create hexbin scatter plots from S3 parquet data using Dask.

**Run:**
```cmd
cd dask_s3_plot
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -it -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 run -n dask-s3-plot -f reana.yaml
```

**Output:** `xg_yg_hexbin.png`, `bprp_mg_hexbin.png`

## Common Commands

### Validate workflow
```cmd
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -it -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 validate -f reana.yaml
```

### Check status
```cmd
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 status -w workflow_name
```

### Download outputs
```cmd
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 download -w workflow_name
```

## Container Image

All workflows use:
- **Runtime**: `gitlab-p4n.aip.de:5005/compute4punch/container-stacks/astro-ml:latest`
- **Client**: `reanahub/reana-client:0.9.4`

The astro-ml container includes: NumPy, Pandas, Matplotlib, SciPy, Scikit-learn, Dask, and 50+ scientific Python packages.

## Documentation

- Each example has its own README.md with specific instructions
- Memory Bank in `memory-bank/` contains project context and patterns for AI agents
