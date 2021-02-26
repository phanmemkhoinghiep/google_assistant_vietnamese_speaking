import os
import yaml
import time

def get_config(request):
    stream = open('config.yaml','r')
    a = yaml.load(stream,Loader=yaml.SafeLoader)
    stream.close()
    a = a[request]
    return a
def set_config(topic,state):
    file_name = "config.yaml"
    with open(file_name) as f:
        doc = yaml.safe_load(f)
    doc[topic] = state
    with open(file_name, 'w') as f:
        yaml.safe_dump(doc, f, default_flow_style=False)        

