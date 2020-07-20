# Medical_science_project

## 소설 "퍼펙트 써전"을 읽고 아이디어를 얻음
### *간략한 줄거리*
장현준 의사의 아버지가 사고를 당했으나 제대로 치료를 받지 못 하고 죽게되었고,

어머니는 희귀병으로 원인없이 아프게 되어,대학교 인턴을 하지 못하고 지인의 피부과 개인병원 시간제로 일한다.

어느날 인공지능을 개발하는 친구 회사에 가서 우연한 기회로 인공지능 로니가 몸에 흡수된다.

로니의 도움으로 훌륭한 의사가 되는 장현준의 이야기이다.


## 얻게 된 아이디어
인공지능 로니가 의사 장현준에게 어떠한 영항을 끼쳤는지를 위주로 소설을 다시 한번 읽어보았다.<br>

<li><del>장현준의 시각(로니가 장현준의 신체를 분석하여 시각[전반적인 신체능력]을 강화시켜줌)을 통해 환자의 x-ray를 보고,</del><br>
빅데이터를 통해 분류해둔 데이터를 기반으로 "A질병일 확률이 97%, B일 확률이 3% 남아있다." 식의 결론을 내려준다.</li>

<li><del>장현준이 수술을 할 때면</del><br>로니는 세계의 의학 학회저술지의 최신 수술법등을 검색하고, 환자에게 더 좋은 방향의 수술방법을 알려준다.

## 생각중인 구상방안
<del>x-ray사진을 학습시켜 새 data에 대해 분류를 해보고,
또한 세계 유명 저널등에 대해 검색하여 같이 알려주는 방식을 만들어 볼 예정이다.
크롤링을 해서 문장에 대해 필요한 단어위주로 분석하여, 어떤 내용인지또한 간단히 나타나게 해보고 싶다.<br>
사실 최근에 읽는중인 'Deep Learning from Scratch2'는 자연어처리에 대한 부분이였고, 이를 이용해 프로젝트도 만들어보고 싶어서 적용해볼 예정이다.
아마 seq2seq와 어텐션 등을 적용해볼 예정이다.</del>


x-ray사진을 학습시켜 새로 들어온 사진에 대해 예측해보고, 예측한 병명을 가지고 SAGE Journals 에서 검색하여 가장 최신 논문 하나를 크롤링해온다.

크롤링해온 단어들중 불용어들을 삭제한 후 나머지 단어들을 가지고 크롤링한 논문에 대한 요약문을 제시해준다.

결과적으로, 이미지 하나를 제시해주면, 예측한 병명과, 이 병명에 대한 가장 최신 논문, 그리고 그 논문의 요약본을 알려주는 모델을 만드는 프로젝트이다.



# 일지
|Date|Description|Official source(참고 주소)|
|:---:|---| --- |
|06_28|x-ray data|https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia|
|ㄴ|SAGE Journals|https://journals.sagepub.com/|
|ㄴ|Open access content only|https://journals.sagepub.com/action/doSearch?AllField=arrList&access=18|
|ㄴ|Only content to which I have full access|https://journals.sagepub.com/action/doSearch?AllField=arrList&access=user|
|ㄴ|arrList is you're looking for What||
|06_29|Start creating a prediction model||
|ㄴ|Images Load||
|06_30|Data preprocessing|https://youtu.be/sDG5tPtsbSA|
|07_01|Hyperparameter Definition||
|ㄴ|Learning Conv2D & Maxpool|https://tykimos.github.io/2017/01/27/CNN_Layer_Talk/|
|07_02|Fully Connected Layers(FC)|https://missinglink.ai/guides/convolutional-neural-networks/fully-connected-layers-convolutional-neural-networks-complete-guide/|
|ㄴ|Build model||
|ㄴ|Conv2D + Maxpool + Conv2D + FC + FC + softmax||
|07_03|Test_Crawling||
|ㄴ|BeautifulSoup4|HTTPError: Forbidden|
|ㄴ|requests|Success|
|ㄴ|selenium|Success|
|07_04|Crawling Model||
|07_05|Get confirmation selenium||
|07_06|Crawling Html||
|ㄴ|Learning NLTK|https://datascienceschool.net/view-notebook/8895b16a141749a9bb381007d52721c1/|
|07_07|Test NLTK||
|07_08|selenium -> url -> crawling -> requests -> html||
|ㄴ|Using pyautogui||
|07_09|requests or BeautifulSoup4|requests = string type, BeautifulSoup4 = Html type|
|ㄴ|selenium -> url -> crawling -> requests -> BeautifulSoup4 -> NLTK||
|ㄴ|Learning seq2seq + attention|https://lovit.github.io/machine%20learning/2019/03/17/attention_in_nlp/|
|ㄴ|Learning BERT|https://keep-steady.tistory.com/19|
|07_10|Stopword processing|Secure versatility|
|ㄴ||https://wikidocs.net/45101|
|ㄴ|Text preprocessing|Clear|
|ㄴ|Vanilla Rnn|Embedding Vector = 10, hidden size = 32|
|07_11|Learning LSTM Text Classification|https://medium.com/analytics-vidhya/neural-network-lstm-example-of-text-classification-398e01cab054|
|ㄴ|LSTM|Embedding Vector = 10, hidden size = 128|
|07_12|Modify the LSTM code||
|07_13|Learning seq2seq|https://tykimos.github.io/2018/09/14/ten-minute_introduction_to_sequence-to-sequence_learning_in_Keras/|
|ㄴ|Learning Attention|https://medium.com/platfarm/%EC%96%B4%ED%85%90%EC%85%98-%EB%A9%94%EC%BB%A4%EB%8B%88%EC%A6%98%EA%B3%BC-transfomer-self-attention-842498fd3225|
|07_14|Add Cnn Prediction Model||
|ㄴ|Vanilla Cnn||
|07_15|Trying to convert it to a library||
|ㄴ|__init__py, P_Model()||
|07_17|Finish Medical_science_project||



