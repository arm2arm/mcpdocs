# Active Context

## Current Work Focus

The project now includes an **MCP (Model Context Protocol) agentic system** with recent library versions, in addition to the existing REANA workflow examples.

### Recent Changes
- ✅ Created MCP agent with latest library versions (mcp ≥1.1.0, numpy ≥2.0.0, pandas ≥2.2.0, dask ≥2024.12.0)
- ✅ Implemented four core tools: generate_sine_data, plot_data, compute_statistics, analyze_s3_data
- ✅ Added pyproject.toml with modern Python packaging (setuptools ≥68.0.0)
- ✅ Created comprehensive MCP agent documentation (MCP_AGENT_README.md)
- ✅ Updated main README with MCP agent integration
- ✅ Added mcp-config.json for easy AI assistant configuration
- ✅ Enhanced .gitignore for Python development artifacts

## Next Steps

Potential future enhancements:
- Add more MCP tools for workflow management
- Integrate with REANA API for remote workflow execution
- Add visualization tools for hexbin plots
- Create example notebooks demonstrating MCP agent usage

## Active Decisions

### Decision: Use MCP Protocol for Agentic System
**Chosen**: Model Context Protocol (MCP) v1.1.0+
**Rationale**: 
- Standard protocol for AI-agent integration
- Works with multiple AI assistants (Claude, Cline, etc.)
- Type-safe with Pydantic validation
- Async-first design for scalability

### Decision: Use Latest Stable Library Versions
**Chosen**: Recent versions of all scientific libraries
**Rationale**:
- numpy ≥2.0.0: Latest performance improvements and API updates
- pandas ≥2.2.0: Modern data manipulation features
- matplotlib ≥3.9.0: Updated visualization capabilities
- dask ≥2024.12.0: Latest distributed computing features
- mcp ≥1.1.0: Current stable MCP SDK

### Decision: Modular Tool Architecture
**Chosen**: Separate tools for each capability
**Rationale**:
- Clear separation of concerns
- Easy to test and maintain
- Users can invoke specific tools as needed
- Extensible for future additions

### Decision: Use pandas for Data Loading
**Chosen**: pandas.read_csv()
**Rationale**: 
- Automatically handles header rows
- Named column access is clearer than numpy array indexing
- More robust for scientific data with metadata
- Pre-installed in astro-ml container

### Decision: Auto-upload Python Scripts via inputs.files
**Chosen**: Include scripts in reana.yaml inputs.files section
**Rationale**:
- No separate upload command needed
- Scripts are version-controlled alongside reana.yaml
- Automatic synchronization when reana.yaml is committed

## Important Patterns & Preferences

1. **MCP Tools**: Use Pydantic models for type-safe parameter validation
2. **REANA Workflow Structure**: Always use `inputs.files` for Python scripts
3. **Data Loading**: Use pandas for files with headers
4. **File Paths**: Always use relative paths in workflow scripts
5. **Container Usage**: Use astro-ml for runtime, reana-client for commands
6. **Error Handling**: Return descriptive TextContent on errors
7. **Image Returns**: Include both text description and base64-encoded image

## Learnings & Insights

### What Worked Well
- MCP protocol provides clean abstraction for AI integration
- Type validation with Pydantic catches errors early
- Async design supports concurrent operations
- Simple serial workflow for basic data processing
- Container-first approach eliminates dependency issues
- Clear separation of data generation and visualization
- Comprehensive documentation in README.md

### Challenges Overcome
- Initial numpy.loadtxt failure due to header row → switched to pandas
- Windows volume mount syntax → used `%cd%` for CMD
- Interactive shell not available in reana-client → removed from docs

### Key Takeaways
1. MCP agents complement traditional workflows with interactive capabilities
2. Latest library versions provide better performance and features
3. Always validate workflows before running
4. Use pandas for data with headers (not numpy.loadtxt)
5. Test data loading in the actual container environment
6. Document both local development and remote execution
7. Async/await pattern enables efficient I/O operations

## Current Status
- [x] Workflow definition (reana.yaml) complete
- [x] Python scripts functional
- [x] Container configuration correct
- [x] Documentation complete
- [x] Git history maintained
- [x] Memory Bank initialized
- [x] MCP agent implemented with latest libraries
- [x] Four core tools operational
- [x] Comprehensive agent documentation
- [x] Integration examples provided
