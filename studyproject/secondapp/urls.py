from django.urls import path
from . import views
urlpatterns = {
    path('', views.exam1, name='exam1'),
    path('exam2/', views.exam2),
    path('exam3/', views.exam3),
    path('exam4/', views.exam4),
    path('exam5/', views.exam5),
    path('exam6/', views.exam6),
    path('exam7/', views.exam7),
    path('exam8/', views.exam8),
    path('exam9/', views.exam9),
    path('exam10/<name>/', views.exam10),
    path('exam11/<name>/<int:age>/', views.exam11),
    path('exam12/<int:num1>/<int:num2>/', views.exam12),
    path('exam13/', views.exam13),
    path('exam14/<word>/<int:num1>/<num2>/', views.exam14),
    path('exam15/', views.exam15),
    path('exam16/', views.exam16, name='unico'),
    path('exam17/', views.exam17),
    path('exam18/', views.exam18),
    path('exam19/', views.exam19),
}