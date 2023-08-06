from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name="post"),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
]
