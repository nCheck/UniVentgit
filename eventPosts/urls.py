from django.conf.urls import url
from django.urls import path, re_path , register_converter
from eventPosts import views

app_name = 'eventPosts'
urlpatterns = [
    path('upcoming/' , views.PostListView.as_view() , name ='post_list') ,
    path('old/' , views.OldPostListView.as_view() , name ='old_post_list') ,

    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='draft'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),




    # path('help/' , views.help , name = 'help') ,
    # path('' , views.index , name = 'index'),
    # path('base/' , views.base , name = 'base'),
    # path('name/' , views.get_name , name = 'name')
]