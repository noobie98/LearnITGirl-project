from django.conf.urls import url

from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$',views.register, name='register'),
    url(r'^login/$',views.login_view, name='login'),
    url(r'^register/success/$',views.register_success, name='register_success'),
    url(r'^category/$',views.get_category,name='getcategory'),
    url(r'^#/$',views.save_bookmark,name='savebookmark'),
]
