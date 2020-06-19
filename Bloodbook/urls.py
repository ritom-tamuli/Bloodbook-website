from django.conf.urls import url
from Bloodbook import views

app_name = 'Bloodbook'
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^search/$',views.search,name='search'),
    url(r'^about/$',views.about,name='about'),

]
