# tdd_project
Для создания Dockerfile для Python проекта с пакетным менеджером Poetry можно использовать следующий шаблон:

```
FROM python:3.9-slim-buster

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . /app

CMD ["python", "app.py"]
```
Рассмотрим по порядку, как оно работает:

1. С помощью команды `FROM python:3.9-slim-buster` устанавливается базовый образ, тут мы используем версию Python 3.9 на базе операционной системы Debian Buster.

2. С помощью команды `WORKDIR /app` устанавливается рабочая директория `/app` для образа.

3. Команда `COPY pyproject.toml poetry.lock ./` копирует файлы `pyproject.toml` и `poetry.lock` внутрь Docker-контейнера.

4. С помощью команды `RUN pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi` устанавливается Poetry и необходимые зависимости из файла pyproject.toml. Опции `--no-interaction` и `--no-ansi` позволяют установить зависимости без запросов в интерактивном режиме и без цветовых выделений текста соответственно.

5. Команда `COPY . /app` копирует все файлы из текущей директории внутрь Docker-контейнера.

6. Команда `CMD ["python", "app.py"]` запускает файл `app.py` при запуске контейнера. Укажите свой файл запуска приложения.

Обратите внимание, что если вы используете файл `.env` для хранения конфиденциальных данных, его необходимо скопировать в Docker-контейнер так же, как и другие файлы, используя команду `COPY .env /app/`.

Для запуска приложения с помощью Dockerfile используйте команду `docker build -t <tag_name> .` для сборки образа Docker, где `tag_name` - это имя образа, а `.` - текущая директория. После успешной сборки можно запустить образ приложения командой `docker run -p 8000:8000 <tag_name>`.