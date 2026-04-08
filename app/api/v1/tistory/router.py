from fastapi import APIRouter, Depends

from app.api.dependencies.tistory import get_tistory_post_service
from app.core.utils.response import success_response
from app.schemas.common import BaseResponse
from app.services.tistory.post import TistoryPostService


router = APIRouter(prefix="/tistory", tags=["tistory"])

@router.get('/', response_model=BaseResponse[dict])
def index():
    return success_response()


@router.get('/post', response_model=BaseResponse[dict])
async def publish_post(
    tistory_post_service: TistoryPostService = Depends(get_tistory_post_service)
):
    await tistory_post_service.do_post()
    return success_response()