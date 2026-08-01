import re
import pandas as pd

def cleaning(link: str, plus_code: str, card_content: str, title: str) -> dict:

    # Using the title to extract the place name and coordinates (latitude and longitude)

    place_name = title.split(' - ')[0].strip()

    # Using regex to extract the rating from the card content

    match = re.search(r'\d+[.,]\d+', card_content)

    if match:
        rate = float(match.group().replace(",", "."))
    else:
        rate = None

    # Using regex to extract latitude and longitude from the link

    match2 = re.search(r'!3d(-?\d+\.\d+)!4d(-?\d+\.\d+)', link)

    if match2:
        latitude = match2.group(1)
        longitude = match2.group(2)

    # Cleaning the Plus Code by removing any unwanted characters

    pcode = plus_code.split(" ")[0]
    pcode = pcode.replace("", "")
    location = plus_code.replace(pcode, "")\
        .strip()

    return {

        #--- Strings

        "card_url": link,
        "plus_code": pcode,
        "place_name": place_name,
        "location": location,

        #--- Floats

        "rating": rate,
        "latitude": latitude,
        "longitude": longitude

    }