from . import views
from django.urls import path

urlpatterns = [
    path("home/",views.home,name="home"),
    path("register/", views.register_user, name="register"),
    path("", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("cart/",views.cart,name="cart"),
    path("suggestions/", views.suggestions, name="suggestions"),
    path("submit_suggestion/", views.submit_suggestion, name="submit_suggestion"),
]