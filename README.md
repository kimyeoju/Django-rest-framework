# Travel Japan (Django REST Framework version) ✈️

 - Django REST Framework를 이용하여 프론트엔드(HTML, CSS)와 백엔드(Django)간의 통신 프로젝트
 - 기존의 Travel Japan(HTML, CSS)프로젝트를 고도화 시킨 DRF 프로젝트

## 1. 목표와 기능

### 1.1 목표
- ChatGPT OpenAI를 이용해 일본 여행 계획을 보다 더 세세하고 정확하게 서비스 전달

### 1.2 기능
- 사용자 기능
  - 회원가입, 로그인, 로그아웃
  - 인증된 사용자만 서비스 접근가능(JSON Web Token 인증 방식)

- 챗봇 기능
  - 챗봇 구현
  - 인증된 사용자 서비스 요청 일일 5번으로 제한(Throttle로 호출횟수 제한)
  - 사용자가 이용한 채팅 내용은 데이터베이스(DB)에 저장
 
## 2. 개발 환경 및 배포 URL

### 2.1 개발 환경

- BackEnd

 <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">

- FrontEnd

<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">


### 2.2 개발 기간

- 2023년 07월 26일 ~ 2023년 08월 02일

### 2.3 배포 URL

 - AWS lightsail 퍼블릭 주소로 axios하여 오류
 - http -> https 추후 수정 필요

Back-End repo : https://github.com/kimyeoju/Django-rest-framework.git

Front-End repo : https://github.com/kimyeoju/Django-rest-framework_FE.git

## 3. 프로젝트 구조와 개발 일정

### 3.1 프로젝트 구조
```
📦 
├─ .DS_Store
├─ .vscode
│  └─ settings.json
├─ projects
│  ├─ .gitignore
│  ├─ chat_project
│  │  ├─ __init__.py
│  │  ├─ asgi.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  └─ wsgi.py
│  ├─ chatbot
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_initial.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ serializers.py
│  │  ├─ templates
│  │  │  ├─ base.html
│  │  │  └─ chat.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ utils.py
│  │  └─ views.py
│  ├─ manage.py
│  └─ user
│     ├─ __init__.py
│     ├─ admin.py
│     ├─ apps.py
│     ├─ forms.py
│     ├─ migrations
│     │  ├─ 0001_initial.py
│     │  └─ __init__.py
│     ├─ models.py
│     ├─ serializers.py
│     ├─ tests.py
│     ├─ urls.py
│     └─ views.py
└─ requirements.txt
```

### 3.2 URL 설계

NAME|URL|
|---|---|
|User|
|회원가입|user/register/|
|로그인|user/login/|
|Token|user/token/refresh/|
|chatbot|
|챗봇|chatbot/|


## 4. 에러

- 프론트엔드에서 요청을 하면 Django에서 사용자가 요청한 값을 응답하는 과정이 힘들었다. 프론트엔드와 백엔드 간의 통신이 원활하게 이루어져야 하는데 프론트엔드에서 요청을 보내도 token이 발급되지 않은 사용자가 요청을 하니 백엔드에서 거절을 하는 상황이었다. 따라서 Forbidden 오류가 지속해서 출력이 되었다.
- 인증된 사용자만이 회원가입, 로그인, 챗봇을 이용할 수 있기 때문에 백엔드에서 프론트엔드로 token을 가져오는 것이 해결책이었다.

