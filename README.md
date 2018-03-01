Instalação das bibliotecas:

    virtualenv -p python3 .vendor
    . .vendor/bin/activate
    .vendor/bin/pip3 install -r requirements.txt

Para recriar o arquivo se necessário:

    .vendor/bin/pip3 freeze > requirements.txt

Sair do virtualenv:

    deactivate

