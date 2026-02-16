# 🔍 Example 7: Perplexity Search MCP Server

This MCP server allows your AI assistant to perform live web searches using **Perplexity AI's online models**. Since you have a Perplexity Pro subscription, you can use your monthly API credits to power this.

## 🔑 Setup

1. **Get your API Key**:
   Visit [https://www.perplexity.ai/settings/api](https://www.perplexity.ai/settings/api) and generate an API key.

2. **Install Dependencies**:
   ```bash
   pip install mcp[fastmcp] httpx
   ```

3. **Configure Claude Desktop**:
   Open your `claude_desktop_config.json` and add:

   ```json
   {
     "mcpServers": {
       "perplexity": {
         "command": "python",
         "args": ["D:/2026/mcp-example/7-perplexity-mcp-server/app.py"],
         "env": {
           "PERPLEXITY_API_KEY": "YOUR_PPLX_API_KEY_HERE"
         }
       }
     }
   }
   ```

## 🚀 Usage
Once configured, your AI will have a `search_perplexity` tool. You can ask:
- "What is the current price of Bitcoin?"
- "Search Perplexity for the latest news on AI Periodic Tables."
- "What happened in the stock market today?"

## 💡 Why use this?
While many AIs have their own search, Perplexity is specifically optimized for high-quality, cited search results. Using it as an MCP server brings that dedicated search power directly into your coding environment or chat.
