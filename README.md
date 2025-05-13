# OpenAI Agent MCP Script

This script demonstrates using the `openai-agents` library to interact with an agent that uses Model Context Protocol (MCP) servers.

## Functionality

- Loads an OpenAI API key from a `.env` file.
- Uses an agent configured with an MCP server (`uvx mcp-server-fetch`) to retrieve web content.
- Uses a custom tool (`current_time`) to get the current timestamp.
- Prompts the agent to fetch a specific URL (Windsurf changelog), summarize it, and include the timestamp.

## Setup

1.  **Environment:** Create a conda environment (e.g., `test`) with Python 3.12+.
    ```bash
    conda create -n test python=3.12
    conda activate test
    ```
2.  **Dependencies:** Install required packages.
    ```bash
    # Assuming pyproject.toml exists and is configured for poetry/pdm/etc.
    # Or install manually:
    pip install python-dotenv "openai-agents>=0.0.11"
    # Ensure 'uvx' command is available in your PATH (e.g., via homebrew)
    ```
3.  **API Key:** Create a `.env` file in the project root with your OpenAI API key:
    ```
    OPENAI_API_KEY=sk-...
    ```
    You can copy `.env.example` to create this file.

## Running

```bash
conda run -n test python openai_mcp.py
```
