from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from app.models import NumberResponse
from app.services import classify_number

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/classify-number", response_model=NumberResponse)
async def classify_number_endpoint(number: str = Query(...)):
    try:
        return classify_number(int(number))
    except ValueError:
        raise HTTPException(status_code=400, detail={"number": number, "error": True})
