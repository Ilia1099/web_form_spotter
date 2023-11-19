from tinydb import TinyDB
from decouple import config
from pathlib import Path

db_name = config("DB_NAME")
path_to_file = Path(__file__).home().joinpath(db_name).resolve()
db_connection = TinyDB(path_to_file)
