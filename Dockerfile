FROM python:3.9

RUN mkdir -p /code
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./Makefile /code/Makefile
RUN make

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]