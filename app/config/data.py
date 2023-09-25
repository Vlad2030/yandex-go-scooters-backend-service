import enum
from utils.get_envs import Environs


class App(enum.Enum):
    def __str__(self) -> str:
        return self.value

    TITLE = Environs.get("APP_TITLE")
    VERSION = Environs.get("APP_VERSION")
    DOCS_URL = Environs.get("APP_DOCS_URL")


class Database(enum.Enum):
    def __str__(self) -> str:
        return self.value

    HOST = Environs.get("POSTGRES_CONTAINER_HOST")
    PORT = Environs.get("POSTGRES_CONTAINER_PORT")
    DB = Environs.get("POSTGRES_DB")
    USER = Environs.get("POSTGRES_USER")
    PASSWORD = Environs.get("POSTGRES_PASSWORD")
