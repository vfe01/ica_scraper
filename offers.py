from scraper import scrape_ica_offers
from datetime import datetime

def get_week_number():
    return datetime.now().isocalendar()[1]

class Offers():
    def __init__(self, url):
            print("init")
            self.url = url
            self.scrape()
                
    def scrape(self):
        self.offers_data =  scrape_ica_offers(self.url)
        self.offers_week = get_week_number()

    def get_latest(self):
        if self.offers_week != get_week_number():
            self.scrape()
    
    def to_html(self):
         return self.offers_data.to_html(index=False, classes="data", escape=False, table_id="fixed-table")



