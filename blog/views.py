from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# Create your views here.
from django.views import View
from user.models import BlogContent
import datetime
#导入分页及异常的模块
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def index(request):
    return HttpResponse('blog_index')


class AddBlog(View):
    def get(self, request):
        return render(request, 'blog/blog_add.html')

    def post(self, request):
        title = request.POST.get('blogtitle')
        content = request.POST.get('blogcontent')
        blogcontent = BlogContent()
        blogcontent.title = title
        blogcontent.content = content
        blogcontent.createtime = datetime.datetime.now()
        blogcontent.lasttime = datetime.datetime.now()
        blogcontent.save()
        return redirect(reverse('bloglist'))


def bloglist(request):
    allblog = BlogContent.objects.all()
    # print(allblog[::-1])
    # 倒序
    pa = Paginator(allblog[::-1], 2)
    current_page = request.GET.get('page', '1')
    try:
        if int(current_page) not in range(1, pa.num_pages+1):
            return redirect('/blog/list')
    except ValueError:
        return redirect('/blog/list')

    page = pa.page(current_page)
    # print()
    return render(request, 'blog/blog_list.html', context={'allblog': allblog, 'page': page, 'pa': pa})


class UpdateBlog(View):
    def get(self, request, blog_id):
        # 通过id查询blog
        blog = BlogContent.objects.filter(id=blog_id).first()
        # print(blog)
        return render(request, 'blog/blog_update.html', context={'blog': blog})

    def post(self, request, blog_id):
        page = request.GET.get('page')
        title = request.POST.get('blogtitle')
        content = request.POST.get('blogcontent')
        blog = BlogContent.objects.filter(id=blog_id).first()
        blog.title = title
        blog.content = content
        blog.lasttime = datetime.datetime.now()
        blog.save()
        return redirect('/blog/list/?page={}'.format(page))


def deleteblog(request, blog_id):
    page = request.GET.get('page')
    BlogContent.objects.filter(id=blog_id).delete()
    return redirect('/blog/list/?page={}'.format(page))


def detialblog(request, blog_id):
    blog = BlogContent.objects.filter(id=blog_id).first()
    return render(request, 'blog/blog_detial.html', context={'blog': blog})


