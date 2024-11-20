import os
from dotenv import load_dotenv
from fastapi import APIRouter
from models.enDeTranslatorModel import EnDeTranlationInputModel, EnDeTranlationOutputModel
from langchain_community.llms import HuggingFaceHub

router = APIRouter()
load_dotenv()


@router.post("/en-de-translator/")
def translate_using_gemini_api(body:EnDeTranlationInputModel):

    text = body.message

    llm = HuggingFaceHub(
        repo_id='Helsinki-NLP/opus-mt-en-de',
        huggingfacehub_api_token = os.getenv("HUGGING_FACE_API_KEY"),
        model_kwargs={})

    response = llm.invoke(text)
 
    return EnDeTranlationOutputModel(translated_text=response)
