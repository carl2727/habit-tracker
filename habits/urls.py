from django.urls import path
from habits import views

urlpatterns = [
    path("", views.index, name="index")

]