from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from langchain_core.messages import HumanMessage

from agent import create_agent

app = FastAPI()
agent_executor = create_agent()


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat(req: ChatRequest):
    result = await agent_executor.ainvoke({"messages": [HumanMessage(content=req.message)]})
    response = result["messages"][-1].content if "messages" in result else ""
    return {"response": response}


HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Agent Chat</title>
</head>
<body>
    <h1>Chat with the Agent</h1>
    <input id="message" type="text" placeholder="Say something..." />
    <button onclick="send()">Send</button>
    <pre id="response"></pre>
    <script>
    async function send() {
        const msg = document.getElementById('message').value;
        const res = await fetch('/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message: msg})
        });
        const data = await res.json();
        document.getElementById('response').textContent = data.response;
    }
    </script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
async def index():
    return HTML_PAGE
