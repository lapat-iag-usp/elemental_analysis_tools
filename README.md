Modules install:

    virtualenv -p python3 .vendor
    . .vendor/bin/activate
    .vendor/bin/pip3 install -r requirements.txt

If needed, recreate the requirements.txt:

    .vendor/bin/pip3 freeze > requirements.txt

Logout from virtualenv:

    deactivate

