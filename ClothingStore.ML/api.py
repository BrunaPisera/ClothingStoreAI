"""
FastAPI service that serves price predictions from a trained ClothingPriceModel.

Run locally:
    uvicorn api:app --reload --port 8000
"""

from contextlib import asynccontextmanager

import joblib
import pandas as pd
from fastapi import FastAPI, Request
from pydantic import BaseModel, Field

from models.clothing_price_model import ClothingPriceModel

MODEL_PATH = "price_model.joblib"

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.price_model = joblib.load(MODEL_PATH)
    yield


app = FastAPI(
    title="Clothing Price Predictor",
    version="1.0",
    lifespan=lifespan,
)

class ClothingItem(BaseModel):
    category: str = Field(
        ...,
        json_schema_extra={"example": "blusa"},
    )   

    premium: str = Field(
        ...,
        json_schema_extra={"example": "yes"},
    )

    costPrice: float = Field(
        ...,
        json_schema_extra={"example": 10.0},
    )
    sleeveType: str = Field(
        ...,
        json_schema_extra={"example": "Manga curta"},
    )


class PredictionResponse(BaseModel):

    predicted_price: int


@app.get("/health")
def health(request: Request):

    return {
        "status": "ok",
        "model_loaded": request.app.state.price_model is not None,
    }


@app.post(
    "/predict",
    response_model=PredictionResponse,
)
def predict(
    item: ClothingItem,
    request: Request,
):

    model: ClothingPriceModel = request.app.state.price_model

    # Convert the JSON request into a DataFrame
    data = pd.DataFrame(
        [item.model_dump()]
    )

    prediction = model.predict(data)[0]

    return PredictionResponse(
        predicted_price=int(prediction)
    )