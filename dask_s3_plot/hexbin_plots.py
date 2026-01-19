#!/usr/bin/env python3
"""
Create hexbin scatter plots from S3 parquet data using Dask.
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import dask.dataframe as dd

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
print("Sampling and persisting data (1% sample)...")
df_sample = df.sample(frac=0.01).persist()
df_compute = df_sample.compute()

print(f"Sample size: {len(df_compute)} rows")

# Create selection mask for galactic coordinates
sel = (np.abs(df_compute.xg + 8.2) < 10) & (np.abs(df_compute.yg) < 10)
df_sel = df_compute[sel]
print(f"Selected rows in galactic region: {len(df_sel)}")

# Figure 1: xg vs yg hexbin
print("Creating xg vs yg hexbin plot...")
fig1, ax1 = plt.subplots()
df_sel.plot(
    x='xg', y='yg',
    kind='hexbin',
    xlim=(-18, 2),
    ylim=(-10, 10),
    norm=mpl.colors.LogNorm(),
    cmap="plasma",
    ax=ax1
)
ax1.set_xlabel('xg (Galactic Longitude)', fontsize=12)
ax1.set_ylabel('yg (Galactic Latitude)', fontsize=12)
ax1.set_title('Galactic Coordinates (Hexbin)', fontsize=14)
plt.tight_layout()
plt.savefig('xg_yg_hexbin.png', dpi=150, bbox_inches='tight')
print("Saved: xg_yg_hexbin.png")

# Figure 2: bprp0 vs mg0 color-magnitude diagram
print("Creating color-magnitude hexbin plot...")
fig2, ax2 = plt.subplots()
df_sel.plot(
    x='bprp0', y='mg0',
    kind='hexbin',
    ylim=(15, -6),
    norm=mpl.colors.LogNorm(),
    cmap="jet",
    ax=ax2
)
ax2.set_xlabel('BP-RP Color', fontsize=12)
ax2.set_ylabel('Magnitude (G)', fontsize=12)
ax2.set_title('Color-Magnitude Diagram (Hexbin)', fontsize=14)
plt.tight_layout()
plt.savefig('bprp_mg_hexbin.png', dpi=150, bbox_inches='tight')
print("Saved: bprp_mg_hexbin.png")

print("\nDone! Created 2 hexbin plots.")
