FROM python:3.12.2-slim-buster

ENV APP_HOME=/app
RUN mkdir APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME


LABEL maintainer='junior.bokanga@gmail.com'
LABEL youtube="https://www.youtube.com/skull"
LABEL description="Development image for Real Estate Project"

ENV PYHTONDONTWRITEBYTECODE 1

ENV PYHTONUNBUFFERED 1

RUN apt-get update \
&& apt-get install -y build_essential \
&& apt-get install -y libpq-dev \
&& apt-get intsall -y gettext \
&& apt-get install -y betcat gcc postgresql \
&& apt-get purge - --auto-remove -o APT::Autoremove::recommendsImportant=false \
&& rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

ENTRYPOINT [ "/entrypoint"]