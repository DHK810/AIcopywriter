# AI copywriter

- 아이디어 creating과정에서 가장 어려운게 맨 처음이다. 
- 이 과정을 줄이고 마지막 수정 작업만 할 수 있도록 도와주기 위한 AI copywriter

책, 안경, 지갑, 약, 음료, 담배 뭐가 되었던 입력값은 산업 분야와 제품군이다. 

기존 포스터, 카피로 학습된 모델로 새로운 문장을 만들어 낸다.

포스터, 카피는 대부분 이미지로 있기 때문에 이미지 읽는 패키지 필요.

지금의 목표는 하나의 산업 또는 하나의 제품 디스플레이 광고에 들어가는 카피 추천해주는 AI만들기.

![1569026220143](C:\Users\15Z970-GA5BK\AppData\Roaming\Typora\typora-user-images\1569026220143.png)



### 광고카피 올라오는 사이트:

1. https://www.adsoftheworld.com/?terms=&medium=484&industry=22&country=473
2. http://creativecriminals.com/archive/country:usa/category:print 프린트 광고 많음
3. http://www.welovead.com/en/ 이미지 15만개 있음



### 이미지에서 텍스트:

- google.vision api



### 해야할 것:

1. 광고 카피 이미지 크롤링
2. 광고 카피 이미지에서 텍스트 추출
3. 새로운 문장 만들어보기(데이터베이스에 없는 문장이어야함)
4. 이후에 매력적인 문구가 무엇인지 정의하고 그에 맞는 알고리즘 개발.



### 우리의 지금 목표 데이터셋:

- product_category, copy

### 이후의 데이터셋:

- industry, product_category, copy, strategy



### 이후 확장 가능:

- 만들어진 문장이 무슨 목적으로, 무슨 효과를 기대하고 만들어졌는지 설명

- 접근방법을 입력값을 받음.(humor, informative, descriptive, emotional)

- 데이터형식: industry, product_category, copy, strategy

- PERSADO는 문구를 Emotional/ Descriptive/ Formatting/ Functional/ Positioning으로 나누어 만든다.  나는 감정을 자극할 수 있는 emotional 문구, 설명의 Descriptive 문구까지 만들고 싶다. 




### ai copywriter 현재(20190921)목표:

타겟 플랫폼: 온라인 쇼핑몰

예상 아웃풋: AI 추천 문장 10가지 정도.

아웃풋 활용: 사람이 괜찮은 문구를 골라서 살짝의 수정을 거친 후 마무리. 

제품군: skirt, pants, jewelry, accesssary, boots, dress, sweater, blazer

copy 분류: 1= Conversion Rate에 관련된 문구, 0 = 제품 설명 문구

### 간략한 멘토링 추가 내용

여러개의 광고를 추천해주는 방식.

여러가지 방법을 실행 (여러 버전)



if 영화포스터 추천
  * 도메인을 줄여서 (영화 포스터의 문구) -> 관객수에 따른 영화 흥행

  몇가지 추출해서 사람들 선택에 따른 가중치

  **포스터 선택 

  영화 주연, 주제, 포스터들의 정보를 토대로 변화를 어떻게 주냐

  포스터를 어떻게 보여줄거냐 ( 문구들을 어떻게 줄거냐 )


