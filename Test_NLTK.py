#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:07:36 2020

@author: cpprhtn
"""


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import nltk
nltk.download('punkt')
import nltk
nltk.download('stopwords')

example = "The South African response in dealing with the Corona pandemic needs to speak to the realities of <i>all</i> people living in the country, including migrant and refugee communities. Reflecting on this in light of ongoing research on the political stakes of migration governance, we find that the virus response shows little change in the government agenda when it comes to dealing with refugees and other migrants. Veritably, we see that the pandemic may even be an excuse for pushing through already-aspired to policies. This includes the securitised agenda behind the sudden building of a border fence to close off Zimbabwe and the xenophobic-rhetorical clout behind the lockdown rules about which shops are allowed to remain open. The temporary stay on renewing asylum seekers permits counts as a perfunctory exception. We show that each of these developments very much play into politics as usual."
stop_words = set(stopwords.words('english')) 

word_tokens = word_tokenize(example)

result = []
for w in word_tokens: 
    if w not in stop_words: 
        result.append(w) 

print(word_tokens) 
print(result) 
