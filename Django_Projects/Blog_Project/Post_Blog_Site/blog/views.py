from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView
                                    ,ListView, DetailView,
                                    CreateView, UpdateView, 
                                    DeleteView)
from django.urls import reverse_lazy

from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.utils import timezone

# Views for blog post.

# Takes to about page
class AboutView(TemplateView):
    template_name = 'about.html'

# Takes to all the blog post view
class PostListView(ListView):
    model = Post

    # Defining how we want to grab post list view, use django ORM
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-pubished_date')
    
# Specific Blog post detail view
class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    # Check for Logged In
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post

# Edit a blog post
class PostUpdateView(LoginRequiredMixin, UpdateView):
    # Check for Logged In
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post
    
# Deleting blog post
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')     
 
# Drafts
class DraftListView(LoginRequiredMixin, ListView):
    # Check for Logged In
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    model = Post

    # Get records where published date is not present
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
    

# Views for comments 

# Comment on a blog post with primary key goes along that post.
@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    # Execute the below code once comment form filled in
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    # if not filled in
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form':form})

# Approve comment function
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)
