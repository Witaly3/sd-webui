from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ml_sd.gradio import launch_gradio
from ml_sd.router import router as router_app


app = FastAPI(title="SD-WEBUI App")

origins = ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin", "Authorization"
    ],
)

app.include_router(router_app)


@app.on_event("startup")
async def startup_event() -> None:
    launch_gradio()
