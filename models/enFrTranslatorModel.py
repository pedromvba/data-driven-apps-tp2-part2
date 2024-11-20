from pydantic import BaseModel

class EnFrTranlationInputModel(BaseModel):
    message: str

class EnFrTranlationOutputModel(BaseModel):
    translated_text: str