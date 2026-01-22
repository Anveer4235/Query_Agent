from crewai.tools import BaseTool
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from pydantic import BaseModel, Field
from typing import Type


class PolicyRetrieverInput(BaseModel):
    query: str = Field(
        ...,
        description="User question to retrieve relevant company policy text"
    )


class PolicyRetrieverTool(BaseTool):
    name: str = "PolicyRetrieverTool"
    description: str = "Retrieve relevant company policy text from internal company policy PDFs using semantic similarity search"
                        
    args_schema: Type[BaseModel] = PolicyRetrieverInput

    def _run(self, query: str) -> str:
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma(
            persist_directory="knowledge/vectorstore",
            embedding_function=embeddings
        )

        results = vectorstore.similarity_search(query, k=3)
        return "\n\n".join([doc.page_content for doc in results])
