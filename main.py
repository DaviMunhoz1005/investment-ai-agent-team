from agno.models.google import Gemini
from agno.team import Team
from agno.playground import Playground

from agents.financial_agent import create_financial_agent
from agents.search_agent import create_search_agent

from dotenv import load_dotenv
import os

load_dotenv()

financialAgent = create_financial_agent()

searchAgent = create_search_agent()

financialTeam = Team(
    name="Financial Team",
    model=Gemini(id="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY")),
    members=[financialAgent, searchAgent],
    instructions="Present results in an ASCII table with columns: Stock Name | Current Price | Recommendation | Key Reason",
    mode="coordinate",
    markdown=True,
    show_members_responses=True,
    enable_agentic_context=True,
    success_criteria="The team shows a complete table with stock name, price, whether it is recommended to buy or hold "
                     "and the key reason for buying or holding",
)

playground = Playground(agents=[financialAgent, searchAgent], teams=[financialTeam])
app = playground.get_app()

if __name__ == "__main__":
    playground.serve(app="main:app", reload=True)