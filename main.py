from fastapi import FastAPI

app= FastAPI()

@app.get("/")
async def main():
    return str("Hello to new website using API")

#MAKE API WITH "PATH PARAMETERS"
@app.get("/user/{user_name}")
async def getUserName(user_name):
    return {"Nombred del usuario:":user_name}