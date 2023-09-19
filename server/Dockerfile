FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --virtual build-dependencies build-base python3-dev libffi-dev openssl-dev

RUN pip install pipenv

WORKDIR /server

COPY Pipfile Pipfile.lock /server/

RUN pipenv install --system --deploy --ignore-pipfile

COPY . /server/

EXPOSE 8000:8000

CMD [ "uvicorn", "api.main:gateway", "--host", "0.0.0.0", "--port", "8000", "--reload" ]
