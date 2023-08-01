from fastapi import Depends, FastAPI
import uvicorn
from fastapi import FastAPI, Form, UploadFile, File
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from Authentication.login import is_technician
from Controllers.network_controller import make_network, get_network
from Controllers.device_controller import view_filter_devices, view_client_devices


app = FastAPI()

security = HTTPBasic()

NETWORK_PATH = "/network"

USER_PATH = "/technician"


@app.get("/")
async def root():
    return "welcome to team 6 project!"


@app.post(f"{USER_PATH}/login")
async def login(password, user_name):
    return await is_technician(password, user_name)


@app.post(f"{NETWORK_PATH}/create_network")
async def create_network(file: UploadFile = File(...), client_id: int = Form(...), premise: str = Form(...), technician_name: str = Form(...)):
    file_content = await file.read()
    date_taken = '2023-07-01'
    is_success = await make_network(file_content, client_id, premise, date_taken, technician_name)
    return is_success


@app.get(f"{NETWORK_PATH}/view_network")
async def view_network(network_id):
    return await get_network(network_id)


@app.get(f"{NETWORK_PATH}/get_filtered_devices")
async def get_filtered_devices(network_id, condition):
    return await view_filter_devices(network_id, condition)


# NTH
@app.get(f"{NETWORK_PATH}/get_client_devices")
async def get_client_devices(client_id):
    return await view_client_devices(client_id)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
