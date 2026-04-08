import asyncio

from pathlib import Path

from app.core.config import config
from app.services.tistory.browser import TistoryBrowserService


tistory_browser_service = TistoryBrowserService()
tistory_storage = Path(config.STORAGE_PATH) / "tistory"
tistory_context = tistory_storage / "browser_context.json"


async def post():
    await tistory_browser_service.init_browser()
    context = await tistory_browser_service.load_context(tistory_context)
    page = await context.new_page()

    await page.goto("https://www.tistory.com", wait_until="domcontentloaded")
    page.once('dialog', lambda dialog: asyncio.create_task(dialog.dismiss()))

    async with context.expect_page() as new_page_info:
        await page.get_by_role('link', name='글쓰기').click()

    page = await new_page_info.value

    await page.locator('#post-title-inp').type('제목입니당...', delay=30)

    await page.wait_for_selector('#editor-tistory_ifr')

    frame = page.frame_locator('#editor-tistory_ifr')

    await frame.locator('#tinymce').type('본문 내용 입니당...', delay=30)

    await page.get_by_role('button', name='완료').click()

    await page.locator('input[name="basicSet"][value="20"]').check()

    await page.get_by_role('button', name='현재').click()

    await page.get_by_role('button', name='공개 발행').click()

    await tistory_browser_service.close_browser()