from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def setup_cors_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=None,
        allow_methods=["GET", "POST", "DELETE", "PATCH", "PUT"],
        allow_headers=["*"],
    )
