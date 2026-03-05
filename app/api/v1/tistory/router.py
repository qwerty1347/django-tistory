from fastapi import APIRouter

from app.core.utils.response import success_response


router = APIRouter(prefix="/tistory", tags=["tistory"])


@router.get('/')
def index():
    return success_response()