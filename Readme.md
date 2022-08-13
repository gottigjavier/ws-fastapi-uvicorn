## App

The app returns two responses:

- http GET: JSON
- sw echo: JSON

Domains (0.0.0.0, 127.0.0.1)

Port: 8000

http://127.0.0.1:8000/nursing/initial_load
returns JSON to GET request

127.0.0.1:8000/ws/appData/
establishes the connection 

Send "message" returns "message /from server"

### Without Docker

Start app:

$ uvicorn main:app --reload


### With Docker

Use DockerHub image:

https://hub.docker.com/r/dizzbo/uvicorn-fastapi-docker

Build image:

$  docker build -t nameimage .


Start app:

$ docker run -p 8000:80 nameimage

You will ca read:

INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)

but port still be: 8000
