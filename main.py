# imports
from fastapi import FastAPI
from routes.simpleChat import router as simpleChatRouter

# FastAPI instance
app = FastAPI()

# include routers
app.include_router(simpleChatRouter)

# root route
@app.get("/")
def root():
    return {"message": "Services are up and running!"}
