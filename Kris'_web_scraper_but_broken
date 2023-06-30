import requests
from bs4 import BeautifulSoup

#let's build a web scraper

def main():
    symbol = "AAPL"
    URL = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"
    headers = {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

    #request page
    response = requests.get(URL, headers=headers)
    
    #parse html using beautifulsoup
    soup = BeautifulSoup(response.text, 'html.parser')

    #use 'table' or 'tr' or 'td'. That was descending order
    #dictionaries are good because you can save value PAIRS
    stock_dictionary = {}
    counter = 1
    for cell in soup.find_all('td'):
        if counter % 2 != 0:
                key = cell.text
        else:
             value = cell.text
             stock_dictionary
        counter += 1
        print(cell.text)

main()
