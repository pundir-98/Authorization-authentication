FROM python:3.6-slim

WORKDIR /

COPY . /

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip3 install pymongo

EXPOSE 5000

CMD ["python3","app.py"]