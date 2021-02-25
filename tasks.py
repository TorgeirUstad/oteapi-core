from celery import Celery
from subprocess import run
import requests
import json
app = Celery('tasks', broker='amqp://guest:guest@broker:5672//')
@app.task
def command(text):
    # ret = run (["ls", "-al"])
    ret = run (["touch", "output.txt"])
    f= open("output.txt","w+")
    f.write(text)
    f.close
    return ret

@app.task
def read(uri):
    # ret = run (["ls", "-al"])
    ret = requests.get(uri)
    return json.loads(ret)