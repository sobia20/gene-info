from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import yaml
from loguru import logger

from yaml.loader import SafeLoader

with open('config.yml') as f:
    config = yaml.load(f, Loader=SafeLoader)
    database_url = f"mysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
    engine = create_engine(
        database_url
    )
    logger.info('Connection with database established successfully')
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base = declarative_base()