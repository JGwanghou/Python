"""
날짜 : 2023/01/17
이름 : 조광호
내용 : 파이썬 기상청 날씨 크롤링 실습하기
"""
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
conn = pymysql.connect(host='127.0.0.1',
                        user='root',
                        password='1234', 
                        db='java2db', 
                        charset='utf8')
cur = conn.cursor()

# 가상 브라우저 실행
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

# 페이지 이동
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# tr들 받아온다
trs = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')

for tr in trs:
    tds = tr.find_elements(By.CSS_SELECTOR, 'td')
    
    # sql 실행
    sql = "insert into `Weather` values ('a401', '노왕짱', '010-9253-9512', '26')"
    conn.commit()
    conn.close()
        


# 가상 브라우저 종료
browser.close()
