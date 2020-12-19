from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Post
from .forms import CommentForm
from .forms import *


# Create your views here.
@login_required
def blogpost(request):
    form=PostForm()
    if request.method == "POST":
        form=PostForm(request.POST) 
        # redirect(home)
        return render(request,'blogpost.html',{'form':form})

def logout_view(request):
    logout(request)
    #return redirect(home)

def signup(request):
    form =SignupForm()
    if request.method == "POST":
        form=SignupForm(request.POST)
    if form.is_valid():
        User=form.save()
        user=form.save()
        user.set_password(user.password)
        user.save()
    return render(request,'registration/signup.html',{'form':form})

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'






