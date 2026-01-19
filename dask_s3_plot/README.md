# Dask S3 Plot Example

Create hexbin scatter plots from S3 parquet data using Dask.

## Overview
This example demonstrates reading large parquet files from S3 using Dask DataFrames, sampling the data, and creating hexbin scatter plots.

## Files
- `reana.yaml` - REANA workflow definition
- `hexbin_plots.py` - Python script for creating plots

## Data Source
- **S3 Bucket**: `s3://shboost2024/shboost_08july2024_pub.parq/`
- **Endpoint**: `https://s3.data.aip.de:9000`
- **Format**: Parquet

## How to Run

Replace `XXXX` with your actual REANA access token:

```cmd
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -it -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 run -n dask-s3-plot -f reana.yaml
```

## Output
- `xg_yg_hexbin.png` - Galactic coordinates hexbin plot
- `bprp_mg_hexbin.png` - Color-magnitude diagram hexbin plot
