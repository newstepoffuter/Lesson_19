from pathlib import Path
from typing import Literal
from pydantic_settings import BaseSettings
import tests


class Config(BaseSettings):
    remote_url: str = 'http://hub.browserstack.com/wd/hub'
    app: str = 'bs://sample.app'
    browser_platform: Literal['android', 'ios'] = 'android'
    timeout: float = 4.0
    user_name: str = ''  # Убрал из общего доступа
    access_key: str = '' # Убрал из общего доступа


config = Config(_env_file=Path(tests.__file__).parent.parent.joinpath('.env').absolute())