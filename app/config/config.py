import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///database.db"
    )

    SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_pre_ping": True,
    "connect_args": {"sslmode": "require"},
    }


