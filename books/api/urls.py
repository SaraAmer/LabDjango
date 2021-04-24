
from django.urls import path ,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
  path("",views.index),
  path("create",views.create),
  path("show/<int:id>/" , views.show),
  path("delete/<int:id>/" , views.delete),
  path("edit/<int:id>/" , views.edit),
  path("signup", views.api_signup),
  path("login", obtain_auth_token),
  

]