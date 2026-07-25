from dataclasses import dataclass

@dataclass
class Config:

    '''Booleans'''

    headless: bool = True

    '''Integers'''

    wait_scroll: int = 3000
    wait_load: int = 5000
    max_pages: int = 100
    card_limit: int = 10

    '''Strings'''

    query: str = "cafeterias em Cotia"
    url: str = "https://www.google.com/maps/search/"