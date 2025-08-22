from environs import Env
from dataclasses import dataclass
from sqlalchemy.engine.url import URL


@dataclass
class DbConfig:
    host: str
    user: str
    database: str
    password: str
    port: int = 5432


    @staticmethod
    def from_env(env: Env) -> "DbConfig":
        return DbConfig(
            host=env.str('PG_HOST'),
            database=env.str('PG_DATABASE'),
            user=env.str('PG_USER'),
            password=env.str('PG_PASSWORD'),
            port=env.int('PG_PORT')
        )


    def construct_url(self, driver: str = 'asyncpg') -> str:
        return URL.create(
            drivername=f'postgresql+{driver}',
            host=self.host,
            database=self.database,
            username=self.user,
            password=self.password,
            port=self.port
        ).render_as_string(hide_password=False)
