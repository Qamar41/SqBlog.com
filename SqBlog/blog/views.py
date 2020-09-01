from django.shortcuts import render, HttpResponse,get_object_or_404
from .models import Post ,Announcement
from django.contrib.auth.models import User
from django.db.models import Q
from	.forms	import		CommentForm

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from  django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,

)
# Create your views here.


# def home(request):
#     context= {
#         'posts':Post.objects.all()
#     }
#     return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10




def latest_posts(request):
    la_posts=Post.objects.order_by('-date_posted')[0:5]
    return  render(request,'blog/latest_posts.html',{'la_posts':la_posts})










class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'





    # comments = post.comments.filter(active=True)
    # new_comment = None
    # if request.method == 'POST':
    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         new_comment = comment_form.save(commit=False)
    #         new_comment.post = post
    #         new_comment.save()
    # else:
    #     comment_form = CommentForm()


class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post

    fields = ['title','post_overview','content']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post

    fields = ['title', 'post_overview','content']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user== post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'



    def test_func(self):
        post=self.get_object()
        if self.request.user== post.author:
            return True
        else:
            return False




class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


def about(request):
    return render(request,'blog/about.html',{'title':'About'})



class UserPostsListView(ListView):
    model = Post
    template_name = 'blog/user_posts_all.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Post.objects.filter(author=user).order_by('-date_posted')



class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search.html'
    # ordering = ['-date_posted']
    paginate_by =50


    def get_queryset(self):  # new
        query = self.request.GET.get('q')


        object_list=Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)).order_by('-date_posted')

        return object_list




class AnnouncementsListView(ListView):
    model = Announcement
    template_name = 'blog/announcements.html'
    context_object_name = 'announcements'
    ordering = ['-date_posted']
    paginate_by = 10


