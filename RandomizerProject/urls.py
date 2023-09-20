from django.urls import path
from Randomizer import views


urlpatterns = [
    path('', views.main),
    path('random', views.myRandom),
]
