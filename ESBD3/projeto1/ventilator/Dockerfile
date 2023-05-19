FROM python:3
WORKDIR /ventilator
COPY . . 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5557

CMD [ "python", "-u", "ventilator.py"]


#docker build --tag ventilator .             # cria a imagem de nome "my_app" a partir das instruções da Dockerfile
#docker run -d --name vent1 ventilator         # cria um container com o nome "app" a partir da imagem de nome "my_app" de forma detatched (sem stdout/err)
#docker run -d -p 5557:5557 --network minha_rede --name vent1 ventilator 
