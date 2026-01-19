# REANA Serial Workflow - Sine Wave Plot

## Overview
A simple REANA serial workflow that generates sine wave data and creates a plot.

## Files
- `reana.yaml` - Workflow definition
- `generate_data.py` - Generates sine wave data points
- `plot_sin.py` - Creates a plot from the data using pandas

## Workflow Structure
1. **generate-data**: Generates 100 sine wave data points (0 to 2π)
2. **plot-sin**: Creates a PNG plot with proper labels and formatting

## How to Run

Replace `XXXX` with your actual REANA access token:

```cmd
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -it -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 run -n test -f reana.yaml
```

### Parameters:
- `-e REANA_SERVER_URL` - REANA server URL
- `-e REANA_ACCESS_TOKEN` - Your access token
- `-v "%cd%:/workdir"` - Mounts current directory (Windows CMD)
- `-w /workdir` - Working directory in container
- `-n test` - Workflow name
- `-f reana.yaml` - Workflow file

## Additional Commands

### Validate the workflow:
```cmd
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -it -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 validate -f reana.yaml
```

### Check workflow status:
```cmd
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 status -w test
```

### View workflow logs:
```cmd
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 logs -w test
```

### Download outputs:
```cmd
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 download -w test
```

### Interactive shell:
```cmd
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -it -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 /bin/bash
```

## Output Files
- `sin_plot.png` - Sine wave plot image
- `sin_data.txt` - Sine wave data points (x, y)

## Container Image
The workflow uses `gitlab-p4n.aip.de:5005/compute4punch/container-stacks/astro-ml:latest` which includes:
- Python 3.x
- NumPy, SciPy, Matplotlib
- Pandas, Scikit-learn
- TensorFlow, XGBoost
- And many more scientific Python libraries
