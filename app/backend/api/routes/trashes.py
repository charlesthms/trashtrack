from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def trashes_list():
    return {"Hello": "World"}


@router.get("/{trash_id}")
def trash_details(trash_id: int):
    return {"Hello": "World"}


@router.get("/count/{limit}")
def trash_details(limit: int):
    return {"Hello": "World"}
