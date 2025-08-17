from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools
from agno.tools.financial_datasets import FinancialDatasetsTools
from dotenv import load_dotenv
import os

load_dotenv()

def create_financial_agent():
    return Agent(
        name="Financial Agent",
        model=Gemini(id="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY")),
        tools=[
            ReasoningTools(add_instructions=True),
            YFinanceTools(stock_price=True, analyst_recommendations=True, company_news=True),
            FinancialDatasetsTools(enable_search=True, enable_news=True, enable_market_data=True, api_key=os.getenv("FINANCIAL_DATASETS_API_KEY")),
        ],
        description=(
            "Specialized agent focused on identifying the stocks US stocks."
            "It analyzes current stock prices, historical trends, analyst recommendations, and market data "
            "to determine which stocks are most promising for investment based on quantitative metrics."
        ),
        instructions=[
            "Retrieve and analyze US stock data using YFinance and FinancialDatasets tools.",
            "Rank stocks based on performance, growth potential, and analyst recommendations.",
            "Provide a clear recommendation for each stock: Buy, Hold, or Wait.",
            "Include quantitative reasoning and key metrics that support each recommendation.",
            "Include general news or market sentiment"
        ],
        show_tool_calls=True,
        markdown=True,
    )