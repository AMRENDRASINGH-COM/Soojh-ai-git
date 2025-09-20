# tools.py
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun

def load_tools():
    arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=500)
    arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_wrapper)

    wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
    wiki_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)

    return [wiki_tool, arxiv_tool]

