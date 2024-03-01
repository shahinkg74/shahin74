from django.urls import path
from .views import ShortVideoListView, ShortVideoDetailView

app_name = 'video'
urlpatterns = [
    path('short/', ShortVideoListView.as_view(), name='short_video_list'),
    path('short/<int:video_id>/<str:video_slug>/', ShortVideoDetailView.as_view(), name='short_video_detail'),
]
