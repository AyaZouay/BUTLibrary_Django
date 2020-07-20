from django.conf.urls import url
from . import views
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    url(r'login$', login_view, name='login'),
    url(r'signup', register_view, name='signup'),
    url(r'logout', logout_view, name='logout'),
    url(r'^login$', views.login_view, name="login.html"),
    url(r'^signup$', views.register_view, name="signup.html"),
    ]