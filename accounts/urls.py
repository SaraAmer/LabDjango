
from django.urls import path ,include
from . import views
urlpatterns = [
    path('signup',views.signup, name="signup"),
    path('accounts/' , include('django.contrib.auth.urls'))
    # path('createISBN' , views.createIsbn , name='createISBN'),

]