from django.contrib import admin
from django.urls import path, include
import firstapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', firstapp.views.welcome),
    # path('mydjango/myname/', firstapp.views.getname),
    path('secondapp/', include('secondapp.urls')),
    path('forthapp/', include('forthapp.urls')),
    path('fifthapp/', include('fifthapp.urls')),
    path('uploadapp/', include('uploadapp.urls')),
    path('redirectapp/', include('redirectapp.urls')),
    path('visitorapp/', include('visitorapp.urls')),
    path('relationapp/', include('relationapp.urls')),
    path('accountapp/', include('accountapp.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
