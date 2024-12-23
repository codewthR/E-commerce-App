from django.contrib import admin
from django.urls import path
from ecomm import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.add_product ,name='home'),
    path('display/',  views.display , name='display'),
    path('display/updates/', views.up , name='updates'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)