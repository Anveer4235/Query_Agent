from agents_queries.tools.custom_tool import PolicyRetrieverTool
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List





# defining the class for our crew
@CrewBase
class AgentsQueries():

    agents: list[BaseAgent]
    tasks: list[Task]

    # define the paths of config files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"


    #================= Agents ====================
    @agent
    def query_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["query_agent"]
        )

    @agent
    def retriever_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["retriever_agent"],
            tools=[PolicyRetrieverTool()]
        )

    @agent
    def policy_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["policy_agent"]
        )

    @agent
    def answer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["answer_agent"]
        )

    #=============================== Tasks ===================
    @task
    def retrieve_task(self) -> Task:
        return Task(
            config=self.tasks_config["retrieve_task"]
        )

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["analysis_task"]
        )

    @task
    def final_task(self) -> Task:
        return Task(
            config=self.tasks_config["final_task"]
        )

    #===================== Crew ==================================
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
    
    

