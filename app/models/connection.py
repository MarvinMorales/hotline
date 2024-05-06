from os import getenv

from dotenv import load_dotenv
from sqlmodel import create_engine

load_dotenv()

db_user = getenv("DB_USER")
db_password = getenv("DB_PASSWORD")
db_host = getenv("DB_HOST")
db_database = getenv("DB_DATABASE")

final_url = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_database}"

engine = create_engine(final_url)
