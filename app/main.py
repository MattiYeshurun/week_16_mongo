from fastapi import FastAPI
from routes import router
import uvicorn
from dal import ping_db_health

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    ping_db_health()

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


