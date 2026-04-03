from django.urls import path
from newapp import views


urlpatterns=[
    path('',views.index,name='my_index'),
    path('services/',views.services,name='my_services'),
    path('vblog/',views.vblog,name='my_vblog'),
    path('blogs/',views.blogs,name='my_blogs'),
    path('creatives/<str:name>/', views.member_blog, name='member_blog'),
]