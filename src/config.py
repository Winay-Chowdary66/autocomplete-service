import os

EXCEL_DATA_PATH = os.getenv(
    "EXCEL_DATA_PATH", "/workspaces/autocomplete-service/data/Product Slate Export.xlsx")
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgres://postgres:postgresPassword@172.24.0.2:5432/postgres?sslmode=disable"
)
