import re
import pandas as pd

def cleaning(link: str, plus_code: str, card_content: str, title: str) -> dict:

    # Using the title to extract the place name and coordinates (latitude and longitude)

    place_name = title.split(' - ')[0].strip()

    # Using regex to extract the rating from the card content

    rate = re.search(r'(\d+,\d+)', card_content).group(1) if rate else None

    # Using regex to extract latitude and longitude from the link

    match = re.search(r'!3d(-?\d+\.\d+)!4d(-?\d+\.\d+)', link)

    if match:
        latitude = match.group(1)
        longitude = match.group(2)

    # Cleaning the Plus Code by removing any unwanted characters

    pcode = plus_code.split(" ")[0]
    pcode = pcode.replace("", "")
    location = plus_code.replace(pcode, "")\
        .strip()

    # Extracting neighborhood, city, and state from the location string

    neighborhood = location.split(",")[0]\
        .strip()
    
    city = location.split(",")[1]\
        .split(" - ")[0]\
        .strip()

    state = location[-2:].strip()

    return {

        #--- Strings

        "card_url": link,
        "plus_code": pcode,
        "place_name": place_name,
        "neighborhood": neighborhood,
        "city": city,
        "state": state,

        #--- Floats

        "rating": rate,
        "latitude": latitude,
        "longitude": longitude
    }