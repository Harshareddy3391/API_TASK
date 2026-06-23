from fastapi import FastAPI


app=FastAPI()


@app.get("/home")
def home():
    return {
        "msg":" this is root requist"
    }