#!/usr/bin/env python3
"""CLI entry point for the MCP server."""

import sys
from mcpdocs_agent.server import main
import asyncio


def run():
    """Run the MCP server."""
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer stopped by user", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    run()
