import os
from typing import List, Type

basedir: str = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    CONFIG_NAME: str = 'base'
    DEBUG: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

class DevelopmentConfig(BaseConfig):
    CONFIG_NAME: str = 'dev'
    WEB_URL: str = 'http://localhost:5000'
    DEBUG: bool = True
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

class TestConfig(BaseConfig):
    CONFIG_NAME: str = 'test'
    WEB_URL: str = 'http://localhost:5000'
    DEBUG: bool = True
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

class ProductionConfig(BaseConfig):
    CONFIG_NAME: str = 'prod'
    WEB_URL: str = 'https://niesdigital.com'
    DEBUG: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig, TestConfig, ProductionConfig]


config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}
