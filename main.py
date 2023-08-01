
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.security import HTTPBasic, OAuth2PasswordRequestForm
from starlette.responses import HTMLResponse

#from Controllers.network_controller import make_network, get_network
from Controllers.device_controller import view_filter_devices, view_client_devices
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, HTTPException, status, Body, Response, encoders, Request

from Authentication.login import User, get_current_active_user, authenticate_user, Token, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from Authentication.check_if_user_db import User, UserInDB


app = FastAPI()

templates = Jinja2Templates(directory="templates")

security = HTTPBasic()

NETWORK_PATH = "/network"

USER_PATH = "/technician"


@app.post("/login", response_model=Token)
async def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    # Depends() can be problem perphaps not empty auto2
    print("form_data.username: ", form_data.username)
    user = await authenticate_user(form_data.username, form_data.password)
    print("user: ", user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user['user_name']}, expires_delta=access_token_expires
    )
    response.set_cookie(
        key="Authorization", value=f"Bearer {encoders.jsonable_encoder(access_token)}",
        httponly=True
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    print(f"got current active user from controller {current_user}  type  {type(current_user)} ")
    return current_user


# @app.get("/users/me/items/")
# async def read_own_items(current_user: User = Depends(Authentication.login.get_current_active_user)):
#     return [{"item_id": "Foo", "owner": current_user.username}]


# @app.get("/network/{network_id}/visualization/", response_class=HTMLResponse)
# async def visualize_network(request: Request, network_id: int):
#     # Fetch the network data using the network_id (you need to implement this)
#     network_data = get_network_data_from_db(network_id)
#     if not network_data:
#         raise HTTPException(status_code=404, detail="Network not found")
#
#     # Render the HTML template with the network_id and network_data
#     return templates.TemplateResponse("network_visualization.html", {"request": request, "network_id": network_id})
#
# @app.post(f"{NETWORK_PATH}/create_network")
# async def create_network(pcap_file, client_id, date_taken, premise_name, technician_name):
#     return await make_network(pcap_file, client_id, date_taken, premise_name, technician_name)
#
#
# @app.get(f"{NETWORK_PATH}/view_network")
# async def view_network(network_id):
#     return await get_network(network_id)
#
#
# @app.get(f"{NETWORK_PATH}/get_filtered_devices")
# async def get_filtered_devices(network_id, condition):
#     return await view_filter_devices(network_id, condition)
#
#
# #NTH
# @app.get(f"{NETWORK_PATH}/get_client_devices")
# async def get_client_devices(client_id):
#     return await view_client_devices(client_id)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
