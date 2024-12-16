from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
from crewai_tools import JSONSearchTool

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

file_path = 'C:/Users/gfulv/Documents/GitHub/CrewAI-Projects/observers/knowledge/agent_knows.txt'
content = ''
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

string_knowledge_source = StringKnowledgeSource(
	content=content,
	chunk_size = 4000,
	chunk_overlap = 200,
 	metadata={"source": "agent_knows.txt"}
)

json_search_tool = JSONSearchTool(json_path='C:/Users/gfulv/Documents/GitHub/CrewAI-Projects/observers/knowledge/moral_stories_full.json')

@CrewBase
class Observers():
	"""Observers crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def observer(self) -> Agent:
		return Agent(
			config=self.agents_config['observer'],
			verbose=True
		)
  
	@agent
	def moralist(self) -> Agent:
		return Agent(
			config=self.agents_config['moralist'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
 
	@task
	def environment_description(self) -> Task:
		return Task(
			config=self.tasks_config['environment_description'],
		)
  
	@task
	def moral_advice(self) -> Task:
		return Task(
			config=self.tasks_config['moral_advice'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Observers crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			knowledge_sources=[string_knowledge_source]
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
