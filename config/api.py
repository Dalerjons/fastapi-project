from dataclasses import dataclass, field


@dataclass
class ApiV1Prefix:
    prefix: str = '/v1'
    categories: str = '/categories'


@dataclass
class ApiConfig:
    prefix: str = '/api'
    v1: ApiV1Prefix = field(default_factory=ApiV1Prefix)
