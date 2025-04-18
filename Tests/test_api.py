import unittest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from Api.routes import app
from Api.models import ArticleResponse

#========================================================================
class TestAPI(unittest.TestCase):
    """Testes para a API"""
    
    def setUp(self):
        """Configura o cliente de teste antes de cada teste"""
        self.client = TestClient(app)
    
    def test_health_check(self):
        """Testa o endpoint de health check"""
        response = self.client.get("/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "healthy"})
    
    @patch('main.create_crew')
    def test_generate_article_success(self, mock_create_crew):
        """Testa a geração de artigo bem-sucedida"""
        # Configura o mock para retornar um artigo
        mock_create_crew.return_value = {
            "title": "Inteligência Artificial: Uma Visão Geral",
            "content": "A Inteligência Artificial (IA) é um campo da ciência da computação dedicado ao desenvolvimento de sistemas capazes de realizar tarefas que normalmente exigiriam inteligência humana. " * 30,  # Texto longo para superar 300 palavras
            "references": ["Wikipedia", "Outras fontes"]
        }
        
        # Faz a solicitação POST
        response = self.client.post(
            "/generate-article/",
            json={"topic": "Inteligência Artificial", "min_words": 300}
        )
        
        # Verifica a resposta
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["topic"], "Inteligência Artificial")
        self.assertEqual(data["title"], "Inteligência Artificial: Uma Visão Geral")
        self.assertTrue(len(data["content"]) > 0)
        self.assertTrue(data["word_count"] >= 300)
        self.assertEqual(len(data["references"]), 2)
    
    @patch('main.create_crew')
    def test_generate_article_error(self, mock_create_crew):
        """Testa o tratamento de erro ao gerar artigo"""
        # Configura o mock para lançar uma exceção
        mock_create_crew.side_effect = Exception("Erro ao gerar artigo")
        
        # Faz a solicitação POST
        response = self.client.post(
            "/generate-article/",
            json={"topic": "Tópico Problemático"}
        )
        
        # Verifica se o erro é tratado corretamente
        self.assertEqual(response.status_code, 500)
        data = response.json()
        self.assertEqual(data["detail"], "Erro ao gerar artigo")
    
    def test_invalid_request(self):
        """Testa uma solicitação inválida"""
        # Faz uma solicitação sem o campo obrigatório 'topic'
        response = self.client.post(
            "/generate-article/",
            json={"min_words": 300}
        )
        
        # Verifica se o erro de validação é retornado
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

#========================================================================
if __name__ == "__main__":
    unittest.main()
