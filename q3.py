from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Placeholder for dataset loading and QA logic


def answer_sales_question(q: str) -> str:
    # Implement NLP and correct data lookup based on the dataset here
    # Must support at least the 20 provided sample questions
    return "42"  # Just a dummy response for illustration


@app.get("/query")
async def query(q: str, request: Request):
    answer = answer_sales_question(q)
    response = JSONResponse(content={"answer": answer})
    response.headers["X-Email"] = "21f1004874@ds.study.iitm.ac.in"
    return response
