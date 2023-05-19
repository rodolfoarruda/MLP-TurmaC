FROM python:3
WORKDIR /sink
COPY . . 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5558
CMD [ "python", "-u", "sink.py"]

#docker build --tag sink .             # cria a imagem de nome "my_app" a partir das instruções da Dockerfile
#docker run -d --name sk1 sink         # cria um container com o nome "app" a partir da imagem de nome "my_app" de forma detatched (sem stdout/err)
#docker run -d --network minha_rede -p 5558:5558 --name sk1 sink 