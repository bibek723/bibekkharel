from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from .forms import CommentForm


# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    context = {
        'blogs':blogs
    }
    return render(request, 'blog/all_blogs.html', context)

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.blog_detail = blog_detail
            form.save()
            return redirect('blog/blog_detail', blog_id= blog_id)

    context = {
        'blog':blog,
        'form':form,

    }
    return render(request, 'blog/blog_detail.html', context)