# 1. 장고 앱 만들기
본 프로젝트는 간단한 설문조사 어플리케이션을 만드는 과정을 기술합니다.   
#### <구성 파트>   
- 개방된 사이트(사람들이 직접 투표 가능)
- 관리용 사이트(관리자가 설문을 추가, 변경, 삭제)
## 1.1 프로젝트 만들기
cmd 창에서 cd명령으로 프로젝트를 진행할 디렉터리로 이동한 후, 다음의 명령을 수행합니다.   
```django-admin startproject [프로젝트 이름]```   
```django-admin startproject [mysite]```   
아래와 같은 폴더와 파일이 생성됨을 확인 할 수 있습니다.   
```python
mysite/
    manage.py        # Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인의 유틸리티
    mysite/          # 프로젝트를 위한 실제 Python 패키지들이 저장됩니다.
        __init__.py  # 패키지 임을 알려주는 파일입니다.
        settings.py  # 현재 Django 프로젝트의 환경 및 구성을 저장합니다.
        urls.py      # 프로젝트의 URL 선언을 저장합니다. 사이트의 <목차>라고 할 수 있습니다.
        asgi.py      # ASGI-호환-웹 서버의 진입점입니다.
        wsgi.py      # WSGI-호환-웹 서버의 진입점입니다.
```   
## 1.2 개발 서버
Django 프로젝트가 잘 작동하는지 확인하겠습니다. mysite 디렉토리에서 다음 명령어를 입력하면 됩니다.   
```py manage.py runserver```
## 2.1 설문조사 앱 만들기
1. 앱을 생성하기 위해 manage.py가 존재하는 디렉토리에서 다음의 명령을 입력합니다.   
```py manage.py startapp polls```   
이 디렉터리 구조는 투표 어플리케이션의 집이 되어줄 것입니다.
2. 첫 번째 뷰 작성하기   
<polls/view.py>를 열어 다음과 같은 파이썬 코드를 입력합니다.   
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```   
뷰를 호출하려면 이와 연결된 URL이 있어야 합니다. 이를 위햐 URLconf가 사용됩니다.   
polls 디렉토리에서 URLconf를 생성하려면 urls.py라는 파일을 생성해야 합니다.   
3. polls 하위에 urls.py 파일 생성   
<polls/urls.py>파일은 다음과 같은 코드로 구성되어 있습니다.   
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```   
4. 최상위 URLconf에서 polls.urls모듈을 바라보게 설정
**주의 polls하위 파일이 아닌 초기 프로젝트 폴더 하위에 있는 urls.py 파일입니다.**  
mysite/urls.py 파일을 열고, **django.urls.inclue**를 import하고, urlpatters 리스트에 **inclue()** 함수를 다음과 같이 추가합니다.   
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```   
- include() 함수는 다른 URLconf들을 참조할 수 있도록 도와줍니다. Django가 함수 include()를 만나게 되면, URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include 된 URLconf로 전달합니다.
- include()에 숨은 아이디어 덕분에 URL을 쉽게 연결할 수 있습니다. polls 앱에 그 자체의 URLconf(polls/urls.py)가 존재하는 한, 그 어떤 다른 root 경로에 연결하더라도, 앱은 여전히 잘 작동할 것입니다.   
i**ndex** 뷰가 URLconf에 연결되었습니다. 잘 작동하는지 확인하기 위해 다음 명령을 입력해 보세요.   
```py manage.py runserver
## 참고문서
- [django guide](https://docs.djangoproject.com/ko/4.0/intro/tutorial01/)
- [명준MJ youtube](https://www.youtube.com/watch?v=9WctwW_Pe1o&list=PLi4xPOplIq7d1vDdLBAvS5PmQR-p6KwUz&index=2)
