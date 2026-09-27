from fastapi import FastAPI

app= FastAPI()

@app.get("/")
async def main():
    return str("Hello to new website using API")