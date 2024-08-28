from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

headers = {"accept": "application/json"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello World"}

@app.get("/test", tags=['test'])
async def test():
    return {"message": "SAM: "}


def start():
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8080, reload=True)