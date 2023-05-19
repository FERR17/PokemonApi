from fastapi import fastAPI

app=FatAPI()

@app.get("/")
def index():
    return "Hola a todos, quieres saber de pokemon"