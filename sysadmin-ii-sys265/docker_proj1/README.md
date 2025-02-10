# SYS265 - Mini Docker Project
flask web-chat app with docker
___


>[!Note]
> I've been learning some network programming lately, so most of the python is my own. but I did use AI for the Dockerfile, some of the javascript, and general troubleshooting (netwoking in a Docker container can get confusing)

## Project Structure
```
├── docker-chat
│   ├── app
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── templates
│   │       └── index.html
│   ├── docker-compose.yml
│   └── Dockerfile
```

___
## 1. create [app.py](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-ii-sys265/docker_proj1/app/app.py)
this is the python/flask backend for the web app. it will open a websocket on port 5000 and handle message sent over it.
```
from flask import Flask, render_template
from flask_socketio import SocketIO, send

# initialize flask and socketio
app = Flask(__name__)
socketio = SocketIO(app)

# default page
@app.route('/')
def index():
    return render_template('index.html')

# runs when message is received on socket
@socketio.on('message')
def handle_message(msg):
    print("message: " + msg)
    send(msg, broadcast=True)

# open websocket, listen on port 5000
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
```

## 2. create [index.html](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-ii-sys265/docker_proj1/app/templates/index.html)
this is the html frontend for the web page, as well as some javascript to be a medium between network connections and the frontend webpage
```
<!DOCTYPE html>
<html>
<head>
<title>sys265 chat</title>
</head>


<body>
<ul id="messages"></ul>
<input id="message_input" type="text">
<button onclick="sendMessage()">send</button>

<!-- import javascript sockets.io library-->
<script src="https://cdn.socket.io/4.0.1/socket.io.min.js"></script>

<script>

// create websocket object
const socket = io()

// update html when a message is sent/received
socket.on('message', function(msg) {
  let li = document.createElement('li');
  li.textContent = msg;
  document.getElementById('messages').appendChild(li);
});

// send message on socket when button is clicked
function sendMessage() {
  const message = document.getElementById('message_input').value;
  socket.send(message);
  document.getElementById('message_input').value = '';
}

</script>

</body>
</html>
```

## 3. create [requirements.txt](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-ii-sys265/docker_proj1/app/requirements.txt)
this includes necessary dependencies. they will be installed via Dockerfile
```
Flask==2.2.2
flask-socketio==5.3.2
werkzeug==2.2.2
```

## 4. create [docker-compose.yml](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-ii-sys265/docker_proj1/docker-compose.yml)
this defines the services to be used. while this could work without the chat-net network, creating an isolated network made setting this up simpley imo, especially since we are already running wordpress.
```
version: '3.8'

services:
  chat-server:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./app:/app
    networks:
      - chat-net

networks:
  chat-net:
    driver: bridge
```

## 5. create [Dockerfile](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-ii-sys265/docker_proj1/Dockerfile)
```
# use this version of python
FROM python:3.12-slim

# create a working directory and copy requirements file to it
WORKDIR /app
COPY app/requirements.txt /app/requirements.txt

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the files to working directory
COPY app /app

# run the python script when the container starts
CMD ["python", "app.py"]
```

## 6. run docker-compose
```
cd docker-chat
docker-compose up -d
```
![image](https://github.com/user-attachments/assets/5e739863-3710-4ea0-8988-2a9c56ddb981)
