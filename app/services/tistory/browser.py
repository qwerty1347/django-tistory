from playwright.async_api import Browser, BrowserContext, Playwright, async_playwright


class TistoryBrowserService:
    def __init__(self):
        self.playwright: Playwright | None = None
        self.browser: Browser | None = None


    async def init_browser(self, headless=False):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=headless)


    async def create_context(self) -> BrowserContext:
        return await self.browser.new_context()


    async def load_context(self, path: str) -> BrowserContext:
        return await self.browser.new_context(storage_state=path)


    async def save_context(self, context: BrowserContext, path: str):
        await context.storage_state(path=path)


    async def close_browser(self):
        await self.browser.close()
        await self.playwright.stop()