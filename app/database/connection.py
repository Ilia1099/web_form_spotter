from tinydb import TinyDB
from decouple import config
from pathlib import Path

db_name = config("DB_NAME")
root = Path(__file__).parent.parent.parent
path_to_file = root.joinpath(db_name).resolve()
db_connection = TinyDB(path_to_file)