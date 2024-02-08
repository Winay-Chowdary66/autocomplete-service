import os
from extract import Extract
from load import Load
# from src import EXCEL_DATA_PATH, DATABASE_URL
from database import Database

def get_external_file_path():
    return os.getenv(
    "EXCEL_DATA_PATH", "/workspaces/autocomplete-service/data/War Room Profiles.xlsx")

def get_database_url():
    return os.environ.get(
        "DATABASE_URL",
        "postgres://postgres:postgresPassword@10.0.0.4:5432/postgres?sslmode=disable"
    )

@lambda _: _()
def main():
    db = Database(database_url=get_database_url())
    # extract data from excel
    extract = Extract(file_path=get_external_file_path())
    # get data in data frame
    df = extract.get_dataframe()
    # load dataframe
    breakpoint()
    load = Load(dataframe=df, database=db)
    # load df into db
    load.load_dataframe()

    db.close()
