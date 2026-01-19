# System Patterns

## Architecture Overview

This project follows a **serial workflow pattern** using REANA's serial workflow engine. The architecture is simple but demonstrates key concepts for reproducible scientific computing.

## Component Relationships

```
┌─────────────────────────────────────────────────────────────┐
│                    REANA Cluster                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Container: astro-ml:latest                          │   │
│  │  ┌─────────────┐    ┌─────────────┐                 │   │
│  │  │  generate   │───▶│    plot     │                 │   │
│  │  │  _data.py   │    │  _sin.py    │                 │   │
│  │  └─────────────┘    └─────────────┘                 │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
         ▲                         ▲
         │                         │
    Input Files              Output Files
    (auto-uploaded)          (sin_plot.png)
```

## Project Structure Pattern

```
mcpdocs/
├── sin_plot/           # Simple serial workflow
├── dask_s3_read/       # Dask + S3 data reading
├── dask_s3_plot/       # Dask + S3 visualization
├── memory-bank/        # Project context
└── .gitignore
```

## Key Design Patterns

### 1. Serial Workflow Pattern
- Steps execute sequentially (not in parallel)
- Each step is a separate containerized job
- Outputs from step N are available to step N+1
- Simple to understand and debug

### 2. Automatic File Upload Pattern
```yaml
inputs:
  files:
    - generate_data.py
    - plot_sin.py
```
- Files are uploaded automatically when workflow runs
- No separate upload command needed
- Files available in working directory

### 3. Container-First Pattern
- All dependencies pre-installed in `astro-ml:latest`
- No runtime pip install needed
- Ensures reproducibility

### 4. Pandas for Data Handling Pattern
```python
# Use pandas for data with headers
df = pd.read_csv('sin_data.txt', sep=' ')
x = df['x'].values
y = df['y'].values
```
- Pandas properly handles header rows
- Easy column access by name
- More robust than numpy.loadtxt for this use case

## Implementation Paths

### Workflow Execution Flow
1. `reana-client run` → Uploads reana.yaml and input files
2. REANA scheduler → Creates workflow workspace
3. Step 1 (generate) → Runs in container, outputs sin_data.txt
4. Step 2 (plot) → Runs in container, reads sin_data.txt, outputs sin_plot.png
5. Files available for download

## Critical Implementation Details

1. **Working Directory**: All scripts run in workflow root
2. **File Paths**: Use relative paths only (e.g., `sin_data.txt`, not `/path/to/file`)
3. **Container Image**: Must exist and be accessible
4. **Outputs**: Must be listed in `outputs.files` to be downloadable

## Dask + S3 Patterns

### S3 Parquet Reading Pattern
```python
import dask.dataframe as dd

df = dd.read_parquet(
    "s3://bucket/path/*.parquet",
    storage_options={
        'use_ssl': True,
        'anon': True,
        'client_kwargs': dict(endpoint_url='https://s3.data.aip.de:9000')
    }
)
```

### Sampling and Persistence Pattern
```python
df_sample = df.sample(frac=0.01).persist()
df_compute = df_sample.compute()
```
- Use `persist()` to keep data in memory across computations
- Sample large datasets before visualization

### S3 Data Access Pattern
- **Endpoint**: `https://s3.data.aip.de:9000`
- **Bucket**: `shboost2024/shboost_08july2024_pub.parq`
- **Format**: Parquet
- **SSL**: Required
- **Anonymous**: True (public access)
