import datetime
from flask import Flask
from flask import render_template
from flask_sockets import Sockets
import select
import time


app = Flask(__name__)
sockets = Sockets(app)
msg_log = []


@sockets.route('/chatsocket')
def chat_socket(ws):
    port = ws.environ['REMOTE_PORT']
    print dir(ws)
    print dir(ws.stream)
    print dir(ws.handler)
    print dir(ws.handler.socket)
    print ws.environ['wsgi.websocket'] == ws
    global msg_log
    msg_index = len(msg_log)
    msg_log.append('%s %s joined.' % (
            datetime.datetime.now().strftime('%H:%M'),
            port))

    while True:
        while msg_index < len(msg_log):
            ws.send(msg_log[msg_index])
            msg_index += 1

        rlist, wlist, xlist = select.select([ws.handler.socket], [], [], 1)
        for ready in rlist:
            message = ws.receive()
            if message is not None:
                msg_log.append('%s %s: %s' % (
                        datetime.datetime.now().strftime('%H:%M'), 
                        port,
                        message))


@app.route('/chat')
def chat():
    return render_template('chat.html')


@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
