from django.shortcuts import get_object_or_404,render

from .models import BlogPost
# Create your views here.



def index(request):
	allPost = BlogPost.objects.all()[::-1]
	context = {'allPost': allPost}
	return render(request, 'index.html', context)

def details(request, blogid):
    blogid = get_object_or_404(BlogPost, pk=blogid)
    return render(request, 'detail.html', {'blogId': blogid})


    
    