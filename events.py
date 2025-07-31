import cloudscraper
from bs4 import BeautifulSoup
import re
import json

scraper = cloudscraper.create_scraper()

def get_clean_card(card):
    remove_duplicate_backslash = re.sub("\\n\n*", "\n", card)
    remove_extra_space = re.sub(r"\ {2,}", " ", remove_duplicate_backslash)
    remove_non_breaking_space = re.sub(r"\xa0", "", remove_extra_space)
    clean_text = remove_non_breaking_space
    cards_clean = clean_text.split("\n")
    cards_clean = [element for element in cards_clean if len(element) > 2]
    return cards_clean

def store_events(events: str, name:str):
    events_json = json.dumps(events, indent=4)
    with open(name, "w") as outfile:
        outfile.write(events_json)

def get_events(date_start: str, date_end: str) -> json:
    """scrape all the events from parisbouge

    Args:
        date_start and date_end (str): the date we want to scrape in the following format YEAR-MONTH-DAY

    Returns:
        json: returns a json file containing all the events
    """
    pages = 1
    events = []
    max_pages = 10

    while True:
        print(f"Scraping page number {pages}")
        url = f"https://www.parisbouge.com/search?type=event&category=&date_start={date_start}&date_end={date_end}&page={pages}"
        response = scraper.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.find_all("div", class_=["card", "bg"])

        current_events = []
        clean_cards = {}
        columns = ["image_url", "category", "title", "date", "location", "organizer"]
        for card in cards:
            clean_cards = {}
            cards_text = get_clean_card(card.text) # Get the text
            img_tag = card.find("img") # Get the img
            if img_tag and img_tag.get("src"):
                clean_cards[columns[0]] = img_tag["src"]
            clean_cards[columns[1]] = cards_text[0]
            clean_cards[columns[2]] = cards_text[1]
            clean_cards[columns[3]] = cards_text[2]
            clean_cards[columns[4]] = cards_text[3]
            try:
                clean_cards[columns[5]] = cards_text[4]
            except:
                clean_cards[columns[5]] = ""
            current_events.append(clean_cards)
        
        events += current_events

        if len(current_events) <= 0:
            print("No more pages")
            break
        elif pages > max_pages:
            break
        else:
            pages += 1
            
    return events



