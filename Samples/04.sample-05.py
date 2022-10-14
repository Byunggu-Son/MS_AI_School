# 환율 정보 가져오기
from currency_converter import CurrencyConverter

from urllib import response
cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')

print(cc.convert(1,'USD','KRW'))




# pip install BeautifulSoup4
import requests
from bs4 import BeautifulSoup

def get_exchange_rate(target, targer2):
    headers = {
        'User-Agent' : 'Mozilla/5.0', #최초 웹브는 mozilla. 모든 웹브에 다 있음. 표준규약으로 보여주라는뜻. 브라우저인척하기 위해서 user Agent써줌.
        'Content-Type' : 'text/html; charest=utf-8' # html을 요청하며 utf8을 요청한다는 뜻. 여기까지 2줄은 명함교환과 비슷
    }
    
    response =  requests.get('https://kr.investing.com/currencies/{}-{}'.format(target,targer2), headers=headers)

    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'data-test': 'instrument-price-last'})
    print(containers.text)

get_exchange_rate('usd','krw')