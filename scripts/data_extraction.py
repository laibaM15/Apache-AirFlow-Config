# data_extraction.py
import requests
from bs4 import BeautifulSoup

def extract_dawn():
    url = 'https://www.dawn.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article')
    data = []
    for article in articles:
        title = article.find('h2').text.strip() if article.find('h2') else 'No title'
        description = article.find('p').text.strip() if article.find('p') else 'No description'
        link = article.find('a')['href'] if article.find('a') else 'No link'
        data.append({'title': title, 'description': description, 'link': link})

    return data

def extract_bbc():
    url = 'https://www.bbc.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('div', class_='media__content')
    data = []
    for article in articles:
        title = article.find('h3').text.strip() if article.find('h3') else 'No title'
        description = article.find('p').text.strip() if article.find('p') else 'No description'
        link = article.find('a')['href'] if article.find('a') else 'No link'
        data.append({'title': title, 'description': description, 'link': link})

    return data

def main():
    dawn_data = extract_dawn()
    bbc_data = extract_bbc()
    return dawn_data + bbc_data

if __name__ == "__main__":
    combined_data = main()
    print(combined_data)

