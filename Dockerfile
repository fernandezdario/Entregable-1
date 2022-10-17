FROM python:3.9.12

COPY ./simpsons.py /app/
COPY ./requirements.txt /app/

WORKDIR /app/
RUN mkdir /General
RUN mkdir /Lisa
RUN mkdir /Homer 
RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "simpsons.py" ]