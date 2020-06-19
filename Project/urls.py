from django.contrib import admin
#from django.urls import path
from django.conf.urls import url,include
from Bloodbook import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url('admin/', admin.site.urls),
    url(r'^Bloodbook/',include('Bloodbook.urls')),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'special/',views.special,name='special'),
]
