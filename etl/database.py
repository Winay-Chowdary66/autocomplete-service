import psycopg2

class Database(object):
    def __init__(self, database_url) -> None:
        self.database_url = database_url
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

    def create_db_if_not_exists(self, database_name):
        database_query = f"""
            SELECT 'CREATE DATABASE {database_name}'
            WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '{database_name}')
        """
        self.cursor.execute(database_query)

        self.connection.commit()

    def create_table_if_not_exists(self, dataframe, table_name):
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        for col_name, col_type in zip(dataframe.columns, dataframe.dtypes):
            col_name = "_".join(col_name.split(" "))
            if "int" in str(col_type):
                col_type_str = "BIGINT"
            elif "float" in str(col_type):
                col_type_str = "NUMERIC"
            else:
                col_type_str = "TEXT"
            create_table_query += f"{col_name} {col_type_str}, "
        create_table_query = create_table_query.rstrip(", ") + ");"
        
        self.cursor.execute(create_table_query)
        self.connection.commit()
 

    def load_dataframe(self, df, table_name, rows):
        try:
            columns = tuple(['_'.join(col.split(" ")).lower() for col in list(df.columns)])
            insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(df.columns))});"
            self.cursor.executemany(insert_query, rows)
            self.connection.commit()
        except ValueError:
            print("ValueError")