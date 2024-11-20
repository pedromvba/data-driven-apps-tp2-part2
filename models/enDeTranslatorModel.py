from pydantic import BaseModel

class EnDeTranlationInputModel(BaseModel):
    message: str

class EnDeTranlationOutputModel(BaseModel):
    translated_text: str