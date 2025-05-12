from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

URL_TO_DB = os.getenv("DATABASE_URL")

engine = create_engine(URL_TO_DB)
Session = sessionmaker(bind=engine)
session = Session()