from django.urls import path
from app1 import views


urlpatterns=[
    path('',views.homeView,name="home_page"),
    path('login',views.loginView,name="login_page"),
    path('profile',views.profileView,name="profile_page"),
    path('logout',views.logoutView,name="logout_page"),
    path('register',views.registerView,name="register_page"),
    path('create',views.tweetView,name="create_page"),
    path('show/<int:rid>',views.display,name="single_page"),
    path('delete/<int:rid>',views.deleteView,name="delete_page"),

]