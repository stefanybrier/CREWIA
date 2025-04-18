# crew.py

from crewai import Crew
from agentes.pesquisador import agente_pesquisador
from agentes.redator import agente_redator
from ferramentas.wikipedia_tool import WikipediaTool

def criar_crew():
    # Defina as ferramentas compartilhadas pelos agentes
    ferramentas = [WikipediaTool()]

    # Configurar os agentes com suas ferramentas
    pesquisador = agente_pesquisador(tools=ferramentas)
    redator = agente_redator(tools=ferramentas)

    # Definir as tarefas
    tarefas = [
        {
            "agent": pesquisador,
            "description": "Pesquise informações sobre o tópico fornecido",
            "expected_output": "Resumo com fontes confiáveis"
        },
        {
            "agent": redator,
            "description": "Com base no resumo, redija um artigo de pelo menos 300 palavras",
            "expected_output": "Artigo finalizado"
        }
    ]

    # Criar a Crew
    crew = Crew(
        agents=[pesquisador, redator],
        tasks=tarefas,
        verbose=True
    )

    return crew
