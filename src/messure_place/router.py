from fastapi import APIRouter, Body

from .dependencies import CreateMessurePlaceData
from .service import create_messure_place as create_messure, get_all

router = APIRouter()


@router.post("/merohely")
async def create_messure_place(data: CreateMessurePlaceData = Body()):
    return await create_messure(dict(data))


@router.get("/merohely")
async def get_merohely():
    return await get_all()
