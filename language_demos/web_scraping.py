import re
import requests


web_sites = [
    "https://finance.yahoo.com/quote/GME?p=GME&.tsrc=fin-srch"
]

r = re.compile(r'data-reactid="55">(.*?)</span>', re.MULTILINE)


for web_site in web_sites:

    response = requests.get(web_site)
    content = response.text

    with open("gme_price.txt", "a") as price_file:
        price_file.write(r.findall(content)[2] + "\n")
