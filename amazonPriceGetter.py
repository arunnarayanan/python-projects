import bs4, requests

price_selector = '#price'

def getAmazonPrice(productUrl):
    res = requests.get(productUrl, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    })
    res.raise_for_status()
    print(res.status_code)
    print(res.text)
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    elems = soup.select(price_selector)
    print(elems)
    price = elems[0].text.strip()
    print(f'The Price is: {price}')
    return price
    
    
if __name__ == '__main__':
    url = input('Enter the amazon product page url : ')
    if len(url) > 10:
        price = getAmazonPrice(url)
        print(price)
    else:
        raise Exception("You need to enter a valid Amazon Product URL") 
    
    