# 퍼스널 컬러 색상 진단 및 제품 추천 플렛폼
## Index
  - [About PersonalColor](#about-personalcolor)
  - [How To Install](#how-to-install)
  - [How To Use](#how-to-use)
  - [Contents](#contents)

## About PersonalColor
- 퍼스널컬러(Personal Color)란 사람의 피부톤과 가장 어울리는 색상을 찾는 색채학 이론이다. 피부톤에 어울리는 색을 웜톤 쿨톤이나 봄, 여름, 가을, 겨울로 나누어 부르는 것이 바로 이 퍼스널 컬러를 기반으로 한 것이다.

- 본인에게 어떤 색이 베스트인지 알고 싶을 때, 혹은 어떤 계열의 색이 미묘하게 안색이 탁해보이거나 어두워보이거나 창백해보이는지 알고 싶을 때 퍼스널컬러를 알면 좋다.
(베스트 색이라는 것은 "안색이 뜨지 않고 건강해보이는 것"을 기준으로 잡고 있다.)

- 그러나 퍼스널 컬러를 알게 되어도 막상 실제 물건( 옷이나 화장품 등)에 퍼스널컬러 결과를 적용해보려고 하면 이 색이 나의 퍼스널 컬러에 맞는지 알기란 쉽지 않다.

- 따라서 위의 문제를 해결하기 위해 자신의 퍼스널 컬러가 무엇인지 알 수 있을 뿐만 아니라 본인이 가지고 있는 혹은 구매할 제품이 자신의 퍼스널 컬러에 맞는 색상인지 알아낼 수 있고 그 색상과 비슷한 제품들을 추천받고 여러 소셜커머스에 등록되어 있는 제품들을 확인할 수 있는 플랫폼을 만들고자 하였다.

## How To Install
Open your ex polder and ... insert this code..

```sh
git clone https://github.com/PersonalColor/Backend.git
cd Backend
npm i
cd src/scripts
python -m venv venv
source venv/Scripts/activate (윈도우)
source venv/bin/activate (맥 또는 우분투)
pip install -r requirements.txt
npm run server
```
## How To Use
1. 로그인 화면
![](/imgs/1.PNG)
아이디와 패스워드를 입력하여 로그인을 할 수 있고 , '아이디가 없으신가요?' 선택 시 회원가입을 할 수있습니다.<br>

2.회원가입
![](/imgs/2.PNG)
이름, 아이디, 패스워드를 입력합니다.
![](/imgs/3.PNG)
사용자의 퍼스널 컬러 정보를 알기 위해 'Person Color 진단하기'를 눌러 자신의 Personal Color를 검사합니다.<br>

3. 퍼스널 컬러 진단
![](/imgs/4.PNG)
퍼스널 컬러 진단은 문답으로 진단하기, 필터로 진단하기, AI로 진단하기 3가지 방법으로 계획하였지만 현재 구현된 것은 문답과 필터로 진단하기입니다.<br>

문답으로 진단
![](/imgs/5.PNG)
여러 질문을 통해 사용자가 웜톤인지 쿨톤인지 확인합니다. 웜톤 이라는 결과가 나오게 되면 봄웜인지 가을웜인지 문답하는 화면으로 넘어가게 되고 쿨이라는 결과가 나오면 겨울 쿨인지, 여름 쿨인지 문답하는 화면으로 넘어가게 됩니다.<br>

쿨톤으로 판정됐을 경우
![](/imgs/6.PNG)
여러 개의 질문을 통해 사용자의 답변으로 겨울 쿨인지 여름 쿨인지 진단하고 <br>

![](/imgs/7.PNG)
진단결과를 보여준 후 저장하기를 누르면 회원정보에 퍼스널 컬러정보가 저장됩니다.<br>

웜톤으로 판정 됐을 경우
![](/imgs/19.PNG)
사용자의 답변으로 봄웜인지 가을웜인지 진단하고
![](/imgs/20.PNG)
진단결과를 보여준 후 저장하기를 누르면 회원정보에 퍼스널 컬러정보가 저장됩니다.
![](/imgs/16.PNG)
![](/imgs/23.PNG)
![](/imgs/21.PNG)
![](/imgs/22.PNG)
![](/imgs/17.PNG)
![](/imgs/18.PNG)
![](/imgs/8.PNG)
![](/imgs/9.PNG)
회원가입한 정보를 입력합니다.
![](/imgs/10.PNG)
상의뿐만 아니라 다른 카테고리도 볼 수 있습니다.
![](/imgs/13.PNG)
Color를 클릭하여 해당 색상의 제품들만 볼 수 있습니다.<br>

제품을 클릭하면 해당 판매 사이트로 넘어갑니다
![](/imgs/11.PNG)
원하는 색상에 맞는 코디도 보여줍니다.
![](/imgs/12.PNG)
원하는 색상에 맞는 코디도 보여줍니다.
![](/imgs/14.PNG)
제품 색 추출 버튼을 누르면 자신의 퍼스널 컬러와 맞는지 궁금한 제품의 사진을 업로드할 수 있습니다.<br>

![](/imgs/15.PNG)
업로드한 제품의 색상명을 보여줍니다.

 
## Contents
### 퍼스널 컬러 자가 진단

- 설문 - 객관식 설문을 통해 퍼스널 컬러를 진단합니다.
- 필터 - 사진을 통해 얼굴에 필터를 변경해가면서 퍼스널 컬러를 진단합니다.

### 제품 사진 업로드 시 색상 분석 및 비슷한 계열 색상의 제품 추천

- 업로드된 제품의 색상을 분석해 해당 색이 어떤 퍼스널 컬러와 맞는지 판단해줍니다.
- 해당 색과 비슷한 계열 제품의 추천 목록을 제공합니다.
    1. 제품 사진 업로드
    2. 이미지 분석
    3. 해당 제품과 비슷한 색상의 제품 추천
        1. 해당 제품을 클릭하면 구매할 수 있는 사이트로 이동

### 코디추천

- 패션 플랫폼에서 수집한 정보를 사용자의 정보(퍼스널 컬러, 성별 등)에 따라 추천합니다
- 퍼스널 컬러 및 기본정보 입력
- 추천


## Authors
  - Backend - [wlsrn3684](https://github.com/wlsrn3684) - **김진구**
  - Crawling - [kinghyeongu](https://github.com/kinghyeongu) - **강현구**
  - Frontend - [jaryeong](https://github.com/jaryeong) - **김자령**
  - Data(open cv, pillow) - [goodsmell](https://github.com/goodsmell) - **조은향**
