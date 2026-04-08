from pathlib import Path

from app.core.config import config
from app.core.utils.file import ensure_directory
from app.services.tistory.browser import TistoryBrowserService


tistory_browser_service = TistoryBrowserService()
tistory_storage = Path(config.STORAGE_PATH) / "tistory"
ensure_directory(tistory_storage)
tistory_context = tistory_storage / "browser_context.json"


async def login():
    await tistory_browser_service.init_browser()
    context = await tistory_browser_service.create_context()
    page = await context.new_page()

    await page.goto("https://www.tistory.com", wait_until="domcontentloaded")

    await page.get_by_role('link', name='카카오계정으로 시작하기').click()

    await page.get_by_role('link', name='카카오계정으로 로그인').click()

    input('로그인 후 Enter 누르세요')

    await tistory_browser_service.save_context(context=context, path=tistory_context)

    await tistory_browser_service.close_browser()