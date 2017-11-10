FROM tiangolo/uwsgi-nginx-flask:python3.6
ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt
