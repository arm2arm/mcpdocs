#!/usr/bin/env python3
"""
Read parquet data from S3 using Dask and compute statistics.
"""

import dask.dataframe as dd
import numpy as np

# Read parquet data from S3
print("Reading parquet data from S3...")
df = dd.read_parquet(
    "s3://shboost2024/shboost_08july2024_pub.parq/*.parquet",
    storage_options={
        'use_ssl': True,
        'anon': True,
        'client_kwargs': dict(endpoint_url='https://s3.data.aip.de:9000')
    }
)

# Persist data for faster computation
print("Sampling and persisting data...")
df_sample = df.sample(frac=0.01).persist()
df_compute = df_sample.compute()

print(f"Sample size: {len(df_compute)} rows")
print(f"Columns: {list(df_compute.columns)}")

# Compute statistics for numeric columns
print("\nComputing statistics...")
stats = df_compute.describe()

# Save statistics to file
with open('stats.txt', 'w') as f:
    f.write("Statistical Summary of S3 Parquet Data\n")
    f.write("=" * 50 + "\n\n")
    f.write(f"Total rows in sample: {len(df_compute)}\n")
    f.write(f"Total columns: {len(df_compute.columns)}\n\n")
    f.write("Descriptive Statistics:\n")
    f.write("-" * 50 + "\n")
    f.write(stats.to_string())

# Also print to stdout
print("\nStatistics saved to stats.txt:")
print(stats)

print("\nDone!")
