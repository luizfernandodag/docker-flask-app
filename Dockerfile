#base python docker image
#FROM python:3.14-rc-bookworm⁠
FROM python:3.9.5-buster

#import code

ADD . /code

#change dir
WORKDIR /code

#installing lib

RUN pip install flask

#Exposing the port
EXPOSE 5001

#Running python file

CMD python main.py