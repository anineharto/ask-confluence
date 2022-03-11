import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from ask_confluence.app.service.answer_service import get_answer_from_confluence
from ask_confluence.exceptions import AnswerNotFoundError

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthCheck")
async def health_check():
    return {"status": "Healthy"}

@app.post("/askConfluence")
async def ask_question(question: str):
    try:
        return {"answer": get_answer_from_confluence(question)}
    except AnswerNotFoundError as error:
        raise HTTPException(status_code=404, detail=f"{error}")

if __name__ == "__main__":
    uvicorn.run(app, host="127:0:0:1", port=8000)