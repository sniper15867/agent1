from langchain_openai import ChatOpenAI
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
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    tools = [calculator, say_hello]
    agent_executor = create_react_agent(model, tools)
    return agent_executor
