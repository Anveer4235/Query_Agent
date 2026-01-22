import warnings
from agents_queries.crew import AgentsQueries
from dotenv import load_dotenv
load_dotenv()


warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        "query" : "What is policy for sick leave?"
    }

    try:
        AgentsQueries().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


