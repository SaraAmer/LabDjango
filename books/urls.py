from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    path('show/<int:id>/' , views.show , name='show'),
    path('delete/<int:id>/' , views.destroy , name='delete'),
    path('create' , views.create , name='create'),
    path('edit/<int:id>/' , views.edit , name='edit'),
    # path('createISBN' , views.createIsbn , name='createISBN'),

]