#  Final model

Prediction_Model.py -> Crawling_Model.py -> Text_preprocessing -> LSTM_text.py *OR* Vanilla_Rnn.py


#


# 느낀점 & 아쉬운점
생각보다 x-ray data가 없어서 아쉽다

x-ray학습 정확도를 더 높이지 못해서 아쉽다.

"밑바닥 부터 시작하는 딥러닝"이라는 책이 손글씨 구별학습을 목표로 신경망을 하나하나 구현해 나가는 책이였는데,

이책을 읽을때와, 따라해볼때, 또 개인프로젝트에 적용해볼때 다 다르다는 것을 느꼈고,

아직은 실력이 많이 부족함을 느꼈다. 공부를 더 많이 해서 더 효율적이고, 더 정확한 모델을 만들어 보고싶다.

# About SAGE Journals
세계 상위권 임팩트 팩터를 보여줌<br>
또한 다양한 지원을 통해 질 높은 논문내용이 올라옴<br>
## Impact Factor & Ranking Results
From the Journal Citation Reports (Web of Science Group, 2019)

With 627 journals now ranked in the JCR, SAGE continues to experience consistent growth within the reports, achieving a 22% increase over the past five years. In this year’s reports, 90 SAGE journals have received a top 10 category rank, with 6 journals receiving their first Impact Factor (IF). 192 titles are now placed in the top 30% of the JCR, and 53% of SAGE journals are ranked within the top half of their subject category. In the 2018 release, SAGE publishes the market leading journal within 16 categories (14 SSCI and 2 SCI) shown below.

A 17% increase in coverage in the SSCI over the last five years means that there are now 420 SAGE journals in the SSCI. 69% of the SSCI journals received an increased IF, of which 11 are newly acquired titles ranked in the 2018 release. 126 journals are now placed in the top 25% of the JCR rankings for their category.

In the 2018 release SAGE publishes the market-leading journal within 14 SSCI categories: Criminology & Penology; Cultural Studies; Education & Educational Research; Education, Special; Family Studies; History; Psychology, Applied; Psychology, Multidisciplinary; Psychology, Psychoanalysis; Psychology, Social; Rehabilitation (SSCI); Social Sciences, Interdisciplinary; Social Work; and Women’s Studies.

Over the last five years, SAGE has seen a 40% increase in the number of titles in the SCI index, primarily due to strategic acquisitions and organic growth across the medical, engineering and technology disciplines, with SAGE now being marked out as one of the top five publishers of medical journals in the world. SAGE continues to significantly grow its coverage within SCI with 254 journals now ranked and 38 journals in the top 25% of their SCI category.

In the 2018 release SAGE publishes the market leading journal within 2 SCI categories: Materials Science, Characterization and Testing; and Orthopedics. By 5 year Impact Factor, SAGE publishes the market-leading journal in Materials Science, Characterization and Testing; and Orthopedics.<br>
출처 | https://uk.sagepub.com/en-gb/asi/impact-factor-ranking-results
