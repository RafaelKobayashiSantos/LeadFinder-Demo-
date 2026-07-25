async def scroll_to_bottom(page):
    """
    Função para rolar a página até o final.
    """
    feed = page.locator("div[role='feed']")

    for _ in range(5):

        await feed.evaluate("el => el.scrollTop = el.scrollHeight")

        await page.wait_for_timeout(300)  # aguarda 1 segundo para o carregamento dos elementos

    await feed.evaluate("el => el.scrollTop = 0")