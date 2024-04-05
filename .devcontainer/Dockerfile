FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

RUN apt-get update && apt-get install -y \
    wget \
    gcc \
    python3-dev \
    openssl

RUN wget https://r.mariadb.com/downloads/mariadb_repo_setup

RUN echo "30d2a05509d1c129dd7dd8430507e6a7729a4854ea10c9dcf6be88964f3fdc25  mariadb_repo_setup" \
    | sha256sum -c -

RUN chmod +x mariadb_repo_setup

RUN sudo ./mariadb_repo_setup \
   --mariadb-server-version="mariadb-10.6"

RUN apt-get update && apt-get install -y \
    libmariadb3 \
    libmariadb-dev