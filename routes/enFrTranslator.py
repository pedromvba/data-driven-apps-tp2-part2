import os
from dotenv import load_dotenv
from fastapi import APIRouter
from models.enFrTranslatorModel import EnFrTranlationInputModel, EnFrTranlationOutputModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

router = APIRouter()
load_dotenv()


@router.post("/en-fr-translator/")
def en_de_translate_gemini(body:EnFrTranlationInputModel):

    text = body.message

    template = ChatPromptTemplate([
        ("system", "You are an English to French translator. Reject any other language."),
        ("user", "Translate this: {text}")
    ])
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=os.getenv("GEMINI_API_KEY"), temperature=0.5)
    response = llm.invoke(template.format_messages(text=text))
 
    return EnFrTranlationOutputModel(translated_text=response.content)