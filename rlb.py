import time
import cloudscraper
import requests
from bs4 import BeautifulSoup 

url = open('1.txt', 'r').read()
print("You Have Entered:")
print(url)
print("Checking Link!")

# ---------------------------------------------------------------------------------------------------------------------
if "toonworld4all" in url:
    site = requests.get(url)
    new = site.url
    t_code=new.split("token=", 1)[-1]
    url = "https://rocklinks.net/"+t_code
elif "takez.co" in url:
    t_code=url.split("token=", 1)[-1]
    url = "https://rocklinks.net/"+t_code
else:
    url = url
# ---------------------------------------------------------------------------------------------------------------------

def rocklinks_bypass(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    DOMAIN = "https://links.spidermods.in"
    url = url[:-1] if url[-1] == '/' else url

    code = url.split("/")[-1]
    final_url = f"{DOMAIN}/{code}?quelle="

    resp = client.get(final_url)
    
    soup = BeautifulSoup(resp.content, "html.parser")
    try:
        inputs = soup.find(id="go-link").find_all(name="input")
    except:
        return "Incorrect Link"
    data = { input.get('name'): input.get('value') for input in inputs }

    h = { "x-requested-with": "XMLHttpRequest" }
    
    time.sleep(6)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    try:
        return r.json()['url']
    except: return "Something went wrong :("

# -----------------------------------

print(rocklinks_bypass(url) ,file=open("2.txt", "w"))
