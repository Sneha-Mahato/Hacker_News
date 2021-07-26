from django.urls import path
from app import views
from app.views.login_view import home
from app.views.login_view import loadcontent

urlpatterns = [
    path('', views.login_view.home, name="home"),
    path('next', views.login_view.loadcontent, name="Loadcontent"),
    # path('login/', views.login_view.login, name="login"),
    # path('signup/', views.login_view.signup, name="signup")

]




