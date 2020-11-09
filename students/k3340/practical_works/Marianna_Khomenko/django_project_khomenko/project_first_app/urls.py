from django.urls import path 
from .views import *


urlpatterns = [
    path('owner/<int:poll_id>', detail),
    path('time/', geeks_view),
    #path('', list_view),
    #path('', GeeksList.as_view()),
    path('carowners/', CarOwnerList),
    path('cars/', CarList.as_view()),
    #path('', create_view),
    path('', GeeksCreate.as_view()),
    path('carownerf/', carowner_create_view),
    path('carf/', CarCreate.as_view()),
]