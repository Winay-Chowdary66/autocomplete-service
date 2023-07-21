from python:3.9

workdir /autocomplete-service

copy ./requirements.txt /autocomplete-service/requirements.txt

run pip install --no-cache-dir --upgrade -r /autocomplete-service/requirements.txt

copy src /autocomplete-service/src

cmd ["uvicorn", "src.main:_app", "--host", "0.0.0.0", "--port", "8003"]