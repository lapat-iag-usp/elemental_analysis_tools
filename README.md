Instalação das bibliotecas:

    pip3 install -r requirements.txt

Para recriar o arquivo se necessário:

    pip3 freeze > requirements.txt

Banco de dados:

    python3 run.py db migrate
    python3 run.py db upgrade
    
Para executar:

    python3 run.py runserver

