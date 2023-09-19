from pydantic import BaseSettings


class Settings(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_ROOT_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_HOST: str
    DATABASE_PORT: int
    MYSQL_HOSTNAME: str

    class Config:
        env_file = "../.env"


settings = Settings()
