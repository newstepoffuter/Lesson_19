from pathlib import Path
from typing import Literal
from pydantic_settings import BaseSettings
import tests


class Config(BaseSettings):
    remote_url: str = 'http://hub.browserstack.com/wd/hub'
    app: str = 'bs://sample.app'
    browser_platform: Literal['android', 'ios'] = 'android'
    timeout: float = 4.0
    user_name: str = 'bsuser_9ztCr6'
    access_key: str = 'mvq9ER7oWHLWipc5V6m3'


config = Config(_env_file=Path(tests.__file__).parent.parent.joinpath('.env').absolute())