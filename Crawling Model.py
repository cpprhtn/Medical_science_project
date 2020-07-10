#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 22:10:42 2020

@author: cpprhtn
"""


'''

셀레니움을 이용하여 논문 검색에 들어감

첫번째 논문에 들어간 후

그 링크를 따옴

requests를 사용해 html을 찾은 뒤

필요한 내용만 따로 가져옴

LNTK 사용

불용어 처리 후 중요도 높은 단어 일부를 가져옴

타 검색결과에서도 적용됨 -> 범용성 인
'''



from selenium import webdriver
import pyautogui 
import time
import requests 



def get_URL(keyword):
    global url
    urlF = "https://journals.sagepub.com/action/doSearch?AllField=" 
    urlB = "&access=18"
    url = urlF + keyword + urlB
    return url


#selenium의 webdriver로 크롬 브라우저를 실행한다
driver = webdriver.Chrome("/Users/cpprhtn/Desktop/chromedriver")
#전체화면
driver.maximize_window()
 

#SAGE Journals에서 Corona에 대해 검색
get_URL("flu")
#"SAGE Journals"에 접속한다
driver.get(url)
 
#페이지의 제목을 체크하여 'SAGE'에 제대로 접속했는지 확인한다
assert "SAGE" in driver.title





#전체 화면 크기
pyautogui.size()

#현재 마우스 위치 확인
pyautogui.position

#마우스 절대주소로 이동
pyautogui.moveTo(500,692,3)


#왼쪽 버튼 클릭
pyautogui.mouseDown()
time.sleep(1)
pyautogui.mouseUp(button='left')
#pyautogui.click(600,572,button='left',clicks=1,interval=5)
#pyautogui.click(clicks=2, interval=2)
#pyautogui.doubleClick()
time.sleep(3)

#현재 url 가져오기
url = driver.current_url
url
 




#requests 크롤링
rs = requests.post(url) 

rs_code = rs.status_code 

if int(rs_code) == 200 :
    print("Okay") 
    rs_text = rs.text 
    print(rs_text) 
    
raw = rs.text
    


from bs4 import BeautifulSoup

#req = requests.get('https://journals.sagepub.com/doi/full/10.1177/0002039720925826')
#raw = req.text

html = BeautifulSoup(raw, 'html.parser')
infos = html.select('div.hlFld-Abstract')

print(infos[0])

clip1 = infos[0]
clip1_title = clip1.select_one('div.abstractSection')
print(clip1_title)

#테그값 제외
print(clip1_title.text)
clip = clip1_title.text
#브라우저를 종료한다
driver.close()



#불용어 처리
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import nltk
nltk.download('punkt')
import nltk
nltk.download('stopwords')

stop_words = set(stopwords.words('english')) 

word_tokens = word_tokenize(clip)

result = []
for w in word_tokens: 
    if w not in stop_words: 
        result.append(w) 

print(word_tokens) 
print(result) 
