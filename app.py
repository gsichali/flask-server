from flask import Flask
import subprocess
import socket
import json, psutil, multiprocessing

app = Flask(__name__)

@app.route('/status')
def status():
    details = {}
    details['hostname'] = socket.gethostname()
    details['ip_address'] = socket.gethostbyname(socket.gethostname())
    details['cpu'] = multiprocessing.cpu_count()
    details['memory'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + "GB"
    return json.dumps(info, sort_keys=True, indent = 444)


if __name__ =='__main__':
    debug = True
    app.run(host='65.52.135.79')
