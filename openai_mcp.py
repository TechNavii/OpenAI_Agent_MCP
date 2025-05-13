import asyncio
from datetime import datetime
import os
from dotenv import load_dotenv

from agents import Agent, Runner, function_tool
from agents.mcp import MCPServerStdio

# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

@function_tool
async def current_time() -> str:
    """Return the current local time in ISO-like format."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def build_mcp_server() -> MCPServerStdio:
    """
    Create and return an MCPServerStdio instance pre-configured
    to run the custom fetch command.
    """
    return MCPServerStdio(
        params={
            "command": "uvx",
            "args": ["mcp-server-fetch"],
        },
    )


def build_agent(server: MCPServerStdio) -> Agent:
    """
    Construct the conversational agent that will perform the
    document fetch and summarisation.
    """
    return Agent(
        name="DocSummariser",
        model="gpt-4.1-mini",
        instructions=(
            "You are a concise, helpful assistant. "
            "Summarise requested web pages in clear bullet points."
        ),
        mcp_servers=[server],
        tools=[current_time],
    )


# ---------------------------------------------------------------------------
# Main coroutine
# ---------------------------------------------------------------------------

async def main() -> None:
    """Entrypoint coroutine."""
    mcp_server = build_mcp_server()

    async with mcp_server:
        agent = build_agent(mcp_server)

        # Add a delay to allow the MCP server process time to start
        await asyncio.sleep(10)

        prompt = (
            "Retrieve https://windsurf.com/changelog and provide:\n"
            "1. A brief summary of the latest changes.\n"
            "2. The timestamp returned by the current_time tool."
        )

        try:
            result = await Runner.run(agent, prompt)
            print(result.final_output)
        except Exception as e:
            print(f"Error during Runner.run: {e}")
            # Optionally re-raise to see full traceback if needed
            # raise


# ---------------------------------------------------------------------------

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"An error occurred: {e}")
