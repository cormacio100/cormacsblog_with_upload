from django.conf.urls import url
import views

# specific app URL pointable from template
app_name = 'posts'

urlpatterns = [
    url(r'^blog/$',views.post_list),
    url(r'^home/$', views.home, name="home"),
    url(r'^post_list/$', views.post_list, name="post_list"),
    url(r'^post_details/(?P<id>[0-9]+)/$', views.post_details, name="post_details"),
    url(r'^post_new/$',views.new_post, name='new_post'),
]