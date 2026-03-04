from fastapi import APIRouter


router = APIRouter(prefix="/tistory", tags=["tistory"])

@router.get('/')
def index():
    return {"message": "Hello tistory"}