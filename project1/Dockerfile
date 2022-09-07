FROM python:3.9

RUN mkdir -p /project1/code
WORKDIR /project1/code

COPY ./requirements.txt /project1/code/requirements.txt
COPY ./Makefile /project1/code/Makefile
RUN make

COPY ./app /project1/code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]