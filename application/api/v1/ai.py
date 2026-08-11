from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class APIQueryRequest(BaseModel):
    question: str
    
@router.post("/ai/query")
def ai_query(request: APIQueryRequest):
    return {
        "question": request.question,
        "answer": "AI response will come later"
    }