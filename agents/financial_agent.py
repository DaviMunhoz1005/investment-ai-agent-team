from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools
from agno.tools.financial_datasets import FinancialDatasetsTools
from dotenv import load_dotenv
import os

load_dotenv()

def create_financial_agent():
    """
    Agent that receives a list of US stock tickers and returns quantitative data:
    current price, historical trends, and analyst recommendations.
    """
    return Agent(
        name="Financial Agent",
        model=Gemini(id="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY")),
        tools=[
            ReasoningTools(add_instructions=True),
            YFinanceTools(stock_price=True, analyst_recommendations=True, company_news=True),
            FinancialDatasetsTools(enable_search=True, enable_news=True, enable_market_data=True, api_key=os.getenv("FINANCIAL_DATASETS_API_KEY")),
        ],
        description=(
            "Specialized agent that provides quantitative financial data for US stocks: "
            "current price, historical trends, and analyst recommendations."
        ),
        instructions=[
            "Receive a list of US stock tickers from the user.",
            "Retrieve stock prices, historical trends, and analyst recommendations.",
            "Return a clear summary per stock including quantitative metrics.",
            "Do not include qualitative news or market sentiment."
        ],
        show_tool_calls=True,
        markdown=True,
    )
