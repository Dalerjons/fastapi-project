from environs import Env
from config.db import DbConfig
from config.api import ApiConfig
from dataclasses import dataclass


@dataclass
class Config:
    db: DbConfig
    api_prefix: ApiConfig


def load_config(env_path: str | None = None):
    env = Env()
    env.read_env(env_path)

    db = DbConfig.from_env(env)
    api_prefix = ApiConfig()

    return Config(
        db=db,
        api_prefix=api_prefix
    )
