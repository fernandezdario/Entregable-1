FROM python:3.9.12

#es muy importante que en el copy al principio pongamos un . y una / porque sino nos pegaria los archvios en la carpeta especifica, en este caso app.
COPY ./lisa.py /app/ 
COPY ./requirements.txt /app/

#el WORKDIR nos permite hacer lo siguiente; Establece el directorio de trabajo para cualquier instrucción posterior ADD, COPY, CMD, ENTRYPOINT o RUN que le siga en el Dockerfile.
WORKDIR /app/
RUN mkdir Personajes
RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "lisa.py" ]