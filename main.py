# imports
from fastapi import FastAPI
from routes.simpleChat import router as simpleChatRouter
from routes.enFrTranslator import router as enFrTranslatorRouter
from routes.enDeTranslator import router as enDeTranslatorRouter

# FastAPI instance
app = FastAPI()

# include routers
app.include_router(simpleChatRouter)
app.include_router(enFrTranslatorRouter)
app.include_router(enDeTranslatorRouter)

# root route
@app.get("/")
def root():
    return {"message": "Services are up and running!"}
