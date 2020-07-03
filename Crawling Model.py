#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 22:10:42 2020

@author: cpprhtn
"""


'''

X-ray 예측결과가 암일 경우

'''
import requests 
urlF = "https://journals.sagepub.com/action/doSearch?AllField=" #front

Prediction = "cancer"

urlB = "&access=18" #back



url = urlF + Prediction + urlB

rs = requests.post(url) 

rs_code = rs.status_code 

if int(rs_code) == 200 :
    print("Okay") 
    rs_text = rs.text 
    print(rs_text) 
    
else : 
    print(rs_code) 
    print("Fail")​