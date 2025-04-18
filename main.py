from crewai import Agent, Task, Crew
from Tools.WikipediaTool import WikipediaTool

# 1. Criar ferramentas (tool)
wikipedia_tool = WikipediaTool()

# 2. Criar agentes
researcher = Agent(
    role="Pesquisador de Conteúdo",
    goal="Pesquisar informações confiáveis e atualizadas sobre o tópico fornecido.",
    backstory="Você é um especialista em busca de informações, capaz de extrair dados relevantes da Wikipedia e outras fontes abertas para ajudar na criação de conteúdo educacional.",
    tools=[wikipedia_tool],
    allow_delegation=False,
    verbose=True
)

writer = Agent(
    role="Redator de Conteúdo",
    goal="Escrever um artigo informativo e envolvente sobre o tema proposto.",
    backstory="Você é um redator habilidoso que transforma pesquisas em textos bem estruturados, com clareza, fluidez e coerência.",
    allow_delegation=False,
    verbose=True
)

editor = Agent(
    role="Editor de Conteúdo",
    goal="Revisar e refinar o artigo para garantir clareza, consistência e correção gramatical.",
    backstory="Você é um editor que revisa cuidadosamente os textos para deixá-los prontos para publicação, mantendo o estilo da marca.",
    allow_delegation=False,
    verbose=True
)

# 3. Criar tarefas
topic = "Energia Solar"

research_task = Task(
    description=f"Pesquisar e resumir informações sobre {topic} usando a Wikipedia e outras fontes abertas.",
    expected_output=f"Resumo completo sobre {topic}, com dados e explicações técnicas acessíveis.",
    agent=researcher
)

writing_task = Task(
    description="Escrever um artigo com base nas informações pesquisadas, incluindo introdução, desenvolvimento e conclusão.",
    expected_output="Artigo bem escrito em formato markdown, com título, subtítulos e ao menos 300 palavras.",
    agent=writer,
    context=[research_task]
)

editing_task = Task(
    description="Revisar o artigo escrito, corrigir erros e aprimorar a clareza e estilo.",
    expected_output="Artigo final revisado, pronto para publicação.",
    agent=editor,
    context=[writing_task]
)

# 4. Criar a Crew
crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, writing_task, editing_task],
    verbose=2
)

# 5. Executar a Crew
if __name__ == "__main__":
    result = crew.kickoff(inputs={"topic": topic})
    print(result)
