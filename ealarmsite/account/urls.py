from django.urls import path
from .views import signin, signup, signout
app_name = 'Login'
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('singout/', signout, name='signout'),
]