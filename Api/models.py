from pydantic import BaseModel, Field
from typing import List

#-------------------------------------------------------------------
class ArticleRequest(BaseModel):
    """
    Modelo para a requisição de geração de artigo
    """
    topic: str = Field(..., description="Tópico sobre o qual o artigo será gerado")
    min_words: int = Field(300, description="Número mínimo de palavras do artigo")

#-------------------------------------------------------------------
class ArticleResponse(BaseModel):
    """
    Modelo para a resposta da geração de artigo
    """
    topic: str = Field(..., description="Tópico do artigo")
    title: str = Field(..., description="Título do artigo")
    content: str = Field(..., description="Conteúdo do artigo")
    word_count: int = Field(..., description="Contagem de palavras do artigo")
    references: List[str] = Field(default=[], description="Referências utilizadas no artigo")