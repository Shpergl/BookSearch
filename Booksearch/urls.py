from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/', auth_views.login, {'template_name': 'booksearch/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('booksearch.urls')),

]
