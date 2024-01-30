import os
import pandas as pd
from src.database import Database
# from etl.load import Load
from src.config import EXCEL_DATA_PATH, DATABASE_URL
from typing import Dict, List, Optional, Any, Union
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware

_app = FastAPI()


# Add CORS middleware
_app.add_middleware(
    CORSMiddleware,
    # Replace "*" with the actual list of allowed origins if needed
    allow_origins=["*"],
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


def get_database_url():
    return DATABASE_URL


def __main__():
    pass


@_app.get("/autocomplete/")
async def autocomplete_search(
    keyword: Optional[str] = Query(None, min_length=1),
    symbol: Optional[str] = Query(None, min_length=1),
    instrument_types: Optional[List[str]] = Query(None),
    category: Optional[str] = Query(None),
    schema: Optional[str] = Query(None),
    publisher: Optional[str] = Query(None),
    region: Optional[str] = Query(None),
    available_history: Optional[str] = Query(None),
    page: int = Query(1, gt=0),
    page_size: int = Query(10, le=100),
) -> List[Dict[str, Any]]:

    database_url = get_database_url()
    db = Database(database_url=database_url)
    print("Filtering the Data")
    data = db.get_data_from_postgres(table_name="product_slate", keyword=keyword, symbol=symbol, instrument_types=instrument_types, category=category,
                                     schema=schema, publisher=publisher, region=region, available_history=available_history, page=page, page_size=page_size)
    db.close()
    return data



# __main__()
