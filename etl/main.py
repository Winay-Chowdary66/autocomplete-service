import os
from extract import Extract
from load import Load
# from src import EXCEL_DATA_PATH, DATABASE_URL
from database import Database

def get_external_file_path():
    return os.getenv(
    "EXCEL_DATA_PATH", "/workspaces/autocomplete-service/data/Product Slate Export.xlsx")

def get_database_url():
    return os.environ.get(
        "DATABASE_URL",
        "postgres://postgres:postgresPassword@172.22.0.2:5432/postgres?sslmode=disable"
    )


def main():
    db = Database(database_url=get_database_url())
    # extract data from excel
    extract = Extract(file_path=get_external_file_path())
    # get data in data frame
    df = extract.get_dataframe()
    # load dataframe
    # print(df)
    load = Load(dataframe=df, database=db)
    # load df into db
    load.load_dataframe()

    db.close()

main()