![image](https://github.com/kimyeoju/Django-rest-framework/assets/131739526/3f7b6b1d-c93b-4886-95fb-a1224f174be3)


- 회원가입, 로그인을 하면 웹 로컬스토리지에 token을 저장해주는 코드

![image](https://github.com/kimyeoju/Django-rest-framework/assets/131739526/12f57601-92b3-40e5-b00c-082f07bbed6a) ![image](https://github.com/kimyeoju/Django-rest-framework/assets/131739526/60e2869a-dc88-4b1e-ac4b-16df754ed49f)

- 성공적으로 웹 로컬스토리지에 token이 발급되는 것을 확인할 수 있다.

![image](https://github.com/kimyeoju/Django-rest-framework/assets/131739526/c7a67023-5aa4-4f97-87b5-b94c07281181)



## 5. 상세 페이지 설명

### 메인 페이지

![chrome-capture-2023-7-3](https://github.com/kimyeoju/Django-rest-framework/assets/131739526/fd34d6e4-9522-4e98-a975-9b41911635ad)

### 로그인 페이지

![chrome-capture-2023-7-3 (1)](https://github.com/kimyeoju/Django-rest-framework/assets/131739526/ef1eaf8a-6a66-46fc-8b17-72843a6e2300)

### 회원가입 페이지

![chrome-capture-2023-7-3 (2)](https://github.com/kimyeoju/Django-rest-framework/assets/131739526/1652492d-d1e2-46c3-af87-0c9ece7814d9)

### 챗봇 페이지

![chrome-capture-2023-7-3 (3)](https://github.com/kimyeoju/Django-rest-framework/assets/131739526/0d9cb544-a190-4226-bc33-5f54cdfc2461)

## 6. 실행 화면

### 회원가입, 로그인 기능

![chrome-capture-2023-7-3](https://github.com/kimyeoju/Django-rest-framework/assets/131739526/f9ea68b4-da25-42e0-a26b-d460e10113b9)

- 회원가입을 하면 Django에서 token을 발급 -> 발급된 token으로 user 인증 !

![image](https://github.com/kimyeoju/Django-rest-framework/assets/131739526/c7a67023-5aa4-4f97-87b5-b94c07281181)

- 주의 !! 회원가입 후, Django에서 token 값을 받아와야 로그인을 할 수 있다




### 챗봇 기능


![chrome-capture-2023-7-3 (1)](https://github.com/kimyeoju/Django-rest-framework/assets/131739526/42049a6c-69c8-4ac5-9909-a5d5e50c6fcd)

- 로그인 된 user만 챗봇 사용 가능

![chrome-capture-2023-7-3 (2)](https://github.com/kimyeoju/Django-rest-framework/assets/131739526/bb66fb10-d13f-4447-8645-3788f104323b)

- 챗봇 답변 출력

![chrome-capture-2023-7-3 (4)](https://github.com/kimyeoju/Django-rest-framework/assets/131739526/7c4bf1fe-fb6f-4181-9406-5cafefaace73)

- 로그인(인증)된 user는 챗봇 서비스 요청을 하루에 5번으로 제한

``` Failed to resource: the server responded with a status of 429 (Too Many Requests) 오류가 뜸 ```

- settings.py Throttle 코드
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_THROTTLE_CLASS': {
        'rest_framework.throttling.UserRateThrottle'
    },
    'DEFAULT_THROTTLE_RATES': {
        'user': '5/d',
    }
}
```

## 7. 느낀점 및 추후 계획

### 느낀점
- Django REST Framework를 이용해 구현을 할 때 렌더링 하는 화면이 없어서 데이터 전송이 제대로 이루어지는지 시각적으로 볼 수 없기 때문에 이러한 문제를 보완하기 위해 Django와 포스트맨 툴을 같이 사용했다. 하지만 포스트맨 툴이 익숙하지 못해서 프로젝트 과정 중에도 포스트맨 툴을 익히느라 초반에 시간을 많이 소요하게 되었다. 프로젝트 중간 단계에서 JWT 모듈을 이용해 회원가입, 로그인 token 발급 기능을 구현하면서 점차 포스트맨의 툴을 익히는 시간이 되었고 Django의 여러가지 모듈과 전체적인 데이터 구조에 대해 보다 더 이해가 깊어지는 시간이었다.

- Django REST Framework 프로젝트를 진행하면서 외부 라이브러리와 모듈이 굉장히 많고 사용하면 편리한 기능들이 많은 것 같아 장고 프로젝트가 끝난 뒤에도 외부 라이브러리 기능에 대해서도 공부 해야겠다는 생각이 들었다.

### 개선점
- 프로젝트를 진행하면서 Django REST Framework의 전체적인 구조를 잡는데 너무 힘들었다. 이해를 온전히 하지 못하고 시작하면 지속해서 오류가 나는 것을 깨달았기 때문에 초반에 시간이 오래 걸리더라도 전체적인 구조 구성, 설계를 보다 더 꼼꼼히 계획해야 하는 것을 느끼는 시간이 되었다.

### 아쉬웠던점
- 시간이 촉박해서 코드를 제대로 이해하지 못한 부분도 작동이 되면 바로 넘어가는 순간이 많았기 때문에 이것 또한 시간 분배를 제대로 해서 코드를 온전히 이해하는 습관을 들여야겠다는 생각이 들었다.

### 추가해야 할 추후 기능

- 회원가입, 로그인, 로그아웃시 성공한 결과를 사용자가 알 수 있는 메시지 웹 화면에 추가
- 회원가입, 로그인 실패시 오류 메시지 웹 화면에 추가
- 리프레쉬해도 이전의 사용자 채팅 내역을 화면에 조회할 수 있는 기능 추가
