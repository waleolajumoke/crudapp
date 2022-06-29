from django.urls import  path
from . import views 

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('profile', views.profile, name='profile'),
    path('signout', views.signout, name='signout')
]