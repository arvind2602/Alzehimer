
from django.contrib import admin
from django.urls import path,include
from .views import home,detect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('auth/',include('docauth.urls')),
    path('detect/alzeimer/',detect),
    # path('chat/',chatbot)
]
