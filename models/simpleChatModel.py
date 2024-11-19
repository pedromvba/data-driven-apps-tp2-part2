from pydantic import BaseModel

class SimpleChatInputModel(BaseModel):
    message: str

class SimpleChatOutputModel(BaseModel):
    bot_message: str