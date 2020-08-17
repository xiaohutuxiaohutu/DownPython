import cfscrape
import cloudscraper

url = 'https://f.w24.rocks/viewthread.php?tid=383147&extra=page%3D1%26amp%3Borderby%3Ddateline%26amp%3Bfilter%3Ddigest'
scraper = cfscrape.create_scraper(delay=10)  # returns a CloudflareScraper instance
# Or: scraper = cfscrape.CloudflareScraper()  # CloudflareScraper inherits from requests.Session
# user_agent = cfscrape.get_tokens("http://somesite.com")
web_data = scraper.get("https://wallhere.com/").content
print(web_data)
# print(user_agent)
print(scraper.get(url))
# print(scraper.get(url).content)  # => "<!DOCTYPE html><html><head>..."
string = cfscrape.get_cookie_string()
# 实例化一个create_scraper对象
# scraper = cfscrape.create_scraper()
# 请求报错，可以加上时延
# scraper = cfscrape.create_scraper(delay = 10)
# 获取网页源代码

# web_data = scraper.get(url).content
# print(web_data)
