

광고 문구생성

책, 안경, 지갑, 약, 음료, 담배 뭐가 되었던 입력값은 산업 분야와 제품군이다. 

기존 포스터, 카피로 학습된 모델로 새로운 문장을 만들어 낸다.

포스터, 카피는 대부분 이미지로 있기 때문에 이미지 읽는 패키지 필요.

지금의 목표는 배너 광고에 들어가는 카피 추천해주는 AI만들기.



광고카피 올라오는 사이트:

1. https://www.adsoftheworld.com/?terms=&medium=484&industry=22&country=473
2. http://creativecriminals.com/archive/country:usa/category:print 프린트 광고 많음
3. http://www.welovead.com/en/ 이미지 15만개 있음



이미지에서 텍스트

- tesseract 
  - https://niceman.tistory.com/155
  - [https://junyoung-jamong.github.io/computer/vision,/ocr/2019/01/30/Python%EC%97%90%EC%84%9C-Tesseract%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%B4-OCR-%EC%88%98%ED%96%89%ED%95%98%EA%B8%B0.html](https://junyoung-jamong.github.io/computer/vision,/ocr/2019/01/30/Python에서-Tesseract를-이용해-OCR-수행하기.html)

해야할 것

1. 광고 카피 이미지 크롤링
2. 광고 카피 이미지에서 텍스트 추출
3. 새로운 문장 만들어보기(데이터베이스에 없는 문장이어야함)
4. 이후에 매력적인 문구가 무엇인지 정의하고 그에 맞는 알고리즘 개발.



이후 확장 가능:

- 만들어진 문장이 어떻게, 왜 만들어졌는지 어떤 이유에 근거해서 만들어졌는지 설명
- 광고의 목적을 입력값을 받음.
- 배너 뿐 아니라 다양한 미디어 채널()
- 인스타 페이지 설명, 마이홈
- PERSADO는 문구를 Emotional/ Descriptive/ Formatting/ Functional/ Positioning으로 나누어 만든다.  나는 감정을 자극할 수 있는 emotional 문구, 설명의 Descriptive 문구까지 만들고 싶다. 

