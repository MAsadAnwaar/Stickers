from django.urls import path,include
from rest_framework import routers
from knox import views as knox_views
from .views import *
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    # Knox Login & Signup 
    path('register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
   
    path('api/like-pack/<int:pack_id>/', AddLikeToPack.as_view(), name='add-like-to-pack'),
    path('packs/<int:pack_id>/', PackDetailView.as_view(), name='pack-detail'),

    path('pack/', packListAPIView.as_view(), name='pack_detail'),
    path('allpack/', packListAPIView.as_view(), name='Pack-List'),
    path('alltrending/', TrendingListAPIView.as_view(), name='Pack-Trending'),
    path('allfeatured/', FeaturedListAPIView.as_view(), name='Pack-Featured'),
    path('allfestive/', FestiveListAPIView.as_view(), name='Pack-Festive'),
    path('allanimated/', AnimatedListAPIView.as_view(), name='Pack-Animated'),
    path('userpack/', UserListAPIView.as_view(), name='Pack-User'),

    path('categories/', catListAPIView.as_view(), name='subcat-List'),
    path('categories/<int:pk>/', CategoryDetailsAPIView.as_view(), name='category-details'),
    path('categories/<int:category_pk>/<int:pack_pk>/', PackDetailsAPIView.as_view(), name='pack-details'),

    
    path('packs/', PackListCreateView.as_view(), name='pack-list-create'),
    path('packs/<int:pk>/', PackRetrieveUpdateDestroyView.as_view(), name='pack-retrieve-update-destroy'),
    # upload sticker
    path('upload_sticker_list/<int:pack_id>/', views.upload_sticker_list, name='upload_sticker_list'),


    

]