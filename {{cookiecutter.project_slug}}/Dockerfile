FROM python:3.9 as base

WORKDIR /app

RUN pip install pipx && pipx install poetry && ln -s /root/.local/bin/poetry /usr/local/bin

COPY poetry.lock pyproject.toml ./

FROM base as deploy
RUN poetry install --only main
COPY . .

ENTRYPOINT [ "poetry" ]

CMD [ "run" , "make", "deploy" ]

FROM base as dev
RUN poetry install
COPY . .

ENTRYPOINT [ "bash", "poetry", "shell" ]
