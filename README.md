# mcpdocs

> **REANA workflow examples for reproducible scientific computing with Python, Dask, and cloud data processing**

[![REANA](https://img.shields.io/badge/REANA-0.9.4-blue.svg)](https://reanahub.io/)
[![Docker](https://img.shields.io/badge/Docker-required-blue.svg)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-See%20Repo-lightgrey.svg)](https://github.com/arm2arm/mcpdocs)
[![Documentation](https://img.shields.io/badge/docs-examples-green.svg)](#examples)

A curated collection of REANA serial workflow examples demonstrating best practices for reproducible scientific computing. Features containerized workflows for data generation, visualization, and distributed computing with real-world astronomy datasets.

---

## Table of Contents

- [Quick Start](#quick-start)
- [Features](#features)
- [Installation & Prerequisites](#installation--prerequisites)
- [Usage Examples](#usage-examples)
- [Repository Structure](#repository-structure)
- [Development](#development)
- [Workflow Examples](#workflow-examples)
- [Common Commands](#common-commands)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Security](#security)
- [License](#license)
- [Maintainers](#maintainers)
- [Links & Resources](#links--resources)

---

## Quick Start

Get started with a simple sine wave plotting workflow in under 2 minutes:

```bash
# 1. Clone the repository
git clone https://github.com/arm2arm/mcpdocs.git
cd mcpdocs/sin_plot

# 2. Set your REANA credentials
export REANA_SERVER_URL=https://reana-p4n.aip.de
export REANA_ACCESS_TOKEN=YOUR_TOKEN_HERE

# 3. Run the workflow using Docker
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -it -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 run -n quickstart -f reana.yaml

# 4. View the generated plot
# Output: sin_plot.png, sin_data.txt
```

**Expected output:** A PNG image showing a sine wave from 0 to 2π with grid and π-based tick marks.

---

## Features

- **Reproducible Workflows**: Containerized scientific computing with REANA
- **Data Visualization**: Generate plots from computed data using Matplotlib
- **Cloud Data Processing**: Read and analyze S3-hosted Parquet datasets
- **Distributed Computing**: Leverage Dask for parallel data processing
- **Docker Integration**: All workflows run in isolated containers
- **Scientific Stack**: Pre-configured with 50+ Python scientific libraries
- **Well-Documented**: Each example includes detailed README and inline comments

---

## Installation & Prerequisites

### Required Software

Before running workflows, ensure you have the following installed:

1. **Docker** (v20.10+)
   ```bash
   # Verify Docker installation
   docker --version
   # Docker version 20.10.0 or higher required
   ```

2. **Git**
   ```bash
   git --version
   # Any modern version will work
   ```

3. **REANA Access Token**
   - Obtain from [https://reana-p4n.aip.de](https://reana-p4n.aip.de)
   - Save securely for authentication

### Setup Steps

```bash
# Clone the repository
git clone https://github.com/arm2arm/mcpdocs.git
cd mcpdocs

# Configure REANA credentials (Linux/macOS)
export REANA_SERVER_URL=https://reana-p4n.aip.de
export REANA_ACCESS_TOKEN=XXXX

# Configure REANA credentials (Windows PowerShell)
$env:REANA_SERVER_URL="https://reana-p4n.aip.de"
$env:REANA_ACCESS_TOKEN="XXXX"

# Verify Docker can pull REANA client
docker pull reanahub/reana-client:0.9.4
```

### Container Images Used

- **REANA Client**: `reanahub/reana-client:0.9.4`
- **Runtime Environment**: `gitlab-p4n.aip.de:5005/compute4punch/container-stacks/astro-ml:latest`
  - Includes: NumPy, Pandas, Matplotlib, SciPy, Scikit-learn, TensorFlow, XGBoost, Dask, Astropy, and 50+ scientific packages

---

## Usage Examples

### Example 1: Simple Data Generation & Plotting

Generate sine wave data and create a visualization:

```bash
cd sin_plot
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -it -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 run -n sin-example -f reana.yaml
```

**What it does:**
1. Generates 100 sine wave data points (0 to 2π)
2. Creates a formatted plot with grid and π-based x-axis
3. Outputs `sin_plot.png` and `sin_data.txt`

### Example 2: S3 Data Analysis

Read Parquet data from S3 and compute statistics:

```bash
cd dask_s3_read
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -it -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 run -n s3-stats -f reana.yaml
```

**What it does:**
1. Connects to S3 bucket: `s3://shboost2024/shboost_08july2024_pub.parq/`
2. Reads Parquet data using Dask for distributed processing
3. Computes and saves statistical summaries to `stats.txt`

### Example 3: Hexbin Visualization from Cloud Data

Create hexbin scatter plots from S3 astronomy data:

```bash
cd dask_s3_plot
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -it -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 run -n hexbin-plots -f reana.yaml
```

**What it does:**
1. Reads astronomy data from S3 using Dask
2. Creates two hexbin plots: `xg_yg_hexbin.png` and `bprp_mg_hexbin.png`
3. Visualizes spatial and color-magnitude distributions

---

## Repository Structure

```
mcpdocs/
├── sin_plot/              # Simple 2-step workflow (generate → plot)
│   ├── README.md          # Example-specific documentation
│   ├── reana.yaml         # REANA workflow definition
│   ├── generate_data.py   # Step 1: Generate 100 sine data points
│   ├── plot_sin.py        # Step 2: Create PNG plot
│   └── sin_plot.png       # Output (tracked in git)
│
├── dask_s3_read/          # Read S3 parquet & compute statistics
│   ├── README.md          # Example-specific documentation
│   ├── reana.yaml         # REANA workflow definition
│   └── read_stats.py      # Dask-based S3 data processing
│
├── dask_s3_plot/          # Create hexbin plots from S3 data
│   ├── README.md          # Example-specific documentation
│   ├── reana.yaml         # REANA workflow definition
│   └── hexbin_plots.py    # Visualization script
│
├── memory-bank/           # AI context & development patterns
│   ├── projectbrief.md    # Project overview and requirements
│   ├── techContext.md     # Technical stack details
│   ├── activeContext.md   # Current development state
│   └── systemPatterns.md  # Architecture patterns
│
├── README.md              # This file - main documentation
└── .gitignore             # Git exclusions
```

---

## Development

### Validating Workflows Locally

Before running workflows, validate the YAML syntax:

```bash
cd <workflow-directory>
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -it -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 validate -f reana.yaml
```

**Expected output:**
```
File reana.yaml is a valid REANA specification file.
```

### Testing Workflows

Run a workflow and monitor its execution:

```bash
# 1. Start the workflow
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -it -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 run -n test-run -f reana.yaml

# 2. Check status
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 status -w test-run

# 3. View logs
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 logs -w test-run
```

### Building Documentation Locally

Each example has its own README.md. To view documentation:

```bash
# View main README
cat README.md

# View example-specific README
cat sin_plot/README.md
```

### Creating a New Workflow Example

1. Create a new directory for your workflow
2. Add a `reana.yaml` file defining your workflow steps
3. Include Python scripts referenced in `reana.yaml`
4. Create a `README.md` with specific instructions
5. Test thoroughly before committing

**Minimal `reana.yaml` structure:**
```yaml
version: 0.6.0
inputs:
  files:
    - script.py
workflow:
  type: serial
  specification:
    steps:
      - name: step-name
        environment: 'gitlab-p4n.aip.de:5005/compute4punch/container-stacks/astro-ml:latest'
        commands:
          - python script.py
outputs:
  files:
    - output.txt
```

---

## Workflow Examples

### 1. sin_plot

**Purpose:** Educational example demonstrating basic REANA workflow structure

**Steps:**
1. `generate-data`: Creates 100 sine wave points from 0 to 2π
2. `plot-sin`: Generates formatted PNG plot with matplotlib

**Files:**
- Input: None (generates data)
- Output: `sin_plot.png`, `sin_data.txt`

**Full documentation:** [sin_plot/README.md](sin_plot/README.md)

---

### 2. dask_s3_read

**Purpose:** Demonstrate cloud data access and distributed computing with Dask

**Steps:**
1. Connect to S3 bucket with astronomy data
2. Read Parquet files using Dask
3. Compute statistical summaries
4. Save results to `stats.txt`

**Files:**
- Input: S3 data (`s3://shboost2024/shboost_08july2024_pub.parq/`)
- Output: `stats.txt`

**Full documentation:** [dask_s3_read/README.md](dask_s3_read/README.md)

---

### 3. dask_s3_plot

**Purpose:** Visualize large-scale astronomy datasets from cloud storage

**Steps:**
1. Read Parquet data from S3 using Dask
2. Create hexbin scatter plots for spatial (xg/yg) and color-magnitude (bprp/mg) distributions
3. Save high-resolution PNG images

**Files:**
- Input: S3 data (`s3://shboost2024/shboost_08july2024_pub.parq/`)
- Output: `xg_yg_hexbin.png`, `bprp_mg_hexbin.png`

**Full documentation:** [dask_s3_plot/README.md](dask_s3_plot/README.md)

---

## Common Commands

### Workflow Management

```bash
# Validate workflow definition
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -it -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 validate -f reana.yaml

# Run a workflow
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -it -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 run -n workflow-name -f reana.yaml

# Check workflow status
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 status -w workflow-name

# View workflow logs
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 logs -w workflow-name

# Download workflow outputs
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 download -w workflow-name

# List all your workflows
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 list

# Delete a workflow
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 delete -w workflow-name
```

### Docker Volume Mounting

**Linux/macOS:**
```bash
-v "$(pwd):/workdir"
```

**Windows Command Prompt:**
```cmd
-v "%cd%:/workdir"
```

**Windows PowerShell:**
```powershell
-v "${PWD}:/workdir"
```

---

## Troubleshooting

### Common Issues

#### 1. Authentication Errors

**Problem:** `Error: unauthorized. Please set REANA_ACCESS_TOKEN`

**Solution:**
```bash
# Verify your token is set
echo $REANA_ACCESS_TOKEN  # Linux/macOS
echo %REANA_ACCESS_TOKEN%  # Windows CMD
echo $env:REANA_ACCESS_TOKEN  # Windows PowerShell

# If empty, set it again
export REANA_ACCESS_TOKEN=YOUR_TOKEN  # Linux/macOS
```

#### 2. Docker Volume Mount Issues

**Problem:** `Error: cannot find reana.yaml`

**Solution:** Ensure you're in the workflow directory and using the correct path syntax:
```bash
# Verify you're in the right directory
ls reana.yaml

# Use absolute paths if needed
docker run ... -v "/full/path/to/workflow:/workdir" ...
```

#### 3. Workflow Validation Fails

**Problem:** `reana.yaml is not valid`

**Solution:**
- Check YAML indentation (use spaces, not tabs)
- Verify all referenced files exist
- Ensure `version: 0.6.0` is specified
- Validate YAML syntax online: [yamllint.com](http://www.yamllint.com/)

#### 4. Workflow Stuck in "running" State

**Problem:** Workflow doesn't complete after several minutes

**Solution:**
```bash
# Check logs for errors
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 logs -w workflow-name

# If stuck, you may need to delete and restart
docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
  --rm -v "$(pwd):/workdir" -w /workdir \
  reanahub/reana-client:0.9.4 delete -w workflow-name
```

#### 5. Docker Permission Denied

**Problem:** `permission denied while trying to connect to the Docker daemon`

**Solution:**
```bash
# Linux: Add user to docker group
sudo usermod -aG docker $USER
# Log out and log back in

# Or run with sudo (not recommended for production)
sudo docker run ...
```

### FAQ

**Q: Can I run workflows without Docker?**  
A: No, Docker is required as REANA workflows run in containers. However, you can install REANA client via pip if you have local REANA server access.

**Q: How do I get a REANA access token?**  
A: Visit your REANA server instance (e.g., https://reana-p4n.aip.de), log in, and generate a token from your profile settings.

**Q: Can I use these workflows on public REANA instances?**  
A: Yes, but you'll need to update `REANA_SERVER_URL` to point to the public instance and ensure S3 bucket access for examples using cloud data.

**Q: How do I add custom Python dependencies?**  
A: The astro-ml container includes most scientific libraries. For custom needs, you can specify a different container image in `reana.yaml` or create your own Docker image.

**Q: Where are workflow outputs stored?**  
A: Outputs are stored on the REANA server. Use the `download` command to retrieve them locally.

---

## Contributing

We welcome contributions! Whether you want to add new workflow examples, improve documentation, or fix bugs, your help is appreciated.

### How to Contribute

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/mcpdocs.git
   cd mcpdocs
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Add new workflow examples in their own directories
   - Update documentation in README.md files
   - Follow existing code style and conventions

4. **Test your changes**
   ```bash
   # Validate new workflows
   cd your-workflow
   docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
     --rm -it -v "$(pwd):/workdir" -w /workdir \
     reanahub/reana-client:0.9.4 validate -f reana.yaml
   
   # Test the workflow runs successfully
   docker run -e REANA_SERVER_URL -e REANA_ACCESS_TOKEN \
     --rm -it -v "$(pwd):/workdir" -w /workdir \
     reanahub/reana-client:0.9.4 run -n test -f reana.yaml
   ```

5. **Commit and push**
   ```bash
   git add .
   git commit -m "Add: description of your changes"
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your feature branch
   - Describe your changes clearly

### Contribution Guidelines

- **New Workflows**: Must include `reana.yaml`, Python scripts, and a detailed README.md
- **Documentation**: Use clear, concise language with code examples
- **Code Style**: Follow PEP 8 for Python code
- **Testing**: All workflows must be tested before submission
- **Commit Messages**: Use conventional commit format (e.g., "Add:", "Fix:", "Update:")

### Code of Conduct

Please be respectful and constructive in all interactions. We're here to learn and build together.

---

## Security

### Reporting Vulnerabilities

If you discover a security vulnerability, please do NOT open a public issue. Instead:

1. Email the maintainers directly (see [Maintainers](#-maintainers) section)
2. Include a detailed description of the vulnerability
3. Provide steps to reproduce if possible
4. Allow time for a fix before public disclosure

### Best Practices

- **Never commit tokens**: Do not include `REANA_ACCESS_TOKEN` in code or configs
- **Use environment variables**: Store credentials in environment variables, not files
- **Review container images**: Be cautious when using custom Docker images
- **Validate inputs**: Sanitize any user inputs in workflow scripts
- **Keep dependencies updated**: Regularly update container images and libraries

---

## License

This project does not currently have a specified license file. Please contact the repository maintainers for licensing information before using or redistributing this code.

**Note to maintainers:** Consider adding a LICENSE file (e.g., MIT, Apache 2.0, GPL) to clarify usage terms.

---

## Maintainers

This project is maintained by:

**arm2arm**  
- GitHub: [@arm2arm](https://github.com/arm2arm)
- Repository: [arm2arm/mcpdocs](https://github.com/arm2arm/mcpdocs)

### Contact

For questions, suggestions, or collaboration:
- **Report Issues**: [GitHub Issues](https://github.com/arm2arm/mcpdocs/issues) - Report bugs or request features
- **Pull Requests**: [Submit PRs](https://github.com/arm2arm/mcpdocs/pulls) - Contribute code or documentation improvements

---

## Links & Resources

### Project Resources

- **Issues**: [Report bugs or request features](https://github.com/arm2arm/mcpdocs/issues)
- **Changelog**: [View release history](https://github.com/arm2arm/mcpdocs/releases)
- **Documentation**: Individual README files in each workflow directory
- **Memory Bank**: [AI context and patterns](memory-bank/)

### External Documentation

- **REANA Documentation**: [https://docs.reana.io/](https://docs.reana.io/)
- **REANA Client CLI**: [https://reana-client.readthedocs.io/](https://reana-client.readthedocs.io/)
- **Docker Documentation**: [https://docs.docker.com/](https://docs.docker.com/)
- **Dask Documentation**: [https://docs.dask.org/](https://docs.dask.org/)
- **Astropy**: [https://www.astropy.org/](https://www.astropy.org/)

### Related Projects

- **REANA**: [https://github.com/reanahub/reana](https://github.com/reanahub/reana)
- **REANA Client**: [https://github.com/reanahub/reana-client](https://github.com/reanahub/reana-client)

---

<div align="center">

**If you find this project useful, please consider giving it a star!**

Maintained by the mcpdocs team. This experimental project is part of the PhysicsLLM agentic work package.

</div>
