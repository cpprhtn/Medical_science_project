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
빅데이터를 통해 분류해둔 데이터를 기반으로 "A질병일 확률이 97%, 하지만 여기가 불확실 하기 때문에 B일 가능성이 3%가 남아있다." 식의 결론을 내려준다.</li>

<li><del>장현준이 수술을 할 때면</del><br>로니는 세계의 의학 학회저술지의 관련 수술법등을 검색하고, 환자에게 더 좋은 수술방법을 알려준다.

## 생각중인 구상방안
x-ray사진을 학습시켜 새 data에 대해 분류를 해보고,
또한 세계 유명 저널등에 대해 검색하여 같이 알려주는 방식을 만들어 볼 예정이다.

크롤링을 해서 문장에 대해 필요한 단어위주로 분석하여, 어떤 내용인지또한 간단히 나타나게 해보고 싶다.<br>
<del>사실 최근에 읽는중인 'Deep Learning from Scratch2'는 자연어처리에 대한 부분이였고, 이를 이용해 프로젝트도 만들어보고 싶어서 적용해볼 예정이다.<br>
아마 seq2seq와 어텐션 등을 적용해볼 예정</del>



# 일지
|Date|Description|Official source|
|:---:|---| --- |
|06_28|x-ray data|https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia|
|ㄴ|SAGE Journals|https://journals.sagepub.com/|
|ㄴ|Open access content only|https://journals.sagepub.com/action/doSearch?AllField=arrList&access=18|
|ㄴ|Only content to which I have full access|https://journals.sagepub.com/action/doSearch?AllField=arrList&access=user|
|ㄴ|arrList is you're looking for What||
|06_29|Start creating a prediction model||
|ㄴ|Images Load||
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
