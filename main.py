from agno.models.google import Gemini
from agno.team import Team

from agents.financial_agent import create_financial_agent
from agents.search_agent import create_news_agent

from dotenv import load_dotenv
import os

load_dotenv()

financialAgent = create_financial_agent()
newsAgent = create_news_agent()

financialTeam = Team(
    name="Financial Team",
    model=Gemini(id="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY")),
    members=[financialAgent, newsAgent],
    instructions="""
    1. Receive a list of US stock tickers from the user.
    2. The Financial Agent provides quantitative data for each stock:
       - Current price
       - Historical trends
       - Analyst recommendations
    3. The News/Research Agent provides qualitative insights:
       - Summarize what recent articles or reports suggest: Buy, Wait, or Hold
       - Include key reasons from sources
    4. Coordinate both responses to produce a single ASCII table with columns:
       Stock Name | Current Price | Recommendation | Key Reason
    5. Ensure that:
       - Quantitative metrics come from the Financial Agent
       - Qualitative justification comes from the News Agent
       - No independent opinions are added; only report data and source insights
    6. Deliver the table in markdown-ready format for easy readability.
    """,
    mode="coordinate",
    markdown=True,
    show_members_responses=True,
    enable_agentic_context=True,
    success_criteria="The team shows a complete table with stock name, price, Buy/Wait recommendation, and key reason from news sources.",
)

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        break
    financialTeam.print_response(user_input, stream=True)