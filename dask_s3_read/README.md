# Dask S3 Read Example

Read parquet data from S3 and compute statistics using Dask.

## Overview
This example demonstrates reading large parquet files from S3 using Dask DataFrames, sampling the data, and computing descriptive statistics.

## Files
- `reana.yaml` - REANA workflow definition
- `read_stats.py` - Python script for reading and stats

## Data Source
- **S3 Bucket**: `s3://shboost2024/shboost_08july2024_pub.parq/`
- **Endpoint**: `https://s3.data.aip.de:9000`
- **Format**: Parquet

## How to Run

Replace `XXXX` with your actual REANA access token:

```cmd
docker run -e REANA_SERVER_URL=https://reana-p4n.aip.de -e REANA_ACCESS_TOKEN=XXXX --rm -it -v "%cd%:/workdir" -w /workdir reanahub/reana-client:0.9.4 run -n dask-s3-read -f reana.yaml
```

## Output
- `stats.txt` - Statistical summary of the sampled data
