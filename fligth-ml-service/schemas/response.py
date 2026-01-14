from pydantic import BaseModel, Field, ConfigDict

class PredictionResponse(BaseModel):
    probabilidade: float = Field(alias = "probabilidade", description = "Probability of flight delay")

    model_config = ConfigDict(populate_by_name=True)
