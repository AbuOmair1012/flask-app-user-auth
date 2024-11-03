FROM python:3.10-alphine
WORKDIR ./flask-app-userLogIn
COPY . /flask-app-userLogIn/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python3 ./app.py 