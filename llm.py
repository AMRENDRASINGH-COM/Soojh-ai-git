#llm.py

from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from google.adk.models.lite_llm import LiteLlm

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

Llm = LiteLlm(openai_api_key=OPENAI_API_KEY, model="openai/gpt-4o")

# Initialize OpenAI LLM via LangChain
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="openai/gpt-4o")

