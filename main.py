from typing import Union
from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class User(BaseModel):
    userName: str
    password: str

@app.get("/")
def read_root():
    return {"Hello": "vamshi"}

@app.post("/login")
def login(user: User):
    if user.userName == "vamshi" and user.password == "1234":
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content={"message": "Login successful"})
    else:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content={"message": "Invalid username or password"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
