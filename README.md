En un terminal dentro de ISA_fin:

*source bin/activate

*sudo apt install python3-pip

*pip3 install -U --user pip && pip3 install rasa

*python3 -m pip install Django

*pip install pandas

*python3 -m pip install --user -U pyTelegramBotAPI

*pip install datetime

*pip install django-import_export

######################################
*sudo apt install curl

*curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok

Si se quiere hacer uso de ngrok sin limite de tiempo se debe de instalar con su cuenta de ngrok en la pagina de ngrok https://ngrok.com/download
####################################

*cd src

*python3 manage.py makemigrations
*python3 manage.py migrate
*python3 manage.py runserver

Aceder a la pagina con el link dado en el teminal seguido de home ej: http://127.0.0.1:8000/home

En otro terminal dentro de ISA_fin:

*ngrok http 5005

Copiar el fowarding desde "https" hasta "ngrok.io" y en el archivo credentials de rasa pegar lo que copió en frente de "webhook_url:" seguido de "/webhooks/telegram/webhook" todo dentro de comillas

Guarde el archivo con "CTRL + s"

Luego de haber hecho el cambio en cedentials se procede a acceder a la pagina y hacer click en el botton de "Actializar ISA"




