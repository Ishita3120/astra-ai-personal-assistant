# Astra – AI-Powered Personal Assistant

Astra is a personal AI assistant built using Python and locally hosted Large Language Models (LLMs) through Ollama.

This project is part of my learning journey into AI agents, LLM integration, and tool calling. The goal is to understand how an LLM can interact with external functions to perform useful tasks.

## Features

- **Local LLM Integration:** Uses Ollama to run language models locally.
- **Tool Calling:** Enables the LLM to identify and invoke Python functions based on user requests.
- **Current Date and Time:** Retrieves the current date and time.
- **Weather Information:** Fetches weather information for a specified city.
- **Modular Structure:** Separates assistant logic from tool implementations.

## Technologies Used

- Python
- Ollama
- OpenAI Python SDK (for Ollama's OpenAI-compatible API)
- Requests
- Python-dotenv
- LLM: Qwen3:4b
- LLM Runtime:Ollama

## Project Structure

```text
astra-ai-personal-assistant/
│
├── simple_ai_assistant.py
├── tools.py
├── .gitignore
├── requirements.txt
├── .env.example
└── README.md
```

## Getting Started

### 1. Prerequisites

- Python installed on your system.
- Ollama installed and running.
- A compatible language model downloaded through Ollama.
- ollama pull qwen3:4b

### 2. Clone the repository

```bash
git clone https://github.com/Ishita3120/astra-ai-personal-assistant.git
cd astra-ai-personal-assistant
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project directory using `.env.example` as a reference.

Configure the Ollama base URL, API key value expected by the client, and model name.

### 5. Run the assistant

```bash
python simple_ai_assistant.py
```

## Learning Objectives

Through this project, I am exploring:

- Integration of locally hosted LLMs with Python.
- Function and tool calling.
- How LLMs interact with external tools.
- Maintaining conversational context.
- Building modular AI assistant applications.

## Future Enhancements

- Add more useful tools and capabilities.
- Improve error handling and response management.
- Explore additional agent workflows.
- Enhance conversational capabilities.

## Project Status

**Ongoing – Personal Learning Project**

This project is actively being developed as I explore local LLMs and AI agent development.
