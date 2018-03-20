from django.conf.urls import url
from django.urls import path

from accounts import views

urlpatterns = [

    path('' , views.index , name = 'index') ,
    path('register/college/' , views.register_college , name = "register-college") ,
    path('college-list/' , views.CollegeListView.as_view() , name = "college-list") ,
    path('college/<slug:slug>/', views.CollegeDetailView.as_view() , name='college-detail') ,
    #url(r'^college/(?P<slug>[\w-]+)/$', views.CollegeDetailView.as_view() , name='college-detail'),
]