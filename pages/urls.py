from django.urls import path

#Creates a route to the home page
from . import views

#Path is empty string for root path/home page
urlpatterns = [
    #Important parameters: 1st is the route, 2nd is the method in views, third is a name to easily access the path
    path("", views.index, name="index"),
    path("about", views.about, name="about")
]