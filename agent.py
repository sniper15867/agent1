import os

from dotenv import load_dotenv
from huggingface_hub import HfApi
from huggingface_hub.errors import RepositoryNotFoundError
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from requests.exceptions import HTTPError

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

    repo_id = "mistralai/Mistral-7B-Instruct"
    try:
        endpoint = HuggingFaceEndpoint(
            repo_id=repo_id,
            temperature=0,
        )
        model = ChatHuggingFace(llm=endpoint)
    except (HTTPError, RepositoryNotFoundError) as exc:
        raise EnvironmentError(
            "Failed to initialize the Hugging Face model. "
            "Please verify your HUGGINGFACEHUB_API_TOKEN and the model ID "
            f"'{repo_id}'."
        ) from exc

    try:
        HfApi().model_info(repo_id=repo_id)
    except (HTTPError, RepositoryNotFoundError) as exc:
        raise EnvironmentError(
            "Unable to access the specified Hugging Face model. "
            "Please check your HUGGINGFACEHUB_API_TOKEN and confirm the model ID "
            f"'{repo_id}' is correct."
        ) from exc

    tools = [calculator, say_hello]
    agent_executor = create_react_agent(model, tools)
    return agent_executor
