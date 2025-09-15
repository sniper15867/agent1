import os

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers."""
    return f"The sum of {a} and {b} is {a + b}"

@tool
def say_hello(name: str) -> str:
    """Useful for greeting a user."""
    return f"Hello {name}, I hope you are well today"


def create_agent():
    """Create and return the ReAct agent executor."""
    if not os.getenv("HUGGINGFACEHUB_API_TOKEN"):
        raise EnvironmentError(
            "A valid Hugging Face token must be available in the environment, e.g. "
            "HUGGINGFACEHUB_API_TOKEN."
        )

    endpoint = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct",
        temperature=0,
    )
    model = ChatHuggingFace(llm=endpoint)
    tools = [calculator, say_hello]
    agent_executor = create_react_agent(model, tools)
    return agent_executor
