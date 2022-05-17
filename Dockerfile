FROM python:3.8-bullseye
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 - 
COPY . /lingua-py
WORKDIR /lingua-py
RUN ~/.poetry/bin/poetry build && python3 -m pip install dist/*.whl && chmod +x fuzz/fuzz.py