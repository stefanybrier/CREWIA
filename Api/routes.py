from fastapi import FastAPI, HTTPException
from Api.models import ArticleRequest, ArticleResponse
from main import create_crew

#-------------------------------------------------------------------
app = FastAPI(
    title="Article Generator API",
    description="API para geração de artigos usando CrewAI",
    version="1.0.0"
)

#-------------------------------------------------------------------
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

#-------------------------------------------------------------------
@app.get("/health/")
async def health_check():
    """
    Endpoint para verificar a saúde da API
    """
    return {"status": "healthy"}