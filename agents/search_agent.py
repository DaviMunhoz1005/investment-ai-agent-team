from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.webbrowser import WebBrowserTools
from dotenv import load_dotenv
import os

load_dotenv()

def create_search_agent():
    return Agent(
        name="Search Agent",
        model=Gemini(id="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY")),
        tools=[
            ReasoningTools(add_instructions=True),
            GoogleSearchTools(),
            WebBrowserTools(),
        ],
        description=(
            "Specialized agent that gathers the latest news and qualitative information about US stocks."
            "It summarizes what recent articles and reports say about whether to Buy or Wait for each stock, "
            "without making its own recommendations."
        ),
        instructions=[
            "Receive a list of US stocks from the Financial Agent.",
            "Search for the latest news, articles, and reports about these stocks.",
            "For each stock, summarize what recent articles suggest: Buy, Wait, or Hold.",
            "Do not give independent opinions; only report what the sources indicate.",
            "Provide concise bullet points or paragraphs with the source of each insight."
        ],
        show_tool_calls=True,
        markdown=True,
    )