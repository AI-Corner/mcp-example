import os
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Perplexity Search")

PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"

@mcp.tool()
async def search_perplexity(query: str) -> str:
    """
    Perform a real-time internet search using Perplexity AI.
    
    Args:
        query: The search query string.
    """
    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        return "Error: PERPLEXITY_API_KEY environment variable not set."

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-sonar-large-128k-online",
        "messages": [
            {
                "role": "system",
                "content": "Be precise and concise."
            },
            {
                "role": "user",
                "content": query
            }
        ]
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(PERPLEXITY_API_URL, headers=headers, json=payload, timeout=30.0)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error connecting to Perplexity: {str(e)}"

if __name__ == "__main__":
    mcp.run()
