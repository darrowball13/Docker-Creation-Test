FROM python:3.12-slim

WORKDIR /app
COPY . /app

RUN python -m pip install -r requirements.txt

EXPOSE 5000

CMD python ./Test_Matrix_Multiplication.py