from django.conf.urls import url
from newApp import views

#Template urls
app_name = 'newApp'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^me/$',views.me,name='me')
]
