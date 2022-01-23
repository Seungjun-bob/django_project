from django.urls import path

from . import views

app_name = 'pybo' # 동일한 URL 별칭 사용의 중복을 막음, 네임스페이스를 의미

urlpatterns = [
    path('', views.index, name='index'), # URL매핑에 name 속성을 부여(http://localhost:8000/pybo/)
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create')
]