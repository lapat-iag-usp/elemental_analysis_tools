Instalação das bibliotecas:

    . .vendor/bin/activate
    .vendor/bin/pip3 install -r requirements.txt
    deactivate

Para recriar o arquivo se necessário:

    .vendor/bin/pip3 freeze > requirements.txt

Banco de dados:

    python3 run.py db migrate
    python3 run.py db upgrade
    
Para executar:

    python3 run.py runserver

Usuário no postgres:

    INSERT INTO users (id, username,password,email) VALUES ((SELECT nextval ('users_id_seq')),'admin','admin','admin@example.com');

