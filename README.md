# Projectname : 퍼스널 컬러 색상 진단 및 제품 추천 플렛폼
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
npm run server
```

```sh
cd ..
git clone https://github.com/PersonalColor/Frontend.git
cd Frontend
npm i
npm start
```
## How To Use
ex
 
## Contents
- 퍼스널 컬러 자가 진단
    1. 설문
        
        객관식 설문을 통해 퍼스널 컬러를 진단합니다.
        
    2. 필터
        
        사진을 통해 얼굴에 필터를 변경해가면서 퍼스널 컬러를 진단합니다.
        
    
- 제품 사진 업로드 시 색상 분석 및 비슷한 계열 색상의 제품 추천
    - 업로드된 제품의 색상을 분석해 해당 색이 어떤 퍼스널 컬러와 맞는지 판단해줍니다.
    - 해당 색과 비슷한 계열 제품의 추천 목록을 제공합니다.
    1. 제품 사진 업로드
    2. 이미지 분석
    3. 해당 제품과 비슷한 색상의 제품 추천
        1. 해당 제품을 클릭하면 구매할 수 있는 사이트로 이동
        
- 코디 추천
    - 패션 플랫폼 혹은 소셜 네트워크 서비스에서 수집한 정보를 사용자의 정보(퍼스널 컬러, 성별 등)에 따라 추천합니다
    - 퍼스널 컬러 및 기본정보 입력
    - 추천



## Authors
  - Backend - [wlsrn3684](https://github.com/wlsrn3684) - **김진구**
  - Crawling - [kinghyeongu](https://github.com/kinghyeongu) - **강현구**
  - Frontend - [jaryeong](https://github.com/jaryeong) - **김자령**
  - Data(open cv, pillow) - [goodsmell](https://github.com/goodsmell) - **조은향**
