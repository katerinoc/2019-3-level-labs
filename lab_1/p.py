import datetime
import requests

practice_date=datetime.date(2019,9,19)
print(practice_date)
print('Hello')
page_url='https://lenta.ru/rubrics/sport/'
lenta_sport_request=requests.get(page_url)
if lenta_sport_request.status_code==200:
    print('succesfull request')
    print(lenta_sport_request.text)
else:
    print('something went wrong')

