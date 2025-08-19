from environs import Env
from .db import DbConfig
from dataclasses import dataclass


@dataclass
class Config:
    db: DbConfig


def load_config(env_path: str | None = None):
    env = Env()
    env.read_env(env_path)

    db = DbConfig.from_env(env)

    return Config(
        db=db
    )
