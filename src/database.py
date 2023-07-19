import psycopg2
from typing import List, Optional, Dict, Any


class Database(object):
    def __init__(self, database_url) -> None:
        self.database_url = database_url
        print(database_url)
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        self.connection = psycopg2.connect(self.database_url, sslmode="prefer")
        self.cursor = self.connection.cursor()
        print("Successfully connected to the database")

    def close(self):
        self.cursor.close()
        self.connection.close()
        print("Closed connection to the database")

    # Function to get data from PostgreSQL based on input parameters

    def get_data_from_postgres(self,
            table_name:str,
            keyword: Optional[str] = None,
            symbol: Optional[str] = None,
            instrument_types: Optional[List[str]] = None,
            category: Optional[str] = None,
            schema: Optional[str] = None,
            publisher: Optional[str] = None,
            region: Optional[str] = None,
            available_history: Optional[str] = None,
            page: int = 1,
            page_size: int = 10,
    ) -> List[Dict[str, Any]]:

        # Construct the base SQL query
        sql_query = f"SELECT * FROM {table_name} WHERE 1=1"

        # Construct the WHERE clause based on the input parameters
        if keyword:
            sql_query += f" AND (LOWER(instrument_name) LIKE LOWER('%{keyword}%') OR LOWER(symbol) LIKE LOWER('%{keyword}%'))"

        if symbol:
            sql_query += f" AND LOWER(symbol) = LOWER('{symbol}')"

        if instrument_types:
            instrument_types_str = ",".join(
                [f"'{i}'" for i in instrument_types])
            sql_query += f" AND asset_class IN ({instrument_types_str})"

        if category:
            sql_query += f" AND category = '{category}'"

        if schema:
            sql_query += f" AND schema = '{schema}'"
        if publisher:
            sql_query += f" AND publisher = '{publisher}'"
        if region:
            sql_query += f" AND region = '{region}'"
        if available_history:
            sql_query += f" AND available_from_date >= '{available_history}'"
        # Add the ORDER BY and LIMIT clauses for ranking and pagination
        sql_query += " ORDER BY CASE"
        sql_query += " WHEN LOWER(symbol) = LOWER('{symbol}') THEN 0"
        sql_query += " WHEN LOWER(symbol) LIKE LOWER('{symbol}%') THEN 1"
        sql_query += " WHEN LOWER(symbol) LIKE LOWER('%{symbol}%') THEN 2"
        sql_query += " WHEN LOWER(instrument_name) LIKE LOWER('%{keyword}%') THEN 3"
        sql_query += " ELSE 4 END,"
        sql_query += " volume DESC NULLS LAST, open_interest DESC NULLS LAST"
        sql_query += f" LIMIT {page_size} OFFSET {(page - 1) * page_size}"
        # Execute the SQL query and fetch the results
        print(sql_query)
        self.cursor.execute(sql_query)
        results = self.cursor.fetchall()
        # Convert the results into a list of dictionaries
        columns = [desc[0] for desc in self.cursor.description]
        data = [dict(zip(columns, row)) for row in results]

        self.connection.commit()
        return data
