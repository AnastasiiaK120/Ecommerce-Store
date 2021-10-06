FROM ubuntu:20.04

WORKDIR /
COPY . . 
RUN apt-get update && apt-get install -y python3.9 && apt-get install -y python3-pip && pip3 install -r requirements.txt
EXPOSE 8000

CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8000" ]