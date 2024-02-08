import os

import pandas as pd

class Load(object):
    def __init__(self, dataframe, database):
        self.df = dataframe
        self.db = database

    def load_dataframe(self):
        database_name = "development"
        table_name = "war_room_profiles"
        
        self.db.create_db_if_not_exists(database_name)
        
        self.db.create_table_if_not_exists(dataframe=self.df, table_name=table_name)
        
        rows = [tuple(row) for row in self.df.itertuples(index=False)]

        self.db.load_dataframe(df=self.df, table_name=table_name, rows=rows)

