# 네이버에서 날씨 웹크롤링
# %%
from bs4 import BeautifulSoup
import requests

html = requests.get(
    'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%8C%8D%EB%AC%B8%EB%8F%99+%EB%82%A0%EC%94%A8')
soup = BeautifulSoup(html.text, 'html.parser')

# 위치
address = soup.find('div', {'class': 'title_area _area_panel'}).find(
    'h2', {'class': 'title'}).text
print(address)

# 날씨정보
temperautre = soup.find('div', {'class': 'weather_info'})

# 현재 온도
weatherStatus = soup.find(
    'div', {'class': 'temperature_text'}).text.strip()[5:]
print(weatherStatus)

# 날씨 상태
air = soup.find('ul', {'class': 'today_chart_list'})
infos = air.find_all('li', {'class': 'item_today'})
# 날씨정보는 4개가 각각 클래스명인 item_today뒤에 level1 level3 ..등으로 붙는데 빼면 다 포함해서 인식이 된다?
# %%
for info in infos:
    print(info.text.strip())

print('*'*100)
# 시간대별 날씨
weatherTime = soup.find_all('li', {'class': '_li'})
# soup.find('li',{'class':'tomorrow _li _day'}).decompose()
# decompose() 일회성으로 해당 태그를 삭제하기에 사용했으나, 내일이 적힌 날씨정보만 없어지고 01시부터 다시 시작하기에 실패.

# 중복된 결과로 3번 나오기에 수정.
# for i in weatherTime:
#     print(i.text.strip())

print('*'*100)
# 위의 결과를 수정하여 오늘의 시간별 날씨 정보만을 가지고 옴.
for i in weatherTime:
    if '내일' not in i.text:
        print(i.text.strip())
    else:
        break
print('*'*100)
# 함수를 사용해서 지역 날씨를 입력하면 네이버 날씨에서 해당 지역 날씨 정보를 가져오게 코딩해보자!~


def WeatherTimeREigon(gu, dong, weathers):

    html = requests.get(
        f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={gu}+{dong}+{weathers}')
    soup = BeautifulSoup(html.text, 'html.parser')
    address = soup.find('div', {'class': 'title_area _area_panel'}).find(
        'h2', {'class': 'title'}).text

    weatherStatus = soup.find(
        'div', {'class': 'temperature_text'}).text.strip()[5:]
    print(address, weatherStatus)
    
    air = soup.find('ul', {'class': 'today_chart_list'})
    infos = air.find_all('li', {'class': 'item_today'})
    for info in infos:
        print(info.text.strip())
    weatherTime = soup.find_all('li', {'class': '_li'})
    for i in weatherTime:
        if '내일' not in i.text:
            print(i.text.strip())
        else:
            break

# 지역명과 날씨를 쳐서 작동여부 확인하기
WeatherTimeREigon('도봉구', '쌍문동', '날씨')
# %%
