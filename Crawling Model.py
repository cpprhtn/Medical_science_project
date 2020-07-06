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

불용어 처리 후 중요도 높은 단어 일부를 가져옴


'''

urlF = "https://journals.sagepub.com/action/doSearch?AllField=" 

search = "corona"

urlB = "&access=18"



url = urlF + search + urlB


from selenium import webdriver
 
#selenium의 webdriver로 크롬 브라우저를 실행한다
driver = webdriver.Chrome("/Users/cpprhtn/Desktop/chromedriver")
 
#"SAGE Journals"에 접속한다
driver.get(url)
 
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
