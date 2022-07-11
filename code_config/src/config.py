import secrets
from pydantic import BaseSettings
import yaml

#load config from yaml file
with open('../config.yaml', 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

class Secrets(BaseSettings):
    db: dict
    host: str
    port: int
    class Config:
        env_file = '../.env'
        env_nested_delimiter = '_'


class Validation(BaseSettings):
    path: str 
    percentage: float

class Data(BaseSettings):
    root: str = config['data']['root']
    train: str = config['data']['train']
    test: str =  config['data']['test']
    validation: Validation = Validation(**config['data']['validation'])

class Train(BaseSettings):
    epochs: int = config['train']['epochs']
    batch_size: int = config['train']['batch_size']
    lr: float = config['train']['lr']
    callback:  bool = config['train']['callback']
    retrain: bool = config['train']['retrain']
 


#create config class from yaml file
class Config(BaseSettings):
    train:Train = Train(**config['train'])
    version: float = config['version']
    debug: bool = config['debug']
    data: Data = Data(**config['data'])
    secrets: Secrets = Secrets()
    
