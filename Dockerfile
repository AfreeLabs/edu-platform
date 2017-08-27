FROM python:3.6

###############################################################
## install app
## copy files one by one and split commands to use docker cache
###############################################################

WORKDIR /code/

COPY requirements.txt /code/requirements.txt
RUN pip install --quiet -r requirements.txt

COPY . /code/

ENTRYPOINT ["/code/entrypoint.sh"]
