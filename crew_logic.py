# Importa a função 'load_dotenv' para carregar variáveis de ambiente a partir de um arquivo .env
from dotenv import load_dotenv

# Importa os agentes de pesquisa e escrita do módulo 'Agents'
from Agents import ResearcherAgent, WriterAgent

# Importa as classes 'Crew' e 'Task' da biblioteca 'crewai', que ajudam a criar equipes e tarefas
from crewai import Crew, Task

# Importa a ferramenta 'WikipediaTool' do módulo 'Tools', que será usada para buscar informações na Wikipedia
from Tools import WikipediaTool

# Importa o módulo 'os', que permite interagir com o sistema operacional (não usado diretamente neste trecho)
import os

# Carrega as variáveis de ambiente do arquivo .env (útil para armazenar configurações sensíveis)
load_dotenv()

# Define a função 'create_crew', que cria e gerencia a execução de uma equipe (crew) de agentes para pesquisar e escrever um artigo
def create_crew(topic):
    # Cria uma instância da ferramenta 'WikipediaTool' para buscar informações sobre o tópico
    wikipedia_tool = WikipediaTool()
    
    # Cria o agente de pesquisa, que usará a ferramenta WikipediaTool para buscar informações
    researcher = ResearcherAgent().create_agent(tools=[wikipedia_tool])
    
    # Cria o agente de escrita, que será responsável por redigir o artigo
    writer = WriterAgent().create_agent()

    # Cria uma tarefa de pesquisa, onde o agente 'researcher' vai buscar informações sobre o tópico
    research_task = Task(
        description=f"Pesquise informações detalhadas sobre {topic}",  # Descrição da tarefa de pesquisa
        agent=researcher,  # O agente responsável por essa tarefa será o 'researcher'
        expected_output="Informações detalhadas sobre o tópico em formato JSON"  # O formato esperado de saída é um JSON com informações detalhadas
    )

    # Cria uma tarefa de escrita, onde o agente 'writer' escreverá um artigo com base nas informações pesquisadas
    writing_task = Task(
        description=f"Escreva um artigo de pelo menos 300 palavras sobre {topic} usando as informações pesquisadas",  # Descrição da tarefa de escrita
        agent=writer,  # O agente responsável por essa tarefa será o 'writer'
        expected_output="Artigo completo com título, introdução, desenvolvimento e conclusão",  # O resultado esperado é um artigo completo
        context=[research_task]  # A tarefa de escrita depende da tarefa de pesquisa, então ela é passada como contexto
    )

    # Cria uma instância de 'Crew', representando a equipe de agentes, e define as tarefas que os agentes vão executar
    crew = Crew(
        agents=[researcher, writer],  # A equipe é composta pelos agentes 'researcher' e 'writer'
        tasks=[research_task, writing_task],  # As tarefas atribuídas são 'research_task' e 'writing_task'
        verbose=True  # Ativa o modo verboso para acompanhar o progresso das tarefas
    )

    # Inicia a execução da equipe e retorna o resultado. O 'kickoff()' provavelmente executa as tarefas de forma sequencial ou paralela.
    return crew.kickoff()
