# MCP servers to handle multimodal medical data

(Example below)
# EEG Server Setup Instructions

This document provides instructions for setting up and configuring the EEG server.

## Prerequisites

- Python environment (Anaconda recommended)
- `uv` package manager installed in your Python environment.

## Installation

1.  **Navigate to the server directory:**
    Open your terminal and change to the `eeg-server` directory:
    ```bash
    cd path/to/your/multimodal-medical-mcp-servers/eeg-server
    ```
    *Replace `path/to/your/` with the actual path to the `multimodal-medical-mcp-servers` directory on your system.*

2.  **Initialize the environment and install dependencies:**
    Use `uv` to set up the environment and install the required Python packages:
    ```bash
    uv init
    uv add mcp[cli] mne
    ```

## Configuration for Claude Desktop

To use this EEG server with Claude Desktop, you need to add its configuration to your `claude_desktop_config.json` file. This file is typically located in your user's application data directory.

1.  **Locate or create `claude_desktop_config.json`**.

2.  **Add the following JSON configuration block:**

    ```json
    {
      "mcpServers": {
        "eeg-server": {
          "command": "C:\\Users\\{user}\\anaconda3\\envs\\mcp\\Scripts\\uv.exe",
          "args": [
            "--directory",
            "C:\\Users\\{path to folder}\\multimodal-medical-mcp-servers\\eeg-server",
            "run",
            "server.py"
          ]
        }
      }
    }
    ```

    **Important Placeholders:**
    *   Replace `{user}` with your Windows username (e.g., `C:\Users\YourUserName\...`).
    *   Replace `{path to folder}` with the full path to the directory where you cloned or placed the `multimodal-medical-mcp-servers` repository (e.g., `C:\Users\YourUserName\Documents\Projects`).


## Running the Server

Once configured in `claude_desktop_config.json`, Claude Desktop should be able to start the EEG server automatically when needed.

If you need to run the server manually for testing or development, you can execute the command specified in the configuration directly in your terminal (ensure you are in an environment where `uv` is available):

```bash
C:\Users\{user}\anaconda3\envs\mcp\Scripts\uv.exe --directory C:\Users\{path to folder}\multimodal-medical-mcp-servers\eeg-server run server.py
```
Make sure to replace the placeholders as described above.