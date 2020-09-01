from django.urls import path
from .import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,UserPostsListView,SearchResultsView,AnnouncementsListView
urlpatterns = [
    path('',PostListView.as_view() , name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view() , name='post-detail'),

    path('post/new',PostCreateView.as_view() , name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view() , name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view() , name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/userposts', UserPostsListView.as_view(), name='user-postses'),
    path('about',views.about , name='blog-about'),
    path('post/latestposts',views.latest_posts , name='latest'),
    # path('post/search',views.search , name='search'),
    path('search/', SearchResultsView.as_view(), name='search_results'),


    path('blog/announcements',AnnouncementsListView.as_view() , name='Announcementsall'),
]
