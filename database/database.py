from peewee import PostgresqlDatabase
from dotenv import load_dotenv
import os


load_dotenv()

database_uri = os.getenv('DATABASE_URI', '')
db = pg_db = PostgresqlDatabase(database_uri)


