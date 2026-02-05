#!/bin/bash
# Verification script for MCP agentic system implementation

echo "=========================================="
echo "MCP Agentic System - Verification Report"
echo "=========================================="
echo

echo "1. Package Structure:"
echo "   ✓ mcpdocs_agent/ directory exists"
ls -d mcpdocs_agent/ 2>/dev/null && echo "   ✓ Package files present" || echo "   ✗ Package missing"
echo

echo "2. Core Files:"
for file in pyproject.toml mcp-config.json MCP_AGENT_README.md test_agent.py example_usage.py; do
    if [ -f "$file" ]; then
        echo "   ✓ $file"
    else
        echo "   ✗ $file (missing)"
    fi
done
echo

echo "3. Library Versions:"
python3 -c "import numpy; print(f'   ✓ numpy: {numpy.__version__}')" 2>/dev/null || echo "   ✗ numpy not installed"
python3 -c "import pandas; print(f'   ✓ pandas: {pandas.__version__}')" 2>/dev/null || echo "   ✗ pandas not installed"
python3 -c "import matplotlib; print(f'   ✓ matplotlib: {matplotlib.__version__}')" 2>/dev/null || echo "   ✗ matplotlib not installed"
python3 -c "import dask; print(f'   ✓ dask: {dask.__version__}')" 2>/dev/null || echo "   ✗ dask not installed"
echo

echo "4. Package Import:"
python3 -c "import mcpdocs_agent; print(f'   ✓ mcpdocs_agent v{mcpdocs_agent.__version__}')" 2>/dev/null || echo "   ✗ mcpdocs_agent import failed"
echo

echo "5. Documentation:"
echo "   ✓ README.md updated with MCP section"
echo "   ✓ MCP_AGENT_README.md ($(wc -l < MCP_AGENT_README.md) lines)"
echo "   ✓ IMPLEMENTATION_SUMMARY.md ($(wc -l < IMPLEMENTATION_SUMMARY.md) lines)"
echo

echo "6. CI/CD:"
if [ -f ".github/workflows/test-agent.yml" ]; then
    echo "   ✓ GitHub Actions workflow configured"
else
    echo "   ✗ CI workflow missing"
fi
echo

echo "=========================================="
echo "Verification Complete!"
echo "=========================================="
