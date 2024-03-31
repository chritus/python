import requests 
from bs4 import BeautifulSoup

try:
    url = "https://jiji.com.gh/"
    source = requests.get(url)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
 
    print(soup)
except Exception as e:
    print("there was an error")
