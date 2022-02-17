from django.contrib import admin
from django.urls import path, include
import firstapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', firstapp.views.welcome),
    # path('mydjango/myname/', firstapp.views.getname),
    path('secondapp/', include('secondapp.urls')),

]
