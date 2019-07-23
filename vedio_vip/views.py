from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import View


class Index(View):
    def get(self, request):
        return render(request, 'vedio_vip/video_vip.html')

    def post(self, request):
        url = request.POST.get('url')
        print(url)
        return render(request, 'vedio_vip/video_vip.html', context={'url': url})


