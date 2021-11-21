from fastapi import APIRouter

from controllers import animais_controller as animais

router = APIRouter()

router.include_router(animais.router, prefix='/animais')