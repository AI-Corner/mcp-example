# 🚀 MCP Examples Hub: Your Gateway to Model Context Protocol

Welcome to the **MCP Examples Hub**! This repository is a curated collection of Model Context Protocol (MCP) servers designed to extend the capabilities of AI assistants (like Claude, ChatGPT, or local agents). 

The Model Context Protocol (MCP) allows AI models to safely and structuredly interact with your local tools, databases, and APIs.

## 📁 Repository Overview

This project contains 6 distinct examples of MCP servers, ranging from simple calculators to complex enterprise integrations.

| # | Example | Description | Technology |
|---|---------|-------------|------------|
| 1 | **[Basic Setup](./1-sample-mcp-setup-with-claude)** | A "Hello World" style setup using a Projectile Calculator. | Python / Gradio |
| 2 | **[Kubernetes (kubectl)](./2-kubectl-mcp-claude-sample)** | Manage your K8s clusters directly from your AI interface. | Python / Docker |
| 3 | **[Google Workspace](./3-google-workspace-mcp-server)** | Interact with Gmail (send/search) and Google Calendar. | Node.js / Google API |
| 4 | **[Excel Automation](./4-excel-mcp-server)** | Query and manipulate Excel spreadsheet data. | Python |
| 5 | **[PowerPoint Creator](./5-powerpoint-mcp-server)** | Generate presentations based on AI-generated content. | Python / UV |
| 6 | **[YouTube Insights](./6-youtube-data-mcp-server)** | Search videos and fetch channel transcripts/data. | Node.js / YouTube API |

---

## 🛠️ General Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (v18+) and **npm**
- **Python** (v3.10+) 
- **Claude Desktop** or an equivalent MCP-compatible client
- **Docker** (Required only for Example #2)

---

## 🚀 Quick Start Guide

### 1. Basic Structure of an MCP Server
Most examples in this repo follow a similar setup:
1. **Configure Environment**: Set up API keys or local permissions.
2. **Launch Server**: Run the server script (usually `app.py` or `index.js`).
3. **Configure Client**: Add the server's endpoint to your AI client's configuration file.

### 2. Configuring your AI Client
To use these servers with the Claude Desktop app, you need to edit your configuration file:

**Location:**
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`

**Example Entry:**
```json
{
  "mcpServers": {
    "my-example-server": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-everything"]
    }
  }
}
```

---

## 🤝 Community & Contributions

We believe the power of MCP lies in community-driven tools. We invite you to:

- **⭐ Star the Repo**: If you find these examples helpful!
- **🍴 Fork & Build**: Use these as blueprints for your own custom servers.
- **🙋 Open an Issue**: If you hit a snag or have a great idea for a new example.
- **🚀 Submit a PR**: We love seeing new integrations (e.g., Salesforce, Slack, Perplexity, etc.).

### How to Contribute a New Example
1. Create a new directory prefixed with the next logical number (e.g., `7-my-new-server`).
2. Include a `README.md` inside that folder with setup instructions.
3. Ensure no sensitive information (API keys, personal file paths) is committed.

---

## 🔒 Security & Privacy
These examples are for educational purposes. Always remember:
- Never commit your `credentials.json`, `.env` files, or API keys.
- Be mindful of the permissions you grant to MCP servers (especially File System or Email access).

---

**Built by the Community for the Community.**
*Let's make AI more useful, one tool at a time.*