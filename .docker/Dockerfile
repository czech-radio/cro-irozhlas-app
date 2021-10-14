FROM python:3.9-slim

WORKDIR /app

COPY src/ ./src
COPY setup.py .
COPY setup.cfg .

RUN python -m pip install --upgrade pip
RUN pip install .

ENTRYPOINT ["program"]
