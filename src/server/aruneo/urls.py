from django.urls import path

from .views import SignUpView,user_login,user_logout,home,data_enter,user_dash,soc_dash

urlpatterns = [
    path("", home, name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", user_login , name="login"),
    path("logout/", user_logout , name="logout"),
    path("data_entry/", data_enter, name="data_entry"),
    path("user_dash/", user_dash, name="user_dash"),
    path("soc_dash/", soc_dash, name="soc_dash"),
]