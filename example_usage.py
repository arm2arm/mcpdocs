#!/usr/bin/env python3
"""
Example usage of the mcpdocs MCP agent tools.

This demonstrates how to use the agent's capabilities programmatically.
"""

import json
import asyncio
from mcpdocs_agent.server import (
    call_tool,
    GenerateDataParams,
    PlotDataParams,
    StatisticsParams,
)


async def example_sine_wave_workflow():
    """Example: Generate sine wave, plot it, and compute statistics."""
    
    print("=" * 60)
    print("Example 1: Complete Sine Wave Analysis Workflow")
    print("=" * 60)
    
    # Step 1: Generate sine wave data
    print("\n1. Generating sine wave data...")
    result = await call_tool(
        "generate_sine_data",
        {
            "num_points": 200,
            "start": 0.0,
            "end": 6.283185307179586,  # 2π
            "function": "sin"
        }
    )
    print(result[0].text)
    
    # Step 2: Compute statistics
    print("\n2. Computing statistics...")
    result = await call_tool(
        "compute_statistics",
        {"data_file": "sin_data.txt"}
    )
    print(result[0].text)
    
    # Step 3: Create plot
    print("\n3. Creating plot...")
    result = await call_tool(
        "plot_data",
        {
            "data_file": "sin_data.txt",
            "output_file": "example_sin_plot.png",
            "title": "Example Sine Wave",
            "xlabel": "x (radians)",
            "ylabel": "sin(x)"
        }
    )
    print(result[0].text)
    if len(result) > 1:
        print(f"  Image generated: {result[1].mimeType}")


async def example_cosine_wave():
    """Example: Generate and analyze cosine wave."""
    
    print("\n" + "=" * 60)
    print("Example 2: Cosine Wave Generation")
    print("=" * 60)
    
    # Generate cosine wave
    print("\nGenerating cosine wave data...")
    result = await call_tool(
        "generate_sine_data",
        {
            "num_points": 150,
            "start": 0.0,
            "end": 12.566370614359172,  # 4π
            "function": "cos"
        }
    )
    print(result[0].text)
    
    # Plot it
    print("\nCreating cosine plot...")
    result = await call_tool(
        "plot_data",
        {
            "data_file": "cos_data.txt",
            "output_file": "example_cos_plot.png",
            "title": "Cosine Wave (0 to 4π)",
            "xlabel": "x",
            "ylabel": "cos(x)"
        }
    )
    print(result[0].text)


async def example_compare_functions():
    """Example: Compare different trigonometric functions."""
    
    print("\n" + "=" * 60)
    print("Example 3: Compare Trigonometric Functions")
    print("=" * 60)
    
    functions = ["sin", "cos", "tan"]
    
    for func in functions:
        print(f"\n--- {func.upper()} Function ---")
        
        # Generate data
        result = await call_tool(
            "generate_sine_data",
            {
                "num_points": 100,
                "start": -3.14,
                "end": 3.14,
                "function": func
            }
        )
        print(result[0].text[:150] + "...")
        
        # Get statistics
        result = await call_tool(
            "compute_statistics",
            {"data_file": f"{func}_data.txt"}
        )
        # Print just the summary line
        lines = result[0].text.split('\n')
        print(f"  Stats computed: {len(lines)} lines")


async def main():
    """Run all examples."""
    print("\n🤖 MCP Agent Examples")
    print("=" * 60)
    print("This demonstrates the capabilities of the mcpdocs MCP agent.")
    print("=" * 60)
    
    try:
        # Run examples
        await example_sine_wave_workflow()
        await example_cosine_wave()
        await example_compare_functions()
        
        print("\n" + "=" * 60)
        print("✓ All examples completed successfully!")
        print("=" * 60)
        print("\nGenerated files:")
        print("  - sin_data.txt, example_sin_plot.png")
        print("  - cos_data.txt, example_cos_plot.png")
        print("  - tan_data.txt")
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
