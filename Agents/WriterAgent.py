# Importa a classe 'Agent' do módulo 'crewai'. A classe 'Agent' é a base para a criação de agentes no sistema.
from crewai import Agent

# Importa o módulo 'os', utilizado para acessar variáveis de ambiente no sistema.
import os

#========================================================================

class WriterAgent:
    """
    Agente responsável por escrever o artigo.
    Esta classe define o comportamento de um agente especializado em escrever artigos.
    """
    
    #------------------------------------------------------------
    def create_agent(self):
        """
        Cria um agente escritor que pode escrever artigos com base em pesquisas fornecidas.
        
        Returns:
            Agent: Uma instância do agente escritor configurado.
        """
        # Cria e retorna uma instância do agente 'WriterAgent' com a configuração definida.
        return Agent(
            role="Escritor de Conteúdo",  # Define o papel do agente como escritor de conteúdo.
            goal="Escrever artigos informativos e envolventes com base nas pesquisas fornecidas",  # Define o objetivo do agente.
            backstory="""Você é um escritor talentoso com experiência em criar
            conteúdos informativos e bem estruturados. Você sabe como
            transformar informações brutas em artigos coesos e interessantes
            que prendem a atenção do leitor do início ao fim.""",  # Define a história do agente, contextualizando suas habilidades e competências.
            verbose=True,  # Ativa mensagens detalhadas (útil para depuração ou logs).
            allow_delegation=False,  # Desativa a delegação de tarefas, ou seja, o agente não delega suas responsabilidades.
            llm=self._get_llm()  # Define o modelo de linguagem (LLM) a ser utilizado pelo agente.
        )
    
    #------------------------------------------------------------
    
    def _get_llm(self):
        """
        Configura o modelo de linguagem para o agente escritor.
        
        Returns:
            LLM: Instância do modelo de linguagem configurado para o agente.
        """
        # Obtém o provedor de modelo de linguagem a partir de uma variável de ambiente chamada 'LLM_PROVIDER'. Caso não exista, o valor padrão será 'groq'.
        llm_provider = os.getenv("LLM_PROVIDER", "groq").lower()
        
        # Se o provedor for 'groq', utiliza o modelo de linguagem Groq.
        if llm_provider == "groq":
            # Importa o módulo necessário para usar o modelo Groq.
            from langchain_groq import ChatGroq
            
            # Retorna uma instância do modelo 'ChatGroq', configurado com a chave de API e o nome do modelo.
            return ChatGroq(
                api_key=os.getenv("GROQ_API_KEY"),  # Obtém a chave de API do Groq a partir de uma variável de ambiente.
                model_name="llama3-70b-8192"  # Define o nome do modelo.
            )
        
        # Se o provedor for 'gemini', utiliza o modelo de linguagem Gemini.
        elif llm_provider == "gemini":
            # Importa o módulo necessário para usar o modelo Gemini.
            from langchain_google_genai import ChatGoogleGenerativeAI
            
            # Retorna uma instância do modelo 'ChatGoogleGenerativeAI', configurado com a chave de API e o nome do modelo.
            return ChatGoogleGenerativeAI(
                api_key=os.getenv("GEMINI_API_KEY"),  # Obtém a chave de API do Gemini a partir de uma variável de ambiente.
                model="gemini-pro"  # Define o nome do modelo Gemini.
            )
        
        # Se o provedor de LLM não for reconhecido, lança um erro.
        else:
            raise ValueError(f"Provedor LLM não suportado: {llm_provider}")
