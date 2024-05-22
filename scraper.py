from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

"""import base64
from PIL import Image
import io"""


# Function to get HTML content of a page
def get_html(url):
    options = webdriver.FirefoxOptions()
    options.headless = True

    service = Service()

    driver = webdriver.Firefox(service=service, options=options)

    driver.get(url)
    driver.implicitly_wait(3)
    
    page_source = driver.page_source
    return page_source

def get_offers(html):
    soup = BeautifulSoup(html, 'html.parser')

    offers_parent = soup.find(class_="offers__container")
    offers = offers_parent.find_all("article")
    offer_dicts = []
    print(len(offers))
    for offer in offers:
        image_parent = offer.find(class_="offer-card__image-container")

        image_url = image_parent.find("img")["src"]
        image_tag = f'<img src="{image_url}"  width="200" height="200">'
        """image = requests.get(image_url).content
        loaded_image = io.BytesIO(image)
        image_b64 = base64.b64encode(loaded_image.read())"""

        price_text = image_parent.find(class_="priceSplashContainer").find(class_="sr-only").text
        
        details_parent = offer.find(class_="offer-card__details-container")

        title = details_parent.find(class_="offer-card__title").text
        
        description_parent = details_parent.find(class_="offer-card__text")
        descriptions = description_parent.find_all("span")
        full_description = ""
        for description in descriptions:
            full_description += description.text
        offer_dict = {"title":title, "price":price_text, "description":full_description, "image": image_tag }
        offer_dicts.append(offer_dict)
        
    return  offer_dicts


def scrape_ica_offers(url):
    html = get_html(url)
    if html:
        data = get_offers(html)
        return pd.DataFrame(data)
        
        
def save_offers(df):
    date_str = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    df.to_csv(f"./data/offers_{date_str}.csv")