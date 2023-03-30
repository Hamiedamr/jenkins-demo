from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Jenkins Demo")


@app.get("/", response_class=HTMLResponse)
def home():
    return """<h1> Jenkins DEMO :)!</h1>"""
