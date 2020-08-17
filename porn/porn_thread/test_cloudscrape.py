import cloudscraper
import requests

session = requests.session()
url = 'https://f.w24.rocks/viewthread.php?tid=383147&extra=page%3D1%26amp%3Borderby%3Ddateline%26amp%3Bfilter%3Ddigest'
# scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
scraper = cloudscraper.create_scraper(delay=10, browser='chrome', sess=session)  # returns a CloudScraper instance
# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
print(scraper.get(url).text)  # => "<!DOCTYPE html><html><head>..."
