from django.urls import path,include
from .views import handlesignup

urlpatterns=[
    path('signup/',handlesignup)
]