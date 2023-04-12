FROM python:3.11.2-slim-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean


COPY ./pyproject.toml ./poetry.lock ./
RUN pip install --upgrade pip \
  && pip install poetry \
  && poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . .

COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]