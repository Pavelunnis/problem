from django.urls import path
from .views import HousePage, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('posts/', HousePage.as_view(), name="housepage"),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
]