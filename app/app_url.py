from . import views
from django.urls import path

from app.views.login_view import home



urlpatterns = [
    path('', views.login_view.home, name='home'),
    path('login/', views.login_view.login, name="login"),
    path('signup/', views.login_view.signup, name="signup")

]




