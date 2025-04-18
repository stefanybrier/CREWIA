# Sistema Multiagentes para Geração de Artigos Utilizando CrewAI

Este projeto é um sistema baseado em múltiplos agentes inteligentes que trabalham em conjunto para gerar artigos de forma automatizada. Utilizando a biblioteca [CrewAI](https://github.com/joaomdmoura/crewAI) e modelos de linguagem (LLMs) gratuitos como **Groq** e **Gemini**, o sistema é capaz de realizar pesquisas na Wikipedia, compor textos coerentes com pelo menos 300 palavras e entregar o resultado por meio de uma API estruturada.

## ✨ Objetivo

Criar um pipeline completo com agentes especializados que se comunicam e colaboram para produzir conteúdos informativos de maneira eficiente, a partir de um único tópico fornecido pelo usuário.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- [**CrewAI**](https://github.com/joaomdmoura/crewAI)
- **crewai-tools** (ferramentas customizadas)
- **FastAPI** (framework para a API)
- **Pydantic** (validação e estruturação dos dados)
- **Wikipedia API** (extração de informações)
- **Groq / Gemini** (LLMs gratuitos)

---

## 🧠 Como Funciona

O sistema segue uma arquitetura modular dividida em ferramentas, agentes, tarefas e fluxos de execução coordenados. A estrutura é baseada em boas práticas de desenvolvimento com ênfase em clareza, reusabilidade e extensibilidade.

---

## 🛠️ Etapas do Desenvolvimento

1. **Preparação do ambiente de desenvolvimento**
    - Configurar um ambiente Python
    - Instalar as bibliotecas necessárias: CrewAI, crewai-tools, pydantic e o framework para API (FastAPI ou Flask)

2. **Estruturação do projeto**
    - Criar a estrutura de diretórios adequada
    - Inicializar um repositório Git
    - Criar o arquivo README.md com as instruções de uso

3. **Desenvolvimento da ferramenta personalizada para a Wikipedia**
    - Implementar uma ferramenta CrewAI customizada para consultar a API da Wikipedia
    - Garantir que a ferramenta possa extrair informações relevantes para os artigos

4. **Definição e implementação dos agentes**
    - Criar pelo menos dois agentes com funções específicas (ex: um para pesquisa, outro para redação)
    - Configurar os LLMs gratuitos (Groq e/ou Gemini) para cada agente
    - Definir as habilidades e ferramentas de cada agente

5. **Implementação da Crew**
    - Desenvolver a lógica para coordenar os agentes
    - Estabelecer o fluxo de trabalho entre os agentes
    - Definir as tarefas e seus requisitos

6. **Criação dos modelos Pydantic**
    - Desenvolver modelos Pydantic para formatar o output da Crew

7. **Desenvolvimento da API**
    - Implementar uma API (FastAPI ou Flask) para executar o sistema
    - Criar os endpoints necessários para receber solicitações e retornar artigos

8. **Aplicação de técnicas de engenharia de prompts**
    - Estruturar prompts eficientes para os agentes
    - Otimizar as instruções para obter melhores resultados dos LLMs

9. **Testes e validação**
    - Testar o sistema para diferentes tópicos
    - Verificar se os artigos gerados têm pelo menos 300 palavras
    - Validar a qualidade e relevância do conteúdo

10. **Documentação do código**
    - Adicionar docstrings e comentários explicativos
    - Documentar a API
    - Completar o README.md com instruções claras de instalação e uso

11. **Publicação no GitHub**
    - Fazer commit do projeto completo
    - Tornar o repositório público
    - Verificar se toda a documentação está adequada

12. **Preenchimento do formulário de conclusão**
    - Preencher o formulário até o dia **18/04/2025**

-----------------------------------------------------

## 1 - Preparação do ambiente de desenvolvimento

Antes de iniciar o desenvolvimento, é necessário gerar as chaves de API dos provedores de LLMs que serão usados: **Groq** e **Gemini (Google AI)**.


- *A. Criação de uma API Key do Groq*
    
    No link  [console.groq.com/keys](https://console.groq.com/keys) 
    
    Clicar no botão **"Create API Key"**
    
    Escolher um nome para a key 
    
    Copiar a key gerada, no meu caso foi:
	
gsk_eEJ4BPdXfNKdW29BjWzRWGdyb3FY9jqNhQSYfITS4gPfHWFd4lj


- *B. Criação de uma API Key do Gemini*
    
    No link do google AI studio [aistudio.google.com/](http://aistudio.google.com/)
    
    Clicar no botão **"Get API Key"**
    
    Clicar no botão Criar chave de API
    
    Copiar a key gerada,  no meu caso foi:

AIzaSyCQwcOMBolAbTq0jWAHL5mevVml8a3aX10

## 🖥️ Instalação (Windows)

Siga os passos abaixo para configurar o ambiente no Windows:

### 1. Pré-requisitos

- Certifique-se de ter o **Python 3.10 ou superior** instalado.  
  Você pode baixá-lo em: https://www.python.org/downloads/

- Recomenda-se o uso do **Windows Terminal**, **PowerShell** ou **Git Bash** para executar os comandos.

---

### 2. Criar e configurar o ambiente

```bash
# Crie uma pasta para o projeto (opcional)
mkdir PaperGeneratorAI
cd PaperGeneratorAI

# Crie um ambiente virtual
python -m venv .venv

# Ative o ambiente virtual
.venv\Scripts\activate


Agora vamos criar um arquivo “.env” com as API Keys. Abrir um editor de notas (gedit) e escrever (substitua as api key pelas keys geradas nos itens A e B):

```bash
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Salvar e fechar.

Agora vamos testar a instalação. Crie um arquivo test_setup.py com o seguinte código:

```python
from crewai import Agent, Task, Crew

print("Instalação do CrewAI bem-sucedida!")
```

Para rodar o script, lembre-se que o ambiente **.venv** do python deve estar ativado no terminal  (na frente do seu nome do usuário deve aparecer .venv). Caso estejas em um terminal novo, com o ambiente desativado, execute o comando primeiramente:

```bash
source .venv/bin/activate
```

Então para rodar o script execute:

```bash
python3 test_setup.py
```

Se apareceu “Instalação do CrewAI bem-sucedida!” no terminal, a instalação está correta. Podes apagar o arquivo test_setup.py.


#2 - Estruturação do Projeto - Resposta da IA Generativa

Seguindo os passos contidos no chat "Passos  e passo 1" me explique como fazer o passo 2 Estruturação do Projeto

Editar

Vejo que você está trabalhando em um projeto de sistema multiagentes usando CrewAI para gerar artigos com base em informações da Wikipedia. Vamos focar na estruturação do projeto (passo 2).

## Estruturação do Projeto para Sistema Multiagentes com CrewAI

A estruturação adequada do projeto é fundamental para garantir organização, manutenibilidade e escalabilidade. Aqui está como você pode estruturar o projeto:

## Estrutura de Diretórios

```

article-generator-crewai/
├── .env                    # Arquivo para variáveis de ambiente (API keys)
├── .gitignore              # Arquivos a serem ignorados pelo git
├── README.md               # Documentação do projeto
├── requirements.txt        # Dependências do projeto
├── main.py                 # Ponto de entrada da aplicação
├── api/                    # Código relacionado à API
│   ├── __init__.py
│   ├── routes.py           # Rotas da API
│   └── models.py           # Modelos Pydantic para validação e resposta
├── agents/                 # Definição dos agentes
│   ├── __init__.py
│   ├── researcher.py       # Agente responsável pela pesquisa
│   └── writer.py           # Agente responsável pela escrita
├── tools/                  # Ferramentas personalizadas
│   ├── __init__.py
│   └── wikipedia_tool.py   # Ferramenta para consultar a API da Wikipedia
└── tests/                  # Testes unitários e de integração
    ├── __init__.py
    ├── test_agents.py
    ├── test_tools.py
    └── test_api.py

```

## Descrição dos Componentes

### 1. Arquivos de Configuração

- **`.env`**: Armazena variáveis de ambiente como chaves de API para LLMs (Groq, Gemini)
- **`.gitignore`**: Lista arquivos que não devem ser versionados (como o .env, **pycache**, etc.)
- **`requirements.txt`**: Lista as dependências do projeto

### 2. Documentação

- **`README.md`**: Contém instruções de instalação, uso e descrição do projeto

### 3. Código-fonte

### Ponto de Entrada

- **`main.py`**: Inicia a aplicação, configura o servidor API e chama os módulos necessários

### API

- **`api/routes.py`**: Define os endpoints da API
- **`api/models.py`**: Define os modelos Pydantic para validar entradas e formatar saídas

### Agentes

- **`agents/researcher.py`**: Define o agente responsável por pesquisar informações
- **`agents/writer.py`**: Define o agente responsável por escrever o artigo

### Ferramentas

- **`tools/wikipedia_tool.py`**: Implementa a ferramenta para consultar a API da Wikipedia

### 4. Testes

- Testes unitários e de integração para verificar o funcionamento dos componentes

## Implementação Base

Vejamos como implementar os arquivos principais:

### requirements.txt

```

crewai>=0.28.0
crewai-tools>=0.1.0
pydantic>=2.0.0
fastapi>=0.95.0
uvicorn>=0.22.0
python-dotenv>=1.0.0
wikipedia-api>=0.5.0
groq>=0.4.0  # Cliente para a API do Groq
google-generativeai>=0.3.0  # Cliente para o Gemini

```

### main.py

```python

python
import os
from dotenv import load_dotenv
import uvicorn
from api.routes import app
from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent
from crewai import Crew, Task
from tools.wikipedia_tool import WikipediaTool

# Carrega variáveis de ambiente
load_dotenv()

def create_crew(topic):
    """
    Cria uma crew com os agentes necessários para gerar um artigo

    Args:
        topic (str): Tópico do artigo a ser gerado

    Returns:
        dict: Artigo gerado em formato de dicionário
    """
# Inicializa as ferramentas
    wikipedia_tool = WikipediaTool()

# Inicializa os agentes
    researcher = ResearcherAgent().create_agent(tools=[wikipedia_tool])
    writer = WriterAgent().create_agent()

# Define as tarefas
    research_task = Task(
        description=f"Pesquise informações detalhadas sobre {topic}",
        agent=researcher,
        expected_output="Informações detalhadas sobre o tópico em formato JSON"
    )

    writing_task = Task(
        description=f"Escreva um artigo de pelo menos 300 palavras sobre {topic} usando as informações pesquisadas",
        agent=writer,
        expected_output="Artigo completo com título, introdução, desenvolvimento e conclusão",
        context=[research_task]
    )

# Cria a crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        verbose=True
    )

# Executa a crew
    result = crew.kickoff()

    return result

if __name__ == "__main__":
# Inicia o servidor FastAPI
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

```

### api/routes.py

```python

python
from fastapi import FastAPI, HTTPException
from api.models import ArticleRequest, ArticleResponse
from main import create_crew

app = FastAPI(
    title="Article Generator API",
    description="API para geração de artigos usando CrewAI",
    version="1.0.0"
)

@app.post("/generate-article/", response_model=ArticleResponse)
async def generate_article(request: ArticleRequest):
    """
    Endpoint para gerar um artigo sobre um tópico específico
    """
    try:
        result = create_crew(request.topic)

# Formata a resposta usando o modelo Pydantic
        response = ArticleResponse(
            topic=request.topic,
            title=result.get("title", f"Artigo sobre {request.topic}"),
            content=result.get("content", ""),
            word_count=len(result.get("content", "").split()),
            references=result.get("references", [])
        )

        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health/")
async def health_check():
    """
    Endpoint para verificar a saúde da API
    """
    return {"status": "healthy"}

```

### api/models.py

```python

python
from pydantic import BaseModel, Field
from typing import List

class ArticleRequest(BaseModel):
    """
    Modelo para a requisição de geração de artigo
    """
    topic: str = Field(..., description="Tópico sobre o qual o artigo será gerado")
    min_words: int = Field(300, description="Número mínimo de palavras do artigo")

class ArticleResponse(BaseModel):
    """
    Modelo para a resposta da geração de artigo
    """
    topic: str = Field(..., description="Tópico do artigo")
    title: str = Field(..., description="Título do artigo")
    content: str = Field(..., description="Conteúdo do artigo")
    word_count: int = Field(..., description="Contagem de palavras do artigo")
    references: List[str] = Field(default=[], description="Referências utilizadas no artigo")

```

### agents/researcher.py

```python

python
from crewai import Agent
from tools.wikipedia_tool import WikipediaTool
import os

class ResearcherAgent:
    """
    Agente responsável por pesquisar informações para o artigo
    """

    def create_agent(self, tools=None):
        """
        Cria um agente pesquisador

        Args:
            tools (list): Lista de ferramentas disponíveis para o agente

        Returns:
            Agent: Instância do agente pesquisador
        """
        return Agent(
            role="Pesquisador Especialista",
            goal="Encontrar informações detalhadas e precisas sobre o tópico solicitado",
            backstory="""Você é um pesquisador meticuloso que sabe como encontrar
            as informações mais relevantes e confiáveis sobre qualquer assunto.
            Você tem uma vasta experiência em coletar dados de diversas fontes
            e organizar informações de maneira coerente.""",
            verbose=True,
            allow_delegation=False,
            tools=tools or [],
            llm=self._get_llm()
        )

    def _get_llm(self):
        """
        Configura o modelo de linguagem para o agente

        Returns:
            LLM: Instância do modelo de linguagem
        """
        llm_provider = os.getenv("LLM_PROVIDER", "groq").lower()

        if llm_provider == "groq":
            from langchain_groq import ChatGroq
            return ChatGroq(
                api_key=os.getenv("GROQ_API_KEY"),
                model_name="llama3-70b-8192"
            )
        elif llm_provider == "gemini":
            from langchain_google_genai import ChatGoogleGenerativeAI
            return ChatGoogleGenerativeAI(
                api_key=os.getenv("GEMINI_API_KEY"),
                model="gemini-pro"
            )
        else:
            raise ValueError(f"Provedor LLM não suportado: {llm_provider}")

```

### agents/writer.py

```python

python
from crewai import Agent
import os

class WriterAgent:
    """
    Agente responsável por escrever o artigo
    """

    def create_agent(self):
        """
        Cria um agente escritor

        Returns:
            Agent: Instância do agente escritor
        """
        return Agent(
            role="Escritor de Conteúdo",
            goal="Escrever artigos informativos e envolventes com base nas pesquisas fornecidas",
            backstory="""Você é um escritor talentoso com experiência em criar
            conteúdos informativos e bem estruturados. Você sabe como
            transformar informações brutas em artigos coesos e interessantes
            que prendem a atenção do leitor do início ao fim.""",
            verbose=True,
            allow_delegation=False,
            llm=self._get_llm()
        )

    def _get_llm(self):
        """
        Configura o modelo de linguagem para o agente

        Returns:
            LLM: Instância do modelo de linguagem
        """
        llm_provider = os.getenv("LLM_PROVIDER", "groq").lower()

        if llm_provider == "groq":
            from langchain_groq import ChatGroq
            return ChatGroq(
                api_key=os.getenv("GROQ_API_KEY"),
                model_name="llama3-70b-8192"
            )
        elif llm_provider == "gemini":
            from langchain_google_genai import ChatGoogleGenerativeAI
            return ChatGoogleGenerativeAI(
                api_key=os.getenv("GEMINI_API_KEY"),
                model="gemini-pro"
            )
        else:
            raise ValueError(f"Provedor LLM não suportado: {llm_provider}")

```

### tools/wikipedia_tool.py

```python

python
from crewai_tools import BaseTool
import requests
import json

class WikipediaTool(BaseTool):
    """
    Ferramenta para consultar a API da Wikipedia
    """

    name = "Wikipedia Tool"
    description = "Ferramenta para consultar informações na Wikipedia"

    def _run(self, topic: str) -> str:
        """
        Consulta a API da Wikipedia para obter informações sobre um tópico

        Args:
            topic (str): Tópico a ser pesquisado

        Returns:
            str: Conteúdo extraído da Wikipedia sobre o tópico
        """
        url = "https://pt.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "prop": "extracts",
            "exlimit": "1",
            "explaintext": "1",
            "titles": topic,
            "format": "json",
            "utf8": "1",
            "redirects": "1"
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()
            pages = data["query"]["pages"]

# O ID da página é desconhecido, então pegamos a primeira
            page_id = list(pages.keys())[0]

            if page_id == "-1":
                return f"Nenhuma informação encontrada sobre '{topic}' na Wikipedia."

            extract = pages[page_id]["extract"]
            title = pages[page_id]["title"]

            result = {
                "title": title,
                "content": extract,
                "source": f"https://pt.wikipedia.org/wiki/{title.replace(' ', '_')}"
            }

            return json.dumps(result, ensure_ascii=False)

        except Exception as e:
            return f"Erro ao consultar a Wikipedia: {str(e)}"

```

### .gitignore

```

# Ambiente virtual
venv/
env/
.env

# Cache Python
__pycache__/
*.py[cod]
*$py.class
.pytest_cache/

# Logs
*.log

# IDEs e editores
.vscode/
.idea/
*.swp
*.swo

# Arquivos temporários
tmp/
temp/

# Arquivos de sistema
.DS_Store
Thumbs.db

```

### README.md

```markdown

markdown
# Sistema Multiagentes para Geração de Artigos

Este projeto utiliza o framework CrewAI para criar um sistema multiagentes que gera artigos com base em informações extraídas da Wikipedia.

## Funcionalidades

- Geração automatizada de artigos com pelo menos 300 palavras
- Pesquisa de informações na Wikipedia
- API para interação com o sistema
- Formatação estruturada do resultado usando Pydantic

## Tecnologias Utilizadas

- Python 3.9+
- CrewAI
- Crewai-tools
- FastAPI
- Pydantic
- API da Wikipedia

## Instalação

1. Clone o repositório:

```

git clone https://github.com/seu-usuario/article-generator-crewai.git
cd article-generator-crewai

```

2. Crie um ambiente virtual e ative-o:

```

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

```

3. Instale as dependências:

```

pip install -r requirements.txt

```

4. Crie um arquivo `.env` na raiz do projeto com suas chaves de API:

```

LLM_PROVIDER=groq  # ou gemini
GROQ_API_KEY=sua_chave_api_groq
GEMINI_API_KEY=sua_chave_api_gemini

```

## Uso

1. Inicie o servidor API:

```

python main.py

```

2. Acesse a documentação da API em `http://localhost:8000/docs`

3. Use o endpoint `/generate-article/` para gerar um artigo:
```json
{
  "topic": "Inteligência Artificial",
  "min_words": 300
}

```

## Estrutura do Projeto

- `main.py`: Ponto de entrada da aplicação
- `api/`: Código relacionado à API
- `agents/`: Definição dos agentes
- `tools/`: Ferramentas personalizadas

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

```

## Próximos Passos

Após estruturar o projeto conforme mostrado acima, você pode prosseguir para:

1. Implementar a lógica dos agentes com engenharia de prompts adequada
2. Desenvolver a ferramenta personalizada para interagir com a API da Wikipedia
3. Configurar a saída formatada com Pydantic
4. Implementar a API usando FastAPI
5. Testar o sistema e refinar conforme necessário

Esta estrutura fornece uma base sólida para o desenvolvimento do seu sistema multiagentes conforme os requisitos especificados.

```


#Desenvolvimento da ferramenta personalizada para a Wikipedia - Resposta da IA Generativa 

Seguindo os passos contidos no chat "Passos  e passo 1" me explique como fazer o passo 3 - Desenvolvimento da ferramenta personalizada para a Wikipedia

Editar

Vou explicar como desenvolver uma ferramenta personalizada para consultar a API da Wikipedia usando CrewAI, conforme solicitado para o passo 3 do seu projeto.

# Desenvolvimento da Ferramenta Personalizada para a Wikipedia

Para criar uma ferramenta personalizada no CrewAI que consulte a API da Wikipedia, precisamos criar uma classe que estenda a classe base `Tool` do pacote `crewai.tools`. Esta ferramenta permitirá que os agentes busquem informações na Wikipedia para gerar os artigos.

Vamos desenvolver essa ferramenta passo a passo:

## 1. Estrutura Básica da Ferramenta

Primeiro, vamos criar um arquivo chamado `wikipedia_tool.py` com a estrutura básica da nossa ferramenta:

```python

python
from crewai.tools import BaseTool
import requests
from typing import Optional

class WikipediaTool(BaseTool):
    """Ferramenta para buscar informações na API da Wikipedia."""

    name: str = "Wikipedia Tool"
    description: str = "Busca informações sobre um assunto específico na Wikipedia."

    def _run(self, query: str, language: Optional[str] = "pt") -> str:
        """
        Executa a busca na API da Wikipedia.

        Args:
            query (str): Termo de busca na Wikipedia.
            language (Optional[str]): Idioma da Wikipedia (padrão: "pt" para português).

        Returns:
            str: Texto extraído da Wikipedia ou mensagem de erro.
        """
        try:
# Implementação da consulta à API da Wikipedia
            return self._search_wikipedia(query, language)
        except Exception as e:
            return f"Erro ao buscar informações na Wikipedia: {str(e)}"

    def _search_wikipedia(self, query: str, language: str) -> str:
        """
        Realiza a consulta à API da Wikipedia.

        Args:
            query (str): Termo de busca.
            language (str): Idioma da Wikipedia.

        Returns:
            str: Conteúdo extraído do artigo.
        """
# Implementação da consulta à API
        pass

```

## 2. Implementação da Consulta à API da Wikipedia

Agora, vamos implementar o método `_search_wikipedia` para realizar a consulta à API da Wikipedia:

```python

python
def _search_wikipedia(self, query: str, language: str) -> str:
    """
    Realiza a consulta à API da Wikipedia.

    Args:
        query (str): Termo de busca.
        language (str): Idioma da Wikipedia.

    Returns:
        str: Conteúdo extraído do artigo.
    """
# URL base da API da Wikipedia
    base_url = f"https://{language}.wikipedia.org/w/api.php"

# Primeiro, realizar uma busca para encontrar o título exato
    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "utf8": 1,
    }

    search_response = requests.get(base_url, params=search_params)
    search_data = search_response.json()

# Verificar se encontrou resultados
    if "query" not in search_data or "search" not in search_data["query"] or len(search_data["query"]["search"]) == 0:
        return f"Nenhum artigo encontrado para '{query}'."

# Pegar o título do primeiro resultado
    page_title = search_data["query"]["search"][0]["title"]

# Agora, buscar o conteúdo do artigo
    content_params = {
        "action": "query",
        "prop": "extracts",
        "exlimit": 1,
        "explaintext": 1,
        "titles": page_title,
        "format": "json",
        "utf8": 1,
        "redirects": 1,
    }

    content_response = requests.get(base_url, params=content_params)
    content_data = content_response.json()

# Extrair o conteúdo
    pages = content_data["query"]["pages"]
    page_id = list(pages.keys())[0]

    if page_id == "-1":
        return f"Não foi possível encontrar o conteúdo para '{page_title}'."

    content = pages[page_id].get("extract", "")

    if not content:
        return f"O artigo '{page_title}' não possui conteúdo."

# Limitar o tamanho do conteúdo se for muito grande
    max_chars = 8000# Defina um limite razoável
    if len(content) > max_chars:
        content = content[:max_chars] + "...\n\n(Conteúdo truncado devido ao tamanho)"

    return f"Título: {page_title}\n\n{content}"

```

## 3. Adição de Métodos Auxiliares

Podemos adicionar outros métodos úteis à nossa ferramenta, como buscar resumos curtos ou listar artigos relacionados:

```python

python
def get_summary(self, query: str, language: str = "pt", max_sentences: int = 3) -> str:
    """
    Obtém um resumo curto sobre o tópico.

    Args:
        query (str): Termo de busca.
        language (str): Idioma da Wikipedia.
        max_sentences (int): Número máximo de sentenças no resumo.

    Returns:
        str: Resumo do artigo.
    """
    full_content = self._search_wikipedia(query, language)

# Extrair apenas o título e as primeiras sentenças do conteúdo
    parts = full_content.split("\n\n", 1)
    if len(parts) < 2:
        return full_content

    title = parts[0]
    content = parts[1]

# Extrair as primeiras sentenças
    sentences = content.split(". ")[:max_sentences]
    summary = ". ".join(sentences)
    if not summary.endswith("."):
        summary += "."

    return f"{title}\n\n{summary}"

def get_related_topics(self, query: str, language: str = "pt", limit: int = 5) -> str:
    """
    Obtém tópicos relacionados ao termo de busca.

    Args:
        query (str): Termo de busca.
        language (str): Idioma da Wikipedia.
        limit (int): Número máximo de tópicos relacionados.

    Returns:
        str: Lista de tópicos relacionados.
    """
    base_url = f"https://{language}.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "utf8": 1,
        "srlimit": limit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if "query" not in data or "search" not in data["query"]:
        return f"Nenhum tópico relacionado encontrado para '{query}'."

    topics = data["query"]["search"]
    result = f"Tópicos relacionados a '{query}':\n\n"

    for i, topic in enumerate(topics, 1):
        result += f"{i}. {topic['title']}\n"

    return result

```

## 4. Implementação Completa da Ferramenta

Juntando tudo, nossa ferramenta completa ficará assim:

```python

python
from crewai.tools import BaseTool
import requests
from typing import Optional
import textwrap

class WikipediaTool(BaseTool):
    """Ferramenta para buscar informações na API da Wikipedia."""

    name: str = "Wikipedia Tool"
    description: str = "Busca informações sobre um assunto específico na Wikipedia."

    def _run(self, query: str, language: Optional[str] = "pt") -> str:
        """
        Executa a busca na API da Wikipedia.

        Args:
            query (str): Termo de busca na Wikipedia.
            language (Optional[str]): Idioma da Wikipedia (padrão: "pt" para português).

        Returns:
            str: Texto extraído da Wikipedia ou mensagem de erro.
        """
        try:
# Implementação da consulta à API da Wikipedia
            return self._search_wikipedia(query, language)
        except Exception as e:
            return f"Erro ao buscar informações na Wikipedia: {str(e)}"

    def _search_wikipedia(self, query: str, language: str) -> str:
        """
        Realiza a consulta à API da Wikipedia.

        Args:
            query (str): Termo de busca.
            language (str): Idioma da Wikipedia.

        Returns:
            str: Conteúdo extraído do artigo.
        """
# URL base da API da Wikipedia
        base_url = f"https://{language}.wikipedia.org/w/api.php"

# Primeiro, realizar uma busca para encontrar o título exato
        search_params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
            "utf8": 1,
        }

        search_response = requests.get(base_url, params=search_params)
        search_data = search_response.json()

# Verificar se encontrou resultados
        if "query" not in search_data or "search" not in search_data["query"] or len(search_data["query"]["search"]) == 0:
            return f"Nenhum artigo encontrado para '{query}'."

# Pegar o título do primeiro resultado
        page_title = search_data["query"]["search"][0]["title"]

# Agora, buscar o conteúdo do artigo
        content_params = {
            "action": "query",
            "prop": "extracts",
            "exlimit": 1,
            "explaintext": 1,
            "titles": page_title,
            "format": "json",
            "utf8": 1,
            "redirects": 1,
        }

        content_response = requests.get(base_url, params=content_params)
        content_data = content_response.json()

# Extrair o conteúdo
        pages = content_data["query"]["pages"]
        page_id = list(pages.keys())[0]

        if page_id == "-1":
            return f"Não foi possível encontrar o conteúdo para '{page_title}'."

        content = pages[page_id].get("extract", "")

        if not content:
            return f"O artigo '{page_title}' não possui conteúdo."

# Limitar o tamanho do conteúdo se for muito grande
        max_chars = 8000# Defina um limite razoável
        if len(content) > max_chars:
            content = content[:max_chars] + "...\n\n(Conteúdo truncado devido ao tamanho)"

        return f"Título: {page_title}\n\n{content}"

    def get_summary(self, query: str, language: str = "pt", max_sentences: int = 3) -> str:
        """
        Obtém um resumo curto sobre o tópico.

        Args:
            query (str): Termo de busca.
            language (str): Idioma da Wikipedia.
            max_sentences (int): Número máximo de sentenças no resumo.

        Returns:
            str: Resumo do artigo.
        """
        full_content = self._search_wikipedia(query, language)

# Extrair apenas o título e as primeiras sentenças do conteúdo
        parts = full_content.split("\n\n", 1)
        if len(parts) < 2:
            return full_content

        title = parts[0]
        content = parts[1]

# Extrair as primeiras sentenças
        sentences = content.split(". ")[:max_sentences]
        summary = ". ".join(sentences)
        if not summary.endswith("."):
            summary += "."

        return f"{title}\n\n{summary}"

    def get_related_topics(self, query: str, language: str = "pt", limit: int = 5) -> str:
        """
        Obtém tópicos relacionados ao termo de busca.

        Args:
            query (str): Termo de busca.
            language (str): Idioma da Wikipedia.
            limit (int): Número máximo de tópicos relacionados.

        Returns:
            str: Lista de tópicos relacionados.
        """
        base_url = f"https://{language}.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
            "utf8": 1,
            "srlimit": limit
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if "query" not in data or "search" not in data["query"]:
            return f"Nenhum tópico relacionado encontrado para '{query}'."

        topics = data["query"]["search"]
        result = f"Tópicos relacionados a '{query}':\n\n"

        for i, topic in enumerate(topics, 1):
            result += f"{i}. {topic['title']}\n"

        return result

```

## 5. Como Usar a Ferramenta com os Agentes no CrewAI

Agora que temos nossa ferramenta personalizada, vamos ver como integrá-la ao CrewAI:

```python

python
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq# ou outro provedor de LLM
from wikipedia_tool import WikipediaTool

# Criar a instância da ferramenta
wikipedia_tool = WikipediaTool()

# Configurar o modelo de LLM (exemplo com Groq)
llm = ChatGroq(
    api_key="sua_api_key_aqui",
    model_name="gemini-pro"# ou outro modelo suportado
)

# Criar o agente de pesquisa
research_agent = Agent(
    role="Pesquisador",
    goal="Pesquisar informações detalhadas sobre o assunto solicitado",
    backstory="Especialista em encontrar informações relevantes e precisas sobre qualquer assunto",
    tools=[wikipedia_tool],
    llm=llm,
    verbose=True
)

# Criar o agente escritor
writer_agent = Agent(
    role="Redator",
    goal="Escrever artigos informativos e atraentes com base nas pesquisas",
    backstory="Redator experiente especializado em criar conteúdo atraente e informativo",
    tools=[],# O escritor não precisa de ferramentas diretamente
    llm=llm,
    verbose=True
)

# Criar tarefa para o pesquisador
research_task = Task(
    description="Pesquisar informações detalhadas sobre {topic} usando a Wikipedia. Obtenha dados suficientes para um artigo de pelo menos 300 palavras.",
    expected_output="Informações detalhadas sobre o assunto, incluindo dados históricos, conceitos e fatos relevantes.",
    agent=research_agent
)

# Criar tarefa para o escritor
writing_task = Task(
    description="Escrever um artigo informativo de pelo menos 300 palavras sobre {topic} usando as informações fornecidas pelo pesquisador.",
    expected_output="Um artigo bem estruturado com pelo menos 300 palavras, incluindo introdução, desenvolvimento e conclusão.",
    agent=writer_agent,
    context=[research_task]# O contexto permite que o escritor acesse o resultado da pesquisa
)

# Criar e executar a crew
crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, writing_task],
    verbose=2
)

# Executar a crew para um tópico específico
result = crew.kickoff(inputs={"topic": "Inteligência Artificial"})
print(result)

```

## 6. Adaptações para Melhorar a Ferramenta

Você pode adicionar estas melhorias à sua ferramenta para torná-la ainda mais útil:

1. **Busca em múltiplos idiomas**:

```python

python
def search_in_multiple_languages(self, query: str, languages: list = ["pt", "en", "es"]) -> str:
    """Busca o mesmo tema em vários idiomas e combina os resultados."""
    results = []
    for lang in languages:
        result = self._search_wikipedia(query, lang)
        results.append(f"Resultados em {lang}:\n{result}\n")
    return "\n".join(results)

```

1. **Busca de imagens relacionadas**:

```python

python
def get_image_urls(self, query: str, language: str = "pt", limit: int = 3) -> str:
    """Obtém URLs de imagens relacionadas ao tema."""
# Implementação para buscar imagens# (Nota: Requer tratamento adicional para obter URLs de imagens)
    pass

```

## Considerações Finais:

Seguindo os passos contidos no chat "Passos  e passo 1" me explique como fazer o passo 3 - Desenvolvimento da ferramenta personalizada para a Wikipedia

Editar

Vou explicar como desenvolver uma ferramenta personalizada para consultar a API da Wikipedia usando CrewAI, conforme solicitado para o passo 3 do seu projeto.

Desenvolvimento da Ferramenta Personalizada para a Wikipedia

Para criar uma ferramenta personalizada no CrewAI que consulte a API da Wikipedia, precisamos criar uma classe que estenda a classe base `Tool` do pacote `crewai.tools`. Esta ferramenta permitirá que os agentes busquem informações na Wikipedia para gerar os artigos.

Vamos desenvolver essa ferramenta passo a passo:

## 1. Estrutura Básica da Ferramenta

Primeiro, vamos criar um arquivo chamado `wikipedia_tool.py` com a estrutura básica da nossa ferramenta:

```python

python
from crewai.tools import BaseTool
import requests
from typing import Optional

class WikipediaTool(BaseTool):
    """Ferramenta para buscar informações na API da Wikipedia."""

    name: str = "Wikipedia Tool"
    description: str = "Busca informações sobre um assunto específico na Wikipedia."

    def _run(self, query: str, language: Optional[str] = "pt") -> str:
        """
        Executa a busca na API da Wikipedia.

        Args:
            query (str): Termo de busca na Wikipedia.
            language (Optional[str]): Idioma da Wikipedia (padrão: "pt" para português).

        Returns:
            str: Texto extraído da Wikipedia ou mensagem de erro.
        """
        try:
# Implementação da consulta à API da Wikipedia
            return self._search_wikipedia(query, language)
        except Exception as e:
            return f"Erro ao buscar informações na Wikipedia: {str(e)}"

    def _search_wikipedia(self, query: str, language: str) -> str:
        """
        Realiza a consulta à API da Wikipedia.

        Args:
            query (str): Termo de busca.
            language (str): Idioma da Wikipedia.

        Returns:
            str: Conteúdo extraído do artigo.
        """
# Implementação da consulta à API
        pass

```

## 3. Adição de Métodos Auxiliares

Podemos adicionar outros métodos úteis à nossa ferramenta, como buscar resumos curtos ou listar artigos relacionados:

```python

python
def get_summary(self, query: str, language: str = "pt", max_sentences: int = 3) -> str:
    """
    Obtém um resumo curto sobre o tópico.

    Args:
        query (str): Termo de busca.
        language (str): Idioma da Wikipedia.
        max_sentences (int): Número máximo de sentenças no resumo.

    Returns:
        str: Resumo do artigo.
    """
    full_content = self._search_wikipedia(query, language)

# Extrair apenas o título e as primeiras sentenças do conteúdo
    parts = full_content.split("\n\n", 1)
    if len(parts) < 2:
        return full_content

    title = parts[0]
    content = parts[1]

# Extrair as primeiras sentenças
    sentences = content.split(". ")[:max_sentences]
    summary = ". ".join(sentences)
    if not summary.endswith("."):
        summary += "."

    return f"{title}\n\n{summary}"

def get_related_topics(self, query: str, language: str = "pt", limit: int = 5) -> str:
    """
    Obtém tópicos relacionados ao termo de busca.

    Args:
        query (str): Termo de busca.
        language (str): Idioma da Wikipedia.
        limit (int): Número máximo de tópicos relacionados.

    Returns:
        str: Lista de tópicos relacionados.
    """
    base_url = f"https://{language}.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "utf8": 1,
        "srlimit": limit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if "query" not in data or "search" not in data["query"]:
        return f"Nenhum tópico relacionado encontrado para '{query}'."

    topics = data["query"]["search"]
    result = f"Tópicos relacionados a '{query}':\n\n"

    for i, topic in enumerate(topics, 1):
        result += f"{i}. {topic['title']}\n"

    return result

```

## 4. Implementação Completa da Ferramenta

Juntando tudo, nossa ferramenta completa ficará assim:

```python

python
from crewai.tools import BaseTool
import requests
from typing import Optional
import textwrap

class WikipediaTool(BaseTool):
    """Ferramenta para buscar informações na API da Wikipedia."""

    name: str = "Wikipedia Tool"
    description: str = "Busca informações sobre um assunto específico na Wikipedia."

    def _run(self, query: str, language: Optional[str] = "pt") -> str:
        """
        Executa a busca na API da Wikipedia.

        Args:
            query (str): Termo de busca na Wikipedia.
            language (Optional[str]): Idioma da Wikipedia (padrão: "pt" para português).

        Returns:
            str: Texto extraído da Wikipedia ou mensagem de erro.
        """
        try:
# Implementação da consulta à API da Wikipedia
            return self._search_wikipedia(query, language)
        except Exception as e:
            return f"Erro ao buscar informações na Wikipedia: {str(e)}"

    def _search_wikipedia(self, query: str, language: str) -> str:
        """
        Realiza a consulta à API da Wikipedia.

        Args:
            query (str): Termo de busca.
            language (str): Idioma da Wikipedia.

        Returns:
            str: Conteúdo extraído do artigo.
        """
# URL base da API da Wikipedia
        base_url = f"https://{language}.wikipedia.org/w/api.php"

# Primeiro, realizar uma busca para encontrar o título exato
        search_params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
            "utf8": 1,
        }

        search_response = requests.get(base_url, params=search_params)
        search_data = search_response.json()

# Verificar se encontrou resultados
        if "query" not in search_data or "search" not in search_data["query"] or len(search_data["query"]["search"]) == 0:
            return f"Nenhum artigo encontrado para '{query}'."

# Pegar o título do primeiro resultado
        page_title = search_data["query"]["search"][0]["title"]

# Agora, buscar o conteúdo do artigo
        content_params = {
            "action": "query",
            "prop": "extracts",
            "exlimit": 1,
            "explaintext": 1,
            "titles": page_title,
            "format": "json",
            "utf8": 1,
            "redirects": 1,
        }

        content_response = requests.get(base_url, params=content_params)
        content_data = content_response.json()

# Extrair o conteúdo
        pages = content_data["query"]["pages"]
        page_id = list(pages.keys())[0]

        if page_id == "-1":
            return f"Não foi possível encontrar o conteúdo para '{page_title}'."

        content = pages[page_id].get("extract", "")

        if not content:
            return f"O artigo '{page_title}' não possui conteúdo."

# Limitar o tamanho do conteúdo se for muito grande
        max_chars = 8000# Defina um limite razoável
        if len(content) > max_chars:
            content = content[:max_chars] + "...\n\n(Conteúdo truncado devido ao tamanho)"

        return f"Título: {page_title}\n\n{content}"

    def get_summary(self, query: str, language: str = "pt", max_sentences: int = 3) -> str:
        """
        Obtém um resumo curto sobre o tópico.

        Args:
            query (str): Termo de busca.
            language (str): Idioma da Wikipedia.
            max_sentences (int): Número máximo de sentenças no resumo.

        Returns:
            str: Resumo do artigo.
        """
        full_content = self._search_wikipedia(query, language)

# Extrair apenas o título e as primeiras sentenças do conteúdo
        parts = full_content.split("\n\n", 1)
        if len(parts) < 2:
            return full_content

        title = parts[0]
        content = parts[1]

# Extrair as primeiras sentenças
        sentences = content.split(". ")[:max_sentences]
        summary = ". ".join(sentences)
        if not summary.endswith("."):
            summary += "."

        return f"{title}\n\n{summary}"

    def get_related_topics(self, query: str, language: str = "pt", limit: int = 5) -> str:
        """
        Obtém tópicos relacionados ao termo de busca.

        Args:
            query (str): Termo de busca.
            language (str): Idioma da Wikipedia.
            limit (int): Número máximo de tópicos relacionados.

        Returns:
            str: Lista de tópicos relacionados.
        """
        base_url = f"https://{language}.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
            "utf8": 1,
            "srlimit": limit
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if "query" not in data or "search" not in data["query"]:
            return f"Nenhum tópico relacionado encontrado para '{query}'."

        topics = data["query"]["search"]
        result = f"Tópicos relacionados a '{query}':\n\n"

        for i, topic in enumerate(topics, 1):
            result += f"{i}. {topic['title']}\n"

        return result

```

## 5. Como Usar a Ferramenta com os Agentes no CrewAI

Agora que temos nossa ferramenta personalizada, vamos ver como integrá-la ao CrewAI:

```python

python
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq# ou outro provedor de LLM
from wikipedia_tool import WikipediaTool

# Criar a instância da ferramenta
wikipedia_tool = WikipediaTool()

# Configurar o modelo de LLM (exemplo com Groq)
llm = ChatGroq(
    api_key="sua_api_key_aqui",
    model_name="gemini-pro"# ou outro modelo suportado
)

# Criar o agente de pesquisa
research_agent = Agent(
    role="Pesquisador",
    goal="Pesquisar informações detalhadas sobre o assunto solicitado",
    backstory="Especialista em encontrar informações relevantes e precisas sobre qualquer assunto",
    tools=[wikipedia_tool],
    llm=llm,
    verbose=True
)

# Criar o agente escritor
writer_agent = Agent(
    role="Redator",
    goal="Escrever artigos informativos e atraentes com base nas pesquisas",
    backstory="Redator experiente especializado em criar conteúdo atraente e informativo",
    tools=[],# O escritor não precisa de ferramentas diretamente
    llm=llm,
    verbose=True
)

# Criar tarefa para o pesquisador
research_task = Task(
    description="Pesquisar informações detalhadas sobre {topic} usando a Wikipedia. Obtenha dados suficientes para um artigo de pelo menos 300 palavras.",
    expected_output="Informações detalhadas sobre o assunto, incluindo dados históricos, conceitos e fatos relevantes.",
    agent=research_agent
)

# Criar tarefa para o escritor
writing_task = Task(
    description="Escrever um artigo informativo de pelo menos 300 palavras sobre {topic} usando as informações fornecidas pelo pesquisador.",
    expected_output="Um artigo bem estruturado com pelo menos 300 palavras, incluindo introdução, desenvolvimento e conclusão.",
    agent=writer_agent,
    context=[research_task]# O contexto permite que o escritor acesse o resultado da pesquisa
)

# Criar e executar a crew
crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, writing_task],
    verbose=2
)

# Executar a crew para um tópico específico
result = crew.kickoff(inputs={"topic": "Inteligência Artificial"})
print(result)

```

## 5. Como Usar a Ferramenta com os Agentes no CrewAI

Agora que temos nossa ferramenta personalizada, vamos ver como integrá-la ao CrewAI:

```python

python
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq# ou outro provedor de LLM
from wikipedia_tool import WikipediaTool

# Criar a instância da ferramenta
wikipedia_tool = WikipediaTool()

# Configurar o modelo de LLM (exemplo com Groq)
llm = ChatGroq(
    api_key="sua_api_key_aqui",
    model_name="gemini-pro"# ou outro modelo suportado
)

# Criar o agente de pesquisa
research_agent = Agent(
    role="Pesquisador",
    goal="Pesquisar informações detalhadas sobre o assunto solicitado",
    backstory="Especialista em encontrar informações relevantes e precisas sobre qualquer assunto",
    tools=[wikipedia_tool],
    llm=llm,
    verbose=True
)

# Criar o agente escritor
writer_agent = Agent(
    role="Redator",
    goal="Escrever artigos informativos e atraentes com base nas pesquisas",
    backstory="Redator experiente especializado em criar conteúdo atraente e informativo",
    tools=[],# O escritor não precisa de ferramentas diretamente
    llm=llm,
    verbose=True
)

# Criar tarefa para o pesquisador
research_task = Task(
    description="Pesquisar informações detalhadas sobre {topic} usando a Wikipedia. Obtenha dados suficientes para um artigo de pelo menos 300 palavras.",
    expected_output="Informações detalhadas sobre o assunto, incluindo dados históricos, conceitos e fatos relevantes.",
    agent=research_agent
)

# Criar tarefa para o escritor
writing_task = Task(
    description="Escrever um artigo informativo de pelo menos 300 palavras sobre {topic} usando as informações fornecidas pelo pesquisador.",
    expected_output="Um artigo bem estruturado com pelo menos 300 palavras, incluindo introdução, desenvolvimento e conclusão.",
    agent=writer_agent,
    context=[research_task]# O contexto permite que o escritor acesse o resultado da pesquisa
)

# Criar e executar a crew
crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, writing_task],
    verbose=2
)

# Executar a crew para um tópico específico
result = crew.kickoff(inputs={"topic": "Inteligência Artificial"})
print(result)

```

## 6. Adaptações para Melhorar a Ferramenta

Você pode adicionar estas melhorias à sua ferramenta para torná-la ainda mais útil:

1. **Busca em múltiplos idiomas**:

```python

python
def search_in_multiple_languages(self, query: str, languages: list = ["pt", "en", "es"]) -> str:
    """Busca o mesmo tema em vários idiomas e combina os resultados."""
    results = []
    for lang in languages:
        result = self._search_wikipedia(query, lang)
        results.append(f"Resultados em {lang}:\n{result}\n")
    return "\n".join(results)

```

1. **Busca de imagens relacionadas**:

```python

python
def get_image_urls(self, query: str, language: str = "pt", limit: int = 3) -> str:
    """Obtém URLs de imagens relacionadas ao tema."""
# Implementação para buscar imagens# (Nota: Requer tratamento adicional para obter URLs de imagens)
    pass

```

## Considerações Finais:

1. **Tratamento de Erros**: A ferramenta deve lidar com casos como termos não encontrados, problemas de conexão, etc.
2. **Limitação de tamanho**: Os LLMs têm limites de contexto, então é importante truncar respostas muito grandes.
3. **Cache**: Para melhorar a performance, considere implementar cache para evitar consultas repetidas.
4. **Documentação**: Adicione docstrings detalhadas a todos os métodos para facilitar o uso.
5. **Testes**: Crie testes unitários para garantir que a ferramenta funcione corretamente.

Esta implementação da ferramenta da Wikipedia no CrewAI permite que seus agentes obtenham informações para gerar artigos completos sobre qualquer assunto disponível na Wikipedia, cumprindo assim um dos requisitos principais do projeto.

 4 - Definição e implementação dos agentes - Resposta da IA Generativa
Seguindo os passos contidos no chat "Passos  e passo 1" me explique como fazer o passo 4 - Definição e implementação dos agentes

Editar

Vou explicar como definir e implementar os agentes para o sistema multiagentes com CrewAI conforme solicitado no requisitos.pdf.

# Passo 4: Definição e implementação dos agentes

Na arquitetura CrewAI, os agentes são componentes fundamentais que realizam tarefas específicas. Para o sistema de geração de artigos usando informações da Wikipedia, precisaremos definir pelo menos dois agentes com funções distintas.

## Estrutura básica de um agente no CrewAI

Primeiro, vamos entender como se define um agente no framework CrewAI:

```python

python
from crewai import Agent

agent = Agent(
    role="Nome do papel",
    goal="Objetivo do agente",
    backstory="História/contexto do agente",
    verbose=True,
    allow_delegation=False,
    tools=[ferramenta1, ferramenta2],# Ferramentas que o agente pode usar
    llm=llm# Modelo de linguagem que o agente usará
)

```

## Implementação dos agentes necessários

Para este sistema, recomendo implementar os seguintes agentes:

### 1. Agente Pesquisador (Research Agent)

Este agente será responsável por buscar e compilar informações relevantes da Wikipedia usando a ferramenta personalizada que criamos:

```python

python
from crewai import Agent
from langchain.llms import Groq# Ou outro LLM de sua escolha# Configuração do LLM
llm = Groq(api_key="sua_chave_api")

research_agent = Agent(
    role="Pesquisador de Conteúdo",
    goal="Coletar informações detalhadas e precisas sobre o tópico solicitado da Wikipedia",
    backstory="Sou um especialista em pesquisa digital com habilidade para encontrar e organizar informações relevantes e confiáveis. Meu trabalho é fornecer dados precisos para criação de conteúdo.",
    verbose=True,
    allow_delegation=False,
    tools=[wikipedia_search_tool],# Ferramenta que criamos para consultar a Wikipedia
    llm=llm
)

```

### 2. Agente Redator (Writer Agent)

Este agente receberá as informações do Pesquisador e criará o artigo final:

```python

python
writer_agent = Agent(
    role="Redator de Artigos",
    goal="Criar artigos informativos, bem estruturados e envolventes com pelo menos 300 palavras",
    backstory="Sou um redator profissional especializado em transformar informações brutas em artigos coesos e interessantes. Tenho experiência em adaptar o tom e estilo para diferentes públicos.",
    verbose=True,
    allow_delegation=False,
    tools=[],# Este agente não precisa de ferramentas específicas
    llm=llm
)

```

### 3. Agente Editor (opcional, mas recomendado)

Para melhorar a qualidade do conteúdo, podemos adicionar um terceiro agente que revisará e aprimorará o texto:

```python

python
editor_agent = Agent(
    role="Editor de Conteúdo",
    goal="Revisar, corrigir e aprimorar artigos para garantir precisão, clareza e qualidade",
    backstory="Sou um editor meticuloso com olhar crítico para detalhes. Minha função é garantir que o conteúdo esteja correto, coeso e otimizado para o público-alvo.",
    verbose=True,
    allow_delegation=False,
    tools=[],# Este agente também não precisa de ferramentas específicas
    llm=llm
)

```

## Técnicas de engenharia de prompts

Para melhorar o desempenho dos agentes, podemos aplicar técnicas de engenharia de prompts nas configurações:

```python

python
# Exemplo com engenharia de prompts para o Writer Agent
writer_agent = Agent(
    role="Redator de Artigos",
    goal="Criar artigos informativos, bem estruturados e envolventes com pelo menos 300 palavras",
    backstory="Sou um redator profissional especializado em transformar informações brutas em artigos coesos e interessantes. Tenho experiência em adaptar o tom e estilo para diferentes públicos.",
    verbose=True,
    allow_delegation=False,
    tools=[],
    llm=llm,
# Engenharia de prompts para melhorar as saídas
    customized_prompt_template="""
    Você está escrevendo um artigo sobre {topic} para um website.

    Use as informações a seguir como base:
    {research_data}

    Diretrizes para redação:
    1. O artigo deve ter pelo menos 300 palavras
    2. Comece com uma introdução envolvente
    3. Organize o conteúdo em seções lógicas com subtítulos
    4. Inclua fatos relevantes e dados importantes
    5. Termine com uma conclusão que resuma os pontos principais
    6. Use tom informativo mas acessível
    7. Evite repetições e informações redundantes

    Formato do artigo:
    # Título

    ## Introdução
    [Conteúdo introdutório]

    ## [Subtítulo relevante]
    [Conteúdo]

    ## [Outro subtítulo relevante]
    [Conteúdo]

    ## Conclusão
    [Conclusão]

    Seu artigo:
    """
)

```

## Variações nos LLMs

Você pode utilizar diferentes LLMs para cada agente, aproveitando seus diferentes pontos fortes:

```python

python
# Exemplo usando Groq para pesquisa (bom em recuperação de informações)
from langchain.llms import Groq
groq_llm = Groq(api_key="sua_chave_api_groq")

# Exemplo usando Gemini para redação (potencialmente criativo)
from langchain.llms import Gemini
gemini_llm = Gemini(api_key="sua_chave_api_gemini")

# Configurando agentes com diferentes LLMs
research_agent = Agent(
# ... outros parâmetros ...
    llm=groq_llm
)

writer_agent = Agent(
# ... outros parâmetros ...
    llm=gemini_llm
)

```

## Implementação completa dos agentes

Aqui está um exemplo de como seria a implementação completa dos agentes em um arquivo Python:

```python

python
# agents.py
from crewai import Agent
from langchain.llms import Groq, Gemini
from tools.wikipedia_tool import WikipediaSearchTool

# Inicializar as ferramentas
wikipedia_tool = WikipediaSearchTool()

# Configurar os LLMs
groq_llm = Groq(api_key="sua_chave_api_groq")
gemini_llm = Gemini(api_key="sua_chave_api_gemini")

# Definir os agentes
def get_research_agent():
    return Agent(
        role="Pesquisador de Conteúdo",
        goal="Coletar informações detalhadas e precisas sobre o tópico solicitado da Wikipedia",
        backstory="Sou um especialista em pesquisa digital com habilidade para encontrar e organizar informações relevantes e confiáveis. Meu trabalho é fornecer dados precisos para criação de conteúdo.",
        verbose=True,
        allow_delegation=False,
        tools=[wikipedia_tool],
        llm=groq_llm
    )

def get_writer_agent():
    return Agent(
        role="Redator de Artigos",
        goal="Criar artigos informativos, bem estruturados e envolventes com pelo menos 300 palavras",
        backstory="Sou um redator profissional especializado em transformar informações brutas em artigos coesos e interessantes. Tenho experiência em adaptar o tom e estilo para diferentes públicos.",
        verbose=True,
        allow_delegation=False,
        tools=[],
        llm=gemini_llm
    )

def get_editor_agent():
    return Agent(
        role="Editor de Conteúdo",
        goal="Revisar, corrigir e aprimorar artigos para garantir precisão, clareza e qualidade",
        backstory="Sou um editor meticuloso com olhar crítico para detalhes. Minha função é garantir que o conteúdo esteja correto, coeso e otimizado para o público-alvo.",
        verbose=True,
        allow_delegation=False,
        tools=[],
        llm=groq_llm
    )

```

## Pontos importantes a considerar

1. **Personalização dos papéis**: Configure os agentes de acordo com as necessidades específicas do seu sistema.
2. **Seleção de LLM apropriado**: Os diferentes modelos têm diferentes pontos fortes. O Groq pode ser mais rápido, enquanto o Gemini pode ter outras capacidades.
3. **Ferramentas**: Apenas os agentes que precisam acessar recursos externos (como a Wikipedia) devem ter ferramentas atribuídas.
4. **Engenharia de prompts**: Personalize as instruções para cada agente para obter melhores resultados.
5. **Verbosidade**: O parâmetro `verbose=True` é útil durante o desenvolvimento para ver o raciocínio dos agentes, mas pode ser desativado em produção.


