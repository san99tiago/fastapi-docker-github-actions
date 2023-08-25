from fastapi import FastAPI

app = FastAPI(
    description="Simple FastAPI sample code",
    contact={"Santiago Garcia Arango": "santiago.garcia1999@hotmail.com"},
    title="Simple FastAPI Example",
    version="0.0.1",
)


@app.get("/")
async def root():
    return {"message": "Hello by Santi"}


@app.get("/status")
async def get_status():
    return {"status": "OK"}
