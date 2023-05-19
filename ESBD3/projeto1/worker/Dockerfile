FROM python:3
WORKDIR /worker
COPY . . 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD [ "python", "-u", "worker.py"]

#docker build --tag workers .             # cria a imagem de nome "my_app" a partir das instruções da Dockerfile
#docker run -d --network minha_rede --name wk1 workers         # cria um container com o nome "app" a partir da imagem de nome "my_app" de forma detatched (sem stdout/err)
#docker run -d --network minha_rede --name wk2 workers

#docker run -d --name wk2 workers