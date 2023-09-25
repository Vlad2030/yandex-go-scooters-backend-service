from fastapi import APIRouter
from routers.routes import ping
from routers.routes.auth import auth
from routers.routes.scooters import scooters
from routers.routes.scooters.accumulator import accumulator
from routers.routes.scooters.battery import battery
from routers.routes.scooters.block import block
from routers.routes.scooters.price import price
from routers.routes.scooters.sound import sound
from routers.routes.scooters.test import test
from routers.routes.scooters.unblock import unblock
from routers.routes.users import users
from routers.routes.users.roles import roles


def create_api_router() -> APIRouter:
    api_router = APIRouter()
    api_router.include_router(auth.router, tags=["auth"])
    api_router.include_router(scooters.router, tags=["scooters"])
    api_router.include_router(accumulator.router, tags=["scooters"])
    api_router.include_router(battery.router, tags=["scooters"])
    api_router.include_router(block.router, tags=["scooters"])
    api_router.include_router(price.router, tags=["scooters"])
    api_router.include_router(sound.router, tags=["scooters"])
    api_router.include_router(test.router, tags=["scooters"])
    api_router.include_router(unblock.router, tags=["scooters"])
    api_router.include_router(users.router, tags=["users"])
    api_router.include_router(roles.router, tags=["roles"])
    api_router.include_router(ping.router, tags=["default"])
    return api_router


router = create_api_router()
