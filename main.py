from fastapi import FastAPI, WebSocket
import uvicorn

app = FastAPI()


@app.websocket("/ws/appData/")
async def echo(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"msg": "Hello from Uvicorn"})
    while True:
        data = await websocket.receive_text()
        print('Message received: ', data)
        await websocket.send_text(data + ' /from server')


@app.get("/nursing/initial_load")
async def read_root():
    msg = {"hello": "World by uvicorn and fastapi"}
    return msg

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")

# Los mensajes http y ws son respondidos.
# El front acusa problemas de cors pero
# en http://0.0.0.0:8000/nursing/initial_load del navegador se ve la respuesta