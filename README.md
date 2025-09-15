# Project1

This project demonstrates a simple LangChain ReAct agent that can be used from the command line or through a FastAPI web application.

## Setup

Provide your Hugging Face Hub API token via a `.env` file in the project root:

```bash
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

## Command Line Interface

Run the interactive CLI:

```bash
uv run python main.py
```

## FastAPI Server

Start the server with:

```bash
uv run uvicorn app:app --reload
```

Open <http://localhost:8000/> in your browser to access a minimal chat interface. Enter a message and the page will display the agent's reply.
