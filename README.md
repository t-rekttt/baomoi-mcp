# Baomoi MCP Server

A Model Context Protocol (MCP) server implementation for accessing Baomoi (Vietnamese news aggregator) content through LLM applications.

## Overview

This MCP server provides a standardized interface for LLMs to interact with Baomoi's API, allowing them to:
- Retrieve news content by type and pagination
- Search for content and topics across the Baomoi platform

## Features

- **List Content by Type**: Fetch news articles based on different list types and pagination
- **Search Functionality**: Search for either content or topics with customizable result sizes
- **Secure API Integration**: Implements HMAC signing for secure API requests

## Prerequisites

- Python 3.7+
- `httpx` library
- MCP SDK

## Installation

1. Clone this repository:
```bash
git clone [repository-url]
cd baomoi-mcp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

The server requires the following environment variables or constants (currently defined in server.py):

- `API_KEY`: Your Baomoi API key
- `SECRET`: Your Baomoi API secret for HMAC signing
- `VERSION`: API version (currently set to '0.7.16')
- `BASE_API_URL`: Base URL for the Baomoi API

## Usage

### Running the Server

```bash
python server.py
```

### Available Tools

1. `list_by_type`:
   - Parameters:
     - `list_type` (int, default=1): Type of news list to retrieve
     - `list_id` (int, default=0): Specific list ID
     - `page` (int, default=1): Page number
     - `ctime` (int): Current timestamp
     - `version` (str): API version

2. `search`:
   - Parameters:
     - `keyword` (str): Search query term
     - `type_` (str): Either 'content' or 'topic'
     - `size` (int, default=10): Number of results to return

## Integration with MCP Clients

This server can be integrated with any MCP-compatible client, such as Claude Desktop or other LLM applications that implement the MCP protocol.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add appropriate license information]

## Acknowledgments

- Built using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- Powered by Baomoi API
