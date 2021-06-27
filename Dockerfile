FROM python:3.8-slim-buster

WORKDIR /app


# Install poetry:
RUN pip install --upgrade pip
RUN pip install poetry

# Copy in the config files:
COPY pyproject.toml poetry.lock ./
# Copy in the config files:
COPY ./docker/start.sh /app/start.sh
RUN chmod +x '/app/start.sh'
# Install only dependencies:
#RUN poetry install --no-root --no-dev

# Copy in everything else and install:
RUN poetry install --no-dev
CMD ["poetry", "run", "gunicorn", "djangoChallenge.djangoChallenge.wsgi", "--bind", "0.0.0.0:8000"]