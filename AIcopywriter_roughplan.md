# AI copywriter

- 아이디어 발상하는 과정에서 가장 어려운게 시작이다. 
- 이 과정을 줄이고 마지막 수정 작업만 할 수 있도록 도와주기 위한 AI copywriter, zeto50
- 자동차의 파워를 말할 때 나오는 단어는 '제로백'. 시속 100킬로미터를 몇초 안에 달성하는지를 측정한다. 아이디어를 만들어내는 과정은 아무리 베테랑이어도 시간이 걸리기 마련이다. 누구나 짧은 시간안에 제로백을 달성하고 싶지 않은가? 시작이 반이라는 격언처럼 일단 시작할 만한 아이디어가 있으면 가지를 붙이거나 쳐내며 다듬어 갈 수 있다. 그 초반의 괴로운 과정을 없애주겠다. zero to 50, zeto50. 50의 노력으로 100의 결과물을 만들어내도록 도와주겠다.



#### 데이터 크롤링 사이트:

- imdb



#### 해야할 것

- 영화제목, 포스터, 태그라인, 영화요약, 영화시놉시스, 영화장르 크롤링
- DB 연동
- 새로운 tagline 만들어낼 알고리즘 구현



#### 목표 데이터셋:

- movie_name, movie_poster_url, movie_summary, movie_synopsis, movie_genre
- 이후에 추가할 데이터셋: 위치데이터(tagline_x, tagline_y, movie_name_x, movie_name_y)



#### 이미지에서 텍스트:

- google.vision api



#### 해야할 것:

1. 광고 카피 이미지 크롤링
2. 광고 카피 이미지에서 텍스트 추출
3. 새로운 문장 만들어보기(데이터베이스에 없는 문장이어야함)
4. 이후에 매력적인 문구가 무엇인지 정의하고 그에 맞는 알고리즘 개발.



#### 우리의 지금 목표 데이터셋:

- product_category, copy

#### 이후의 데이터셋:

- industry, product_category, copy, strategy




#### ai copywriter 현재(20190925)목표:

- 크롤링 
- DB 연동

- 예상 아웃풋: AI 추천 태그라인 10가지

- 아웃풋 활용: 사람이 괜찮은 문구를 골라서 살짝의 수정을 거친 후 마무리. 

- 영화 장르: ['comedy', 'sci-fi', 'horror', 'romance', 'action', 'thriller', 'drama', 'mystery', 'crime', 'animation', 'adventure', 'fantasy', 'comedy-romance', 'action-comedy', 'superhero']





#### 이후 확장 가능:

- 온라인 display 광고 카피
- text to image로 포스터 제작
- 제목과 태그라인 위치 추천
- 맞춤형 문구 추천

#### 광고 올라오는 사이트:

1. https://www.adsoftheworld.com/?terms=&medium=484&industry=22&country=473
2. http://creativecriminals.com/archive/country:usa/category:print 프린트 광고 많음
3. http://www.welovead.com/en/ 이미지 15만개 있음



#### 0921_간략한 멘토링 추가 내용

여러개의 광고를 추천해주는 방식.

여러가지 방법을 실행 (여러 버전)



if 영화포스터 추천
  * 도메인을 줄여서 (영화 포스터의 문구) -> 관객수에 따른 영화 흥행

  몇가지 추출해서 사람들 선택에 따른 가중치

  **포스터 선택 

  영화 주연, 주제, 포스터들의 정보를 토대로 변화를 어떻게 주냐

  포스터를 어떻게 보여줄거냐 ( 문구들을 어떻게 줄거냐 )


