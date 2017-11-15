FROM tiangolo/uwsgi-nginx-flask:python3.6
ADD . /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
