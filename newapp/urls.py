from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from newapp import views

urlpatterns = [
    path('', views.index, name='my_index'),
    path('services/', views.services, name='my_services'),
    path('vblog/', views.vblog, name='my_vblog'),
    path('blogs/', views.blog_list, name='my_blogs'),
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('creatives/<str:name>/', views.member_blog, name='member_blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)