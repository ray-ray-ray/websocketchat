'''
Chat using web sockets

RAY 20131223
'''
import datetime
from flask import Flask
from flask import render_template
from flask_sockets import Sockets
import select
import time


#
# Global app, sockets, and message history
#
app = Flask(__name__)
sockets = Sockets(app)
msg_log = []


@sockets.route('/chatsocket')
def chat_socket(ws):
    '''
    Read/write on the chatsocket.
    '''
    #
    # Use port as chat handle and add a "join" message to the history.
    #
    port = ws.environ['REMOTE_PORT']
    global msg_log
    msg_index = len(msg_log)
    msg_log.append('%s %s joined.' % (
            datetime.datetime.now().strftime('%H:%M'),
            port))

    #
    # Read/write loop
    #
    while True:
        #
        # Send the remaining history.
        #
        while msg_index < len(msg_log):
            ws.send(msg_log[msg_index])
            msg_index += 1

        #
        # For 1 second, try to read the socket.
        #
        rlist, wlist, xlist = select.select([ws.handler.socket], [], [], 1)
        for ready in rlist:
            #
            # If there's a message waiting on the socket, read it and
            # add it to the history.
            #
            message = ws.receive()
            if message is not None:
                msg_log.append('%s %s: %s' % (
                        datetime.datetime.now().strftime('%H:%M'), 
                        port,
                        message))


@app.route('/chat')
def chat():
    '''
    Serve the chat UI
    '''
    return render_template('chat.html')


@app.route('/')
def hello():
    '''
    Am I alive?
    '''
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
