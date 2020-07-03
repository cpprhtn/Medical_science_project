#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:56:41 2020

@author: cpprhtn
"""

#BeautifulSoup 실패
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://journals.sagepub.com/action/doSearch?AllField=arrList&access=18")  
#HTTPError: Forbidden


bsObject = BeautifulSoup(html, "html.parser") 


print(bsObject)



#requests 성공
import requests 
urlF = "https://journals.sagepub.com/action/doSearch?AllField=" 

urlB = "&access=18"



url = urlF + urlB

rs = requests.post(url) 

rs_code = rs.status_code 

if int(rs_code) == 200 :
    print("Okay") 
    rs_text = rs.text 
    print(rs_text) 
    
else : 
    print(rs_code) 
    print("Fail")​





#selenium 성공
from selenium import webdriver
 
#selenium의 webdriver로 크롬 브라우저를 실행한다
driver = webdriver.Chrome("/Users/cpprhtn/Desktop/chromedriver")
 
#"SAGE Journals"에 접속한다
driver.get("https://journals.sagepub.com/")
 
#페이지의 제목을 체크하여 'SAGE'에 제대로 접속했는지 확인한다
assert "SAGE" in driver.title
 
#검색 입력 부분에 커서를 올리고
#검색 입력 부분에 다양한 명령을 내리기 위해 elem 변수에 할당한다
elem = driver.find_element_by_name("id")
 
#입력 부분에 default로 값이 있을 수 있어 비운다
elem.clear()
 
#검색어를 입력한다
elem.send_keys("Selenium")
 
#검색을 실행한다
elem.submit()
 
#검색이 제대로 됐는지 확인한다
assert "No results found." not in driver.page_source
 
#브라우저를 종료한다
driver.close()
