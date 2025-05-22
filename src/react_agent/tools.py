"""This module provides example tools for web scraping and search functionality.

It includes a basic Tavily search function (as an example)

These tools are intended as free examples to get started. For production use,
consider implementing more robust and specialized tools tailored to your needs.
"""

from typing import Any, Callable, List, Optional, cast
from langchain_core.messages import AIMessage, HumanMessage
from langchain_tavily import TavilySearch  # type: ignore[import-not-found]

from react_agent.configuration import Configuration
from react_agent.state import InputState, State
from langgraph.types import interrupt,Command

import yaml,asyncio

async def search(query: str) -> Optional[dict[str, Any]]:
    """Search for general web results.

    This function performs a search using the Tavily search engine, which is designed
    to provide comprehensive, accurate, and trusted results. It's particularly useful
    for answering questions about current events.
    """
    configuration = Configuration.from_context()
    wrapped = TavilySearch(max_results=configuration.max_search_results)
    return cast(dict[str, Any], await wrapped.ainvoke({"query": query}))


# --- Tool 2: Save AI response to YAML ---
async def save_to_file(content: str, filename: str = "ai_output.yaml") -> dict[str, Any]:
    """Save Workflows to Yaml file.
    This function saves the AI's response to a YAML file."""
    data = {"response": content}

    def write_file():
        with open(filename, "w") as f:
            yaml.dump(data, f)

    await asyncio.to_thread(write_file)

    return {
        "status": "success",
        "filename": filename,
        "message": f"Saved content to {filename}"
    }



TOOLS: List[Callable[..., Any]] = [search,save_to_file]
