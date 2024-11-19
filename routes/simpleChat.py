from fastapi import APIRouter
from models.simpleChatModel import SimpleChatInputModel, SimpleChatOutputModel
from langchain_community.llms import FakeListLLM

router = APIRouter()

@router.post("/fakebot/")
def simplechat(body:SimpleChatInputModel) -> SimpleChatOutputModel:
    prompt = body.message

    responses = [ "Hello! How can I assist you today?, I'm just a simulated bot, but I'm here to help!"]

    fake_llm = FakeListLLM(responses=responses)

    response = fake_llm.invoke(prompt)
    return SimpleChatOutputModel(bot_message=response)
