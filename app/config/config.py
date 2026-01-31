import os


def _get_database_uri():
    uri = os.getenv("DATABASE_URL", "sqlite:///database.db")
    # Render/Heroku usam postgres://, SQLAlchemy 1.4+ exige postgresql://
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    return uri


def _get_engine_options():
    uri = os.getenv("DATABASE_URL", "")
    if uri.startswith("postgres"):
        return {
            "pool_pre_ping": True,
            "connect_args": {"sslmode": "require"},
        }
    # SQLite - sem opções específicas de PostgreSQL
    return {"pool_pre_ping": True}


class Config:
    SQLALCHEMY_DATABASE_URI = _get_database_uri()
    SQLALCHEMY_ENGINE_OPTIONS = _get_engine_options()

