from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from urllib.parse import unquote

from .models import ShortVideo


class ShortVideoListView(View):
    def get(self, request):
        videos = ShortVideo.objects.all().order_by('-created_at')
        videos_length = len(videos)
        # paginator
        page = request.GET.get('page', 1)
        paginator = Paginator(videos, 8)
        try:
            video_list = paginator.page(page)
        except PageNotAnInteger:
            video_list = paginator.page(1)
        except EmptyPage:
            video_list = paginator.page(paginator.num_pages)
        
        context = {
            'videos': video_list,
            'videos_length': videos_length
        }
        return render(request, 'video/short_video_list.html', context)


class ShortVideoDetailView(View):
    def get(self, request, video_id=None, video_slug=None):
        video_slug = unquote(video_slug)
        video = get_object_or_404(ShortVideo, id=video_id, slug=unquote(video_slug))
        context = {'video': video}
        return render(request, 'video/short_video_detail.html', context)
