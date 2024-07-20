from django.shortcuts import render, get_object_or_404
from .models import MainContent

# Create your views here.
def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)

def detail(request,content_id):
    content_list = get_object_or_404(MainContent,pk=content_id)
    context = {'content_list': content_list}
    return render(request, 'mysite/content_detail.html',context)