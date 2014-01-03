websocketchat
=============

Proof of concept chat app using websockets

1. git clone https://github.com/ray-ray-ray/websocketchat.git
2. virtualenv websocketchat
3. cd websocketchat
4. source bin/activate
5. pip install -r requirements.txt
6. python websocketchat.py (to test flask setup)
7. gunicorn -k flask_sockets.worker websocketchat:app (to start server for chat)
8. http://127.0.0.1:8000/chat