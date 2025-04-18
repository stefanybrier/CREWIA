# Importa a classe 'Agent' do módulo 'crewai', que é a base para criação de agentes.
from crewai import Agent

# Importa a classe 'BaseTool' de 'Tools.base_tool', possivelmente para o uso de ferramentas personalizadas.
from Tools.base_tool import BaseTool # type: ignore

# Importa o módulo 'WikipediaTool' de 'Tools', provavelmente uma ferramenta que auxilia na pesquisa de informações da Wikipedia.
from Tools import WikipediaTool

# Importa a biblioteca 'os', usada para acessar variáveis de ambiente.
import os

# Importa novamente 'BaseTool' de 'crewai_tools.base_tool', pode ser um erro ou redundância no código.
# Removed redundant or unresolved import for 'crewai_tools.base_tool'.

#========================================================================

class ResearcherAgent:
    """
    Agente responsável por pesquisar informações para o artigo.
    Esta classe cria e configura um agente especializado em pesquisa.
    """

    #-------------------------------------------------------------
    def create_agent(self, tools=None):
        """
        Cria um agente pesquisador com ferramentas específicas.
        
        Args:
            tools (list): Lista de ferramentas que o agente poderá usar. Pode ser vazio.
            
        Returns:
            Agent: Uma instância do agente configurado para realizar tarefas de pesquisa.
        """
        return Agent(
            role="Pesquisador Especialista",  # Define o papel do agente como pesquisador.
            goal="Encontrar informações detalhadas e precisas sobre o tópico solicitado",  # Define o objetivo do agente.
            backstory="""Você é um pesquisador meticuloso que sabe como encontrar
            as informações mais relevantes e confiáveis sobre qualquer assunto.
            Você tem uma vasta experiência em coletar dados de diversas fontes
            e organizar informações de maneira coerente.""",  # Definindo a história do agente para dar mais contexto.
            verbose=True,  # Habilita mensagens detalhadas (útil para depuração ou logs).
            allow_delegation=False,  # Define se o agente pode delegar suas tarefas para outros agentes.
            tools=tools or [],  # Define as ferramentas que o agente pode usar, se não fornecer nada, usa uma lista vazia.
            llm=self._get_llm()  # Obtém o modelo de linguagem a ser usado pelo agente.
        )
    
    #------------------------------------------------------------

    def _get_llm(self):
        """
        Configura o modelo de linguagem para o agente.
        
        Returns:
            LLM: Instância do modelo de linguagem configurado para o agente.
        """
        # Recupera o provedor de modelo de linguagem a partir de uma variável de ambiente, com valor padrão "groq".
        llm_provider = os.getenv("LLM_PROVIDER", "groq").lower()

        # Se o provedor for "groq", utiliza o modelo de linguagem Groq.
        if llm_provider == "groq":
            # Importa a classe 'ChatGroq' da biblioteca 'langchain_groq' para o modelo de linguagem Groq.
            from langchain_groq import ChatGroq
            
            # Retorna uma instância do modelo 'ChatGroq' com a chave de API configurada.
            return ChatGroq(
                api_key=os.getenv("GROQ_API_KEY"),  # Obtém a chave de API do Groq da variável de ambiente.
                model_name="llama3-70b-8192"  # Define o nome do modelo.
            )
        
        # Se o provedor for "gemini", utiliza o modelo de linguagem Gemini.
        elif llm_provider == "gemini":
            # Importa a classe 'ChatGoogleGenerativeAI' para o modelo Gemini.
            from langchain_google_genai import ChatGoogleGenerativeAI
            return ChatGoogleGenerativeAI(
                api_key=os.getenv("GEMINI_API_KEY"),  # Obtém a chave de API do Gemini da variável de ambiente.
                model="gemini-pro"  # Define o nome do modelo Gemini.
            )
        
        # Se o provedor não for reconhecido, levanta um erro.
        else:
            raise ValueError(f"Provedor LLM não suportado: {llm_provider}")
