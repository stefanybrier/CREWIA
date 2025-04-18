from crewai_tools.tools.base_tool import BaseTool
import requests


class WikipediaTool:
    name = "Wikipedia Tool"
    description = "Usa a Wikipedia para buscar informações sobre um tópico"

    def run(self, topic: str) -> str:
        """
        Executa a busca na Wikipedia

        Args:
            topic (str): Tópico a ser pesquisado

        Returns:
            str: Resumo extraído da Wikipedia
        """
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic.replace(' ', '_')}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data.get("extract", "Nenhuma informação encontrada.")
        else:
            return f"Erro ao buscar informações na Wikipedia. Código de status: {response.status_code}"
