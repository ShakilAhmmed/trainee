FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /trainee_management
WORKDIR /trainee_management
COPY requirements.txt /trainee_management/
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev  -y
COPY . /trainee_management

