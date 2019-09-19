from bs4 import BeautifulSoup
import requests


page_url='https://lenta.ru/rubrics/sport/'
lenta_sport_request=requests.get(page_url)

lenta_sport_content=lenta_sport_request.text
if lenta_sport_request.status_code==200:
    print('succesfull request')
  #  print(lenta_sport_content)
else:
    print('something went wrong')

parsed_page=BeautifulSoup(lenta_sport_content)

print(type(parsed_page))

print(parsed_page.title.text)