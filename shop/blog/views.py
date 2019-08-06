# from django.template import loader
from datetime import datetime
from django.shortcuts import render , get_object_or_404 , get_list_or_404
# from django.http import HttpResponse , Http404
from .models import Post
from django.views.decorators.http import require_http_methods , require_GET , require_safe
# Create your views here.


@require_http_methods(["GET"])
def index(request):
    latest_posts_list = Post.objects.order_by('publish')[:5]
    # output = ',\n'.join([p.slug for p in latest_posts_list])
    # template = loader.get_template('index.html')
    context = {
        'latest_posts_list' : latest_posts_list,
    }
    # return HttpResponse(template.render(context , request))
    return render(request , 'index.html', context)

@require_GET
def detail (request , post_id):

    post = get_object_or_404(Post , pk = post_id)
    # try:
    #     post = Post.objects.get(pk = post_id)
    # except Post.DoesNotExist:
    #     raise Http404("post doesn't exist.")
    # template = loader.get_template('detail.html')
    context = {
        'post' : post,
    }
    return render(request , 'detail.html', context)
@require_GET
def archive_year (request , year):
    # current_year = datetime.today().year
    year_archive_posts = get_list_or_404(Post , publish__year = year)
    '''Post.objects.filter(publish__year = year)'''
    context = {
        'year_archive_posts' : year_archive_posts,
    }
    return render(request, 'archive.html' , context )