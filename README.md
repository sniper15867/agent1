<h1 align="center" id="title">AI AGENT</h1>

<p align="center"><img src="https://socialify.git.ci/sniper15867/agent1/image?language=1&amp;owner=1&amp;name=1&amp;stargazers=1&amp;theme=Light" alt="project-image"></p>

<p id="description">This project demonstrates a simple LangChain AI agent that can be used from the command line or through a FastAPI web application.</p>

<p align="center"><img src="https://img.shields.io/badge/python-1" alt="shields"><img src="https://img.shields.io/badge/Langchain-1" alt="shields"></p>

<h2>🛠️ Installation Steps:</h2>

<p>1. Setup - Provide your Hugging Face Hub API token via a .env file in the project root:</p>

```
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

<p>2. Command Line Interface - Run the interactive CLI:</p>

```
uv run python main.py
```

<p>3. FastAPI Server - Open http://localhost:8000/ in your browser to access a minimal chat interface. Enter a message and the page will display the agent's reply.</p>

```
uv run uvicorn app:app --reload
```

Open <http://localhost:8000/> in your browser to access a minimal chat interface. Enter a message and the page will display the agent's reply.
