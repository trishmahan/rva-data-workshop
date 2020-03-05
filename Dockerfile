FROM python:3.7.2
RUN mkdir -p /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN pip install .
RUN pytest
ENTRYPOINT python calculations/calculations.py
