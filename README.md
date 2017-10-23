Instalação do pip e virtualenv:

    sudo apt-get install python-setuptools
    sudo easy_install pip
    sudo pip install virtualenv

Criando, acessando e instalando bibliotecas virtualenv thiagolibs:

    cd ~
    virtualenv -p python3 thiagolibs
    . ~/thiagolibs/bin/activate
    ~/thiagolibs/bin/pip3 install flask

Listar bibliotecas instaladas em thiagolibs:

    ~/thiagolibs/bin/pip3 freeze > requirements.txt

Instalar bibliotecas a partir de uma arquivo:

    ~/thiagolibs/bin/pip3 install -r requirements.txt

