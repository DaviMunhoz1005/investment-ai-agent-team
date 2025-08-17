from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.webbrowser import WebBrowserTools
from dotenv import load_dotenv
import os

load_dotenv()

def create_news_agent():
    """
    Agent that receives a list of US stock tickers and searches recent news:
    summarizes if articles suggest Buy, Wait, or Hold.
    """
    return Agent(
        name="News/Research Agent",
        model=Gemini(id="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY")),
        tools=[
            ReasoningTools(add_instructions=True),
            GoogleSearchTools(),
            WebBrowserTools(),
        ],
        description=(
            "Specialized agent that gathers and summarizes recent news for US stocks. "
            "Reports what sources indicate about Buy, Wait, or Hold for each stock."
        ),
        instructions=[
            "Receive a list of US stock tickers from the user.",
            "Search recent news, articles, and reports for each stock.",
            "Summarize what the sources indicate (Buy, Wait, Hold) and provide the key reason.",
            "Do not give personal recommendations; focus on what news sources say.",
            "Provide concise bullet points or short paragraphs per stock."
        ],
        show_tool_calls=True,
        markdown=True,
    )
