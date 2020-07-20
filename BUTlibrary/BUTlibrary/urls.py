from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

   # path('', TemplateView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^', include('accounts.urls')),
    url(r'^', include('library.urls')),

]