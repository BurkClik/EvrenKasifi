from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdatedView,
    PostDeleteView,
    UserPostListView,
    TravelPostListView,
    MoviePostListView,
    BookPostListView,
    GamePostListView,
    CodePostListView,
    AviationPostListView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdatedView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('travel/', TravelPostListView.as_view(), name='travel-home'),
    path('movie/', MoviePostListView.as_view(), name='movie-home'),
    path('book/', BookPostListView.as_view(), name='book-home'),
    path('game/', GamePostListView.as_view(), name='game-home'),
    path('code/', CodePostListView.as_view(), name='code-home'),
    path('aviation/', AviationPostListView.as_view(), name='aviation-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name='blog-about'),
    path('404/', views.construction, name='blog-construction'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)